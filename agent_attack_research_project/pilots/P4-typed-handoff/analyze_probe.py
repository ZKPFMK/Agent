#!/usr/bin/env python3
"""Recompute P4 typed-handoff mock probe from raw JSONL."""
from __future__ import annotations
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
TOOLKIT=ROOT.parent/"Agent-Attack-Research"
sys.path.insert(0,str(TOOLKIT/"lib"/"agentattack"))
from agentattack.metrics import Rate, rate_table
HERE=Path(__file__).resolve().parent
rows=[json.loads(x) for x in (HERE/"trials.jsonl").read_text().splitlines() if x.strip()]
assert len(rows)==150
assert all(r["parse_ok"] and r["utility"] for r in rows)
assert all(r["provenance_ok"] for r in rows if r["arm"] != "candidate")
assert all(not r["provenance_ok"] for r in rows if r["arm"] == "candidate")
groups=rate_table(rows,["arm"],"success")
by={g["arm"]:g["rate"] for g in groups}
summary={"groups":[{**g,"rate":g["rate"].as_dict()} for g in groups],"interpretation":"synthetic MockBackend harness only"}
(HERE/"analysis.json").write_text(json.dumps(summary,indent=2)+"\n")
lines=["# P4 typed/provenance conversion mock probe","","This is harness validation, not evidence about a real LLM or Agent.","","| arm | attacker-canary rate [95% CI], n |","|---|---|"]
for arm in sorted(by): lines.append(f"| {arm} | {by[arm].fmt()} |")
lines += ["","- provenance/type/parse/utility invariants: 100%","- candidate mechanism: unsafe conversion drops provenance and upgrades trust","- next gate: run an independent local-model implementation only after full-text screen and protocol freeze"]
(HERE/"probe_summary.md").write_text("\n".join(lines)+"\n")
print("\n".join(lines))
