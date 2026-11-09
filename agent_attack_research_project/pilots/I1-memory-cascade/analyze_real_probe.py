#!/usr/bin/env python3
"""Recompute the local-gateway I1 pilot from real_trials.jsonl."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parents[3] / "Agent-Attack-Research"
sys.path.insert(0, str(TOOLKIT / "lib" / "agentattack"))

from agentattack.metrics import Rate, mcnemar, paired_counts, rate_table
from agentattack.runner import load_records

HERE = Path(__file__).resolve().parent
TRIALS = HERE / "real_trials.jsonl"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected", type=int, default=150)
    args = parser.parse_args()
    rows = load_records(str(TRIALS))
    if not rows:
        raise SystemExit("no real pilot rows")
    if len(rows) != args.expected:
        print(f"WARN partial pilot: {len(rows)}/{args.expected} rows", file=sys.stderr)
    if not all(row.get("local_truth_ok") is True for row in rows):
        raise SystemExit("local truth oracle failed")

    groups = rate_table(rows, ["arm"], "success")
    parse_groups = rate_table(rows, ["arm"], "parse_ok")
    paired = {}
    for row in rows:
        paired.setdefault((row["episode"], row["seed"]), {})[row["arm"]] = row
    complete_keys = [key for key, arms in paired.items() if "narrative" in arms and "random" in arms]
    candidate = [paired[key]["narrative"]["success"] for key in sorted(complete_keys)]
    random_arm = [paired[key]["random"]["success"] for key in sorted(complete_keys)]
    only_candidate, only_random = paired_counts(candidate, random_arm)
    narrative_rate = Rate(sum(candidate), len(candidate))
    random_rate = Rate(sum(random_arm), len(random_arm))
    total_cost = sum(float(row.get("estimated_cost_usd", 0.0)) for row in rows)
    total_input = sum(int(row.get("input_tokens_est", 0)) for row in rows)
    total_output = sum(int(row.get("output_tokens_est", 0)) for row in rows)

    summary = {
        "rows": len(rows),
        "complete_paired_keys": len(complete_keys),
        "groups": [{**item, "rate": item["rate"].as_dict()} for item in groups],
        "parse_groups": [{**item, "rate": item["rate"].as_dict()} for item in parse_groups],
        "paired": {
            "candidate": narrative_rate.as_dict(),
            "random": random_rate.as_dict(),
            "only_candidate": only_candidate,
            "only_random": only_random,
            "mcnemar_p": mcnemar(only_candidate, only_random),
        },
        "input_tokens_est": total_input,
        "output_tokens_est": total_output,
        "estimated_cost_usd": total_cost,
        "interpretation": "exploratory local-gateway pilot; no real deployment claim; memory and downstream blocks not run",
    }
    (HERE / "real_analysis.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# I1 local-gateway order pilot",
        "",
        "This is an exploratory run against the authorized loopback gateway and synthetic evidence only. It does not test a live Agent deployment and does not establish a general vulnerability or novelty claim.",
        "",
        "## Group rates",
        "",
        "| arm | false-causal-belief rate [95% CI], n | parse/utility rate [95% CI], n |",
        "|---|---|---|",
    ]
    parse_by_arm = {item["arm"]: item["rate"] for item in parse_groups}
    for item in groups:
        lines.append(f"| {item['arm']} | {item['rate'].fmt()} | {parse_by_arm[item['arm']].fmt()} |")
    lines += [
        "",
        "## Paired narrative versus random",
        "",
        f"- narrative: {narrative_rate.fmt()}",
        f"- random: {random_rate.fmt()}",
        f"- discordant pairs: narrative-only={only_candidate}, random-only={only_random}",
        f"- exact McNemar p-value: {mcnemar(only_candidate, only_random):.6f}",
        f"- estimated tokens: input={total_input}, output={total_output}",
        f"- estimated cost from gateway metadata: ${total_cost:.4f} (hard cap $50)",
        "- local truth oracle: 100% required; see raw rows for every episode",
        "",
        "## Interpretation gate",
        "",
        "The result only updates the exploratory C2 pilot record. It does not support a memory-persistence or downstream-propagation claim, because those blocks were not run. The bridge-swap control failed and D-4 closes I1; preserve this raw log as a negative boundary result. Any future order-direction or semantic-composition idea requires a fresh R4 claim and protocol.",
    ]
    (HERE / "real_probe_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
