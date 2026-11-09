# PAPER-GOAL — Agent Attack paper target

## Objective

Produce one defensible Agent Attack paper suitable for submission to **ACL 2027 through ACL Rolling Review (ARR)**. The project is complete only
when it has one central surviving contribution, a reproducible evaluation, a verified related-work position,
responsible research documentation and an artifact that can regenerate the reported results.

I1 is a completed negative direction. Its raw logs and falsification record remain part of the research history,
but I1 is not the paper thesis.

## What counts as a paper contribution

The next direction must contribute at least one mechanism-level result that is distinct from a prompt, model,
dataset, topology or agent-count change. It must explain:

- attacker access and why it is realistic;
- the system state or decision process that changes;
- the mechanism that causes the change;
- the control that removes the mechanism;
- the security consequence and the benign utility trade-off;
- the defense boundary and the limitation.

A benchmark or evaluation contribution is acceptable when it measures a previously unseparated attack mechanism
with independent state checks, meaningful controls and a reproducible task suite. A high attack success rate alone
is not a contribution.

## Minimum evidence bar before writing the main claim

The selected direction should reach these project gates before paper drafting:

- one open claim survives the falsifier and has a precise weakened wording if needed;
- at least two model families or a documented reason a second family is impossible;
- at least two agent frameworks or benchmark environments, or a clearly justified framework-independent testbed;
- clean, naive, proposed and mechanism-control arms on paired tasks and seeds;
- at least one relevant static defense and an adaptive attacker against that defense;
- effectiveness, benign utility, false-trigger, detection/stealth, transfer, latency and cost;
- exact or independently validated evaluation, with human-label agreement for semantic judges;
- every rate has n and a 95% interval, every paper number has an EVIDENCE row, and raw logs are retained;
- full-text related-work verification, a fresh public novelty search and an explicit nearest-paper delta;
- ethics, containment, redaction and artifact-release decisions are complete.

These are the project's quality gates. They do not replace the official ACL 2027 CFP or ARR instructions, which
must be checked again before the R0 gate closes and before submission.

## Current state

- venue record: see `VENUE-RESEARCH.md`
- target venue: ACL 2027 main conference through ARR
- exact venue and deadline: ARR submission deadline 2027-01-04; current ACL/ARR instructions and artifact/ethics rules remain an R0 checklist item
- paper thesis: not selected; R4 must choose a fresh idea after I1's negative result
- active evidence: 54-paper A/B/C corpus and I1 negative result
- available local pilot budget: ≤$50 equivalent through the authorized loopback gateway
- publication status: exploratory; no paper claim is currently promoted

## Selection rule for the next idea

A candidate advances from R4 only if it has a stronger paper path than I1:

1. distinct mechanism after full-text and public novelty checks;
2. a one-variable entry experiment and an independent evaluator;
3. a believable path to two model families or two environments;
4. a defense and adaptive-attacker experiment;
5. an informative negative result even if the main effect fails;
6. safe, reproducible, redacted execution.

I3, tool-metadata preference to persistent routing, is a candidate for screening, not a chosen thesis. It must pass
this selection rule before any claim or model run.

## Writing and release gates

Do not write an abstract or contribution list until the central claim is `survived` or `weakened`. Do not call a
result novel from a local corpus gap. Do not publish a mock-only result as an Agent vulnerability. Do not release
working payloads, secrets, personal data or live-target procedures. Any artifact release requires a human-approved
redaction and disclosure decision.
