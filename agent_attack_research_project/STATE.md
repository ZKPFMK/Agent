# STATE — I1 memory persistence cascade

> Owner: `pi-orchestrator`. Every agent reads this first; only the PI changes `phase`.

- **Phase:** R4 fresh mechanism mining after C4 closure — ACL 2027 ARR paper
- **kb:** `/Users/dj/Documents/paper/Agent/research_attack_ideas/paper_inventory.md` (summary-level positioning view; no separate curated KB supplied)
- **papers:** `/Users/dj/Documents/paper/Agent/papers`
- **research profile:** `agent-attack-v1`; read-only corpus: `/Users/dj/Documents/paper/Agent/research_attack_ideas`; graph: `RESEARCH-GRAPH.md`
- **Target venue / deadline:** ACL 2027 main conference through ARR; official ARR deadline 2027-01-04; current ACL/ARR checklist still open
- **One-sentence thesis:** pending a fresh R4 mechanism; C4 is closed as a pre-empted parser regression, while P4 and I1 remain negative-boundary/protocol results.
- **API / compute budget:** local gateway `http://127.0.0.1:3425/v1`, model route `auto/gpt-6.1-sol`, temperature 0, max output 256; pilot cap ≤$50 equivalent and ≤2 CPU-hours; no live target or external service
- **Last updated:** 2026-11-08 by pi-orchestrator

## Gate P0 (scoping)
<!-- `cra gate P0` / gate_check.py read the section whose heading contains "Gate P<k>".
     When the phase advances, add "## Gate P<k+1>" (keep old gate sections as the log).
     Waive an item only with a DECISIONS id: "- [~] ... WAIVED: <reason> (DECISIONS D-<n>)". -->
- [ ] thesis is one falsifiable sentence: target system class, attack goal, success metric and the baseline value
- [ ] venue + deadline set; current CFP read (incl. ethics / open-science policy)
- [x] knowledge base path recorded (kb: line) and in-scope / out-of-scope list written
- [x] compute + API budget set (models, tokens, $)
- [x] ethics pre-screen: only owned or sandboxed targets, no real users / live third-party services
- [x] kill criteria and kill date set

## Errata and rolling updates   (later agents read this first)

- 2026-11-07: The imported corpus is summary-level evidence. The two source records with missing summaries remain unverified; no title, mechanism, year or number is inferred from their filenames.
- 2026-11-07: I1 is an exploratory cross-surface hypothesis, not a confirmed attack or novelty claim. The first probe varies evidence order only; memory and downstream aggregation are held fixed in separate blocks.
- 2026-11-07: R5 narrative-vs-random separation is a deterministic MockBackend harness result. C1 is weakened; D-2 blocks real-model interpretation and execution until model/backend and budget are selected.
- 2026-11-07: R6 local-gateway C2 is refuted: narrative 17/30 vs random 14/30 (p=0.607239), bridge-swap 23/30. I1 order/adjacency mechanism is closed; memory/downstream blocks were not run.
- 2026-11-07: D-4 closes I1 as a negative boundary result. Any continuation must start a fresh R4 idea and claim.
- 2026-11-07: D-5 reopens R0 for a paper-oriented project. Target is an AAAI or ICML submission; I1 remains background/negative evidence, not the thesis.
- 2026-11-07: D-6 briefly selected ICML 2027 during an earlier venue check; D-9 supersedes it after the user selected ACL.
- 2026-11-07: D-9 selects ACL 2027 main conference through ARR, with official ARR submission deadline 2027-01-04. ACL/ARR format, ethics and artifact checklist remains open in R0.
- 2026-11-07: D-7 does not run I3; public screening found direct or near-direct overlap with MCPTox, MCP-ITP, MemMorph and A2M. A revised mechanism or a new R4 direction is required.
- 2026-11-07: D-8 does not run I2; MemSecBench, MPBench, BackdoorAgent and trust-propagation work cover the proposed external-input-to-memory-to-collaboration chain.
- 2026-11-08: D-11 accepts the P4 v2 150-row loopback result as a bounded protocol survivor; candidate/control model-visible payloads and raw responses matched, and final separation came from deterministic authorization. R6 remains open for second adapter/model, defense and adaptive-attacker checks.
- 2026-11-08: D-12 closes the broad P4 provenance-erasure novelty framing after full-text verification of Trust Cascade; only a typed/schema conversion delta remains, and it must pass a new R4 screening before further expensive runs.
- 2026-11-08: D-13 closes P4 as a paper candidate after the narrow-delta screen found direct adjacent coverage from multi-CaMeL, structured delegation contracts, authority laundering and provenance-aware authorization work. P4 records remain protocol/negative-boundary artifacts; return to R4.
- 2026-11-08: R4 generated Q1, a validator/executor parser differential at a structured inter-agent handoff. Q2 cache collision, Q3 capability union, Q4 monitor disagreement and Q5 failure-status laundering were screened out before experiments. Q1 remains unregistered pending full-text/public pre-emption.
- 2026-11-08: C4 was registered after Q1's initial screen. The deterministic mock passed independently on 120 rows; candidate 30/30, canonical/canonicalized/reject controls 0/30, with AST mismatch only in the candidate. No model or tool execution is authorized yet.
- 2026-11-08: An independent Node implementation reproduced all 120 Q1 outcomes exactly. C4 remains open; the next gate is threat/protocol review and a decision on whether model integration adds evidence beyond the parser boundary.
- 2026-11-08: Sol and Astra loopback transport smokes each preserved the candidate duplicate-key envelope and reproduced the parser outcome with zero errors; this is transport integration evidence only, not a model vulnerability result.
- 2026-11-08: The actual `cra_mcp.adapter.ToolBox.call` execution parser path reproduced C4 with a fake in-memory server: candidate 30/30, controls 0/30, utility 120/120, false triggers 0. No project mutation or real tool execution occurred.
- 2026-11-08: D-15 accepts C4 as a bounded survived protocol claim and advances to R7 parser variants, framework baselines and adaptive grammar search. Paper contribution wording remains blocked.
- 2026-11-08: R7 grammar matrix produced 720 rows across eight variants and three arms. Nested, top-level and Unicode-equivalent duplicate variants survived candidate-only; canonicalization and strict rejection removed them; no false triggers occurred.
- 2026-11-08: The same R7 variants through `cra_mcp.adapter.ToolBox.call` produced 240 rows: candidate 30/30, controls 0/30, utility 240/240 and false triggers 0. C4 remains bounded; public parser screen and final R7 review remain.
- 2026-11-08: D-16 closes C4 as a paper candidate after MCP Go SDK issue #805 and ATR-2026-02350 verified the same parser mismatch and a case-sensitive parsing fix. Preserve C4 artifacts as regression/negative-boundary evidence; return to R4.
- 2026-11-08: R4 screen B rejects dynamic task-graph rewrite, identity collision, stale-state resurrection, privacy-budget composition and covert-channel directions as directly covered. No new claim or experiment is authorized; broaden the search axis.

## Active tasks
| task | owner agent | input | expected output | status |
|---|---|---|---|---|
| R0 | pi-orchestrator | brief, corpus manifest, safety profile | ATTACK-RESEARCH.md, ETHICS.md, P0 gate | done |
| R1 | lit-scout / kb-curator | PAPER-MATRIX.csv, corpus analysis | LITERATURE.md, evidence crosswalk | running |
| R2 | lit-scout | PAPER-MATRIX.csv, LITERATURE.md | ATTACK-CHAIN.md | queued |
| R3 | kb-curator / lit-scout | ATTACK-CHAIN.md, category comparison | GAP-MATRIX.md, KB-POSITION.md | queued |
| R4 | idea-miner | GAP-MATRIX.md, KB-POSITION.md | IDEA-BRIEF.md, open claim | done; C1 weakened |
| R5 | experimenter | IDEA-BRIEF.md, local mock testbed | pilots/I1-memory-cascade | done; mock-only boundary |
| R6 | threat-modeler / experimenter | weakened C1, D-3, protocol | real_trials.jsonl, C2 falsification | done; C2 refuted; I1 closed |
| R0-PAPER | pi-orchestrator | PAPER-GOAL.md, VENUE-RESEARCH.md, D-5/D-6 | venue, CFP, paper thesis and budget | running; CFP watch open |
| R4-I2 | idea-miner / lit-scout | local gaps, public pre-emption screen | R4-I2-screening.md | pre-empted; no experiment |
| R4-I3 | idea-miner / lit-scout | local gaps, public pre-emption screen | R4-I3-screening.md | pre-empted; no experiment |
| R4-P4 | idea-miner / lit-scout | R4-CANDIDATE-POOL.md, multi-CaMeL/PACE/AuthorityFlow full text | typed/provenance conversion screen | R4 passed; C3 open |
| R5-P4 | experimenter / falsifier | IDEA-BRIEF-P4.md, PROTOCOL-v2.md, v2 pilot | local-gateway typed-handoff pilot | done; v2 raw recomputation passed; C3 bounded survivor |
| R6-P4 | threat-modeler / experimenter / lit-scout | THREAT-MODEL-P4.md, v2 raw logs, R6-P4-screening-2026-11-08.md | threat/protocol and public pre-emption review | done as bounded result; broad provenance-erasure framing pre-empted; narrow delta pending |
| R4-P4-narrowing | idea-miner / lit-scout / pi-orchestrator | R6-P4-screening-2026-11-08.md, Trust Cascade full text, P4 protocol | typed-conversion-specific gap and claim | closed by D-13; no paper claim |
| R4-fresh | idea-miner / lit-scout / pi-orchestrator | GAP-MATRIX.md, KB-POSITION.md, full-text/public search | new mechanism candidate | Q1 parser-differential handoff selected for screening; Q2-Q5 screened out |
| R4-Q1-screening | lit-scout / pi-orchestrator | R4-FRESH-CANDIDATES-2026-11-08.md, parser/security leads | full-text/public pre-emption and exact claim design | done; C4 registered after initial screen |
| R5-Q1-mock | experimenter / falsifier | CLAIMS.md C4, Q1 PROTOCOL.md | deterministic parser differential probe | done; 120-row mock passes; Python/Node outcomes match |
| R6-Q1 | threat-modeler / experimenter / pi-orchestrator | C4, Python/Node raw logs, Sol/Astra smoke, cra_mcp ToolBox path, THREAT-MODEL-Q1.md | threat/protocol review and model-integration decision | done as bounded survivor; toolkit executor path passes with fake server; no real tool or production target |
| R7-Q1 | baseline-engineer / experimenter / falsifier | IDEA-BRIEF-Q1.md, C4 raw logs, parser variants, cra_mcp variant path, R7-Q1-screening-2026-11-08.md | parser variants, framework baselines and adaptive grammar search | closed by D-16; exact parser mismatch pre-empted; artifacts preserved |
| R4-fresh-2 | idea-miner / lit-scout / pi-orchestrator | GAP-MATRIX.md, KB-POSITION.md, R7-Q1-screening-2026-11-08.md, current public search | new mechanism candidate | screen B rejected Q6-Q10; broaden search axis before any claim or experiment |
| R4-fresh-2 | idea-miner / lit-scout / pi-orchestrator | GAP-MATRIX.md, KB-POSITION.md, R7-Q1-screening-2026-11-08.md | new mechanism candidate | running; no experiment until full-text/public pre-emption passes |

## Blockers / questions for the human
- I1 is closed as a negative boundary result. Do not reuse C2 or run its memory/downstream blocks.
- C4 is closed as a paper candidate after direct MCP parser-mismatch pre-emption. A fresh R4 mechanism, claim and full-text/public screen are required before any new experiment.
- Confirm current ACL/ARR CFP, submission cycle, format, artifact/ethics rules and anonymization requirements before writing the thesis.
- Estimated local-gateway cost is $0.0757 for I1 plus $0.0271 for P4 v2; no live target or external service was used.
