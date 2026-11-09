#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
TOOLKIT=HERE.parents[2]/"Agent-Attack-Research"
sys.path.insert(0,str(TOOLKIT/"lib"/"agentattack"))
from agentattack.metrics import rate_table,mcnemar,paired_counts
rows=[json.loads(x) for x in (HERE/"real_trials.jsonl").read_text().splitlines() if x.strip()]
assert rows and all(r["parse_ok"] and r["utility"] for r in rows)
assert all(r["provenance_ok"] for r in rows if r["arm"]!="candidate")
assert all(not r["provenance_ok"] for r in rows if r["arm"]=="candidate")
groups=rate_table(rows,["arm"],"success")
by={(r["episode"],r["seed"]):r for r in rows}
# one row per arm/key, so build explicit paired maps
paired=defaultdict(dict)
for r in rows: paired[(r["episode"],r["seed"])][r["arm"]]=r
keys=sorted(k for k,v in paired.items() if "candidate" in v and "mechanism_control" in v)
a=[paired[k]["candidate"]["success"] for k in keys]; b=[paired[k]["mechanism_control"]["success"] for k in keys]
x,y=paired_counts(a,b)
summary={"rows":len(rows),"groups":[{**g,"rate":g["rate"].as_dict()} for g in groups],"paired":{"keys":len(keys),"only_candidate":x,"only_control":y,"mcnemar_p":mcnemar(x,y)},"errors":[r["error"] for r in rows if r["error"]]}
(HERE/"real_analysis.json").write_text(json.dumps(summary,indent=2)+"\n")
for g in groups: print(g["arm"],g["rate"].fmt())
print("candidate-only",x,"control-only",y,"p",mcnemar(x,y))
print("errors",len(summary["errors"]))
