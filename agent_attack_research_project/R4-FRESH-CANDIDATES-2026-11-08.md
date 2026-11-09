# R4 fresh candidate screen — 2026-11-08

**Rule:** no model run or expensive experiment is authorized from this file. Each item needs a full-text/public
pre-emption check and a falsifiable one-variable design before it can enter `CLAIMS.md`.

## Q1 — validator/executor parser differential at an inter-agent handoff

**Status:** initial full-text/public screen passed; C4 registered; deterministic mock gate passed; independent implementation pending.

**Provisional mechanism.** An upstream Agent or project-owned adapter emits one serialized structured handoff. The
validator and executor parse the same bytes with different rules: for example, duplicate-key handling, Unicode
canonicalization, alternate field names or first-key/last-key resolution. The validator approves a safe canary while the
executor resolves an attacker-chosen canary. The attack is a split between validation semantics and execution semantics,
not a change in model preference.

**One-variable intervention.** Keep the serialized bytes, task, model-visible message, schema and canary task fixed;
vary only whether the envelope is canonical or parser-ambiguous. Candidate and mechanism-control use the same visible
value and task. The exact evaluator records raw bytes, parser ASTs, validation decision, execution AST and final canary.

**Threat model.** The attacker controls one synthetic upstream value or serialized handoff field in a project-owned
sandbox. They cannot modify model weights, system prompts, validator code, executor code or real tools. The executor is a
fixed no-side-effect canary. No real JSON/tool payload, credential, URL or live service is used.

**Controls.** Canonical JSON with one parser; duplicate-key rejection; canonical reserialization before validation and
execution; Unicode normalization; unknown-field rejection; a benign trusted envelope; and a parser-pair control in which
validator and executor share the same canonical AST.

**Kill switches.** Full-text work already evaluates the same validator/executor differential at an Agent handoff; both
components always produce the same AST; the effect disappears when raw bytes are canonicalized; or the result is only a
library-specific implementation defect with no Agent/security mechanism worth studying.

**Potential contribution if it survives.** A benchmark dimension for semantic non-equivalence between security
validation and Agent execution at structured message boundaries, with exact byte/AST traces and a canonicalization
defense. This wording remains a hypothesis and must not be called novel yet.

## Screened out before any experiment

### Q2 — provenance-blind semantic result-cache collision

**Verdict:** pre-empted/overlap. Semantic cache poisoning and cache-key collision work directly covers response
hijacking; persistent-memory provenance work covers origin-bound defenses. A cache-specific Agent benchmark would need a
new cross-agent mechanism beyond cache poisoning and is not authorized.

### Q3 — capability union at fan-in

**Verdict:** pre-empted/overlap. Current delegated-capability work and security standards explicitly address authority
attenuation, amplification, fan-in and purpose-bound capabilities. No experiment is authorized from the generic union
hypothesis.

### Q4 — monitor-verdict disagreement compression

**Verdict:** pre-empted/overlap. Recent work studies local monitors missing compositional harm, disagreement-aware
moderation and provenance-linked verdicts. A majority-vote or dissent-suppression matrix would be incremental unless a
new state transition is identified.

### Q5 — failure-status or verification-state laundering

**Verdict:** pre-empted/overlap. Recent work directly studies verification-status laundering, endogenous authorization
laundering and typed failure/structured delegation state. No experiment is authorized.

## Evidence leads for Q1

- **Output Constraints as Attack Surface:** <https://arxiv.org/abs/2503.24191>. Full-text/public check completed:
  EnumAttack and DictAttack steer grammar-guided generation, but the paper does not compare inconsistent validator and
  executor parsers or inter-agent serialized handoffs. It is adjacent structured-generation work, not a direct Q1 match.
- **General parser-differential security:** <https://www.cs.dartmouth.edu/~sws/pubs/as23.pdf>. General security
  background; not an Agent Attack result.
- **Agent session smuggling:** <https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/>.
  Implementation threat report covering stateful A2A instruction smuggling, not parser differential; verify full text if
  the endpoint becomes available.
- **Tool parser implementation lead:** <https://pypi.org/project/agent-tool-parser/>. Library lead only; the page was
  not independently readable in this pass and is not evidence of novelty.
- **Parser differential implementation advisory lead:**
  <https://github.com/theagentrouter/agent-router/security/advisories/GHSA-4gph-2hhr-5mwg>. Advisory endpoint was
  inaccessible to the fetch tool; treat as an unverified lead, not a paper fact.
- **Multi-agent compositional monitoring:** <https://arxiv.org/abs/2607.11751>. Directly adjacent local-monitor
  composition work; it does not describe parser differentials in the supplied abstract.

## Next gate

Register a precise Q1 claim only after freezing the parser-pair semantics and running the deterministic mock gate. The
claim must remain scoped to validator/executor semantic non-equivalence at an inter-agent structured boundary; it must
not claim that malformed JSON is a general LLM vulnerability. The mock must pass before any local-model formatting probe.
