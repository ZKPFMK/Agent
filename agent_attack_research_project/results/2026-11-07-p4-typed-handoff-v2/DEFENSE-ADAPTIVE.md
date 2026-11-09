# P4 source-preserving defense and adaptive check — 2026-11-08

## Scope

This is a deterministic local check over synthetic canaries. The attacker changes value representation and declared type;
no model, tool, network, credential or external action is used.

## Reproduction

```text
python3 -I pilots/P4-typed-handoff/defense_adaptive_check.py
```

## Result

The check generated 70 rows: 60 adaptive attacker variants and 10 benign trusted `CANARY_B` controls.

- vulnerable baseline success on adaptive variants: 20/60;
- source-preserving defense success on adaptive variants: 0/60;
- benign trusted routing success: 0/10 for attacker `CANARY_A` authorization;
- false triggers on benign `CANARY_B`: 0/10;
- utility rows: 70/70;
- statuses: 40 untrusted-source blocks, 20 provenance-mismatch blocks and 10 benign allowed routes;
- overall check: `pass=true`.

The defense preserves the benign control's safe `CANARY_B` route while blocking all tested untrusted or provenance-
mismatched variants. This is a protocol defense result and does not establish generalization beyond the tested adapter.
