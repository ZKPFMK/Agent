# P4 typed/provenance conversion mock probe

This is harness validation, not evidence about a real LLM or Agent.

| arm | attacker-canary rate [95% CI], n |
|---|---|
| candidate | 100.0% [88.6, 100.0] (n=30) |
| clean | 0.0% [0.0, 11.4] (n=30) |
| mechanism_control | 0.0% [0.0, 11.4] (n=30) |
| naive | 0.0% [0.0, 11.4] (n=30) |
| reject_control | 0.0% [0.0, 11.4] (n=30) |

- provenance/type/parse/utility invariants: 100%
- candidate mechanism: unsafe conversion drops provenance and upgrades trust
- next gate: run an independent local-model implementation only after full-text screen and protocol freeze
