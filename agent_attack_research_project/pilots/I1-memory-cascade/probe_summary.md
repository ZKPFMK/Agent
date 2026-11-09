# I1 R5 evidence-order probe

This result uses a deterministic `MockBackend` whose order sensitivity is intentionally synthetic. It validates the experiment harness, paired controls, exact oracle and provenance. It is not a claim about real LLM behaviour.

## Group rates

| arm | false-causal-belief rate [95% CI], n |
|---|---|
| bridge_swap | 13.3% [5.3, 29.7] (n=30) |
| chronological | 3.3% [0.6, 16.7] (n=30) |
| narrative | 83.3% [66.4, 92.7] (n=30) |
| random | 20.0% [9.5, 37.3] (n=30) |

## Paired narrative versus random

- narrative: 83.3% [66.4, 92.7] (n=30)
- random: 20.0% [9.5, 37.3] (n=30)
- discordant pairs: narrative-only=21, random-only=2
- exact McNemar p-value: 0.000066
- local truth oracle: 100% for all 120 records
- utility invariant: 100% for all 120 records

## Gate B verdict

The synthetic candidate should proceed to a mechanism-control review only as a harness demonstration. The result cannot advance to a real-model claim because the backend policy encodes the tested susceptibility.
