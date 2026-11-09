# I1 local-gateway order pilot

This is an exploratory run against the authorized loopback gateway and synthetic evidence only. It does not test a live Agent deployment and does not establish a general vulnerability or novelty claim.

## Group rates

| arm | false-causal-belief rate [95% CI], n | parse/utility rate [95% CI], n |
|---|---|---|
| bridge_swap | 76.7% [59.1, 88.2] (n=30) | 100.0% [88.6, 100.0] (n=30) |
| chronological | 16.7% [7.3, 33.6] (n=30) | 100.0% [88.6, 100.0] (n=30) |
| clean | 0.0% [0.0, 11.4] (n=30) | 100.0% [88.6, 100.0] (n=30) |
| narrative | 56.7% [39.2, 72.6] (n=30) | 100.0% [88.6, 100.0] (n=30) |
| random | 46.7% [30.2, 63.9] (n=30) | 100.0% [88.6, 100.0] (n=30) |

## Paired narrative versus random

- narrative: 56.7% [39.2, 72.6] (n=30)
- random: 46.7% [30.2, 63.9] (n=30)
- discordant pairs: narrative-only=9, random-only=6
- exact McNemar p-value: 0.607239
- estimated tokens: input=27360, output=2100
- estimated cost from gateway metadata: $0.0757 (hard cap $50)
- local truth oracle: 100% required; see raw rows for every episode

## Interpretation gate

The result only updates the exploratory C2 pilot record. It does not support a memory-persistence or downstream-propagation claim, because those blocks were not run. The bridge-swap control failed and D-4 closes I1; preserve this raw log as a negative boundary result. Any future order-direction or semantic-composition idea requires a fresh R4 claim and protocol.
