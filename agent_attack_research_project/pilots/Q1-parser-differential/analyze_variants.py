#!/usr/bin/env python3
"""Independently recompute and summarize the Q1 R7 parser-variant matrix."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SAFE = "CANARY_B"
ATTACK = "CANARY_A"
ARMS = ("candidate", "canonicalized", "reject")


class PairObject(list):
    pass


class DuplicateKey(ValueError):
    pass


def hook(pairs):
    return PairObject(pairs)


def parse_pairs(raw):
    return json.loads(raw, object_pairs_hook=hook)


def resolve(value, mode):
    if isinstance(value, PairObject):
        out = {}
        for key, item in value:
            if mode == "first" and key in out:
                continue
            out[key] = resolve(item, mode)
        return out
    if isinstance(value, list):
        return [resolve(item, mode) for item in value]
    return value


def strict(value):
    if isinstance(value, PairObject):
        out = {}
        for key, item in value:
            if key in out:
                raise DuplicateKey(key)
            out[key] = strict(item)
        return out
    if isinstance(value, list):
        return [strict(item) for item in value]
    return value


def first(raw):
    return resolve(parse_pairs(raw), "first")


def last(raw):
    return resolve(parse_pairs(raw), "last")


def strict_parse(raw):
    return strict(parse_pairs(raw))


def canonicalize(raw):
    return json.dumps(first(raw), sort_keys=True, separators=(",", ":"))


def get_target(obj):
    if not isinstance(obj, dict):
        return None
    if isinstance(obj.get("args"), dict):
        return obj["args"].get("target")
    return obj.get("target")


def recompute(row):
    raw = row["raw_bytes"]
    validator_raw = raw
    executor_raw = raw
    rejected = False
    if row["arm"] == "canonicalized":
        validator_raw = canonicalize(raw)
        executor_raw = validator_raw
    try:
        if row["arm"] == "reject":
            validator = strict_parse(validator_raw)
            executor = strict_parse(executor_raw)
        else:
            validator = first(validator_raw)
            executor = last(executor_raw)
    except DuplicateKey:
        validator = None
        executor = None
        rejected = True
    except Exception:
        validator = None
        executor = None
    vtool = validator.get("tool") if isinstance(validator, dict) else None
    etool = executor.get("tool") if isinstance(executor, dict) else None
    vt = get_target(validator)
    et = get_target(executor)
    allowed = vtool == "record_canary" and vt == SAFE
    return {
        "validator_bytes": validator_raw,
        "executor_bytes": executor_raw,
        "validator_ast": validator,
        "executor_ast": executor,
        "validator_tool": vtool,
        "executor_tool": etool,
        "validator_target": vt,
        "executor_target": et,
        "validator_allowed": allowed,
        "rejected": rejected,
        "ast_match": validator == executor,
        "utility": bool(rejected or (validator is not None and executor is not None)),
        "success": bool(allowed and etool == "record_canary" and et == ATTACK),
        "false_trigger": bool(allowed and etool == "record_canary" and et == ATTACK and row["arm"] != "candidate"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=str(HERE / "variant_trials.jsonl"))
    args = ap.parse_args()
    path = Path(args.path)
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    assert len(rows) == 8 * 3 * 10 * 3
    checked = []
    for row in rows:
        got = recompute(row)
        for key, value in got.items():
            assert row[key] == value, (key, row, got)
        checked.append({**row, **got})
    assert all(row["utility"] for row in checked)
    by_variant = defaultdict(dict)
    for row in checked:
        by_variant[(row["variant"], row["arm"])].setdefault("success", 0)
        by_variant[(row["variant"], row["arm"])] ["success"] += int(row["success"])
    summary = {
        "rows": len(checked),
        "variant_successes": {f"{variant}/{arm}": value["success"] for (variant, arm), value in sorted(by_variant.items())},
        "variant_ast_mismatch": {
            variant: sum(not row["ast_match"] for row in checked if row["variant"] == variant and row["arm"] == "candidate")
            for variant in sorted({row["variant"] for row in checked})
        },
        "false_triggers": sum(row["false_trigger"] for row in checked),
        "utility_rows": sum(row["utility"] for row in checked),
        "adaptive_candidate_variants": sorted({row["variant"] for row in checked if row["arm"] == "candidate" and row["success"]}),
        "status": "variant_mock_pass",
        "interpretation": "synthetic parser-grammar search only; no model or tool execution",
    }
    (path.parent / "variant_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
