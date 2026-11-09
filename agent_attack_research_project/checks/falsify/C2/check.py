#!/usr/bin/env python3
"""Recompute the local-gateway C2 kill conditions from real_trials.jsonl."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TRIALS = ROOT / "pilots" / "I1-memory-cascade" / "real_trials.jsonl"
rows = [json.loads(line) for line in TRIALS.read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(rows) == 150, len(rows)
assert all(row["parse_ok"] and row["utility"] and row["local_truth_ok"] for row in rows)

groups = defaultdict(list)
for row in rows:
    groups[row["arm"]].append(bool(row["success"]))
for arm in sorted(groups):
    vals = groups[arm]
    print(f"{arm}: {sum(vals)}/{len(vals)} = {sum(vals) / len(vals):.6f}")

paired = defaultdict(dict)
for row in rows:
    paired[(row["episode"], row["seed"])][row["arm"]] = row["success"]
narrative = [paired[key]["narrative"] for key in sorted(paired)]
random_arm = [paired[key]["random"] for key in sorted(paired)]
only_narrative = sum(a and not b for a, b in zip(narrative, random_arm))
only_random = sum(b and not a for a, b in zip(narrative, random_arm))
print(f"paired narrative-only={only_narrative} random-only={only_random}")

# The primary C2 kill conditions are descriptive and pre-registered: no narrative advantage over random,
# or the surface-matched bridge-swap control is at least as high as narrative.
narrative_rate = sum(groups["narrative"]) / len(groups["narrative"])
random_rate = sum(groups["random"]) / len(groups["random"])
bridge_rate = sum(groups["bridge_swap"]) / len(groups["bridge_swap"])
refuted = narrative_rate <= random_rate or bridge_rate >= narrative_rate
print("C2 verdict: REFUTED" if refuted else "C2 verdict: not refuted")
sys.exit(0 if refuted else 1)
