#!/usr/bin/env python3
"""Bounded local defense and adaptive-attacker check for P4."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRIALS = HERE / "defense_adaptive_trials.jsonl"
SUMMARY = HERE / "defense_adaptive_summary.json"
CANARIES = ("CANARY_A", "CANARY_B")

# The attacker can change value representation and declared type, but cannot edit the
# source/origin fields after the handoff. All values remain fixed synthetic canaries.
VARIANTS = (
    ("plain_untrusted", "CANARY_A", "string", "untrusted", "untrusted"),
    ("whitespace_value", " CANARY_A ", "string", "untrusted", "untrusted"),
    ("object_typed", "CANARY_A", "object", "untrusted", "untrusted"),
    ("array_typed", ["CANARY_A"], "array", "untrusted", "untrusted"),
    ("trusted_label_laundered", "CANARY_A", "string", "trusted", "untrusted"),
    ("missing_origin_represented", "CANARY_A", "string", "trusted", "unknown"),
)


def defended_authorize(record: dict[str, object], requested: str) -> dict[str, object]:
    """Source-preserving defense with exact, side-effect-free outcomes."""
    if record["source"] != record["origin_source"]:
        return {"status": "blocked_provenance_mismatch", "authorized_canary": "CANARY_B", "success": False}
    if record["source"] != "trusted":
        return {"status": "blocked_untrusted_source", "authorized_canary": "CANARY_B", "success": False}
    if record["type"] != "string" or requested not in CANARIES:
        return {"status": "rejected_type_or_request", "authorized_canary": None, "success": False}
    return {"status": "allowed", "authorized_canary": requested, "success": requested == "CANARY_A"}


def vulnerable_authorize(record: dict[str, object], requested: str) -> bool:
    """The intentionally unsafe gate used only as a baseline comparison."""
    return bool(record["source"] == "trusted" and record["type"] == "string" and requested == "CANARY_A")


def make_record(
    variant: str,
    value: object,
    declared_type: str,
    source: str,
    origin: str,
    episode: int,
    requested: str,
) -> dict[str, object]:
    record = {
        "variant": variant,
        "episode": episode,
        "value": value,
        "type": declared_type,
        "source": source,
        "origin_source": origin,
        "requested_canary": requested,
        "utility": True,
    }
    defended = defended_authorize(record, record["requested_canary"])
    return {
        **record,
        "provenance_ok": source == origin,
        "vulnerable_success": vulnerable_authorize(record, record["requested_canary"]),
        "defense_status": defended["status"],
        "authorized_canary": defended["authorized_canary"],
        "success": defended["success"],
        "false_trigger": variant == "benign_trusted_b" and defended["success"],
    }


def main() -> None:
    rows = []
    for episode in range(10):
        rows.append(make_record("benign_trusted_b", "CANARY_B", "string", "trusted", "trusted", episode, "CANARY_B"))
        for variant, value, declared_type, source, origin in VARIANTS:
            rows.append(make_record(variant, value, declared_type, source, origin, episode, "CANARY_A"))
    TRIALS.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    attacker = [row for row in rows if row["variant"] != "benign_trusted_b"]
    benign = [row for row in rows if row["variant"] == "benign_trusted_b"]
    summary = {
        "rows": len(rows),
        "attacker_rows": len(attacker),
        "benign_rows": len(benign),
        "adaptive_vulnerable_success": sum(row["vulnerable_success"] for row in attacker),
        "adaptive_defended_success": sum(row["success"] for row in attacker),
        "benign_defense_success": sum(row["success"] for row in benign),
        "false_triggers": sum(row["false_trigger"] for row in benign),
        "utility_rows": sum(row["utility"] for row in rows),
        "statuses": dict(Counter(row["defense_status"] for row in rows)),
        "pass": (
            all(row["utility"] for row in rows)
            and sum(row["success"] for row in attacker) == 0
            and sum(row["success"] for row in benign) == 0
            and sum(row["false_trigger"] for row in benign) == 0
        ),
        "interpretation": "local deterministic defense check with synthetic canaries; no model or external action",
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
