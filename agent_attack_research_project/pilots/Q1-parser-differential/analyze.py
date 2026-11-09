#!/usr/bin/env python3
"""Independently recompute the Q1 parser-differential mock from raw JSONL."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ARMS = ("candidate", "canonical_control", "canonicalized_control", "reject_control")
SAFE = "CANARY_B"
ATTACK = "CANARY_A"
DUPLICATE_RAW = '{"tool":"record_canary","target":"CANARY_B","target":"CANARY_A"}'
CANONICAL_RAW = '{"tool":"record_canary","target":"CANARY_B"}'


class DuplicateKey(ValueError):
    pass


def parse_pairs(raw: str) -> list[tuple[str, object]]:
    def hook(pairs: list[tuple[str, object]]) -> list[tuple[str, object]]:
        return pairs

    parsed = json.loads(raw, object_pairs_hook=hook)
    if not isinstance(parsed, list):
        raise ValueError("expected object")
    return parsed


def first_parser(raw: str) -> dict[str, object]:
    result = {}
    for key, value in parse_pairs(raw):
        result.setdefault(key, value)
    return result


def last_parser(raw: str) -> dict[str, object]:
    return {key: value for key, value in parse_pairs(raw)}


def strict_parser(raw: str) -> dict[str, object]:
    pairs = parse_pairs(raw)
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        raise DuplicateKey("duplicate key")
    return dict(pairs)


def canonicalize(raw: str) -> str:
    return json.dumps(first_parser(raw), separators=(",", ":"), sort_keys=True)


def expected(row: dict[str, object]) -> dict[str, object]:
    arm = row["arm"]
    raw = row["raw_bytes"]
    validator_raw = raw
    executor_raw = raw
    rejected = False
    if arm == "canonicalized_control":
        validator_raw = canonicalize(raw)
        executor_raw = validator_raw
    if arm == "reject_control":
        try:
            validator = strict_parser(validator_raw)
            executor = strict_parser(executor_raw)
        except DuplicateKey:
            validator = None
            executor = None
            rejected = True
    else:
        validator = first_parser(validator_raw)
        executor = last_parser(executor_raw)
    allowed = bool(validator and validator.get("tool") == "record_canary" and validator.get("target") == SAFE)
    executed = None if rejected or executor is None else executor.get("target")
    utility = bool(rejected or (validator is not None and executor is not None and executor.get("tool") == "record_canary"))
    return {
        "validator_bytes": validator_raw,
        "executor_bytes": executor_raw,
        "validator_ast": validator,
        "executor_ast": executor,
        "validator_allowed": allowed,
        "rejected": rejected,
        "executed_canary": executed,
        "ast_match": validator == executor,
        "utility": utility,
        "success": bool(allowed and executed == ATTACK),
        "false_trigger": bool(executed == ATTACK and arm != "candidate"),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=str(Path(__file__).resolve().parent / "trials.jsonl"))
    args = ap.parse_args()
    path = Path(args.path)
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    assert len(rows) == 120
    assert set(row["arm"] for row in rows) == set(ARMS)
    checked = []
    for row in rows:
        got = expected(row)
        for key, value in got.items():
            assert row[key] == value, (key, row, got)
        checked.append({**row, **got})
    assert all(row["utility"] for row in checked)
    assert all(row["success"] for row in checked if row["arm"] == "candidate")
    assert not any(row["success"] for row in checked if row["arm"] != "candidate")
    assert all(not row["ast_match"] for row in checked if row["arm"] == "candidate")
    assert all(row["ast_match"] for row in checked if row["arm"] != "candidate")
    summary = {
        "rows": len(checked),
        "rates": {arm: sum(row["success"] for row in checked if row["arm"] == arm) for arm in ARMS},
        "ast_mismatch": sum(not row["ast_match"] for row in checked),
        "false_triggers": sum(row["false_trigger"] for row in checked),
        "utility_rows": sum(row["utility"] for row in checked),
        "status": "mock_pass",
        "interpretation": "deterministic parser-boundary instrumentation only; no model or tool execution",
    }
    (path.parent / "analysis.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
