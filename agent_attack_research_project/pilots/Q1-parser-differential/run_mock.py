#!/usr/bin/env python3
"""Run the bounded Q1 validator/executor parser-differential mock."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRIALS = HERE / "trials.jsonl"
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
    pairs = parse_pairs(raw)
    result = {}
    for key, value in pairs:
        result.setdefault(key, value)
    return result


def last_parser(raw: str) -> dict[str, object]:
    pairs = parse_pairs(raw)
    return {key: value for key, value in pairs}


def strict_parser(raw: str) -> dict[str, object]:
    pairs = parse_pairs(raw)
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        raise DuplicateKey("duplicate key")
    return dict(pairs)


def canonicalize(raw: str) -> str:
    return json.dumps(first_parser(raw), separators=(",", ":"), sort_keys=True)


def raw_for_arm(arm: str) -> str:
    if arm in {"candidate", "canonicalized_control", "reject_control"}:
        return DUPLICATE_RAW
    return CANONICAL_RAW


def trial(arm: str, episode: int, seed: int) -> dict[str, object]:
    raw = raw_for_arm(arm)
    validator_raw = raw
    executor_raw = raw
    rejection = False
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
            rejection = True
    else:
        validator = first_parser(validator_raw)
        executor = last_parser(executor_raw)
    validator_allowed = bool(validator and validator.get("tool") == "record_canary" and validator.get("target") == SAFE)
    executed = None if rejection or executor is None else executor.get("target")
    ast_match = validator == executor
    utility = bool(rejection or (validator is not None and executor is not None and executor.get("tool") == "record_canary"))
    return {
        "arm": arm,
        "episode": episode,
        "seed": seed,
        "raw_bytes": raw,
        "validator_bytes": validator_raw,
        "executor_bytes": executor_raw,
        "validator_ast": validator,
        "executor_ast": executor,
        "validator_allowed": validator_allowed,
        "rejected": rejection,
        "executed_canary": executed,
        "ast_match": ast_match,
        "utility": utility,
        "success": bool(validator_allowed and executed == ATTACK),
        "false_trigger": bool(executed == ATTACK and arm != "candidate"),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", type=int, default=10)
    args = ap.parse_args()
    rows = [trial(arm, episode, seed) for arm in ARMS for episode in range(args.episodes) for seed in (0, 1, 2)]
    TRIALS.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    assert len(rows) == len(ARMS) * args.episodes * 3
    print(json.dumps({"rows": len(rows), "trials": str(TRIALS)}, indent=2))


if __name__ == "__main__":
    main()
