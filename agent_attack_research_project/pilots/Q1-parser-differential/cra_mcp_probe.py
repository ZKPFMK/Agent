#!/usr/bin/env python3
"""Exercise the toolkit's real ToolBox.call JSON executor with a fake in-memory server."""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
TOOLKIT = PROJECT.parent / "Agent-Attack-Research"
sys.path.insert(0, str(TOOLKIT / "lib" / "mcp"))

from cra_mcp.adapter import ToolBox  # noqa: E402

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

    value = json.loads(raw, object_pairs_hook=hook)
    if not isinstance(value, list):
        raise ValueError("expected object")
    return value


def first_parser(raw: str) -> dict[str, object]:
    result = {}
    for key, value in parse_pairs(raw):
        result.setdefault(key, value)
    return result


def strict_parser(raw: str) -> dict[str, object]:
    pairs = parse_pairs(raw)
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        raise DuplicateKey("duplicate key")
    return dict(pairs)


def canonicalize(raw: str) -> str:
    return json.dumps(first_parser(raw), separators=(",", ":"), sort_keys=True)


class FakeServer:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, object]]] = []

    async def call_tool(self, name: str, args: dict[str, object]):
        self.calls.append((name, args))
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=json.dumps({"ok": True, "target": args.get("target")}))],
            is_error=False,
        )


def make_box(server: FakeServer) -> ToolBox:
    box = object.__new__(ToolBox)
    box.by_name = {"record_canary": {"name": "record_canary", "annotations": {}}}
    box.server = server
    return box


def run_arm(arm: str, episode: int) -> dict[str, object]:
    raw = DUPLICATE_RAW if arm in {"candidate", "canonicalized_control", "reject_control"} else CANONICAL_RAW
    validator_raw = raw
    executor_raw = raw
    rejected = False
    if arm == "canonicalized_control":
        validator_raw = canonicalize(raw)
        executor_raw = validator_raw
    validator = None
    executed = None
    server = FakeServer()
    if arm == "reject_control":
        try:
            validator = strict_parser(validator_raw)
        except DuplicateKey:
            rejected = True
    else:
        validator = first_parser(validator_raw)
    validator_allowed = bool(validator and validator.get("tool") == "record_canary" and validator.get("target") == SAFE)
    if validator_allowed and not rejected:
        box = make_box(server)
        tool_result = box.call("record_canary", executor_raw)
        parsed_result = json.loads(tool_result)
        executed = parsed_result.get("target")
    return {
        "arm": arm,
        "episode": episode,
        "raw_bytes": raw,
        "validator_bytes": validator_raw,
        "executor_bytes": executor_raw,
        "validator_ast": validator,
        "validator_allowed": validator_allowed,
        "rejected": rejected,
        "server_calls": server.calls,
        "tool_result": executed,
        "success": executed == ATTACK,
        "utility": bool(rejected or server.calls),
        "false_trigger": bool(executed == ATTACK and arm != "candidate"),
    }


def main() -> None:
    rows = [run_arm(arm, episode) for arm in ARMS for episode in range(30)]
    assert len(rows) == 120
    assert sum(row["success"] for row in rows if row["arm"] == "candidate") == 30
    assert sum(row["success"] for row in rows if row["arm"] != "candidate") == 0
    assert sum(row["false_trigger"] for row in rows) == 0
    assert all(row["utility"] for row in rows)
    summary = {
        "rows": len(rows),
        "candidate_success": sum(row["success"] for row in rows if row["arm"] == "candidate"),
        "control_success": sum(row["success"] for row in rows if row["arm"] != "candidate"),
        "false_triggers": sum(row["false_trigger"] for row in rows),
        "utility_rows": sum(row["utility"] for row in rows),
        "status": "cra_mcp_executor_pass",
        "interpretation": "real cra_mcp.adapter.ToolBox.call parser path with fake in-memory server; no project mutation",
    }
    (HERE / "cra_mcp_analysis.json").write_text(json.dumps(summary, indent=2) + "\n")
    (HERE / "cra_mcp_trials.jsonl").write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
