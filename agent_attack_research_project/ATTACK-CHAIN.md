# ATTACK-CHAIN — I1 memory persistence cascade

Use this file to map corpus evidence and project experiments to the shared chain. Paper facts stay separate from
cross-paper inference.

```text
environment/input -> context/perception/retrieval -> interpretation/planning/routing
-> tool/message -> memory/state/permission -> outcome/propagation/persistence/detection
```

| paper or experiment id | input / environment | context or retrieval | cognition / routing | tool or message | state affected | outcome | evidence level | source |
|---|---|---|---|---|---|---|---|---|
| C18 | attacker selects locally true evidence fragments | Writer/Editor/Director/Sybil composition | order and juxtaposition induce a global causal interpretation | downstream narrative / agent output | belief state; persistent memory not established in summary | false causal belief and downstream deception | abstract-verified | `PAPER-MATRIX.csv` C18; local summary |
| B10 | query-only interaction | memory-generating interaction and later retrieval | bridge steps make a record retrievable | future query response | long-term memory entry / retrieval state | delayed memory injection | abstract-verified | `PAPER-MATRIX.csv` B10; local summary |
| B13 | apparently benign query set | multi-record memory retrieval | cooperative queries jointly guide memory | future agent behavior | long-term memory | hidden multi-record behavior change | abstract-verified | `PAPER-MATRIX.csv` B13; local summary |
| C19 | controlled community knowledge input | retrieval and trusted-platform context | propagation through agent community | messages and shared knowledge | RAG/history storage | pollution persistence and spread | abstract-verified | `PAPER-MATRIX.csv` C19; local summary |
| B02 | controlled image/memory interaction | peer conversation and retrieval | one agent influences peers | peer messages | agent memories | contagious influence | abstract-verified | `PAPER-MATRIX.csv` B02; local summary |
| C04/C07 | malicious or optimized content in one agent | graph routing and retrieval/copying | multi-hop adoption and replication | inter-agent messages | peer beliefs / prompts | propagation and collaboration loss | abstract-verified | `PAPER-MATRIX.csv` C04, C07 |
| I1-block-1 | synthetic fact fragments; attacker controls order only | fixed summary input | causal-edge inference under random / chronological / narrative order | no downstream message; single-agent probe | no persistent memory; belief probe only | false causal-belief rate | inference / planned measurement | `ATTACK-RESEARCH.md`, `experiment_plan.md` |
| I1-block-2 | selected order from block 1 | automatic summary and memory write | later retrieval and planning | fixed canary choice | memory entry and persistence | memory contamination and later false edge | inference / planned measurement | `ATTACK-RESEARCH.md`, `experiment_plan.md` |
| I1-block-3 | same facts and selected memory policy | summary with or without provenance | fixed downstream roles interpret shared summary | downstream message/repetition | downstream belief state | repetition / transfer rate and utility | inference / planned measurement | `ATTACK-RESEARCH.md`, `experiment_plan.md` |

## Mechanism notes

### C18 — local truth versus global causal error

- direct source evidence: the local summary describes individually true fragments whose ordering/juxtaposition can
  induce false causal belief.
- inference made by this project: automatic summarisation may convert a transient interpretation into a stored
  causal edge; this is not established by C18's summary.
- unresolved link: whether memory writes the inferred edge, whether it survives reset, and whether downstream
  agents treat the summary as independent evidence.
- control required: random/chronological order, local-truth oracle, memory-off arm and provenance-preserving arm.

### B10/B13 — query-only memory change

- direct source evidence: the summaries describe query-only or apparently benign query mechanisms affecting future
  memory or behaviour.
- inference made by this project: evidence ordering is a lower-capability input that may produce a related state
  change without direct trigger or database access.
- unresolved link: memory implementation and retrieval threshold may explain the effect.
- control required: no-write, write-then-clear, unrelated-trigger and atomic-provenance controls.

### I1 — planned causal chain

- direct source evidence: adjacent A/B/C rows cover parts of the chain, not one verified unified benchmark.
- inference made by this project: `true fragments -> ordered interpretation -> automatic memory -> downstream
  repetition` is a cross-surface gap candidate.
- unresolved link: first block must establish an order effect before any persistence or collaboration claim.
- control required: release one variable per block and keep intermediate state logs.
