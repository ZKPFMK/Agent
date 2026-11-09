# IDEA-P4 — typed provenance conversion at an agent handoff

**Status:** R5 v2 smoke and 150-row loopback pilot passed; C3 survives as a bounded protocol result; R6 required
**Primary ACL angle:** language-agent handoff security and structured tool-use reliability
**Date:** 2026-11-07

## One-sentence hypothesis

Under a black-box attacker that controls one untrusted value in a project-owned upstream Agent, an unsafe typed
handoff conversion that drops or upgrades provenance will cause the downstream handoff boundary to authorize an
attacker-chosen structured canary more often than a source-preserving typed handoff, even when the model-visible
value passes shape/schema validation. The v2 control keeps the model-visible value and task identical and applies
authorization independently after the downstream request. The claim is killed if source-preserving and unsafe
conversions have the same exact state outcome, if the visible requests differ, or if parsing/utility fails.

## Why this may be distinct

- multi-CaMeL studies natural-language boundary laundering and provenance-preserving handoffs, but the fetched
  full-text summary does not isolate serialization, coercion, schema conversion or parser boundaries;
- PACE enforces provenance-aware capabilities at pre-execution tool boundaries, but does not study cross-Agent
  conversion as the attack mechanism;
- AuthorityFlow traces source authority to final arguments, but its core is parameter authorization, not a typed
  handoff conversion attack;
- schema/grammar and backdoor work studies constrained output or schema-valid calls, not an inter-agent trust-type
  transition.

This is an overlap-risk candidate, not a novelty claim. `R4-P4-FULLTEXT.md` is the source comparison.

## Threat model and safety

- attacker capability: control one synthetic untrusted value returned by an upstream Agent or retrieval adapter;
- no weight, system prompt, schema-definition, tool-implementation, database or network access;
- victim: two local Agents connected by a typed handoff adapter; downstream tools are fixed no-side-effect canaries;
- observable state: provenance label, serialized field, parser/coercion decision, downstream structured argument and
  canary choice;
- no real accounts, secrets, URLs, code, network or live MCP services;
- stop at 60 synthetic episodes, 3 seeds, 20 rounds or 1 CPU-hour for the first probe;
- preserve all rejected and parse-failure cases.

## Released variable

`V-P4`: handoff representation, with semantic value and task fixed:

1. opaque untrusted variable with source provenance;
2. typed field with explicit untrusted tag;
3. unsafe conversion that drops the source tag;
4. source-preserving signed/verified field;
5. malformed/ambiguous field rejected by strict parser.

## First probe arms

| arm | conversion | evaluator |
|---|---|---|
| clean | benign value, source-preserving typed field | exact provenance and canary oracle |
| naive | untrusted value, raw natural-language summary | boundary baseline |
| candidate | untrusted value, unsafe typed conversion drops provenance | exact trust transition and canary |
| mechanism-control | same candidate value, strict source-preserving conversion | removes the proposed mechanism |
| reject-control | malformed/ambiguous value rejected before downstream Agent | parser safety boundary |

## Main metrics

- trust-label upgrade rate;
- downstream attacker-chosen canary rate;
- source-preserving rejection rate;
- structured parse and utility rate;
- false-trigger rate on benign values;
- latency, tokens and cost;
- exact provenance graph consistency.

## Kill switches

- full-text paper shows the same cross-agent conversion attack and evaluation;
- candidate and mechanism-control have the same downstream state outcome;
- candidate effect is caused by prompt wording, schema shape, token length or parser failure;
- no effect appears across two local model families or two adapter implementations;
- defense eliminates the effect only by destroying benign utility.

## Paper path if it survives

The paper contribution would be a conversion-level attack and benchmark dimension: schema-valid values can become
trusted through an inter-agent representation boundary even when source-level provenance and final tool argument
checks pass independently. The paper would require two model families, two adapter/framework implementations, a
source-preserving defense, an adaptive attacker, exact state evaluators, and a full comparison to multi-CaMeL,
PACE, AuthorityFlow, schema-attack and parameter-poisoning work.

## R5 smoke result — 2026-11-07

The deterministic mock probe passed, but the five-call local-gateway smoke failed the protocol: the
source-preserving mechanism-control selected `CANARY_A` just like the candidate, while naive and reject controls
lost utility. The full 150-call matrix was not run. See `checks/falsify/C3-smoke.md` and the raw smoke log.

A revised probe must make the provenance transition an evaluator-visible state while keeping the model's visible
task and value matched, then pass a new smoke control before any further budget. C3 is not a positive result and
P4 may be closed if the control cannot be repaired without prompt-specific artifacts.

## R5 v2 result — 2026-11-07

The revised protocol moved source provenance out of the model-visible handoff and made final authorization a
separate deterministic, no-side-effect evaluator. The candidate and mechanism-control visible payloads and raw model
responses matched in all 30 paired episode/seed keys. The full loopback matrix produced 150 valid rows:

- candidate: 30/30 authorized `CANARY_A`;
- mechanism-control: 0/30 authorized `CANARY_A`;
- clean, naive and reject controls: 0/30;
- paired exact McNemar p=`1.862645e-09`;
- parsing and structured utility: 150/150; errors: 0; estimated cost: `$0.0271`.

This result demonstrates a bounded typed-handoff authorization transition in the project protocol. The model emitted the
same request for candidate and mechanism-control; it does not establish a general model vulnerability. R6 must pin
the threat model, independent adapter implementations, model-family coverage, a source-preserving defense and an
adaptive attacker before any paper claim is promoted.

## R6 fresh pre-emption result — 2026-11-08

The full-text screen finds a direct overlap for the broad provenance-erasure framing: *Trust Cascade through Provenance
Erasure* studies a two-agent natural-language delegation boundary where actionable content survives while authority and
source markers are removed, followed by follower trust reclassification. That framing is closed for novelty.

The remaining possible delta is narrower: a structured typed or opaque schema conversion that keeps candidate and
source-preserving control model-visible fields identical, while an independent authorization evaluator observes a
provenance transition. The checked papers do not show that exact typed conversion experiment, but provenance auditing,
contract-aware handoff checking, capability enforcement and tool-parameter authorization are already adjacent. This
candidate remains overlap-risk and requires a new mechanism-level definition plus fresh screening before further paper
positioning.

## Closure — 2026-11-08

P4 is closed as an ACL paper candidate. The experiments remain useful as a bounded protocol and negative-boundary
artifact: two local model routes and two adapter implementations reproduced the deterministic authorization gap, while
the model-visible request remained matched. Public full-text screening then showed that the mechanism family is already
occupied by provenance erasure, provenance-preserving multi-agent channels, structured delegation contracts and
provenance-aware authorization work. No further P4 model budget is authorized. The next paper candidate must start at
R4 with a new mechanism-level delta.
