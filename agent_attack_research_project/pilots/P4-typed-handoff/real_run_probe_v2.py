#!/usr/bin/env python3
"""Run the authorized loopback local-gateway P4 v2 smoke or pilot."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
TOOLKIT = PROJECT.parent / "Agent-Attack-Research"
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLKIT / "lib" / "agentattack"))
sys.path.insert(0, str(HERE))

from agentattack.llm import CachedBackend, OpenAICompatible  # noqa: E402
from agentattack.runner import env_record, run_matrix  # noqa: E402
from protocol_v2 import (  # noqa: E402
    ARMS,
    build_messages,
    evaluate,
    handoff,
    parse_response,
    assert_static_invariants,
    visible_handoff,
)

BASE = os.environ.get("P4_BASE_URL", "http://127.0.0.1:3425/v1").rstrip("/")
MODEL = os.environ.get("P4_MODEL", "auto/gpt-6.1-sol")
TRIALS = HERE / "v2_real_trials.jsonl"
CACHE = HERE / "v2_real_cache.jsonl"


def trial(condition: dict[str, object], seed: int, backend: CachedBackend) -> dict[str, object]:
    arm = str(condition["arm"])
    episode = int(condition["episode"])
    full = handoff(arm)
    visible = visible_handoff(full)
    if arm == "reject_control":
        raw_response = "<rejected by strict parser>"
        response = None
        outcome = evaluate(full, response, model_called=False)
        backend_name = "deterministic-parser"
    else:
        raw_response = backend.chat(build_messages(visible, episode, seed), seed=seed)
        response = parse_response(raw_response)
        outcome = evaluate(full, response, model_called=True)
        backend_name = MODEL
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
    if os.environ.get("P4_ALLOW_REAL") != "1":
        raise SystemExit("set P4_ALLOW_REAL=1 after reviewing PROTOCOL-v2.md")
    if not (BASE.startswith("http://127.0.0.1") or BASE.startswith("http://localhost")):
        raise SystemExit("non-loopback endpoint refused")
    assert_static_invariants()
    episodes = 1 if args.smoke else 10
    seeds = [0] if args.smoke else [0, 1, 2]
    inner = OpenAICompatible(BASE, MODEL, temperature=0.0, max_tokens=256, timeout=90, retries=2)
    cached = CachedBackend(inner, str(CACHE))
    result = run_matrix(
        {"arm": ARMS, "episode": range(episodes)},
        lambda condition, seed: trial(condition, seed, cached),
        seeds,
        str(TRIALS),
        env=env_record(
            research="P4 typed handoff v2 local pilot",
            model=MODEL,
            endpoint=BASE,
            temperature=0.0,
            max_tokens=256,
            budget_cap_usd=10.0,
        ),
    )
    rows = [json.loads(line) for line in TRIALS.read_text().splitlines() if line.strip()]
    expected = len(ARMS) * episodes * len(seeds)
    estimate = sum(len(json.dumps(row.get("visible_handoff", {}))) / 4 * 0.000002 for row in rows)
    estimate += sum(len(row.get("raw_response", "")) / 4 * 0.00001 for row in rows if row.get("model_called"))
    print(json.dumps({"runner": result, "rows": len(rows), "estimated_cost_usd": estimate, "expected": expected, "model": MODEL}, indent=2))


if __name__ == "__main__":
    main()
