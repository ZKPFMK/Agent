# RESEARCH-GRAPH — I1 memory persistence cascade

`pi-orchestrator` owns this graph. One node has one owner and one primary output. Independent nodes may run in
parallel only when they write separate scratch outputs; an aggregate file has one synthesis writer.

## Graph state

- **last updated:** 2026-11-08
- **current node:** R4-fresh-2
- **resume rule:** start at the first node whose check is not `PASS`
- **source hash / model snapshot change:** corpus matrix SHA-256 `5c2e7fc2b465660adc9eec9a0634c07debb175993eab058de6af34f4e1e51359`; no model snapshot

## Nodes

| id | node | owner | depends on | primary output | check | status | blocker / next |
|---|---|---|---|---|---|---|---|
| R0 | scope and safety | pi-orchestrator | STATE.md | ATTACK-RESEARCH.md, ETHICS.md, PAPER-GOAL.md | P0 paper scope + safety review | REOPENED | venue/CFP and fresh thesis pending |
| R1 | corpus evidence | lit-scout, kb-curator | R0 | PAPER-MATRIX.csv, LITERATURE.md | `check_framework.py --project .` | PASS | R2 |
| R2 | attack-chain map | lit-scout | R1 | ATTACK-CHAIN.md, taxonomy notes | required axes and evidence levels present | PASS | R3 |
| R3 | cross-surface gaps | kb-curator, lit-scout | R1, R2 | GAP-MATRIX.md, KB-POSITION.md | A×B, A×C, B×C, A×B×C have paper IDs | PASS | R4 idea selection |
| R4 | candidate hypotheses | idea-miner | R3 | IDEA-BRIEF-P4.md, IDEAS.md, C3 | one variable, mechanism, control and kill switch | PASS (P4) | C3 v2 survives bounded protocol pilot; R6 required |
| R5 | cheap probes | idea-miner, experimenter | R4 | `pilots/P4-typed-handoff/` | clean, naive and mechanism control; 3 seeds | PASS (v2) | 150-row loopback pilot passed raw recomputation |
| R6 | threat and protocol | threat-modeler, experimenter | R5 | THREAT-MODEL-P4.md, `results/2026-11-07-p4-typed-handoff-v2/PROTOCOL.md` | threat validator, independent raw evaluator and public pre-emption screen | CLOSED (P4 paper candidate); CLOSED (I1) | P4 records retained as protocol/negative-boundary artifacts; R4 fresh idea required |
| R7 | fair baselines | baseline-engineer | R6 | baselines/MANIFEST.md, IDEA-BRIEF-Q1.md | pinned parser variants, framework discrepancy log and adaptive grammar manifest | IN PROGRESS (Q1) | C4 bounded survivor; paper promotion waits for R7 |
| R8 | main measurement | experimenter | R6, R7 | results/, EVIDENCE.md | n, CI, utility, false-trigger, detection, cost | NOT STARTED | no surviving mechanism |
| R9 | falsification | falsifier | R4, R8 | CLAIMS.md, `checks/falsify/` | no open paper claims | PASS (current claims) | C1 weakened; C2 refuted |
| R10 | paper and review | writer, figure-artist, reviewer-sim | R9 | paper/, REVIEWS.md, SUBMISSION.md | claim/evidence/audit checks | NOT STARTED | no paper claim promoted |

## Node record

### R0 — 2026-11-07 — GO
- owner: pi-orchestrator
- inputs and source hashes: user brief; `research_attack_ideas/paper_matrix.csv` SHA-256 `5c2e7fc2b465660adc9eec9a0634c07debb175993eab058de6af34f4e1e51359`
- output: ATTACK-RESEARCH.md, ETHICS.md, STATE.md P0 scope
- check command and exit status: `check_framework.py --project .` pending final R1 artifact check; scope safety review completed
- evidence: `research_attack_ideas/idea_ranking.md` ranks I1 first; `experiment_plan.md` defines a synthetic, no-side-effect plan
- failed controls or blockers: venue is provisional and waived for exploratory work
- decision / DECISIONS id: D-1
- next node: R1
- do not repeat: do not infer paper facts from filenames or run any live target

### R1 — 2026-11-07 — GO
- owner: lit-scout / kb-curator
- inputs and source hashes: imported `PAPER-MATRIX.csv`; corpus matrix SHA-256 `5c2e7fc2b465660adc9eec9a0634c07debb175993eab058de6af34f4e1e51359`
- output: `LITERATURE.md` and evidence crosswalk
- check command and exit status: `python3 -I Agent-Attack-Research/skills/agent-attack-research/scripts/check_framework.py --project agent_attack_research_project` → 0
- evidence: eight nearest rows linked to C18, B10, B13, C19, B02, C04, C07 and C12; no full-text claim upgraded
- failed controls or blockers: public 30-day novelty search and full-text checks pending
- decision / DECISIONS id: none
- next node: R2
- do not repeat: do not treat summary-level numbers as project measurements

### R2 — 2026-11-07 — GO
- owner: lit-scout
- inputs and source hashes: `PAPER-MATRIX.csv`, `LITERATURE.md`, local category comparison and gap analysis
- output: `ATTACK-CHAIN.md`
- check command and exit status: required input/state/outcome columns reviewed; 0 missing source labels in the written rows
- evidence: C18/B10/B13/C19 mapped to distinct input, cognition, message, state and outcome links
- failed controls or blockers: memory write and downstream provenance links remain inference until measured
- decision / DECISIONS id: none
- next node: R3
- do not repeat: do not collapse belief, memory pollution and propagation into one ASR

### R3 — 2026-11-07 — GO
- owner: kb-curator / lit-scout
- inputs and source hashes: `ATTACK-CHAIN.md`, local `cross_category_gaps.md`, `category_comparison.md`
- output: `GAP-MATRIX.md`, `KB-POSITION.md`
- check command and exit status: A×B, A×C, B×C and A×B×C rows each contain motivating IDs and a separating experiment
- evidence: I1 positioned as overlap-risk with a measurable state-and-propagation delta
- failed controls or blockers: no public novelty search; defenses not yet imported or pinned
- decision / DECISIONS id: none
- next node: R4
- do not repeat: do not call I1 novel before full-text and public pre-emption checks

### R4 — 2026-11-07 — GO
- owner: idea-miner / pi-orchestrator
- inputs and source hashes: `GAP-MATRIX.md`, `KB-POSITION.md`, `PAPER-MATRIX.csv`; C18/B10/B13/C19 overlap risk preserved
- output: `IDEA-BRIEF.md`, `IDEAS.md`, claim C1
- check command and exit status: one released variable, one mechanism control, independent exact evaluator and kill switch recorded
- evidence: C1 registered before probe; R5 design separates order, memory and downstream aggregation
- failed controls or blockers: full-text/public novelty search pending; no real-model budget
- decision / DECISIONS id: D-2
- next node: R5
- do not repeat: do not treat a proposed cascade as a result

### R5 — 2026-11-07 — GO (mock-only)
- owner: idea-miner / experimenter
- inputs and source hashes: `IDEA-BRIEF.md`, `ATTACK-RESEARCH.md`; local toolkit code; no external model
- output: `pilots/I1-memory-cascade/trials.jsonl`, `probe_summary.md`, `checks/falsify/C1/check.md`
- check command and exit status: `python3 -I pilots/I1-memory-cascade/run_probe.py` and `analyze_probe.py` → 0; 120 rows, local truth and utility invariants pass
- evidence: narrative 25/30 versus random 6/30; bridge-swap 4/30; paired McNemar p=0.000066
- failed controls or blockers: mock policy encodes adjacency sensitivity; result cannot support real-agent or novelty claim
- decision / DECISIONS id: D-2; C1 weakened
- next node: R6 only after model/backend and budget selection
- do not repeat: do not report mock rates as LLM attack rates

### R6 — 2026-11-07 — UNCERTAIN / BLOCKED
- owner: threat-modeler / experimenter
- inputs and source hashes: weakened C1, `ATTACK-RESEARCH.md`, `ETHICS.md`, R5 raw log and D-2
- output: `THREAT-MODEL.md`, `threat/I1-memory-cascade.json`, `results/2026-11-07-i1-memory-cascade/PROTOCOL.md`
- check command and exit status: `aa threat-check threat/I1-memory-cascade.json` → threat model OK
- evidence: protocol has separated order, memory and downstream blocks plus exact evaluators and kill criteria
- failed controls or blockers: no permitted model/backend, venue or budget selected; no real run authorized
- decision / DECISIONS id: D-2
- next node: human selects model/backend and budget, or close I1 as a mock-only boundary
- do not repeat: do not begin R8 or call an external model while the execution gate is unchecked

### R6 completion — 2026-11-07 — GO / CLOSED
- owner: threat-modeler / experimenter
- inputs and source hashes: loopback gateway `auto/gpt-6.1-sol`, `real_trials.jsonl`, D-3; estimated cost $0.0757
- output: complete 150-row order pilot and `real_probe_summary.md`
- check command and exit status: `analyze_real_probe.py --expected 150` → 0; `checks/falsify/C2/check.py` → 0
- evidence: all arms parse/utility-valid; local truth 150/150; narrative 17/30, random 14/30, bridge-swap 23/30
- failed controls or blockers: primary comparison p=0.607239; bridge-swap control exceeded narrative
- decision / DECISIONS id: D-3, D-4; C2 refuted and I1 closed
- next node: R4 for a fresh idea, or close the project
- do not repeat: do not run memory/downstream blocks for I1

### R9 current-claim review — 2026-11-07 — GO
- owner: falsifier
- inputs and source hashes: C1/C2, mock and local raw logs, threat model and protocol
- output: `CLAIMS.md`, `checks/falsify/C1/`, `checks/falsify/C2/`
- check command and exit status: C1 weakened; C2 refuted; no open claim remains for the closed I1 direction
- evidence: raw logs and exact evaluators are preserved; no EVIDENCE row promoted to paper
- failed controls or blockers: full-text novelty and defense search remain pending for any new direction
- decision / DECISIONS id: D-2, D-3, D-4
- next node: R4 fresh gap/idea selection
- do not repeat: do not reuse C2 as a positive result

### R0 paper reset — 2026-11-07 — PARTIAL
- owner: pi-orchestrator
- inputs and source hashes: PAPER-GOAL.md, D-5, D-6, 54-paper matrix SHA-256 `5c2e7fc2b465660adc9eec9a0634c07debb175993eab058de6af34f4e1e51359`, I1 negative logs
- output: PAPER-GOAL.md, VENUE-RESEARCH.md, ICML/AAAI target decision
- check command and exit status: official AAAI-27 and ICML-27 pages checked; P0 thesis/CFP gate remains open
- evidence: AAAI-27 full-paper deadline 2026-07-28 passed; ICML-27 CFP/deadline not posted; I1 C2 refuted
- failed controls or blockers: exact ICML submission deadline and new R4 thesis not selected
- decision / DECISIONS id: D-5, D-6
- next node: R4 fresh idea screening while monitoring ICML CFP
- do not repeat: do not write paper contributions from I1's failed mechanism

### R0 venue correction — 2026-11-07 — PARTIAL
- owner: pi-orchestrator
- inputs and source hashes: user venue selection, `VENUE-RESEARCH.md`, official ACL 2027 call
- output: ACL 2027 ARR target and 2027-01-04 submission deadline
- check command and exit status: official ACL pages checked; P0 gate remains open for format/ethics/artifact details
- evidence: `https://2027.aclweb.org/`, `https://www.aclweb.org/portal/content/acl-2027-first-call-papers`
- failed controls or blockers: fresh paper thesis not selected; ACL/ARR checklist still needs review
- decision / DECISIONS id: D-9
- next node: R4 fresh idea screening and ACL-specific paper planning
- do not repeat: do not plan against the superseded ICML/AAAI target

### R4-I2 screen — 2026-11-07 — NO-GO
- owner: idea-miner / lit-scout
- inputs and source hashes: local A/B/C gaps; public pre-emption screen recorded in R4-I2-screening.md
- output: `R4-I2-screening.md`
- check command and exit status: MemSecBench, MPBench, BackdoorAgent and trust-propagation work cover the proposed chain; no claim or model run
- evidence: public sources listed with direct links in the screening record
- failed controls or blockers: I2 as stated lacks a mechanism-level delta
- decision / DECISIONS id: D-8
- next node: R4 new idea generation or a revised full-text-backed I2
- do not repeat: do not call state-aware decomposition alone a novel contribution

### R4-P4 candidate — 2026-11-07 — GO TO R5
- owner: idea-miner / lit-scout
- inputs and source hashes: `R4-P4-FULLTEXT.md`, multi-CaMeL/PACE/AuthorityFlow/schema screens
- output: `IDEA-BRIEF-P4.md`, claim C3
- check command and exit status: full-text screen found no paper isolating the cross-agent typed conversion boundary; C3 registered before probe
- evidence: candidate is limited to source/provenance loss during typed/opaque handoff; no novelty wording yet
- failed controls or blockers: local model pilot and second adapter implementation pending
- decision / DECISIONS id: none
- next node: R5-P4 local pilot
- do not repeat: do not equate schema-valid single-agent output attacks with this handoff candidate

### R4-I3 screen — 2026-11-07 — NO-GO
- owner: idea-miner / lit-scout
- inputs and source hashes: local A10/A11/A19/B13/B14/C17 neighbours; public screen recorded in R4-I3-screening.md
- output: `R4-I3-screening.md`
- check command and exit status: public pre-emption screen found MCPTox, MCP-ITP, MemMorph and A2M overlap; no claim or model run
- evidence: direct or near-direct persistent tool-selection/tool-poisoning work listed with URLs
- failed controls or blockers: I3 as stated lacks a mechanism-level delta
- decision / DECISIONS id: D-7
- next node: R4 new idea generation or a revised full-text-backed I3
- do not repeat: do not treat persistent preference, more tasks or more Agents as novel by itself

### R5-P4 v2 — 2026-11-08 — GO
- owner: experimenter / falsifier
- inputs and source hashes: `PROTOCOL-v2.md`, local loopback route `auto/gpt-6.1-sol`, v2 mock and raw pilot logs
- output: `pilots/P4-typed-handoff/v2_real_trials.jsonl`, `v2_real_analysis.json`, `checks/falsify/C3-v2.md`
- check command and exit status: `analyze_v2.py --expected 150` → 0; candidate 30/30 vs mechanism-control 0/30; raw-pair equality and utility invariants pass
- evidence: candidate/control visible handoffs and raw responses matched in all 30 paired keys; estimated cost `$0.0271`
- failed controls or blockers: final outcome is deterministic authorization, so model-family and adapter generalization remain untested
- decision / DECISIONS id: D-11
- next node: R6-P4 threat and protocol review
- do not repeat: do not label the bounded authorization transition as a general model vulnerability or novelty claim

### R6-P4 — 2026-11-08 — PARTIAL
- owner: threat-modeler / experimenter
- inputs and source hashes: v2 raw pilot, C3-v2 recomputation, P4 threat model and ACL paper goal
- output: `THREAT-MODEL-P4.md`, `threat/P4-typed-handoff-v2.json`, `results/2026-11-07-p4-typed-handoff-v2/PROTOCOL.md`
- check command and exit status: framework threat validator → threat model OK; project checker → PASS; raw evaluator → PASS
- evidence: access point, capabilities, safety boundary, exact success criterion, source-preserving defense and rollback are recorded
- failed controls or blockers: Astra replication and deterministic defense passed; public pre-emption found direct overlap for broad provenance erasure; typed-conversion delta remains unscreened
- decision / DECISIONS id: D-11, D-12
- next node: R4-P4 narrowing before any R7 baseline
- do not repeat: do not proceed to paper writing or R7 claim promotion before the remaining kill gates pass

### R6-P4 pre-emption — 2026-11-08 — NO-GO (broad) / PARTIAL (narrow)
- owner: lit-scout / pi-orchestrator
- inputs and source hashes: official ACL Anthology pages and PDFs for Trust Cascade and Lost in the Handoff; public abstracts for PACE, ToolFence, AuthGraph and AGATE
- output: `R6-P4-screening-2026-11-08.md`
- check command and exit status: official full-text/abstract comparison completed; broad provenance-erasure mechanism directly overlaps Trust Cascade
- evidence: Trust Cascade Sections 3.2–3.4 and 4.4 cover delegation provenance erasure and follower trust reclassification; no checked section isolates P4's typed/schema conversion
- failed controls or blockers: broad P4 novelty framing is closed; the narrow typed-conversion delta needs a new R4 claim and pre-emption screen
- decision / DECISIONS id: D-12
- next node: R4-P4-narrowing
- do not repeat: do not call any provenance-erasure-at-delegation result novel after Trust Cascade

### P4 closure — 2026-11-08 — CLOSED
- owner: pi-orchestrator
- inputs and source hashes: R6-P4-screening-2026-11-08.md; Trust Cascade, multi-CaMeL, structured delegation, authority-laundering and provenance-aware authorization sources
- output: `IDEA-BRIEF-P4.md`, `IDEAS.md`, `CLAIMS.md`, `DECISIONS.md` D-13
- check command and exit status: full-text/public pre-emption screen completed; no clean ACL mechanism-level delta remained
- evidence: P4 v2 and Astra replication are preserved raw protocol results; model-visible candidate/control responses match
- failed controls or blockers: P4 is not a paper thesis; a fresh R4 mechanism and claim are required
- decision / DECISIONS id: D-13
- next node: R4-fresh
- do not repeat: do not spend new model budget on P4 or relabel its bounded protocol result as novelty

### R4 fresh candidate screen — 2026-11-08 — PARTIAL
- owner: idea-miner / lit-scout / pi-orchestrator
- inputs and source hashes: `GAP-MATRIX.md`, `KB-POSITION.md`, `PAPER-GOAL.md`, recent public parser/security leads
- output: `R4-FRESH-CANDIDATES-2026-11-08.md`
- check command and exit status: candidate screen completed; Q1 retained for full-text/public pre-emption; Q2-Q5 rejected before claims or experiments
- evidence: Q1 is a validator/executor parser differential at a structured handoff; direct arXiv search found no exact duplicate-key/parser-differential Agent paper; implementation leads remain unverified
- failed controls or blockers: Q1 may collapse into generic parser security or existing output-constraint work; no claim or model run authorized
- decision / DECISIONS id: none yet
- next node: R4-Q1-screening
- do not repeat: do not call the parser candidate novel from absence of search hits or run it before full-text comparison

### R5-Q1 mock — 2026-11-08 — GO (mock-only)
- owner: experimenter / falsifier
- inputs and source hashes: C4, `R4-FRESH-CANDIDATES-2026-11-08.md`, `pilots/Q1-parser-differential/PROTOCOL.md`
- output: `pilots/Q1-parser-differential/trials.jsonl`, `analysis.json`
- check command and exit status: `run_mock.py` then `analyze.py` → 0; 120 rows; candidate 30/30 and all controls 0/30
- evidence: validator/executor AST mismatch occurs only in candidate; canonicalization and rejection remove the effect; utility 120/120; false triggers 0
- failed controls or blockers: deterministic parser instrumentation only; independent parser/framework implementation and any real-agent integration remain untested
- decision / DECISIONS id: none yet
- next node: R6-Q1 independent implementation
- do not repeat: do not promote C4 from a mock result or execute any real tool

### R6-Q1 independent implementation — 2026-11-08 — GO (bounded)
- owner: experimenter / falsifier
- inputs and source hashes: C4, Python Q1 mock, Q1 protocol
- output: `pilots/Q1-parser-differential/run_node_probe.js`, `node_trials.jsonl`, `node_analysis.json`
- check command and exit status: `node --check run_node_probe.js` and Node probe → 0; Python/Node outcome comparison → 0
- evidence: candidate 30/30, controls 0/30, AST mismatch 30/30 only candidate, utility 120/120, false triggers 0 in both implementations
- failed controls or blockers: parser boundary is reproduced, but Agent framework integration and model evidence value remain unresolved
- decision / DECISIONS id: none yet
- next node: R6-Q1 protocol review
- do not repeat: do not call two deterministic parsers a general Agent vulnerability or paper result

### R6-Q1 protocol — 2026-11-08 — PARTIAL
- owner: threat-modeler / pi-orchestrator
- inputs and source hashes: C4, Python/Node raw logs, Q1 protocol and independent parser comparison
- output: `THREAT-MODEL-Q1.md`, `threat/Q1-parser-differential.json`, `results/2026-11-08-q1-parser-differential/PROTOCOL.md`
- check command and exit status: framework threat validator → threat model OK; project checker → PASS
- evidence: attacker access, parser-boundary success criterion, canonicalization/rejection defenses, rollback and no-side-effect safety are frozen
- failed controls or blockers: C4 remains open; model/framework integration may add no evidence because the mechanism is parser-semantic
- decision / DECISIONS id: none yet
- next node: R6-Q1 integration decision
- do not repeat: do not run a live tool or promote C4 before deciding what independent evidence the model can add

### R6-Q1 transport smoke — 2026-11-08 — GO (smoke-only)
- owner: experimenter / falsifier
- inputs and source hashes: C4, Q1 threat model, Python/Node parser pair, loopback gateway routes `auto/gpt-6.1-sol` and `auto/gpt-6-astra`
- output: `pilots/Q1-parser-differential/sol_model_smoke_trials.jsonl`, `astra_model_smoke_trials.jsonl`, summaries
- check command and exit status: bounded four-row smoke per route → 0; candidate bytes preserved and final `CANARY_A`; canonical controls final `CANARY_B`; zero errors
- evidence: transport integration reproduces the protocol effect under two local model routes; strict rejection makes no model call
- failed controls or blockers: this is not a model vulnerability result; framework-level parser coverage and full C4 falsification remain open
- decision / DECISIONS id: none yet
- next node: R6-Q1 integration decision
- do not repeat: do not expand to a full model matrix until a framework-level evidence plan is justified

### R6-Q1 toolkit adapter — 2026-11-08 — GO (bounded)
- owner: experimenter / falsifier
- inputs and source hashes: C4, Q1 threat model, `cra_mcp.adapter.ToolBox.call`
- output: `pilots/Q1-parser-differential/cra_mcp_probe.py`, `cra_mcp_trials.jsonl`, `cra_mcp_analysis.json`
- check command and exit status: toolkit executor-path probe → 0; candidate 30/30, controls 0/30, utility 120/120, false triggers 0
- evidence: actual `ToolBox.call` JSON executor path consumed duplicate-key bytes; fake in-memory server recorded only local arguments
- failed controls or blockers: no project mutation or real tool execution; C4 remains a protocol-level open claim
- decision / DECISIONS id: none yet
- next node: R6-Q1 integration decision
- do not repeat: do not interpret toolkit parser reproduction as framework prevalence or an LLM vulnerability

### D-15 / R7-Q1 handoff — 2026-11-08 — GO (bounded)
- owner: pi-orchestrator / baseline-engineer / experimenter / falsifier
- inputs and source hashes: C4, Q1 threat model, Python/Node/ToolBox/transport artifacts
- output: `IDEA-BRIEF-Q1.md`, D-15, R7-Q1 task
- check command and exit status: C4 protocol checks all pass; no real side effect; paper claim remains gated
- evidence: parser differential converges across two runtimes, toolkit executor path and two local transport routes
- failed controls or blockers: parser variants, framework baselines, adaptive grammar search and full-text refresh pending
- decision / DECISIONS id: D-15
- next node: R7-Q1
- do not repeat: do not run a full model matrix or write the paper contribution before R7 evidence passes

### R7-Q1 grammar matrix — 2026-11-08 — GO (bounded)
- owner: experimenter / falsifier
- inputs and source hashes: C4, IDEA-BRIEF-Q1.md, Q1 parser pair and defenses
- output: `pilots/Q1-parser-differential/variant_trials.jsonl`, `variant_summary.json`
- check command and exit status: `run_variants.py` then `analyze_variants.py` → 0; 720 rows; utility 720/720; false triggers 0
- evidence: top-level, nested and Unicode-equivalent duplicates produce candidate-only execution; canonicalization/rejection remove them; other grammar controls do not trigger
- failed controls or blockers: framework baseline and refreshed public parser/schema screen pending
- decision / DECISIONS id: D-15
- next node: R7-Q1 framework baseline
- do not repeat: do not call adaptive grammar coverage a paper result until framework and public screens pass

### R7-Q1 cra_mcp variant baseline — 2026-11-08 — GO (bounded)
- owner: experimenter / falsifier
- inputs and source hashes: C4, R7 generic grammar matrix, `cra_mcp.adapter.ToolBox.call`
- output: `pilots/Q1-parser-differential/cra_mcp_variants.py`, `cra_mcp_variant_trials.jsonl`, `cra_mcp_variant_summary.json`
- check command and exit status: toolkit variant probe → 0; candidate 30/30, controls 0/30, utility 240/240, false triggers 0
- evidence: nested, top-level and Unicode-equivalent variants reproduce through the actual executor parser path
- failed controls or blockers: public parser/schema-smuggling screen and final R7 review pending
- decision / DECISIONS id: D-15
- next node: R7-Q1 public screen and review
- do not repeat: do not promote C4 before public nearest-work screening passes

### D-16 / C4 closure — 2026-11-08 — CLOSED
- owner: pi-orchestrator / lit-scout
- inputs and source hashes: R7 parser matrices, `R7-Q1-screening-2026-11-08.md`, MCP Go SDK issue #805 and ATR-2026-02350
- output: `IDEA-BRIEF-Q1.md`, `CLAIMS.md` C4 weakened, `DECISIONS.md` D-16
- check command and exit status: public parser/schema-smuggling screen completed; exact authorization/execution mismatch already reported and fixed in MCP SDK
- evidence: C4 artifacts reproduce the known class across Python, Node, cra_mcp and local transport; no new attack mechanism remains
- failed controls or blockers: C4 is not a paper thesis; fresh R4 candidate required
- decision / DECISIONS id: D-16
- next node: R4-fresh-2
- do not repeat: do not spend new C4 model budget or relabel the fixed MCP parser issue as novel

### R4 screen B — 2026-11-08 — NO-GO (Q6-Q10)
- owner: idea-miner / lit-scout / pi-orchestrator
- inputs and source hashes: current public search and `R7-Q1-screening-2026-11-08.md`
- output: `R4-FRESH-CANDIDATES-2026-11-08-B.md`
- check command and exit status: dynamic routing, identity collision, stale-state resurrection, privacy composition and covert-channel directions each found direct/near-direct coverage
- evidence: FlowSteer/conjunctive routing, Agent Name Collision, revocation/stale-state work, compositional privacy and covert-channel lines are recorded as blockers
- failed controls or blockers: no mechanism-level candidate survived this screen; search axis must broaden
- decision / DECISIONS id: none yet
- next node: R4-fresh-2
- do not repeat: do not build another candidate by merely combining these already covered families

## Parallelism rule

Read-only scouts may fan out by A, B, C and defense/benchmark context. They return candidate evidence in separate
scratch files. The lead merges them only after comparing IDs, evidence levels and overlapping mechanisms. Agents
must not concurrently edit `LITERATURE.md`, `GAP-MATRIX.md`, `IDEAS.md`, `CLAIMS.md` or `EVIDENCE.md`.
