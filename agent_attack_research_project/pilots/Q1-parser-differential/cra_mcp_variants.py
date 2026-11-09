#!/usr/bin/env python3
"""Run R7 parser variants through the toolkit's real ToolBox.call executor path."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
TOOLKIT = PROJECT.parent / "Agent-Attack-Research"
sys.path.insert(0, str(TOOLKIT / "lib" / "mcp"))
sys.path.insert(0, str(HERE))

from cra_mcp.adapter import ToolBox  # noqa: E402
from run_variants import ARMS, ATTACK, SAFE, canonicalize, first, get_target, parse_pairs, strict, variants, DuplicateKey  # noqa: E402


class FakeServer:
    def __init__(self):
        self.calls = []

    async def call_tool(self, name, args):
        self.calls.append((name, args))
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=json.dumps({"ok": True, "args": args}))],
            is_error=False,
        )


def make_box(server):
    box = object.__new__(ToolBox)
    box.by_name = {"record_canary": {"name": "record_canary", "annotations": {}}}
    box.server = server
    return box


def run_one(variant, raw, arm, episode):
    validator_raw = raw
    executor_raw = raw
    rejected = False
    if arm == "canonicalized":
        validator_raw = canonicalize(raw)
        executor_raw = validator_raw
    try:
        if arm == "reject":
            validator = strict(parse_pairs(validator_raw))
        else:
            validator = first(validator_raw)
    except DuplicateKey:
        validator = None
        rejected = True
    server = FakeServer()
    allowed = bool(validator and validator.get("tool") == "record_canary" and get_target(validator) == SAFE)
    executed = None
    if allowed and not rejected:
        result = make_box(server).call("record_canary", executor_raw)
        payload = json.loads(result)
        if payload.get("ok") and server.calls:
            executed = get_target(server.calls[-1][1])
    return {
        "variant": variant,
        "arm": arm,
        "episode": episode,
        "validator_allowed": allowed,
        "rejected": rejected,
        "server_calls": server.calls,
        "executed_canary": executed,
        "success": executed == ATTACK,
        "utility": bool(rejected or validator is not None),
        "false_trigger": bool(executed == ATTACK and arm != "candidate"),
    }


def main():
    rows = []
    for variant, raw in variants().items():
        for arm in ARMS:
            for episode in range(10):
                rows.append(run_one(variant, raw, arm, episode))
    assert len(rows) == 8 * 3 * 10
    assert all(row["utility"] for row in rows)
    summary = {
        "rows": len(rows),
        "candidate_success": sum(row["success"] for row in rows if row["arm"] == "candidate"),
        "control_success": sum(row["success"] for row in rows if row["arm"] != "candidate"),
        "false_triggers": sum(row["false_trigger"] for row in rows),
        "utility_rows": sum(row["utility"] for row in rows),
        "adaptive_candidate_variants": sorted({row["variant"] for row in rows if row["arm"] == "candidate" and row["success"]}),
        "status": "cra_mcp_variant_pass",
        "interpretation": "real cra_mcp.adapter.ToolBox.call variant path with fake server; no real tool or project mutation",
    }
    (HERE / "cra_mcp_variant_trials.jsonl").write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    (HERE / "cra_mcp_variant_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    assert summary["candidate_success"] == 30
    assert summary["control_success"] == 0
    assert summary["false_triggers"] == 0
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
