# IDEA-Q1 — validator/executor parser differential at an Agent handoff

**Status:** closed as an ACL paper candidate after R7 public pre-emption; preserve as a parser regression/negative-boundary artifact
**Target venue:** ACL 2027 main conference through ARR

## One-sentence hypothesis

When an attacker controls one serialized structured handoff, a validator and executor that interpret duplicate or
ambiguous fields differently can approve a safe representation while executing an attacker canary; canonical AST binding
and strict duplicate rejection remove the gap.

## Why this is distinct enough to test

- *Output Constraints as Attack Surface* studies malicious schema/grammar constraints steering generation, not two
  components interpreting the same serialized handoff differently.
- Trust Cascade and multi-CaMeL study provenance and trust transitions across agent messages, not parser AST
  non-equivalence between validation and execution.
- Generic parser-differential security is established outside Agent systems; Q1 tests the boundary in a structured
  Agent handoff and records exact validator/executor ASTs.
- This is a protocol/security mechanism claim, not a claim that an LLM spontaneously emits duplicate keys.

This remains an overlap-risk position until R7 checks parser variants, framework behavior and public implementation leads.

## Threat model and safety

The attacker controls one synthetic serialized envelope emitted by an upstream Agent or adapter. They cannot modify
parser code, model weights, system prompts, schema definitions, authorization policy or real tools. The executor is a
fixed in-memory canary. Values are only `CANARY_A` and `CANARY_B`; no network, credentials, URLs, code, project writes
or live MCP services are used.

## Released variable and controls

- candidate: duplicate `target` keys; first-key validator approves `CANARY_B`, last-key executor selects `CANARY_A`;
- canonical control: one safe `target` key;
- canonicalized control: same raw bytes canonicalized before both stages;
- reject control: strict duplicate-key rejection before execution.

The exact evaluator records raw bytes, validator/executor bytes, parser ASTs, validation decision, rejection state,
executed canary, utility and false triggers.

## Current evidence

- Python independent mock: 120 rows; candidate 30/30, all controls 0/30; AST mismatch only candidate;
- independent Node implementation: identical outcomes on all 120 rows;
- loopback Sol and Astra transport smoke: candidate bytes preserved and `CANARY_A` selected; canonical controls select
  `CANARY_B`; zero errors;
- actual `cra_mcp.adapter.ToolBox.call` executor path with a fake in-memory server: candidate 30/30, controls 0/30,
  utility 120/120, false triggers 0;
- R7 grammar matrix: 720 rows across eight variants, three arms and three seeds; nested duplicate, top-level duplicate
  and Unicode-equivalent duplicate variants each produced 30/30 candidate successes and 0/30 canonicalized/reject
  successes; attack-first, tool-field, unknown-field and canonical controls produced no attacker canary;
- the actual `cra_mcp.adapter.ToolBox.call` path reproduced the same adaptive variant set across 240 rows: candidate
  30/30, all controls 0/30, utility 240/240, false triggers 0;
- all runs are bounded protocol or transport evidence; no real tool or production framework was used.

## R7 requirements before paper promotion

1. Initial parser-variant arms and synthetic grammar search are complete: nested, Unicode-equivalent, top-level,
   unknown-field, tool-field, attack-first and canonical controls were recorded in `variant_trials.jsonl`.
2. Compare at least two real adapter/framework execution paths or document why the canonical boundary is framework-
   independent; preserve exact bytes and ASTs.
3. The initial adaptive grammar search is complete and found three candidate variants; expand only if a framework baseline
   requires additional syntax, with no tool invocation.
4. Measure canonicalization/rejection utility, false triggers, latency and parser coverage; report n and 95% CIs.
5. Complete a fresh full-text/public screen of parser-differential, schema-smuggling, tool-call and inter-agent work.
6. Decide whether model calls add evidence. The current mechanism is parser-semantic; model output rates must not be
   used as a substitute for parser coverage.

## Kill switches

- a verified paper directly evaluates the same inter-agent validator/executor parser differential;
- all parser/framework pairs produce one canonical AST;
- adaptive variants cannot create a mismatch beyond duplicate-key toy cases;
- canonicalization/rejection causes unacceptable benign utility loss;
- the result remains an isolated library defect with no reusable Agent boundary or benchmark dimension.

## R7 closure — 2026-11-08

C4 is closed as an ACL paper candidate. R7 expanded the protocol to nested and Unicode-equivalent duplicate keys and
reproduced the effect through the actual `cra_mcp.adapter.ToolBox.call` executor path. The refreshed public screen then
verified a direct MCP Go SDK case-insensitive JSON unmarshalling issue with the same authorization-versus-execution
mismatch; the issue was fixed in go-sdk v1.3.1. Preserve Q1 as a redacted regression and negative-boundary artifact,
not as a novel attack contribution. Return to R4 for a new mechanism.
