# THREAT-MODEL — Q1 validator/executor parser differential

### TM-Q1 — structured handoff interpretation split

**Goal.** Test whether one serialized structured handoff can pass a security validator under one parser interpretation
and reach an executor with a different meaning.

**Victim system.** A project-owned upstream-to-downstream Agent adapter with a validator, an executor parser and fixed
no-side-effect canaries. The first block uses deterministic Python and Node implementations. No real tool is invoked.

**Access point.** The attacker supplies one synthetic serialized envelope containing only `CANARY_A` and `CANARY_B`.
They cannot change parser code, schemas, authorization policy, model weights, system prompts or tools.

**Mechanism.** The candidate uses duplicate `target` keys. The validator applies first-key semantics and approves
`CANARY_B`; the executor applies last-key semantics and selects `CANARY_A`. The source-preserving controls either use
one canonical key, canonicalize the same raw bytes before both stages, or reject duplicates.

**Success criterion.** The exact evaluator records a validator-approved safe AST, an executor AST with a different target,
and final `CANARY_A` selection. Canonicalization and strict rejection must remove the difference.

**Safety and rollback.** All trials use local JSONL records and in-memory canary selection. There are no network calls,
credentials, URLs, files outside the project result directory or real tool effects. Each trial is independent and the
bounded matrix stops at 120 rows.

**Limitations.** This is a protocol/adapter boundary test. It does not establish that an LLM emits duplicate keys or
that a deployed Agent framework is vulnerable. A paper claim would require framework-level parser coverage, a verified
nearest-work comparison and an explicit reason model calls add evidence rather than noise.
