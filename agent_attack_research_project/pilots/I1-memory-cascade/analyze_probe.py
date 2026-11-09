#!/usr/bin/env python3
"""Recompute the I1 R5 probe from raw JSONL and write an auditable summary."""
from __future__ import annotations

import json
import sys
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parents[3] / "Agent-Attack-Research"
sys.path.insert(0, str(TOOLKIT / "lib" / "agentattack"))

from agentattack.metrics import Rate, mcnemar, paired_counts, rate_table
from agentattack.runner import load_records

HERE = Path(__file__).resolve().parent
TRIALS = HERE / "trials.jsonl"


def main() -> int:
    rows = load_records(str(TRIALS))
    if len(rows) != 120:
        raise SystemExit(f"expected 120 rows, found {len(rows)}")
    if not all(row.get("local_truth_ok") is True for row in rows):
        raise SystemExit("local truth oracle failed")
    if not all(row.get("utility") is True for row in rows):
        raise SystemExit("utility invariant failed")

    groups = rate_table(rows, ["arm"], "success")
    by_key = {(row["episode"], row["seed"]): row for row in rows}
    candidate = [by_key[key]["success"] for key in sorted(by_key) if by_key[key]["arm"] == "narrative"]
    random_arm = [by_key[key]["success"] for key in sorted(by_key) if by_key[key]["arm"] == "random"]
    # The key dictionary contains one row per arm, so build paired rows explicitly.
    paired = {}
    for row in rows:
        paired.setdefault((row["episode"], row["seed"]), {})[row["arm"]] = row
    candidate = [paired[key]["narrative"]["success"] for key in sorted(paired)]
    random_arm = [paired[key]["random"]["success"] for key in sorted(paired)]
    only_candidate, only_random = paired_counts(candidate, random_arm)
    p_value = mcnemar(only_candidate, only_random)
    narrative_rate = Rate(sum(candidate), len(candidate))
    random_rate = Rate(sum(random_arm), len(random_arm))

    summary = {
        "rows": len(rows),
        "groups": [{**item, "rate": item["rate"].as_dict()} for item in groups],
        "paired": {
            "candidate": narrative_rate.as_dict(),
            "random": random_rate.as_dict(),
            "only_candidate": only_candidate,
            "only_random": only_random,
            "mcnemar_p": p_value,
        },
        "interpretation": "synthetic MockBackend harness check only; not evidence about a real LLM agent",
    }
    (HERE / "analysis.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# I1 R5 evidence-order probe",
        "",
        "This result uses a deterministic `MockBackend` whose order sensitivity is intentionally synthetic. It validates the experiment harness, paired controls, exact oracle and provenance. It is not a claim about real LLM behaviour.",
        "",
        "## Group rates",
        "",
        "| arm | false-causal-belief rate [95% CI], n |",
        "|---|---|",
    ]
    for item in groups:
        lines.append(f"| {item['arm']} | {item['rate'].fmt()} |")
    lines += [
        "",
        "## Paired narrative versus random",
        "",
        f"- narrative: {narrative_rate.fmt()}",
        f"- random: {random_rate.fmt()}",
        f"- discordant pairs: narrative-only={only_candidate}, random-only={only_random}",
        f"- exact McNemar p-value: {p_value:.6f}",
        "- local truth oracle: 100% for all 120 records",
        "- utility invariant: 100% for all 120 records",
        "",
        "## Gate B verdict",
        "",
        "The synthetic candidate should proceed to a mechanism-control review only as a harness demonstration. The result cannot advance to a real-model claim because the backend policy encodes the tested susceptibility.",
    ]
    (HERE / "probe_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
