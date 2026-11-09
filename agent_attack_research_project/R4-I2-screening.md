# R4 screening — I2 external input to memory to collaboration

**Date:** 2026-11-07
**Status:** overlap / do not run as currently stated
**Paper target:** ICML 2027 primary; next AAAI cycle secondary

## Candidate

I2 proposed measuring whether an external indirect input enters automatic memory, changes a later task and then
propagates through downstream Agents, with intermediate state metrics separating immediate injection from persistence.

## Local-corpus neighbours

A02, A04, A14, B10, B12, C10, C11 and C16 already cover external/context injection, query-only memory change,
message infection and compositional routing. The local cross-category gap treated I2 as an exploratory combination,
not a novelty claim.

## Public pre-emption screen

Recent public work directly covers the proposed state-aware chain:

- [MemSecBench](https://arxiv.org/abs/2607.27080) tracks memory poisoning from persistence through downstream
  execution, external consequences and repair;
- [MPBench](https://arxiv.org/abs/2606.04329) evaluates multiple memory-write channels and structural memory
  vulnerabilities;
- [BackdoorAgent](https://aclanthology.org/2026.findings-acl.791.pdf) instruments planning, memory and tool-use
  stages across multi-step workflows;
- [Trust propagation and structural containment](https://arxiv.org/abs/2609.17648) studies shared-memory poisoning and
  indirect prompt injection in a multi-agent pipeline with containment defenses;
- [Multi-agent memory-poisoning propagation](https://doi.org/10.1145/3806262.3806294) measures propagation depth,
  detection and repair under varying poison ratios.

## Verdict

I2 is **too close to current public benchmark and attack work as stated**. Its intermediate-state decomposition is
useful for our research discipline, but it is not enough for a paper contribution without a new attacker capability,
state mechanism, defense boundary or benchmark dimension demonstrated by full-text comparison.

No I2 claim is registered and no I2 experiment is run.

## Reopen condition

A revised direction must identify a specific unmeasured causal intervention after reading these papers in full. It
must outperform the existing benchmark framing in mechanism clarity, threat realism, control quality and
reproducibility. Otherwise retain I2 as related-work context and move to another R4 idea.
