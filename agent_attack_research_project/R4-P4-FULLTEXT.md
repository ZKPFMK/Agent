# R4 P4 full-text refinement — typed provenance conversion at agent handoff

**Date:** 2026-11-07
**Status:** candidate after full-text narrowing; C3 registered for a bounded synthetic probe

## Existing overlap

[Can CaMeLs Talk? / Multi-CaMeL](https://arxiv.org/abs/2610.05640) directly covers a natural-language boundary
laundering attack: tainted data from one agent is summarized and inserted into a downstream agent's instruction.
It also evaluates opaque runtime variables and provenance-preserving multi-agent communication.

The paper's experiments and protocol use structured variables (`dict[str, Any]`), Pydantic/output parsing and
runtime handoffs, but the fetched full-text summary states that it does not isolate:

- serialization/deserialization behavior;
- type coercion or malformed structured values;
- schema validation as a security boundary;
- conversion of an opaque variable back into trusted instruction text;
- the conversion layer between variables and downstream tool arguments/output parsers.

## Narrowed candidate

**Typed/provenance conversion attack at an agent handoff:** An attacker controls a value that is untrusted in the
source agent. A formatter, schema adapter, serializer, output parser or tool-argument converter changes its type or
trust representation at the handoff. The downstream agent then consumes the value as a trusted instruction or
high-impact argument even though the original provenance should remain untrusted.

## Proposed mechanism intervention

Keep the same semantic value and task while changing only the handoff representation:

1. opaque untrusted variable with source/provenance preserved;
2. natural-language summary inserted into child instructions;
3. typed structured field with explicit untrusted tag;
4. typed field after an unsafe conversion/coercion;
5. source-preserving signed/verified field;
6. malformed or ambiguous type rejected by the parser.

## Exact evaluator

- provenance graph: source trust label before and after conversion;
- type/schema transition: field type, parser decision and coercion result;
- downstream tool argument or canary choice;
- independent source re-verification;
- benign task utility and false-trigger rate.

No LLM-only judge is needed for the core state transitions.

## Pre-emption status

The candidate is distinct from the natural-language summarization attack only if existing work does not measure the
conversion/coercion boundary as the attack mechanism. The second screen found substantial overlap risk:

- [Output Constraints as Attack Surface](https://arxiv.org/abs/2503.24191) studies malicious behavior encoded in
  schema or grammar constraints;
- [Kerkoporta](https://arxiv.org/abs/2611.00138) studies schema-valid attacker-selected tool calls under triggers;
- [Attractive Metadata Attack](https://arxiv.org/abs/2508.02110) covers structured tool-selection metadata;
- [PACE](https://arxiv.org/abs/2611.04673) uses provenance-aware capability and schema-effect enforcement at tool
  execution;
- [Right Tool, Wrong Parameters / AuthorityFlow](https://arxiv.org/abs/2610.01349) traces authority to tool
  arguments and detects parameter poisoning;
- [OWASP schema/message validation guidance](https://github.com/OWASP/AISVS/blob/main/1.0/research/chapters/C10-MCP-Security/C10-04-Schema-Message-Validation.md)
  covers schema-valid but semantically unsafe values, duplicate keys and structured-message manipulation.

These sources cover most single-boundary schema, argument, provenance and output attacks. The remaining possible
delta is specifically a **cross-agent conversion intervention**: the same value is accepted by a source agent,
serialized into a typed/opaque handoff, coerced or re-parsed by a downstream adapter, and then becomes trusted in a
way that neither source-level provenance nor final tool-argument authorization detects. The full-text screen did not
find a paper that isolates this conversion boundary as its attack mechanism. C3 is registered only for a bounded
synthetic probe; a failed control or a new direct paper closes the direction.
