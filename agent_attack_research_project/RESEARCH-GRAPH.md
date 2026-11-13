# RESEARCH-GRAPH — MCP attack research

`pi-orchestrator` owns this graph. One node has one owner and one primary output. Independent nodes may run in
parallel only when they write separate scratch outputs; an aggregate file has one synthesis writer.

## Graph state

- **last updated:** 2026-11-13
- **current node:** R4-MCP-prompt-lifecycle-handler-screen — RUNNING read-only implementation/novelty/threat checks; no new experiment
- **resume rule:** start at the first node whose check is not `PASS`
- **source hash / model snapshot change:** corpus matrix SHA-256 `5c2e7fc2b465660adc9eec9a0634c07debb175993eab058de6af34f4e1e51359`; no model snapshot

## Nodes

| id | node | owner | depends on | primary output | check | status | blocker / next |
|---|---|---|---|---|---|---|---|
| R0 | scope and safety | pi-orchestrator | STATE.md | ATTACK-RESEARCH.md, ETHICS.md, PAPER-GOAL.md | P0 paper scope + safety review | REOPENED | venue/CFP and fresh thesis pending |
| R1 | corpus evidence | lit-scout, kb-curator | R0 | PAPER-MATRIX.csv, LITERATURE.md | `check_framework.py --project .` | PASS | R2 |
| R2 | attack-chain map | lit-scout | R1 | ATTACK-CHAIN.md, taxonomy notes | required axes and evidence levels present | PASS | R3 |
| R3 | cross-surface gaps | kb-curator, lit-scout | R1, R2 | GAP-MATRIX.md, KB-POSITION.md | A×B, A×C, B×C, A×B×C have paper IDs | PASS | R4 idea selection |
| R4 | candidate hypotheses | pi-orchestrator / scouts | R3 and historical closures | R4-MCP-SYNTHESIS-2026-11-10.md; dated screening records | reachable implementation, nearest-work screen, one variable, control and kill switch | RUNNING (prompt lifecycle/handler axis) | effect-history, sampling, default-order, resource_link, handshake, stream, gateway, broad contract/effect, elicitation, MRTR, pagination, batch, resource subscription, dynamic tools, resource-template, trusted retry/finalization, task-handle, authorization audience, roots, annotation, tool identity and code-execution framing closed by D-21–D-43; prompt lifecycle/handler binding is the current bounded screen; no new pilot |
| R5 | cheap probes | idea-miner, experimenter | R4 | `pilots/P4-typed-handoff/` | clean, naive and mechanism control; 3 seeds | PASS (v2) | 150-row loopback pilot passed raw recomputation |
| R6 | threat and protocol | threat-modeler, experimenter | R5 | THREAT-MODEL-P4.md, `results/2026-11-07-p4-typed-handoff-v2/PROTOCOL.md` | threat validator, independent raw evaluator and public pre-emption screen | CLOSED (P4 paper candidate); CLOSED (I1) | P4 records retained as protocol/negative-boundary artifacts; R4 fresh idea required |
| R7 | fair baselines | baseline-engineer | R6 | baselines/MANIFEST.md, IDEA-BRIEF-Q1.md | pinned parser variants, framework discrepancy log and adaptive grammar manifest | CLOSED (Q1, D-16) | known parser mismatch; no baseline phase opened for the current MCP candidates |
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

### R4-MCP-screen — 2026-11-10 — UNCERTAIN / NO-GO for current preferred candidate

- owner: pi-orchestrator; independent literature, idea, KB and threat scouts completed.
- inputs: existing R0–R9 history, read-only MCP paper corpus, current public specifications and toolkit source; evidence levels and exact sources are recorded in the synthesis.
- output: `R4-MCP-SYNTHESIS-2026-11-10.md`, independent KB/threat reports, `DECISIONS.md` D-17.
- findings: MCP-R4-02 lacks an actual automatic binding/approval-inheritance path and overlaps P4/prior work; 01/03/04/05 remain UNCERTAIN. No new scientific claim or effectiveness result passed a gate.
- checks: project structure and P0 checklist pending the final ledger check; no experiment was executed.
- corrections: do not infer sampling availability from prompts/get; cancellation is not a rollback guarantee; attacker-owned duplicate effects are not an authorization bypass.
- follow-up completed: a bounded source checker found content-only runtime consumption; only test assertion helpers fall back between result fields. No two actual safety consumers or security-state split were found. D-18 closes MCP-R4-03 for this toolkit; external implementations remain unverified.
- next: this round is complete without a thesis. Reopening 03 requires a pinned external implementation, two actual consumer paths, independent security-state evidence and a new nearest-work comparison.
- do not repeat: do not rerun the content-only toolkit check, create a permissive broker to manufacture the hypothesized attack, restart I1/P4/Q1, or spend model-evaluation budget without a new registered claim and threat/protocol checks.

### R4-ADAPTIVE-TOOLCHAIN — 2026-11-11 — REVIEW COMPLETE; NOVELTY UNCERTAIN

- owner: main coordinator; independent kb-curator, lit-scout and threat-modeler completed bounded nodes. Main coordinator archived the lit-scout hand-back as WEB-LITERATURE.md; the scout retained downloaded source material.
- input: user-authored `papers/10_MCP攻击/自适应工具链与Agent行为扩展_研究构想.md`, SHA-256 `63ca1233a225b6ea87ed6ed07857c4c7568bcdd4de593089a830f4df233f413c`; historical closures remain closed.
- output directory: `reviews/adaptive-toolchain-2026-11-11/`; primary output `REPORT.md`, with LOCAL-PRIOR.md, WEB-LITERATURE.md, DESIGN-REVIEW.md, MCP-SEMANTICS.md, SCOPE.md and CHECKS.md.
- scope/evidence: four local papers' relevant full-text sections, eleven public papers' method/evaluation sections, fixed MCP semantics and a local loop inspection; no new attack, model-evaluation run or effectiveness claim.
- decision D-20: the broad fixed-chain-versus-autonomous-new-attack framing is unsupported. MCP-UPD has no-prior-configuration and unnamed-tool payload evidence; AgentDojo already delegates goals, AgentDyn covers dynamic feedback. The stricter tool-knowledge/neutral-real-failure/unspecified-alternative-path question remains UNCERTAIN, not a novelty survivor.
- checks: project/corpus structure, source fingerprints and final artifact/link audit are recorded with exact status in CHECKS.md; structure PASS is not a scientific gate.
- clarification: the user's A11 reference means `When MCP Servers Attack` A11 Prompt Logic Attack (Prompt handler server-side self-execution), not KB A11 MPMA. Code-execution increment adds CODE-EXECUTION-LITERATURE.md and CODE-EXECUTION-DESIGN.md; INFUSE/CIBER establish sandbox code-execution precedents, while host/production RCE remains unestablished.
- next: choose whether to study A11 handler execution or Agent-generated code execution as separate questions. Compare exact prior conditions, freeze user authorization/equal-knowledge baselines and independent effect oracle before considering R5. No scientific gate or experiment was advanced; failure-route study is secondary.

### R4 effect-history / receipt / notification — 2026-11-11 — NO-GO (taken)

- owner: pi-orchestrator; literature, source, idea and threat scouts completed.
- inputs: current MCP corpus, public search and specifications/advisories, fixed `cra_mcp 0.2.0` commit `463779b318f78a7c9e62e86639fec135c0423bc5`, fixed `mcp-agent 0.2.6` commit `f62d849350816588b1c6294e7914bbe4d8b84072`.
- output: `R4-EFFECT-HISTORY-SCREEN-2026-11-11.md`, `DECISIONS.md` D-21.
- check: eight mechanism queries, 38 arXiv hits with incomplete secondary-index coverage, eight checked high-relevance sources, and two fixed source checks; direct overlap and missing implementation chain make the broad candidate NO-GO.
- evidence: TRAP and GHSA directly cover result misbinding/replay and cross-client misrouting; other checked sources cover effect anomalies, workflow/semantic/approval replay and cross-call state mixing.
- blocker: no new mechanism-level delta or independent honest-effect witness; only receipt-to-workflow and notification-to-commit remain as implementation leads.
- next: bounded MCP sampling recipient/session binding screen; no claim, broker or experiment.
- do not repeat: do not relabel replay, stale state, P4 provenance, parser differential, task-ID isolation or approval inheritance as a new effect-history attack.

### R4 MCP sampling recipient/session binding — 2026-11-11 — NO-GO

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP sampling specification, pinned host/client implementations, current corpus and D-17–D-21 closures.
- output: `R4-MCP-SAMPLING-SCREEN-2026-11-11.md`, `DECISIONS.md` D-22.
- check: VS Code, mcp-agent/Python SDK and TypeScript SDK source paths preserve the bound server/session or original request ID; eight literature/spec/advisory sources checked; no non-GHSA recipient/session-to-honest-effect chain.
- evidence: VS Code sampling consumes server messages/systemPrompt without active chat history; mcp-agent forwards through bound upstream; GHSA covers shared transport cross-client sampling misrouting.
- blocker: no independent honest protected-effect witness and no new mechanism-level delta. A ContextVar/connection-manager lead remains only an implementation question.
- next: bounded sampling `tools`/`toolChoice`/`includeContext` semantics screen; no claim, broker or experiment.
- do not repeat: do not repackage GHSA cross-client routing, generic sampling prompt injection, or missing prompts/get support as a new attack.

### R4 MCP sampling tool/context semantics — 2026-11-11 — NO-GO (broad)

- owner: pi-orchestrator with bounded source/literature follow-up.
- inputs: MCP sampling specification, fixed host/client/SDK source, current corpus and D-17–D-22 closures.
- output: `R4-MCP-SAMPLING-TOOLS-SCREEN-2026-11-11.md`, `DECISIONS.md` D-23.
- check: fixed VS Code/mcp-agent paths do not connect tools/toolChoice/includeContext to a host protected executor/private reader; final public checks found no direct field-to-honest-effect precedent.
- evidence: sampling specification semantics, GHSA, Unit 42 and Breaking the Protocol checks recorded in the screen.
- blocker: narrow host implementation question remains unverified, but no complete chain or independent effect exists.
- next: bounded MCP-R4-01 default-value approval ordering screen; no claim, broker or experiment.
- do not repeat: do not call a host ignoring includeContext a vulnerability, or repackage model jailbreak, sampling abuse, GHSA routing, completion, P4 or approval inheritance.

### R4 MCP-R4-01 default-value approval ordering — 2026-11-11 — NO-GO (checked implementations)

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP tool input/default semantics, fixed host/client implementations, current corpus and D-17–D-23 closures.
- output: `R4-MCP-DEFAULT-ORDER-SCREEN-2026-11-11.md`, `DECISIONS.md` D-24.
- check: fixed cra_mcp, VS Code, Python SDK and TypeScript SDK sources were traced; no complete approval-snapshot→default/coercion→honest protected-effect chain was found. Literature direct=0 but nearest-work overlap remains.
- evidence: cra_mcp approves raw args and fixed write tools have no defaults; VS Code forwards rawInput; SDKs parse defaults without an approval snapshot.
- blocker: external callers/dependency locks are not exhaustively checked, so broad implementation safety is not claimed; no claim or experiment is authorized.
- next: bounded MCP-R4-04 resource_link cross-source dereference screen.
- do not repeat: do not build a permissive broker or treat model-selected parameters, missing validation, error text or attacker-owned effects as success.

### R4 MCP-R4-04 resource_link cross-source dereference — 2026-11-11 — NO-GO (checked implementations)

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP resource_link/resource semantics, fixed host/client implementations, current corpus and D-17–D-24 closures.
- output: `R4-MCP-RESOURCE-LINK-SCREEN-2026-11-11.md`, `DECISIONS.md` D-25.
- check: fixed VS Code, mcp-agent, Python SDK and TypeScript SDK paths were traced; no automatic cross-source resolver→identity/ACL→honest protected effect chain; eight sources were near but not direct.
- evidence: VS Code binds image links to original server and sends `resources/read` only there; mcp-agent read is explicit; SDKs return validated results without automatic dereference.
- blocker: uninspected external hosts remain uncertain; no claim or experiment is authorized.
- next: bounded initialize version/capability downgrade screen.
- do not repeat: do not treat resource metadata, attacker-owned reads, ordinary URL fetching, prompt injection or logs as unauthorized effect.

### R4 MCP initialize version/capability downgrade — 2026-11-11 — NO-GO / UNCERTAIN

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP initialization/versioning specifications, fixed host/client handshake implementations, current corpus and D-17–D-25 closures.
- output: `R4-MCP-HANDSHAKE-SCREEN-2026-11-11.md`, `DECISIONS.md` D-26.
- check: no legal initialize response was found to change a negotiated security state and trigger an honest canary; standards/defenses already cover floors, fallback and feature gates.
- evidence: fixed SDK/VS Code checks and versioning/lifecycle/OWASP/MCPS/Go issue sources recorded in the screen.
- blocker: dual-era external hosts remain unverified; no clean novelty or protected-effect witness.
- next: canonical streaming/notification/cancel state-machine screen.
- do_not_repeat: do not use duplicate keys, Unicode/parser ambiguity, DNS/transport hijack, tool poisoning or attacker-owned effects.

### R4 MCP canonical streaming/notification/cancel state — 2026-11-11 — NO-GO

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: canonical MCP streaming/notification/cancellation semantics, fixed host/client implementations, current corpus and D-17–D-26 closures.
- output: `R4-MCP-STREAM-SCREEN-2026-11-11.md`, `DECISIONS.md` D-27.
- check: VS Code, TypeScript SDK, Python SDK and mcp-agent clean pending handlers on final/cancel/timeout; no canonical event→honest protected effect chain; literature has only near neighbours.
- evidence: progress/log do not re-enter tool execution, late final uses unknown ID, and no exactly-once/atomic protected sink ledger is present.
- blocker: external host finalizers remain unverified; no claim or experiment is authorized.
- next: gateway capability subject/audience/purpose binding screen.
- do_not_repeat: do not relabel duplicate-key parsing, stale revocation/checkpoint, ordinary failure/logging, or network timing as this axis.

### R4 MCP gateway capability subject/audience/purpose binding — 2026-11-11 — NO-GO (checked implementations)

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP gateway capability semantics, fixed gateway/host implementations, current corpus and D-17–D-27 closures.
- output: `R4-MCP-GATEWAY-CAPABILITY-SCREEN-2026-11-11.md`, `DECISIONS.md` D-28.
- check: no fixed implementation supplied ref→cross-server→B ACL→protected effect; eight sources were direct=0/near.
- evidence: cra_mcp is single-project; GatewayBench is an evaluation artifact; PRECINCT has owner/expiry handles but fixed upstream dispatch and no complete tuple/effect path.
- blocker: uninspected external gateways remain uncertain; no claim or experiment is authorized.
- next: non-filesystem declared contract vs actual effect/data-flow screen.
- do_not_repeat: do not use name/session collision, model-selected target, attacker-owned effect, leaked B token or permissive broker.

### R4 MCP non-filesystem declared contract vs actual effect/data-flow — 2026-11-12 — NO-GO (taken)

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP tool contract/effect papers, fixed benign servers/hosts, current corpus and D-17–D-28 closures.
- output: `R4-MCP-CONTRACT-EFFECT-SCREEN-2026-11-12.md`, `DECISIONS.md` D-29.
- check: AWS DocumentDB and Tabularis advisories directly cover read-only/benign schema paths to non-filesystem DB writes; GitHub/Postgres source chains had no distinct new mechanism.
- evidence: AWS `$out/$merge` and Tabularis stacked SQL provide independent database effects; broad framing is pre-empted.
- blocker: no new claim or experiment; only a distinct future mechanism could reopen.
- next: elicitation URL-mode consent/callback binding screen.
- do_not_repeat: do not relabel filesystem laundering, hidden code, model intent, schema poisoning, token passthrough or attacker-owned effects.

### R4 MCP elicitation URL-mode consent/callback binding — 2026-11-12 — NO-GO (checked implementations)

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP elicitation URL-mode semantics, fixed host/client/server implementations, current corpus and D-17–D-29 closures.
- output: `R4-MCP-ELICITATION-SCREEN-2026-11-12.md`, `DECISIONS.md` D-30.
- check: VS Code is form-only; mcp-agent forwards to an app callback without browser/state/tenant binding; Python completion is no-op by default; literature direct=0 and standards cover consent/requestState/elicitationId.
- evidence: no host-mediated browser callback/result→honest sink chain; E3 origin/tenant omission is pre-empted by GHSA/MSRC, E1/E2 remain unverified.
- blocker: external URL-mode hosts remain uncertain; no claim or experiment is authorized.
- next: MRTR requestState end-to-end binding screen.
- do_not_repeat: do not relabel ordinary server elicitation, token passthrough, prompt injection, logs or attacker-owned effects.

### R4 MCP MRTR requestState end-to-end binding — 2026-11-12 — NO-GO/UNCERTAIN

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP MRTR requestState semantics, fixed host/client/server implementations, current corpus and D-17–D-30 closures.
- output: `R4-MCP-MRTR-SCREEN-2026-11-12.md`, `DECISIONS.md` D-31.
- check: strict direct=0/8; Python/TS/Ruby/Juneau paths bind or reject changed method/target/args; no valid-state→changed-request→honest-effect chain.
- evidence: MRTR spec and codecs cover integrity/request binding; no protected effect witness.
- blocker: external host chains remain uncertain; no claim or experiment is authorized.
- next: pagination/cursor binding screen.
- do_not_repeat: do not use weak toy state, forged signatures, parser ambiguity, approval inheritance, stale task IDs or attacker-owned effects.

### R4 MCP pagination/cursor binding — 2026-11-12 — NO-GO

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP pagination/cursor semantics, fixed host/client/server implementations, current corpus and D-17–D-31 closures.
- output: `R4-MCP-PAGINATION-SCREEN-2026-11-12.md`, `DECISIONS.md` D-32.
- check: VS Code/mcp-agent auto-follow only same server/method/client connection; TS SDK no auto-follow; no A cursor→B ACL/effect chain; literature direct=0 but no reachability.
- evidence: source paths and pagination specification recorded in screen; public cursor issues are correctness/DoS, not cross-source protected reads.
- blocker: external multi-tenant hosts remain uncertain; no claim or experiment is authorized.
- next: batch/bulk item-level authorization binding screen.
- do_not_repeat: do not relabel ordinary pagination, parser ambiguity, token passthrough, model text or attacker-owned resources.

### R4 MCP batch/bulk item-level authorization binding — 2026-11-12 — NO-GO

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP batch/bulk tool semantics, fixed host/client/server implementations, current corpus and D-17–D-32 closures.
- output: `R4-MCP-BATCH-AUTH-SCREEN-2026-11-12.md`, `DECISIONS.md` D-33.
- check: cra_mcp/VS Code/TS/Go/conformance objects expose single tool calls; JSON-RPC transport batches are independent dispatch; no overall approval/item expansion/ACL/effect chain.
- evidence: per-call approval and single `callTool` paths; arrays are schema data, not batch semantics; literature direct=0.
- blocker: external compound operations remain unverified; no claim or experiment is authorized.
- next: resource subscription/update binding screen.
- do_not_repeat: do not relabel ordinary arrays, model-selected items, invalid items, attacker-owned effects or permissive batch brokers.

### R4 MCP resource subscription/update binding — 2026-11-12 — NO-GO

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP resource subscription/update semantics, fixed host/client/server implementations, current corpus and D-17–D-33 closures.
- output: `R4-MCP-RESOURCE-SUBSCRIPTION-SCREEN-2026-11-12.md`, `DECISIONS.md` D-34.
- check: VS Code updates only fire events and explicit reads stay original-server bound; TS SDK/mcp-agent expose explicit APIs; no automatic B refresh/protected effect chain; literature direct=0.
- evidence: source and notification paths recorded in screen.
- blocker: external auto-refresh hosts remain uncertain; no claim or experiment is authorized.
- next: dynamic tool registration/list-changed binding screen.
- do_not_repeat: do not relabel resource_link, logs, DoS, stale state, token passthrough or attacker-owned resources.

### R4 MCP dynamic tool registration/list-changed binding — 2026-11-12 — NO-GO (broad/taken)

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP dynamic tools/list/list_changed semantics, fixed host/client/server implementations, current corpus and D-17–D-34 closures.
- output: `R4-MCP-DYNAMIC-TOOLS-SCREEN-2026-11-12.md`, `DECISIONS.md` D-35.
- check: FCD arXiv:2609.35088 directly covers dynamic refresh/stale approval/handler drift protected effects; fixed hosts have no registry→approval→protected sink chain.
- evidence: VS Code re-lists/updates metadata but no auto invocation; mcp-agent/Python explicit refresh; TS autoRefresh caller-configured; no ACL/effect ledger.
- blocker: source/session/tenant-specific defect remains unverified and high-overlap; no claim or experiment is authorized.
- next: resource-template URI variable binding screen.
- do_not_repeat: do not relabel tool descriptions, dynamic visibility, logs, model choice or attacker-owned tools.

### R4 MCP resource-template URI variable binding — 2026-11-12 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP resource-template/URI-template semantics, fixed host/client/server implementations, current corpus and D-17–D-35 closures.
- output: `R4-MCP-RESOURCE-TEMPLATE-SCREEN-2026-11-12.md` and one decision entry only after synthesis.
- check: identify legal template expansion where A-controlled variable resolves to B tenant/object protected resource in a fixed host and produces an independent effect; strict origin/template/ACL checker must reject, utility remain.
- blocker: resource_link, SSRF, path traversal, pagination, ordinary resource read and P4 are excluded; actual template consumer and B ACL are required.
- next: literature, implementation, idea and threat scouts run in parallel; close if no distinct URI-variable binding difference.
- do_not_repeat: do not relabel resource_link, URL fetch, path traversal, logs, public resources or attacker-owned effects.
- verdict: D-36 NO-GO for checked implementations and RT-1/RT-2/RT-3; unpinned external host remains UNCERTAIN only.
- evidence: exact direct literature=0, but Object-Authz Lab S8, Stochastic Deputy, n8n-MCP advisory and URI/tenant guidance block broad novelty; TS SDK is caller-explicit and no automatic cross-source/B-effect chain is present.
- next: narrow MCP-R4-05 trusted retry/finalization binding screen.
- do_not_repeat: do not rebuild a template resolver, broker, B ACL/sink, or relabel BOLA, SSRF, path traversal, Q1/C4, Q2, Q7, D-28 or D-35.

### R4 MCP-R4-05 trusted retry/finalization binding — 2026-11-12 — QUEUED

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: narrow trusted retry/finalization semantics, fixed host/client/server implementations, current corpus and D-21/D-36 closures.
- output: dated screen record and one decision entry only after synthesis.
- check: determine whether a low-trust server can legally trigger a fixed host to resubmit a previously approved trusted protected call or reuse an effect permit, reaching an independent protected sink beyond the authorized effect.
- blocker: broad effect-history/replay, TRAP/GHSA, ordinary cancellation residue, FCD handler drift, network timing and attacker-owned duplicate effects are excluded; fixed canonical retry/finalizer consumer and independent sink ledger are required.
- next: literature, implementation, idea and threat scouts run in parallel; close if only replay, stale state, duplicate transport delivery, or attacker-owned effect is found.
- do_not_repeat: do not construct a retry broker, weak approval state, permissive finalizer, cross-client transport or protected sink to manufacture the chain.
- verdict: D-37 NO-GO for the checked fixed-source range and C-1/C-2/C-3; unpinned external host remains UNCERTAIN only.
- evidence: direct literature=0/8, with AID-Guard/CapLease/Permission to Retry as defense/recovery near work and TRAP/GHSA/FCD as adjacent exclusions; no server-event→automatic resubmission→permit reuse→trusted B ledger chain.
- next: task-augmented request/task-result handle binding screen.
- do_not_repeat: do not relabel transport duplicates, ordinary idempotent retry, late final, cancellation residue, replay/misbinding or handler drift.

### R4 MCP task-augmented request/task-result handle binding — 2026-11-12 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP task-augmented request/task-result semantics, fixed host/client/server implementations, current corpus and D-21/D-31/D-37 closures.
- output: `R4-MCP-TASK-HANDLE-SCREEN-2026-11-12.md` and one decision entry only after synthesis.
- check: determine whether a legal A task handle or `tasks/get`/`tasks/result` response is automatically rebound by a fixed host to B session/tenant/object/protected effect without original request/approval/source binding; strict handle/source/ACL checker must reject while benign async utility remains.
- blocker: MRTR requestState, ordinary async replay, transport ID misbinding, effect-history, dynamic tools, resource-template and attacker-owned tasks are excluded; an existing task consumer, B ACL and independent ledger are required.
- next: literature, implementation, idea and threat scouts run in parallel; close if MCP tasks are only explicit application APIs or no protected effect chain exists.
- do_not_repeat: do not construct a task broker, cross-session resolver, weak cache, B sink or permissive task registry to manufacture the chain.
- verdict: D-38 NO-GO for broad task-handle/session isolation and H1/H2/H3; fixed-source uncertainty is an audit limitation only.
- evidence: Python/TypeScript task-store advisories directly cover cross-session access; legacy/current task APIs differ; no fixed automatic A-handle→B consumer, B ACL or independent ledger.
- next: authorization resource-indicator/token-audience binding screen.
- do_not_repeat: do not relabel task ID isolation, explicit polling, MRTR, result flow, replay, transport ID mismatch or retry/finalization.

### R4 MCP authorization resource-indicator/token-audience binding — 2026-11-12 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP authorization/protected-resource metadata/resource indicators, fixed HTTP host/client implementations, current corpus and D-28/D-30/D-38 closures.
- output: `R4-MCP-AUTH-RESOURCE-INDICATOR-SCREEN-2026-11-12.md` and one decision entry only after synthesis.
- check: determine whether a legal A `401` challenge or protected-resource metadata causes a fixed host/client to send a token/approval to an existing B protected synthetic endpoint despite origin/resource/audience binding; strict audience/origin checker must reject and benign A authorization utility remain.
- blocker: SSRF, attacker-owned token sink, OAuth phishing, transport redirect, gateway capability, handshake downgrade, real credentials and ordinary token passthrough are excluded; existing B ACL/audience denial and independent receiver ledger are required.
- next: literature, implementation, idea and threat scouts run in parallel; close if authorization metadata is explicit caller-controlled, token audience is correctly bound, or no B protected effect exists.
- do_not_repeat: do not construct an OAuth broker, permissive redirector, fake B resource, real token or live endpoint to manufacture the chain.
- verdict: D-39 NO-GO for checked fixed-source range and AI-1/AI-2/AI-3; unpinned external host remains UNCERTAIN only.
- evidence: direct complete chain=0/8; MCP/RFC defenses and three SDK metadata/issuer advisories cover broad boundary, but attacker-owned credential sinks are excluded and no automatic A metadata→B route/B ledger exists.
- next: roots boundary binding screen.
- do_not_repeat: do not relabel token passthrough, SSRF, redirect, OAuth phishing, D-26/D-28/D-30 or weak verifier.

### R4 MCP roots boundary binding — 2026-11-12 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: `roots/list` and root-context semantics, fixed host implementations, prior H1 roots disclosure screen, D-39 and earlier closures.
- output: `R4-MCP-ROOTS-BOUNDARY-SCREEN-2026-11-12.md` and one decision entry only after synthesis.
- check: determine whether a legal A roots request or root-context consumer makes fixed host expose B workspace/tenant root capability or use an over-broad root for a protected operation, with an independent synthetic canary and strict root/ACL reference rejection.
- blocker: general roots disclosure, ordinary file read, path traversal, resource-template, SSRF, user-shared roots, attacker-owned files and prompt injection are excluded; fixed automatic root consumer, B root ACL and independent ledger are required.
- next: literature, implementation, idea and threat scouts run in parallel; close if roots are explicit host configuration and no protected effect crosses the A/B boundary.
- do_not_repeat: do not build a root broker, permissive filesystem adapter, fake B workspace or real-file canary to manufacture the chain.
- verdict: D-40 NO-GO for checked range and R-1/R-2/R-3; unpinned external host remains UNCERTAIN only.
- evidence: direct complete chain=0/8; IBM root registry disclosure is partial; fixed VS Code records show host-configured roots and no A-triggered B consumer, B ACL/effect ledger or protected file operation.
- next: tool annotation/effect-hint binding screen.
- do_not_repeat: do not relabel general roots disclosure, filesystem laundering, path/symlink, stale list_changed, resource-template or root broker behavior.

### R4 MCP tool annotation/effect-hint binding — 2026-11-12 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: MCP tool annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`), fixed host approval/dispatch implementations, D-29/D-40 and prior annotation notes.
- output: `R4-MCP-ANNOTATION-EFFECT-HINT-SCREEN-2026-11-12.md` and one decision entry only after synthesis.
- check: determine whether A-controlled legal annotations change fixed host approval/dispatch scope for an existing trusted B protected operation while actual effect is not revalidated; strict effect/reference checker must reject and benign utility remain.
- blocker: generic tool poisoning, prompt injection, D-29 broad contract/effect escape, model selection, explicit user approval, attacker-owned tools and hosts that ignore annotations are excluded; existing B ACL/effect ledger is required.
- next: literature, implementation, idea and threat scouts run in parallel; close if annotations are advisory only, host does not use them for security, or no protected effect chain exists.
- do_not_repeat: do not build an approval broker, fake B sink, permissive annotation interpreter or tool whose actual effect is attacker-owned.
- verdict: D-41 NO-GO for checked range and AH-1/AH-2/AH-3; unpinned external host remains UNCERTAIN only.
- evidence: direct complete chain=0/8; broad untrusted-hint/approval boundary is covered by MCP/OWASP/ToolHive/destructive-approval work; no fixed field-level annotation→security gate→trusted B ledger chain.
- next: tool identity/name shadowing binding screen.
- do_not_repeat: do not relabel inaccurate annotations, D-29 contract/effect, generic tool poisoning, UI/model text or retry/replay.

### R4 MCP tool identity/name shadowing binding — 2026-11-12 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: multi-server tool registry/name/approval identity semantics, fixed host registry/dispatch implementations, D-35/D-41 and prior tool poisoning exclusions.
- output: `R4-MCP-TOOL-IDENTITY-SHADOWING-SCREEN-2026-11-12.md` and one decision entry only after synthesis.
- check: determine whether a legal A same-name tool definition/metadata changes B's existing approval/dispatch identity or causes B protected operation to be invoked under A-derived policy, with B ACL/effect ledger and strict server/session/tool identity binding.
- blocker: generic tool poisoning, model/tool selection, attacker-owned A effect, dynamic list_changed/stale approval, shared transport response misrouting, user explicit selection and ordinary no-effect name collision are excluded; pre-existing B protected operation and ledger are required.
- next: literature, implementation, idea and threat scouts run in parallel; close if host namespaces tools by server/session or no B protected effect exists.
- do_not_repeat: do not construct a global tool registry, shadow broker, fake B sink or permissive cross-server dispatcher to manufacture the chain.
- verdict: D-42 NO-GO for checked range and TS-1/TS-2/TS-3; unpinned external multi-server host remains UNCERTAIN only.
- evidence: direct complete chain=0/8; Docker/WeKnora/LangChain/IBM/Applied Sciences cover broad registry/name collision family; no fixed A metadata→B trusted dispatch→B ACL/effect ledger chain.
- next: MCP external-content code-execution boundary screen.
- do_not_repeat: do not relabel attacker-owned wrong dispatch, DoS, generic poisoning, D-21 transport misrouting, D-35 stale approval or global registry construction.

### R4 MCP external-content code-execution boundary — 2026-11-13 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: INFUSE/CIBER/code-execution literature and design, MCP-specific external/indirect content boundaries, fixed host/runner implementations, D-42 and prior MCP closures.
- output: `R4-MCP-CODE-EXECUTION-BOUNDARY-SCREEN-2026-11-13.md` and one decision entry only after synthesis.
- check: determine whether a single low-trust external MCP content item, with attacker unaware of exact tool registry and no online feedback, can in a fixed MCP host cause Agent-generated code to be submitted/executed in a local sandbox and produce an independently observed synthetic effect beyond matched baselines; do not claim first code-execution mechanism.
- blocker: host RCE/escape, real files/credentials/network, malicious MCP server self-execution, direct user prompt injection, payload construction and experiment are excluded; G/T/X/E event chain and fixed sandbox boundary are required.
- next: literature, implementation, idea and threat scouts run in parallel; close if this is only INFUSE/CIBER replication, ordinary tool call, prompt injection, or no fixed MCP code runner/effect oracle exists.
- do_not_repeat: do not run code, models, services or paper code; do not write payloads or call real targets.
- verdict: D-43 NO-GO for checked local range and V1/V2/V3; broad mechanism covered by INFUSE/CIBER/CE-MCP; no fixed MCP runner/oracle.
- evidence: local cra_mcp is ordinary function calling; design G/T/X/E is static; no artifact parser, code runner, independent state oracle or server-self-execution monitor.
- next: prompt lifecycle/handler binding screen.
- do_not_repeat: do not relabel ordinary tools/call, direct user MCE, malicious server self-execution, sandbox effect as RCE or construct a runner/canary.

### R4 MCP prompt lifecycle/handler binding — 2026-11-13 — RUNNING

- owner: pi-orchestrator with four bounded read-only scouts.
- inputs: `prompts/get` and Prompt handler lifecycle, fixed host prompt consumers, A11 server-side execution boundary, D-30 and D-43 closures.
- output: `R4-MCP-PROMPT-LIFECYCLE-HANDLER-SCREEN-2026-11-13.md` and one decision entry only after synthesis.
- check: determine whether a legal A prompt result/argument/role/content metadata is automatically promoted by a fixed host into trusted system/instruction/context or a protected downstream operation without source/session/approval binding; exclude A11 handler self-execution and ordinary model prompt injection.
- blocker: user explicit prompt selection, completion, sampling, elicitation, generic prompt injection, A11 server-side self-execution, model-selected tools, ordinary text result and attacker-owned effects are excluded; existing B ACL/effect ledger required.
- next: literature, implementation, idea and threat scouts run in parallel; close if prompt results only return to caller/model or no protected consumer exists.
- do_not_repeat: do not start prompt handlers, invoke models, construct injected content, build a prompt broker or fake B sink.


## Parallelism rule

Read-only scouts may fan out by A, B, C and defense/benchmark context. They return candidate evidence in separate
scratch files. The lead merges them only after comparing IDs, evidence levels and overlapping mechanisms. Agents
must not concurrently edit `LITERATURE.md`, `GAP-MATRIX.md`, `IDEAS.md`, `CLAIMS.md` or `EVIDENCE.md`.
