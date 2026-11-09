#!/usr/bin/env python3
"""Run the bounded P4 v2 protocol with a deterministic mock backend."""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
TOOLKIT = PROJECT.parent / "Agent-Attack-Research"
sys.path.insert(0, str(TOOLKIT / "lib" / "agentattack"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from agentattack.llm import CachedBackend, MockBackend  # noqa: E402
from agentattack.metrics import rate_table  # noqa: E402
from agentattack.runner import env_record, run_matrix  # noqa: E402
from protocol_v2 import (  # noqa: E402
    ARMS,
    build_messages,
    evaluate,
    handoff,
    mock_response,
    assert_static_invariants,
    visible_handoff,
)

HERE = Path(__file__).resolve().parent
TRIALS = HERE / "v2_trials.jsonl"
CACHE = HERE / "v2_cache.jsonl"


def trial(condition: dict[str, object], seed: int) -> dict[str, object]:
    arm = str(condition["arm"])
    episode = int(condition["episode"])
    full = handoff(arm)
    visible = visible_handoff(full)
    if arm == "reject_control":
        response = None
        outcome = evaluate(full, response, model_called=False)
        raw_response = "<rejected by strict parser>"
        backend_name = "deterministic-parser"
    else:
        backend = MockBackend(
            lambda messages: json.dumps(mock_response(json.loads(messages[-1]["content"])["handoff"])),
            name="mock-typed-handoff-v2",
        )
        cached = CachedBackend(backend, str(CACHE))
        raw_response = cached.chat(build_messages(visible, episode, seed), seed=seed)
        response = json.loads(raw_response)
        outcome = evaluate(full, response, model_called=True)
        backend_name = backend.name
    return {
        **condition,
        "seed": seed,
        "handoff": full,
        "visible_handoff": visible,
        "provenance_ok": full["source"] == full["origin_source"],
        "response": response,
        "raw_response": raw_response,
        "backend": backend_name,
        **outcome,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    assert_static_invariants()
    episodes = 1 if args.smoke else 10
    seeds = [0] if args.smoke else [0, 1, 2]
    result = run_matrix(
        {"arm": ARMS, "episode": range(episodes)},
        trial,
        seeds,
        str(TRIALS),
        env=env_record(research="P4 typed handoff v2 mock", backend="MockBackend"),
    )
    rows = [json.loads(line) for line in TRIALS.read_text().splitlines() if line.strip()]
    expected = len(ARMS) * episodes * len(seeds)
    assert len(rows) == expected
    assert all(row["parse_ok"] and row["utility"] for row in rows)
    assert all(row["provenance_ok"] for row in rows if row["arm"] != "candidate")
    assert all(not row["provenance_ok"] for row in rows if row["arm"] == "candidate")
    candidate_visible = next(row["visible_handoff"] for row in rows if row["arm"] == "candidate")
    assert all(
        row["visible_handoff"] == candidate_visible
        for row in rows
        if row["arm"] == "mechanism_control"
    )
    groups = rate_table(rows, ["arm"], "success")
    summary = {
        "runner": result,
        "rows": len(rows),
        "groups": [{**group, "rate": group["rate"].as_dict()} for group in groups],
        "interpretation": "synthetic protocol instrumentation only",
    }
    (HERE / "v2_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    for group in groups:
        print(group["arm"], group["rate"].fmt())


if __name__ == "__main__":
    main()
