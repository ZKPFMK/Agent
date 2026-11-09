# R6 fresh public pre-emption screen — P4 typed handoff

**Date:** 2026-11-08  
**Status:** P4 is closed as an ACL paper candidate; experiments are preserved as a protocol boundary result

## Evidence standard

The EMNLP and REALM papers below were checked from official ACL Anthology pages and downloaded PDF text. PACE,
ToolFence, AuthGraph and AGATE were checked from their public abstracts. Search-result summaries were not used as
standalone evidence.

## Direct or adjacent work

### Trust Cascade through Provenance Erasure

Official page: <https://aclanthology.org/2026.emnlp-main.1005/>  
PDF: <https://aclanthology.org/2026.emnlp-main.1005.pdf>

**Full-text verified.** Zhou et al., EMNLP 2026, studies a two-agent natural-language delegation boundary. Section 3.2
defines provenance erasure as preserving actionable content while removing format markers, authority entities and source
attribution. Section 3.3 measures follower trust reclassification after the boundary. Section 4.4 calls this a structural
mechanism, and the paper evaluates a provenance auditor at the delegation boundary. The appendix includes marker
ablation and a future direction for structured delegation protocols.

**Overlap decision.** The broad P4 statement that a delegation boundary can erase provenance and reclassify an
attacker-controlled instruction into a trusted channel is directly pre-empted. P4 cannot claim provenance erasure at a
multi-agent handoff as its novelty.

**Remaining distinction.** The checked paper uses natural-language delegation and channel trust. It does not, in the
checked sections, isolate a typed/opaque schema conversion in which candidate and source-preserving control expose
byte-equivalent value/type/task fields while a deterministic authorization gate consumes hidden provenance metadata.
This distinction is an overlap-risk hypothesis, not a novelty claim.

### Lost in the Handoff: Contract-Aware Compliance Checking for Multi-Agent LLM Systems

Official page: <https://aclanthology.org/2026.realm-1.89/>  
PDF: <https://aclanthology.org/2026.realm-1.89.pdf>

**Full-text verified.** He et al., REALM 2026, studies routing, privacy and instruction constraint loss at agent-message
handoffs. C2-FAIC keeps contracts outside agent context and checks candidate messages before shared-trace admission.
The paper does not present provenance tracking, authority laundering or typed conversion as the attack mechanism.

**Overlap decision.** It pre-empts a generic “handoff loses requirements” framing but leaves the typed provenance-to-
authorization transition as a narrower adjacent question.

### Provenance-aware authorization and runtime defenses

- **PACE:** <https://arxiv.org/abs/2610.01349>. The abstract covers provenance-aware capability and effect enforcement
  before tool execution; it does not state a cross-agent typed handoff conversion attack.
- **ToolFence:** <https://arxiv.org/abs/2609.37196>. The abstract covers typed authorization plans, value provenance and
  within-tool argument manipulation; it does not state inter-agent typed conversion.
- **AuthGraph:** <https://arxiv.org/abs/2605.26497>. The abstract covers execution provenance versus user-intent
  authorization graphs and final tool arguments; it does not state cross-agent handoff conversion.
- **AGATE:** <https://arxiv.org/abs/2609.30830>. The abstract covers provenance and authorization at instrumented
  agent-harness boundaries and compositional attacks; it does not state typed inter-agent conversion.

These works make the narrow P4 claim harder to position. A paper must demonstrate a mechanism-level delta beyond
provenance auditing, capability enforcement and final parameter authorization.

### Additional narrow-delta screen

- **Agent Memory Is a Surface for Endogenous Authorization Laundering:** <https://arxiv.org/abs/2609.01836> directly
  studies typed-memory updates that make forbidden actions appear authorized. It is a different state surface, but it
  removes authority laundering as a new label by itself.
- **Memory Provenance Laundering in LLM Agents:** <https://arxiv.org/abs/2607.29167> studies lossy consolidation
  that rewrites untrusted observations as user history or workflow guidance, then checks memory authority against tool
  risk. It is not a handoff experiment, but it covers authority upgrades through a lossy representation boundary.
- **Securing LLM-Agent Long-Term Memory Against Poisoning:** <https://arxiv.org/abs/2606.24322> binds authority to
  origin and studies non-malleable provenance under summarization, trusted-tool echoes and fabricated corroboration.
- **The Provenance Paradox in Multi-Agent LLM Routing:** <https://arxiv.org/abs/2603.18043> introduces structured
  delegation contracts, attested identity and typed failure semantics. It does not present P4's exact conversion attack,
  but it makes structured delegation/provenance contracts prior art.
- **Can CaMeLs Talk?:** <https://arxiv.org/abs/2610.05640> explicitly addresses downstream agents treating untrusted
  output as trusted input and proposes provenance-preserving channel separation across agent boundaries.

Taken together, the remaining P4 distinction is an implementation-level combination of known provenance, delegation,
channel and authorization controls. It is not a sufficiently clean mechanism-level ACL thesis under the current
protocol, especially because the measured model response is identical across candidate and control.

## R6 decision

1. Close the broad “provenance erasure across agent delegation” novelty framing as pre-empted by Trust Cascade.
2. Preserve the P4 v2 and Astra experiments as bounded protocol and negative-boundary artifacts. Their candidate/control
   separation is real under the tested deterministic authorization policy, but the model emits the same request in both arms.
3. Keep C3 as an internal bounded experimental record only; do not promote it to a paper contribution or novelty sentence.
4. Close P4 as a paper candidate and return to R4 for a new mechanism. Do not spend more model budget on P4 unless a
   future independent result exposes a materially different attack surface and passes a new full-text screen.
