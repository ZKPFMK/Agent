# P4 typed-handoff v2 result protocol

**Date:** 2026-11-07–2026-11-08  
**Status:** closed as an ACL paper candidate; preserved as a bounded protocol and negative-boundary artifact  
**Scope:** project-owned loopback sandbox only

## Reproduction

```text
python3 -I pilots/P4-typed-handoff/run_probe_v2.py
P4_ALLOW_REAL=1 python3 -I pilots/P4-typed-handoff/real_run_probe_v2.py
P4_ALLOW_REAL=1 P4_ALT_MODEL=auto/gpt-6-astra python3 -I pilots/P4-typed-handoff/alt_adapter_probe.py
python3 -I pilots/P4-typed-handoff/analyze_v2.py --expected 150
python3 -I pilots/P4-typed-handoff/defense_adaptive_check.py
```

The primary local run used loopback endpoint `http://127.0.0.1:3425/v1`, route `auto/gpt-6.1-sol`, temperature 0
and max output 256. Estimated cost was `$0.0271`. The independent adapter run used `auto/gpt-6-astra` and
estimated `$0.1356`. Both runners wrote 150 rows and exited with code 0.

## Design

The candidate and mechanism-control model-visible handoffs are identical in task, value and type. The source
provenance transition is retained in the full handoff record and applied by an independent deterministic
no-side-effect authorization evaluator after the model response. The reject-control is handled by a deterministic
parser and does not call the model.

## Raw artifacts

- `pilots/P4-typed-handoff/v2_real_trials.jsonl`
- `pilots/P4-typed-handoff/v2_real_analysis.json`
- `pilots/P4-typed-handoff/v2_alt_real_trials.jsonl`
- `pilots/P4-typed-handoff/v2_alt_real_analysis.json`
- `pilots/P4-typed-handoff/v2_trials.jsonl`
- `pilots/P4-typed-handoff/defense_adaptive_trials.jsonl`
- `pilots/P4-typed-handoff/defense_adaptive_summary.json`
- `pilots/P4-typed-handoff/PROTOCOL-v2.md`
- `checks/falsify/C3-v2.md`
- `threat/P4-typed-handoff-v2.json`
- `R6-P4-screening-2026-11-08.md`

## Result

Both the primary Sol route and the independent adapter/Astra route produced candidate authorization 30/30 and
mechanism-control authorization 0/30, with paired exact McNemar `p=1.862645e-09`. Each 150-row matrix passed raw
recomputation, parsing and structured utility; candidate/control visible payloads and raw model responses matched in
all 30 paired keys. The deterministic defense blocked 0/60 adaptive synthetic variants and produced 0/10 false
triggers on benign trusted controls.

These are bounded protocol results. The model emits the same request in candidate and control, and public full-text
screening found direct adjacent coverage across provenance erasure, provenance-preserving multi-agent channels,
structured delegation contracts, authority laundering and provenance-aware authorization. P4 is therefore closed as a
paper candidate; preserve the logs for artifact and negative-boundary analysis, and return to R4 for a new mechanism.
