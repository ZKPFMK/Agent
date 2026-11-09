# R4 candidate pool — ACL 2027 paper search

**Date:** 2026-11-07
**Rule:** no claim or model run until full-text and public pre-emption checks pass.

## Screened out

### P1 — same payload, different channel

**Status:** pre-empted / do not run.

The proposed matrix would compare identical content in user message, tool metadata, tool output and route
messages. Existing work directly studies channel trust asymmetry, MCP-layer surfaces and tool-routing benchmarks:
SAS / *Same Payload, Different Channel*, MCP Security Bench and COPEX. See the public screening links in the
session record. A new paper would need an unmeasured mechanism beyond another channel matrix.

### P2 — individually safe defenses fail after handoff composition

**Status:** pre-empted / do not run.

Recent work on multi-CaMeL, conjunctive prompt attacks and beyond-single-model injection already frames trusted
handoffs, individually benign components and provenance-preserving composition. A new contribution would need a
specific state or formal failure mode absent from those papers.

### P3 — duplicated messages manufacture independent corroboration

**Status:** overlap / do not run as stated.

Recent work studies false consensus, Sybil-style multi-agent message duplication and source-correlated evidence.
The local C18/C19 line is also adjacent. Repeating this as a propagation-rate benchmark is insufficient.

## Candidate requiring the next pre-emption pass

### P4 — typed/provenance conversion at an agent handoff

**Status:** candidate after narrowing; no claim registered.

**Existing overlap:** multi-CaMeL directly covers natural-language boundary laundering at agent handoffs. Its
structured variables and output parsing are relevant, but the fetched full text does not isolate serialization,
deserialization, type coercion, schema validation or conversion of opaque variables into trusted tool arguments.
See `R4-P4-FULLTEXT.md`.

**Hypothesis sketch:** An attacker controls a value that is untrusted in the source agent. A formatter, schema
adapter, serializer, output parser or tool-argument converter changes its type or trust representation at the
handoff. The downstream agent consumes it as a trusted instruction or high-impact argument even though its source
provenance should remain untrusted.

**Potential mechanism:** type/provenance conversion at a structured handoff boundary, rather than a raw prompt or
natural-language summary. The intervention keeps semantic value and task fixed while varying opaque untrusted,
explicitly typed untrusted, unsafe coercion, source-preserving signed and rejected malformed representations.

**Potential evaluator:** exact provenance graph, type/schema transition, parser decision, downstream tool argument or
canary choice and utility; no LLM-only judge.

**Potential controls:** source-preserving variable, independent re-verification, strict schema rejection and a
semantically matched benign value.

**Kill switch:** full-text work already measures the same conversion/coercion failure; the trust label changes only
because of prompt wording; or the downstream action disappears under an equivalent source-preserving representation.

**Safety:** synthetic observations, fixed schemas, no real tools or data, local canaries only.

**Next:** screen structured output injection, schema poisoning, unsafe deserialization, typed tool arguments,
Pydantic/JSON coercion and agent handoff provenance before registering a claim.
