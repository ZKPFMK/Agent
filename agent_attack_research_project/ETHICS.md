# ETHICS — I1 memory persistence cascade

> This project is an offline, synthetic, no-side-effect study. `threat-modeler` owns the frozen threat model;
> `submission-rebuttal` would own any later disclosure or release decision.

## Ground rules (project-wide)

- Run only local mock agents and project-owned synthetic testbeds; never live third-party agent products,
  public registries/pages, real users or real accounts.
- Use synthetic event graphs, synthetic evidence fragments and fixed canary strings. Do not store real secrets,
  personal data, credentials, URLs or working external attack payloads.
- Keep the imported research corpus read-only. Do not copy PDFs or private paper material into a release artifact.
- If a later local-model result appears transferable to a deployed product, stop and write a disclosure decision
  before any external communication.

## TM-I1 harm & containment — 2026-11-07

harm: The study could be misread as evidence that truthful evidence is intrinsically unsafe, or could produce a
misleading implementation claim if intermediate state is not logged. Defender value is a controlled test of
provenance, memory-write and cross-agent verification defenses.

containment: offline mock backend; synthetic facts and causal graphs; no network; no real tools; fixed `CANARY_A`
and `CANARY_B`; 30-episode and 20-step caps; reset memory between trials unless persistence is the variable;
raw traces remain in the local project and contain no personal data.

release: redacted — publish methods and aggregate measurements only after falsification; do not release deployable
payloads or live-target procedures.

## Disclosure log (append-only)
| date | vendor / maintainer | channel | what was reported (finding id, no payload here) | response | embargo until | status |
|---|---|---|---|---|---|---|

## Release decision
| artifact item | level (full / redacted / on-request / none) | reason | approved by |
|---|---|---|---|
| synthetic harness and aggregate logs | redacted / on-request | only after claim and privacy checks | pending |
| working external payloads | none | outside scope | pending |
