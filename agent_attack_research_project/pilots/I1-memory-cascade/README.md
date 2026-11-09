# I1 R5 evidence-order pilot

This directory contains a bounded, offline harness check for the first I1 block.

## Run

```bash
python3 -I run_probe.py
python3 -I analyze_probe.py
```

The run uses `agentattack.runner.run_matrix`, `agentattack.llm.MockBackend`, `CachedBackend` and
`agentattack.metrics`. It creates 4 arms × 10 synthetic episodes × 3 paired seeds = 120 trial rows.

## Boundary

The mock policy intentionally assigns a higher probability to the false edge `A->C` when the locally true
fragments `AB` and `BC` are adjacent. Therefore the result checks the research harness, exact local oracle,
paired controls, resumability and evidence provenance. It is not a measurement of a real LLM or Agent.

Raw artifacts:

- `config.json` — synthetic configuration and safety contract;
- `trials.jsonl` — one record per arm/episode/seed;
- `trials.jsonl.env.json` — environment provenance;
- `cache.jsonl` — mock response cache;
- `analysis.json` and `probe_summary.md` — recomputed rates and paired check;
- `../checks/falsify/C1/check.md` — falsifier verdict and weakened wording.
