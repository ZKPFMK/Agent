# progress — MCP attack research

This is the resume ledger for the research graph. Append a record after each node; do not rewrite history.

## Current state

- graph node: R4-MCP-screen
- phase: R4 implementation/novelty screening; I1, P4 and C4 remain closed negative-boundary/protocol results
- last successful check: four MCP scouts and the bounded MCP-R4-03 source check completed; runtime is content-only, with no two safety consumers or observed authorization/execution split
- next action: current R4 round complete without a thesis. Reopen 03 only if a pinned external SDK/host supplies two actual consumer paths and a distinct security state; do not repeat the toolkit check
- blockers: no paper thesis selected; MCP-R4-02 NO-GO as framed; MCP-R4-03 NO-GO locally; 01/04/05 and external generalization UNCERTAIN; current ACL/ARR checklist remains open; no new experiment
- budget used / remaining: I1 $0.0757 plus P4 Sol $0.0271 plus Astra $0.1356 estimated; local-gateway cap remains ≤$50

## Node log

| date | node | owner | verdict | output | check | decision / blocker | next |
|---|---|---|---|---|---|---|---|
| 2026-11-07 | R0 | pi-orchestrator | GO | ATTACK-RESEARCH.md, ETHICS.md, STATE.md | scope and safety review | D-1 provisional exploratory venue | R1 |
| 2026-11-07 | R1 | lit-scout / kb-curator | GO | LITERATURE.md | framework checker; 54 rows A=21/B=14/C=19 | full-text and public novelty search pending | R2 |
| 2026-11-07 | R2 | lit-scout | GO | ATTACK-CHAIN.md | required chain columns and evidence levels present | memory and propagation links are inference | R3 |
| 2026-11-07 | R3 | kb-curator / lit-scout | GO | GAP-MATRIX.md, KB-POSITION.md | four intersections have IDs, objections and controls | I1 is overlap-risk, not a novelty claim | R4 |
| 2026-11-07 | R4 | idea-miner / pi-orchestrator | GO | IDEA-BRIEF.md, IDEAS.md, CLAIMS.md C1 | one variable, mechanism control, kill switch and exact evaluator | C1 registered then weakened by falsifier | R5 |
| 2026-11-07 | R5 | idea-miner / experimenter | GO (mock-only) | pilots/I1-memory-cascade | 120 raw rows; local truth/utility pass; paired controls pass | D-2 blocks real-model interpretation | R6 |
| 2026-11-07 | R6 | threat-modeler / experimenter | GO / CLOSED | THREAT-MODEL.md, threat JSON, PROTOCOL.md, real_trials.jsonl | threat-check; 150-row pilot; exact evaluator | C2 primary comparison/control failed | R9 |
| 2026-11-07 | R9 | falsifier | GO | CLAIMS.md, checks/falsify/C1/, checks/falsify/C2/ | C1 weakened; C2 refuted; no open I1 claim | I1 closed; new idea required | R4 |
| 2026-11-07 | R5-P4-v2 | experimenter / falsifier | GO | pilots/P4-typed-handoff/v2_real_trials.jsonl, v2_real_analysis.json, checks/falsify/C3-v2.md | raw recomputation passed; candidate 30/30 vs mechanism-control 0/30; matched visible payloads and responses | D-11 accepts bounded protocol survivor; no general LLM or novelty claim | R6-P4 |
| 2026-11-07 | R6-P4 | threat-modeler / experimenter | PARTIAL | THREAT-MODEL-P4.md, threat/P4-typed-handoff-v2.json, results/2026-11-07-p4-typed-handoff-v2/PROTOCOL.md | threat JSON passes validator; protocol and safety boundary frozen | second adapter/model, defense, adaptive attacker and fresh pre-emption pending | R7-P4 after R6 completion |
| 2026-11-08 | R6-P4 replication | experimenter / falsifier | GO (bounded) | v2_alt_real_trials.jsonl, v2_alt_real_analysis.json, DEFENSE-ADAPTIVE.md | independent adapter + Astra: candidate 30/30 vs mechanism-control 0/30; defense adaptive rows 0/60, false triggers 0/10 | broad mechanism still overlaps public provenance-erasure work | R4-P4 narrowing |
| 2026-11-08 | R6 pre-emption screen | lit-scout / pi-orchestrator | NO-GO (broad framing) | R6-P4-screening-2026-11-08.md | Trust Cascade full text directly covers natural-language delegation provenance/authority loss and trust reclassification | only typed/schema conversion delta remains overlap-risk; no novelty wording | R4-P4 narrowing or close |
| 2026-11-08 | D-13 P4 closure | pi-orchestrator | CLOSED | R6-P4-screening-2026-11-08.md, DECISIONS.md D-13 | second screen found adjacent direct coverage across multi-CaMeL, structured delegation, authority laundering and provenance-aware authorization | preserve P4 logs as protocol/negative-boundary artifacts | R4-fresh |
| 2026-11-08 | R4 fresh candidate screen | idea-miner / lit-scout | PARTIAL | R4-FRESH-CANDIDATES-2026-11-08.md | Q1 parser differential retained for screening; Q2 cache, Q3 capability union, Q4 monitor disagreement, Q5 failure laundering rejected before experiments | full-text/public pre-emption and claim registration pending | R4-Q1-screening |
| 2026-11-08 | R5-Q1 mock | experimenter / falsifier | GO (mock-only) | pilots/Q1-parser-differential/trials.jsonl, analysis.json, PROTOCOL.md | independent recomputation: 120 rows; candidate 30/30, controls 0/30; AST mismatch only candidate; utility 120/120 | C4 remains open; no model/tool claim | R6-Q1 independent implementation |
| 2026-11-08 | R6-Q1 independent implementation | experimenter / falsifier | GO (bounded) | pilots/Q1-parser-differential/run_node_probe.js, node_trials.jsonl, node_analysis.json | separate Node parser pair matches Python outcomes on all 120 rows; no false triggers | model integration and framework-level scope remain to be decided | R6-Q1 protocol review |
| 2026-11-08 | R6-Q1 protocol | threat-modeler / pi-orchestrator | PARTIAL | THREAT-MODEL-Q1.md, threat/Q1-parser-differential.json, results/2026-11-08-q1-parser-differential/PROTOCOL.md | threat JSON passes validator; safety, capabilities, success and rollback are frozen | decide whether model/framework integration adds evidence; C4 remains open | R6-Q1 integration decision |
| 2026-11-08 | R6-Q1 transport smoke | experimenter / falsifier | GO (smoke-only) | sol/astra_model_smoke_trials.jsonl, summaries | Sol and Astra each preserve candidate bytes and reproduce CANARY_A vs control CANARY_B with zero errors | transport validation only; no model vulnerability claim | R6-Q1 integration decision |
| 2026-11-08 | R6-Q1 toolkit adapter | experimenter / falsifier | GO (bounded) | cra_mcp_probe.py, cra_mcp_trials.jsonl, cra_mcp_analysis.json | real `cra_mcp.adapter.ToolBox.call` parser path with fake server: candidate 30/30, controls 0/30, utility 120/120, false triggers 0 | no real tool or project mutation; C4 still open | R6-Q1 integration decision |
| 2026-11-08 | D-15 C4 bounded survivor | pi-orchestrator | GO (bounded) | IDEA-BRIEF-Q1.md, DECISIONS.md D-15, Q1 protocol result | Python/Node/toolkit/transport evidence converges; no real side effect | R7 parser variants, baselines and adaptive grammar search required | R7-Q1 |
| 2026-11-08 | R7-Q1 grammar matrix | experimenter / falsifier | GO (bounded) | variant_trials.jsonl, variant_summary.json, analyze_variants.py | 720 rows; nested/top-level/Unicode duplicate variants candidate-only; canonical/reject controls and false triggers pass | framework baseline and public parser screen pending | R7-Q1 framework baseline |
| 2026-11-08 | R7-Q1 cra_mcp variants | experimenter / falsifier | GO (bounded) | cra_mcp_variants.py, cra_mcp_variant_trials.jsonl, cra_mcp_variant_summary.json | actual ToolBox executor path: 240 rows; candidate 30/30, controls 0/30, utility 240/240, false triggers 0 | public parser/schema-smuggling screen pending | R7-Q1 review |
| 2026-11-08 | D-16 C4 closure | pi-orchestrator | CLOSED | R7-Q1-screening-2026-11-08.md, DECISIONS.md D-16 | MCP Go SDK issue #805 and ATR-2026-02350 directly cover the parser mismatch and fix | preserve regression artifacts; return to R4 | R4-fresh-2 |
| 2026-11-08 | R4 screen B | idea-miner / lit-scout | NO-GO (Q6-Q10) | R4-FRESH-CANDIDATES-2026-11-08-B.md | dynamic graph rewrite, identity collision, stale-state resurrection, privacy composition and covert channels have direct current coverage | broaden search axis; no claim or experiment | R4-fresh-2 |

## MCP scout round — 2026-11-10

- User requested MCP-focused auto-research with actual subagent execution. Four independent roles completed: literature scout, idea miner, KB curator and threat modeler.
- Output: `R4-MCP-SYNTHESIS-2026-11-10.md`, `R4-SCOUT-kb-mcp-2026-11-10.md`, `R4-SCOUT-threat-mcp-2026-11-10.md`. Literature and idea hand-backs were delivered in the main session; no standalone files for those two are claimed.
- Decision: D-17. MCP-R4-02 is NO-GO as framed; 01/03/04/05 remain UNCERTAIN. The coordinator checked the actual toolkit loop and found no result-field auto-binding or approval-token inheritance in that path.
- New experiments, LLM evaluation calls and ASR measurements: none. This excludes the research assistant/subagent conversations themselves and does not estimate their usage cost.
- Errata: `prompts/get` availability is not sampling availability; cancellation is not rollback; a malicious tool repeating its own effects does not establish a victim authorization failure.
- Next: one pinned real-adapter read-only code-path check for MCP-R4-03; kill it if there is no actual validation/model-input split or security consequence. No unbounded candidate generation and no mock attack result promoted to an LLM finding.
- Checks: project structure and P0 checklist to be run after ledger updates. A structural PASS is not a novelty or feasibility PASS; existing unchecked P0 thesis/CFP items must remain unchecked.

## MCP-R4-03 source check closure — 2026-11-10

- Independent source checker found runtime `ToolBox.call` reads only `res.content`; the agent loop consumes that returned string. The only dual-field fallback is in a test helper, not a deployed security consumer.
- No two actual safety consumers, authorization split or execution-state witness were found. No model call, service launch or attack experiment occurred.
- Decision D-18 closes 03 for the inspected toolkit only; external SDK/host versions remain unverified. Source hashes and exact paths are in the synthesis §6.
- Current round is complete without a thesis or effectiveness claim. Do not repeat the local check; an external reopening needs a pinned implementation and an independent security-state witness first.

## MRTR screen — 2026-11-11

- Three subagents screened MRTR requestState integrity/argument binding. The specification and SDK contract require integrity/request binding for security-sensitive state, but no fixed host/client/server chain accepted a valid state with changed arguments and produced an independent unauthorized effect.
- The TypeScript deploy example only returns success text; it has no protected deployment effect. The Python SDK source contract was partial and did not prove a vulnerability.
- Decision: retain MRTR as UNCERTAIN, no claim and no experiment. Q1 parser, P4 provenance, R4-02 approval inheritance and ordinary parameter poisoning remain excluded.
- Next loop axis: MCP task/result lifecycle and server task-status/result binding, only if a read-only public implementation and independent effect witness can be found. Avoid relabeling failure/status laundering or stale-state as new.

## MCP task lifecycle screen — 2026-11-11

- Public task ID/session isolation issue GHSA-hvrp-rf83-w775 covers broad cross-client enumeration/read/cancel/queue access; do not repackage it.
- Fixed TypeScript SDK v1.29.0 commit `e12cbd7078db388152f6e839abdbe09ba01f3f32` in-memory task store keys tasks/queues by taskId and ignores `_sessionId`, but no evidence yet that independent user connections share the store instance and cross an identity boundary. This is implementation risk, not a demonstrated attack.
- `tasks/result` draining queued server-to-client messages is a narrow check point, but there is no host/approval/protected-effect witness. Keep UNCERTAIN and do not run a broker or canary experiment.
- Next loop must move to a different attack axis after this task screen; task ID isolation is not a new contribution without a concrete deployment beyond the published advisory.

## User-directed adaptive-toolchain review — 2026-11-11

- Request: auto-research the existing `自适应工具链与Agent行为扩展_研究构想.md`, without modifying its content. Original SHA-256 remains `63ca1233a225b6ea87ed6ed07857c4c7568bcdd4de593089a830f4df233f413c`.
- Completed independent local-paper, public-literature and threat/design nodes; main coordinator checked MCP semantics/local loop and merged reports. Output: `reviews/adaptive-toolchain-2026-11-11/REPORT.md` plus node reports and source materials. The public scout retained downloads and delivered its report as a hand-back; the coordinator wrote WEB-LITERATURE.md.
- Evidence: relevant sections in four local papers and method/evaluation sections in eleven public papers. Not a claim that every page of every paper or all cited-by literature was read. Source versions, quotes, limitations and exact checks are retained.
- Decision D-20: broad new autonomous-toolchain framing unsupported; MCP-UPD already rejects a prior-configuration requirement and has a no-function-name diagnostic payload; AgentDojo delegates goals; AgentDyn covers dynamic feedback. Strict registry knowledge, one new external-content ingestion and neutral real-failure/unspecified-alternative-path behavior remain an unverified evaluation question.
- Design corrections: same loop/feedback/budget in all arms; merge equivalent naive/goal conditions; use equal-knowledge fixed/capability baselines; distinguish user-task authorization abuse from privilege escalation; verify real canary flow and assigned-episode denominators. Normal history replay is not a new attacker instruction.
- New attack/model-evaluation runs, ASR measurements and EVIDENCE entries: none. Research assistant/subagent reasoning usage is not estimated as evaluation spend.
- Checks: corpus/project structure pass and source fingerprints match; final artifact, local-link and unchanged-input audit recorded in CHECKS.md. A documentation audit does not pass novelty or an experiment gate.
- Resume: remain R4. Pick one bounded question and freeze a realistic capability graph, authorization table, independent oracle and protocol before considering R5. I1/P4/Q1 remain closed; no new claim or experiment was registered.

## Code-execution clarification — 2026-11-12

- User clarified that “A11 中的恶意代码执行” refers to A11 Prompt Logic Attack in *When MCP Servers Attack*, not the knowledge-base A11 MPMA record and not necessarily Agent-generated code.
- A11 original chain: user selects an MCP Prompt → server-side Prompt handler runs prewritten logic → server-side effect; LLM participation is not required. If the handler also returns poisoned prompt text, later model influence is a separate A11+A12 composition.
- Incremental literature screen: INFUSE and CIBER directly establish external/indirect content → Agent-generated shell/Python/code → Docker sandbox execution → independent file/process/network/state effects. This is a prior for Agent code execution, not a first mechanism. MCP-SafetyBench MCE is mainly direct user-side or server implementation conditions; MSB is real MCP tool side effects, not proof of Agent-generated code execution.
- New artifacts: `reviews/adaptive-toolchain-2026-11-11/CODE-EXECUTION-LITERATURE.md`, `CODE-EXECUTION-DESIGN.md`, and updated `REPORT.md`/`SCOPE.md`. No model, code, MCP server, shell, payload or live target was run.
- Decision boundary: study A11 handler execution and Agent-generated sandbox code execution as separate questions. `G→T→X→E` (generated, submitted, sandbox-executed, canary effect) is required for the latter. Sandbox execution is not host RCE; malicious server self-execution is not prompt-induced Agent execution.
- Strict combined condition (unknown registry + one exposure + no online feedback + unspecified code-tool path + host/production RCE) remains unestablished and cannot be claimed novel.

## R4 effect-history screen — 2026-11-11

- Four bounded subagents completed literature, source, idea and threat checks. The broad effect-history/receipt/notification framing is `TAKEN/NO-GO`; no claim or experiment was authorized.
- Literature scout ran eight mechanism queries over the preceding 12 months: 38 arXiv hits, 17 in the preceding 30 days, and checked eight highest-relevance full texts/specifications/advisories. DBLP/Semantic Scholar rate limits and an OpenReview field-parsing failure make coverage incomplete, but direct overlap is sufficient for a NO-GO.
- Direct/near-direct coverage: TRAP covers tool-result misbinding/replay; GHSA-345p-7cg4-v4c7 covers shared transport cross-client response/notification/sampling/elicitation misrouting; effect-history covers duplicate/aborted/provisional effects; RAC, CapLease and Residual Authority Replay cover workflow/semantic/approval replay; Signed Sealed Leaked covers cross-call state mixing; MRTR specifies requestState integrity and binding requirements.
- Fixed source check: local `cra_mcp 0.2.0` commit `463779b318f78a7c9e62e86639fec135c0423bc5` and `mcp-agent 0.2.6` commit `f62d849350816588b1c6294e7914bbe4d8b84072` expose only a model-mediated A-result-to-B-parameter path; no automatic history-to-authorization or honest protected-effect chain was found.
- Candidate screen retained `receipt→workflow promotion` and `notification→terminal commit` only as UNCERTAIN implementation leads; `effect-history→retry/compensation` was rejected as a duplicate of covered recovery/replay boundaries. D-21 closes the broad axis and moves the loop to MCP sampling recipient/session binding.
- New model calls, MCP services, attack runs, ASR measurements and EVIDENCE entries: none. Continue to require a fixed host/client/server chain, independent effect ledger, nearest-work screen, and threat check before any pilot.

## R4 sampling recipient/session screen — 2026-11-11

- Four bounded subagents completed literature, fixed-source, idea and threat checks. The recipient/session binding framing is `NO-GO` for the checked implementations; no claim or experiment was authorized.
- Literature coverage checked eight high-relevance sources across recent and older material. GHSA-345p-7cg4-v4c7 directly covers shared transport/server cross-client sampling misrouting; other sources cover sampling abuse, context pollution, source confusion or sessionless state, without a distinct isolated-transport recipient-binding attack.
- Fixed source evidence: VS Code 1.106.0 tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57` binds the original server/request and does not read active chat history; mcp-agent 0.2.6 commit `f62d849350816588b1c6294e7914bbe4d8b84072` forwards through bound upstream sessions; Python SDK 1.23.1 commit `8e02fc17e196295116d3fa4e993116ce6e017c1` responds to the original session/id; TypeScript SDK 1.29.0 commit `e12cbd7078db388152f6e839abdbe09ba01f3f32` retains transport/request binding. A connection-manager/ContextVar lead remains unclosed only until a real caller and honest effect are shown; it is not a claim.
- Candidate screen found no GO variant. Model text, normal callback, allowed-model selection, logs, successful responses and attacker-owned side effects fail the independent-effect criterion. The only possible next read-only axis is sampling `tools`/`toolChoice`/`includeContext` semantics; do not treat a host ignoring `includeContext` as a vulnerability.
- D-22 closes the checked recipient/session framing and moves R4 to the bounded sampling tool/context semantics screen. No new model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 sampling tool/context screen — 2026-11-11

- The four-agent round ended with broad framing `NO-GO`; two agents timed out or hit a server-side 502, so their partial results were not treated as complete evidence. Two bounded follow-up checks then completed the source and literature boundary without running code or services.
- Fixed VS Code 1.106.0 source (`mcpSamplingService.ts:58–108`) uses server `messages/systemPrompt`, `options={}`, and returns text; `tools`, `toolChoice` and `includeContext` do not enter a host tool executor or private-context reader. mcp-agent 0.2.6 keeps `server_names=[]` and `use_history=False` in the checked sampling path.
- Final public checks: the MCP specification defines `toolChoice` as a model-generation constraint and a server-side multi-turn tool loop; `includeContext` may be ignored or constrained by client capability. GHSA covers shared transport misrouting; Unit 42's sampling example is a prompt-induced malicious-server tool action; Breaking the Protocol reports sampling injection/context leakage without this field-to-honest-effect chain. No direct precedent or fixed implementation witness passed the gate.
- The only remaining delta is a hypothetical server-only field reaching a protected host executor/private reader; it is `UNCERTAIN`, not a claim. D-23 closes the broad axis and moves the loop to MCP-R4-01 default-value approval ordering. No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP-R4-01 default-order screen — 2026-11-11

- Four bounded subagents completed literature, fixed-source, idea and threat checks. Default-value approval ordering is `NO-GO` for the checked implementations; no claim or experiment was authorized.
- Literature check through 2026-11-11 found direct=0 for `approval A → default/coercion B → honest protected effect`; nearest work includes Approve What, Exactly?, MCPTox, When Neither Side Confirms, MCP Tools, CoSAI MCP Security and normalization advisories. Direct novelty is not a reachability result.
- Fixed source evidence: cra_mcp approves raw arguments and removes null but fixed write tools have no default parameters; VS Code retains rawInput and forwards it; Python/TypeScript SDKs parse function/schema defaults but do not provide the required approval snapshot or attacker-controlled honest-tool default path.
- Candidate variants (omitted-field late default and null→omitted) were killed by missing schema-to-honest-sink reachability, defaults already covered by authorization, or attacker-controlled effects only. D-24 closes the checked axis and moves R4 to MCP-R4-04 resource_link cross-source dereference.
- New model calls, services, attack runs, ASR measurements and EVIDENCE entries: none. A future reopening requires a fixed caller, dependency lock, independent authorization/effect ledger and fresh nearest-work screen.

## R4 MCP-R4-04 resource-link screen — 2026-11-11

- Four bounded subagents completed literature, fixed-source, idea and threat checks. Resource-link cross-source dereference is `NO-GO` for the checked implementations; no claim or experiment was authorized.
- Eight sources were near but not direct: MCP resources/tools specifications, AWS AgentCore warning, Python SDK external-ref advisory, Mecatl fetch guard, COPEX, cross-framework resource injection and Filesystem Capability Laundering. They cover SSRF/confused-deputy, resource injection or filesystem capability boundaries, without the required third effect segment.
- Fixed source evidence: VS Code 1.106.0 binds image links to the original server and sends `resources/read` only to that server; mcp-agent exposes explicit `read_resource`; Python SDK 1.23.1 and TypeScript SDK 1.29.0 validate/return results without automatic cross-source dereference. No independent resource/effect ledger path exists.
- Image-link candidate, ordinary URI/resource reads, and attacker-owned resources were killed by source binding, lack of protected sink, or normal/SSRF semantics. D-25 closes the checked axis and moves R4 to initialize version/capability negotiation downgrade.
- New model calls, services, attack runs, ASR measurements and EVIDENCE entries: none. External host generalization remains unverified; reopening requires a fixed caller and fresh screen.

## R4 MCP initialize handshake screen — 2026-11-11

- Four bounded subagents completed literature, fixed-source, idea and threat checks. Initialize version/capability downgrade is `NO-GO/UNCERTAIN`; no claim or experiment was authorized.
- Literature and design checks found no direct attack evidence for a legal initialize response changing negotiated state and then changing authorization/response validation/protected action. However, MCP versioning/lifecycle, OWASP AISVS C10-03, TypeScript protocol-version docs and MCPS design already cover minimum-version floors, legacy fallback, feature gates and transcript binding; clean novelty is unavailable. Go SDK header/body precedence is parsing behavior, not a security downgrade.
- Fixed source checks found no negotiated-state-to-security-gate-to-honest-effect chain: TS SDK validation uses supported versions/outputSchema rather than a returned version to disable checks; VS Code stores handshake results without feeding them to approval/local execution gates; capabilities affect feature enumeration/notifications/logs; 2026-07-28 probing precedes per-request versioning.
- Candidate mining found zero surviving variants. Version differences, missing features, malformed parsing, authority/transport spoofing, session DoS and attacker-owned effects were killed. D-26 closes the checked axis and moves R4 to canonical streaming/notification/cancel state-machine screening.
- New model calls, services, attack runs, ASR measurements and EVIDENCE entries: none. Reopening requires a fixed dual-era host/client, dependency lock and independent handshake/action trace.

## R4 MCP canonical stream state screen — 2026-11-11

- Four bounded subagents completed literature, fixed-source, idea and threat checks. The canonical streaming/notification/cancel axis is `NO-GO` for the checked implementations; no claim or experiment was authorized.
- Literature: P18/P21 are mainly metadata/social-engineering tests; effect-history, TRAP, CapLease, Limbo and Recovery cover duplicate, cancellation, replay, delayed commit and recovery neighbours, but no direct response-only canonical FSM attack evidence. Cancellation remains best-effort and MCP does not promise rollback or exactly-once.
- Fixed source evidence: VS Code removes pending handlers on cancel/final/timeout and treats late final as unknown; TypeScript and Python SDKs similarly pop/clean handlers; progress/log are callbacks/logging; mcp-agent delegates one `tools/call` and retry targets the original tool. Server progress/final does not re-enter `invokeTool`; no honest protected finalizer, approval snapshot and independent effect ledger chain was found. Correct Python SDK public tag is `8e02fc17e196295116d3fa4e993116ce6e0171c7`; the longer SHA in older notes does not exist.
- Candidate variants (progress=100% plus final, old stream reconnect/re-entry) were killed by UI-only effects, invalid second final/old protocol semantics, or generic retry/idempotency overlap. D-27 closes the checked axis and moves R4 to gateway capability subject/audience/purpose binding.
- New model calls, services, attack runs, ASR measurements and EVIDENCE entries: none. Reopening requires a fixed host finalizer, approval ledger and honest sink.

## R4 MCP gateway capability screen — 2026-11-11

- Four bounded subagents completed literature, fixed-source, idea and threat checks. Gateway capability subject/audience/purpose binding is `NO-GO` for checked implementations; no claim or experiment was authorized.
- Literature: eight sources were direct=0/near. HCP v2, attenuating tokens, state-handle hijacking, MCP authorization and ABAC cover binding, per-hop audience, attenuation and token-passthrough principles. MCPHub is a serverName IDOR, and GatewayBench measures exposure/injection rather than A-owned ref forwarding to B effect.
- Fixed source evidence: local cra_mcp commit `463779b318f78a7c9e62e86639fec135c0423bc5` is single-project; GatewayBench `2610.23449v1` is a research artifact with no auditable gateway commit; PRECINCT commit `a1fe87c117e091f1e70ad3ac1523ace8e0835b02` has random ref, expiry and SPIFFE owner checks, but fixed upstream dispatch has no ref→other server→B ACL→protected effect chain. Its store lacks issuer/audience/session and ToolName does not enforce purpose.
- Candidate variants: purpose-only and expiry-only changes cannot create B access; subject/audience remains an unverified implementation question. Q7 identity collision, P4 provenance, token passthrough, leaked B credentials and permissive brokers are excluded. D-28 closes the checked axis and moves R4 to non-filesystem contract/effect data-flow.
- New model calls, services, attack runs, ASR measurements and EVIDENCE entries: none. Reopening requires a pinned real cross-server ref consumer, B ACL/sink and independent tuple/effect ledger.

## R4 MCP non-filesystem contract/effect screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, idea and threat checks. The broad declared benign/read-only contract→non-filesystem effect framing is `TAKEN/NO-GO`; no claim or experiment was authorized.
- Literature direct evidence: AWS DocumentDB `GHSA-j694-4m5j-w8hc` accepts `$out/$merge` through authenticated default read-only aggregate and writes an independent DB; Tabularis `GHSA-xrx3-j98v-67x9` lets schema-valid benign introspection reach stacked SQL writes/deletes with an independent SQLite effect. DCI, ChainCaps, CXI and destructive-approval work are near/static/defense evidence.
- Fixed source checks found real benign effects in GitHub issue creation and archived Postgres read tools, but no declared-out effect, independent ledger or strict/reference block under the project threat model. CE-1 read→DB trigger/outbox remains only an audit question after broad pre-emption; CE-2 tenant fan-out is an IDOR/gateway/parameter near-neighbor.
- D-29 closes the broad axis as taken/no-go. No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred. Next R4 axis is elicitation URL-mode consent/callback binding, excluding ordinary elicitation, automatic private-form reading and routine OAuth/redirect flaws.

## R4 MCP elicitation URL-mode screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, idea and threat checks. URL-mode elicitation consent/callback binding is `NO-GO` for checked implementations; no claim or experiment was authorized.
- Literature: MCP 2025/2026 elicitation specs, SEP-1036, MRTR and TypeScript SDK docs cover consent, requestState/elicitationId, completion recipient and Alice→Bob threat scenarios but provide no direct exploit. Recent search found no direct URL-mode callback binding paper/advisory; generic OAuth/CSRF, phishing, SSRF, Inspector RCE and host unsupported issues are excluded.
- Fixed source evidence: VS Code 1.106.0 is form-only and treats URL as a URI field; mcp-agent forwards URL/form to an application callback without browser/state/tenant binding; Python SDK URL mode requires custom callback and completion is no-op by default. No host-mediated browser callback/result to honest sink exists.
- Candidate E3 origin/tenant omission is pre-empted by GHSA/MSRC callback/state binding; E1 global pending-slot and E2 completion≠consent remain unverified but lack host-owned protected sink. D-30 closes the checked axis and moves R4 to MRTR requestState end-to-end integrity/argument binding.
- No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred. Reopening requires a fixed real URL-mode host and independent consent/effect ledger.

## R4 MCP MRTR requestState screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, idea and threat checks. MRTR state-binding omission is `NO-GO/UNCERTAIN`; no claim or experiment was authorized.
- Literature: MRTR specifies integrity and original-request retry, with principal/TTL/method+salient-args binding guidance; Python, TypeScript, Ruby and Juneau codecs cover method/target/args/principal/TTL in various configurations. TRAP/RAC/CapLease/Residual Authority Replay and task-ID work are near or excluded. Strict direct=0/8; standards/codec design is not an exploit.
- Fixed source checks found no valid-state+changed-request+honest-effect chain. Where method/target/args are bound, changed requests are rejected before handler; where session/single-use are optional, no protected sink/effect witness exists. TypeScript example success text and partial Python contract do not count.
- V1 method binding and V2 effect-selector omission remain only implementation audit questions; no broker, weak state or experiment. D-31 closes MRTR and moves R4 to pagination/cursor binding.
- New model calls, services, attack runs, ASR measurements and EVIDENCE entries: none.

## R4 MCP pagination/cursor screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, idea and threat checks. Pagination/cursor source binding is `NO-GO` for checked implementations; no claim or experiment was authorized.
- Literature: 12-month arXiv/ACL/advisory checks found direct=0, but this is not full-index proof. MCP pagination defines opaque cursors and prohibits cross-session persistence; TS/Go/Python/Java helpers remain local to a client/list method. Cursor bugs found are repeated cursor, serialization, missing-page, OOM or public-list issues, not cross-server protected-read effects.
- Fixed source evidence: VS Code auto follows `nextCursor` inside one handler/server/list method; mcp-agent loops per server connection; TS SDK does not auto-follow. Everything resources are static/public with no tenant ACL/ledger. No A cursor reaches B method/session/tenant and no independent B protected effect exists.
- V1 source-unbound automatic continuation remains an audit hypothesis only; V2 method-unbound continuation died at Gate A. D-32 closes checked pagination and moves R4 to batch/bulk item-level authorization.
- New model calls, services, attack runs, ASR measurements and EVIDENCE entries: none.

## R4 MCP batch/bulk authorization screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, idea and threat checks. Batch item-level authorization is `NO-GO` for checked implementations; no claim or experiment was authorized.
- Literature: MCP core has single `CallToolRequest`/`ReadResourceRequest`; ext-apps, SEP-2848, RAC, approval-laundering and destructive-approval work are near/defense/proposal, not direct batch item effect. Strict direct=0.
- Fixed source evidence: cra_mcp and VS Code issue single tool calls; multiple model calls are separately approved/executed; TS SDK single `callTool`; Go SDK rejects JSON-RPC batch for newer versions; conformance server has no batch schema/ACL/sink. Arrays are schema data, not batch dispatch.
- Candidate V2 tenant fan-out is ordinary BOLA/tenant authorization and closed; V1 relation/subobject expansion and V3 server action plan remain only external implementation audit hypotheses with no source witness. D-33 closes checked batch and moves R4 to resource subscription/update binding.
- No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP resource subscription/update screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, idea and threat checks; two source/candidate agents initially timed out, then a narrow source retry completed. Subscription/update binding is `NO-GO` for checked implementations; no claim or experiment was authorized.
- Literature: 12-month/recent checks direct=0/8. MCP interaction is application-driven; TS/Python/Cloudflare paths route notifications but do not require automatic read. OverServe is resource amplification/DoS, not this chain.
- Fixed source evidence: VS Code `watch` binds the original server and subscribes; `resources/updated` only fires an event; `resources/read` is explicit and remains original-server bound. TS SDK exposes explicit read/subscribe/unsubscribe; mcp-agent exposes explicit `read_resource`; Python SDK is transport/API forwarding. No automatic notification→read, cross-source cache key, B ACL or effect ledger.
- D-34 closes the checked axis and moves R4 to dynamic tool registration/list-changed binding. No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP dynamic tool registration/list_changed screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, idea and threat checks. Dynamic tool registration/list_changed is `TAKEN/NO-GO` in broad framing; no claim or experiment was authorized.
- FCD arXiv:2609.35088 directly covers dynamic refresh, stale formation/approval and handler drift reaching protected effects. MCP tools spec/best practices and OWASP/SEP guidance cover list_changed refresh and reapproval, but are not exploit evidence.
- Fixed source evidence: VS Code re-lists and updates registry/approval metadata on list_changed but does not invoke tools; mcp-agent/Python use explicit refresh/list; TS SDK autoRefresh is caller-configured and has no host approval/ACL/sink. No `registry→approval→honest protected effect` chain.
- V1 source-key fan-out and V2 auth-scope cache crossing remain high-overlap audit hypotheses; V3 generation-skewed commit has no fixed protected sink. D-35 closes the checked axis and moves R4 to resource-template URI variable binding. No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP resource-template URI variable binding screen — 2026-11-12

- Four bounded subagents completed the literature, fixed-implementation, candidate and threat checks. No service, model, experiment, claim registration or EVIDENCE number was produced.
- Literature result: `exact direct = 0`, but the broad mechanism is pre-empted by close coverage: MCP Object-Authz Lab S8 (resource URI tenant/object selector), The Stochastic Deputy (model-controlled tenant scope), n8n-MCP cross-tenant advisory, and RFC/OWASP URI/tenant/confused-deputy guidance. Any surviving delta would have to be a legal A template/source with host-mediated automatic expansion that crosses B source/session/tenant binding.
- Implementation result: TypeScript SDK v1.29.0 returns templates to the caller and requires a concrete URI for explicit read; no automatic cross-source consumer, B ACL or effect ledger. VS Code/mcp-agent fixed source witnesses were unavailable in the local tree, so their external behavior remains an audit question rather than evidence.
- Candidate result: RT-1 variable-source binding omission is uncertain but collapses into P4 provenance or BOLA without a pre-existing host router; RT-2 bind-before-canonicalize has no real two-stage witness and risks Q1/C4/path traversal; RT-3 source-blind template registry key has no registry→B ACL→protected effect and overlaps Q2/Q7/D-28/D-35.
- Threat result: a valid result requires A legal template/value, automatic host expansion, independent B ACL denial, B protected synthetic reader/sink and append-only ledger, strict/reference source/tenant binding, and preserved benign A utility. Completion, URI, logs, model text, ordinary read, B handler denial and attacker-owned effects do not count.
- D-36 closes the checked resource-template axis as NO-GO, retaining only an unverified external-host question as UNCERTAIN. The next bounded axis is the narrow MCP-R4-05 trusted retry/finalization binding question; do not rebuild a retry broker or weak approval state. No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP-R4-05 trusted retry/finalization binding screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, candidate and threat checks. No service, model, experiment, claim registration or EVIDENCE number was produced.
- Literature result: `direct=0/8`, `near=5/8`, `excluded adjacent=3/8`. AID-Guard, CapLease and Permission to Retry cover approval/recovery/effect-count defenses; workflow effect-history covers retry/abort/late effects; TRAP/GHSA/FCD cover replay, misbinding and drift. Cancellation is best-effort and does not itself define rollback or exactly-once semantics. Recent-index failures are not counted as novelty proof.
- Implementation result: prior fixed-source records preserve original request/server/session, clean pending/final/cancel/timeout paths and expose explicit tool dispatch; they do not show server event→host automatic resubmission or permit reuse. The current tree lacks the fixed snapshots, so this is bounded prior evidence, not a new universal safety claim. Local cra_mcp lacks retry/finalizer, approval ledger, trusted B and independent effect sink.
- Candidate result: C-1 attempt-blind/non-idempotent same-effect retry is D-21/D-27 duplicate/replay unless a new semantic attempt produces a second protected commit; C-2 cancel-terminal permit survival needs a distinct finalization effect and has no witness; C-3 retry-selector snapshot staleness needs host-owned target change and a stale approval snapshot, with no witness and high overlap with MRTR/FCD/approval replay.
- Threat result: success requires original p0 approval, legal A event, existing host retry/finalization transition, independent attempt/effect scope, trusted B ACL and append-only ledger, strict reference rejection, no p1, no idempotent retry, no transport duplicate and benign utility. Logs, UI, receipts, late finals and A-owned effects do not count.
- D-37 closes R4-05 for the checked fixed-source range as NO-GO, preserving only an unverified external-host question as UNCERTAIN. The next bounded axis is MCP task-augmented request/task-result handle binding; no model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP task-augmented request/task-result handle binding screen — 2026-11-12

- Four bounded subagents completed the literature, implementation, candidate and threat checks. This supplements the earlier task lifecycle record; no service, model, experiment, claim registration or EVIDENCE number was produced.
- Mechanism/version: 2025-11-25 experimental Tasks used `tasks/get` + `tasks/result`; 2026-07-28 moved Tasks to an extension, embeds terminal result in `tasks/get`, removes `tasks/result`/`tasks/list` and adds `tasks/update`. Mixing these eras would create a false API finding.
- Literature/advisory: GHSA-hvrp-rf83-w775/CVE-2026-52870 directly covers Python task cross-session enumerate/read/result/cancel; GHSA-22jm-h49p-29qw directly covers TypeScript shared task-store cross-session list/read/cancel. C# polling and a VS Code issue show task lifecycle polling but only return the original A result; RAC is adjacent workflow authorization drift. Known task-store isolation is not a new protected-effect attack.
- Implementation result: the four pinned source snapshots are unavailable in the current tree. Historical TypeScript task-store notes do not prove shared connections, host automatic B dispatch, source/tenant/approval binding or an independent ledger; local `cra_mcp` only has unrelated pilot `task_id` fields and no task consumer or B sink.
- Candidate result: H1 issuer/session/tenant-blind registry, H2 terminal result→B selector rebinding and H3 terminal/expiry permit survival are all blocked. H1 overlaps the advisories; H2 requires an unobserved host-owned automatic A-result→B path and risks P4/approval inheritance; H3 is D-37/D-21 late/cancel/replay overlap.
- Threat result: success requires R0 approval, A-issued handle, automatic consumer, original A tuple denied by B ACL, actual B protected commit in an independent append-only ledger, strict source/issuer/session/tenant/approval/expiry binding rejection, and benign async utility. Task data/control access, explicit polling, model/application-mediated B calls, logs and A-owned effects do not count.
- D-38 closes the broad task-handle axis and H1/H2/H3 as NO-GO; fixed-source uncertainty remains an audit limitation only. The next bounded axis is MCP authorization resource-indicator/token-audience binding. No model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP authorization resource-indicator/token-audience binding screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, candidate and threat checks. No real/synthetic token was sent, no service/model/experiment ran, and no claim or EVIDENCE number was produced.
- Literature result: strict complete-chain `direct=0/8`, `near/adjacent=8/8`. MCP authorization/discovery and RFC 8707/9728 cover the resource/audience/issuer defense boundary; Rust/Python/TypeScript SDK advisories cover metadata or issuer mix-ups but terminate at attacker-owned credential/token sinks, which this screen excludes. `direct=0` is not a novelty proof.
- Implementation result: the four pinned sources/locks are unavailable locally; no authorization challenge, protected-resource metadata, resource indicator, token cache/key, issuer/audience route or B ledger witness can be read. Local `cra_mcp` has only static Bearer/Host checks and is not an OAuth host or B protected endpoint.
- Candidate result: AI-1 origin-stripped auth-cache key and AI-2 post-challenge metadata tuple rebinding remain conditional audit hypotheses with no cache/transaction witness; AI-3 challenge-origin-blind selector is ordinary OAuth misconfiguration, redirect/SSRF or token passthrough and is closed.
- Threat result: success requires automatic A metadata consumption, existing B route/ACL/receiver, B expected deny but independent acceptance/commit, strict origin/resource/issuer/audience rejection and benign A utility. A token receipt, A-owned sink, logs, 401/403, weak B verifier and real credential exposure do not count.
- D-39 closes the checked auth resource-indicator/token-audience axis as NO-GO, retaining only an unverified fixed-host audit question. The next bounded axis is roots boundary binding; no model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP roots boundary binding screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, candidate and threat checks. No service, real file/workspace, model, experiment, claim registration or EVIDENCE number was produced.
- Literature result: strict direct complete-chain coverage `0/8`; roots disclosure, filesystem boundary, tenant-scope guidance and root registry/list confusion are near/partial. IBM MCP Context Forge GHSA-x39c-q2jx-f325 is the strongest real advisory but requires root registration/admin access and ends at cross-session root disclosure; it does not show A legal `roots/list` triggering B protected effect. `direct=0` is not novelty proof.
- Implementation result: historical VS Code H1 evidence shows server request→roots callback→host-configured `explicitRoots`/workspace folders with remote-authority filtering. The four target source trees/locks are unavailable locally; local `cra_mcp` has no roots consumer, root registry, B workspace/tenant ACL or independent ledger. Official filesystem semantics narrow roots and guard refresh generations; no A→B root consumer was found.
- Candidate result: R-1 source/session/tenant-blind root registry key lacks a registry→B effect witness and overlaps D-28/D-35/D-36; R-2 ambient root-context union lacks a context injector and overlaps D-21/D-38; R-3 stale/overbroad root snapshot is Q6/Q8/D-35 stale-state and remains closed.
- Threat result: success requires legal A roots request/context, existing automatic root consumer, pre-existing B root/ACL, trusted protected file operation, independent append-only canary ledger with expected A deny, strict root tuple rejection and benign A utility. Disclosure, URI/name, ordinary read, user sharing, path/symlink, SSRF, prompt injection, filesystem laundering and attacker-owned files do not count.
- D-40 closes roots boundary binding for the checked range as NO-GO, retaining only an unverified external-host audit question. The next bounded axis is tool annotation/effect-hint binding; no model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP tool annotation/effect-hint binding screen — 2026-11-12

- Four bounded subagents completed literature, fixed-source, candidate and threat checks. No service, model, experiment, claim registration or EVIDENCE number was produced.
- Literature result: strict direct coverage `0/8`; MCP/official annotation guidance, OWASP, ToolHive and destructive-approval work cover untrusted hints and confirmation boundaries. Dynatrace GHSA is an adjacent read-only/parameter injection case; no source contains A annotation→fixed host security gate→trusted B ledger chain. `direct=0` is not novelty proof.
- Implementation result: target source trees/locks are absent. Historical VS Code data shows registry/approval metadata refresh, raw-input confirmation and explicit calls, not field-level annotation security gates; mcp-agent/SDK are explicit APIs. Local `cra_mcp` maps hints to confirmation inside a single non-target toolbox and has no A/B trusted sink, ACL or ledger.
- Candidate result: AH-1 destructive/read-only confirmation downgrade remains a conditional audit question with no host witness; AH-2 is D-29 contract/effect overlap; AH-3 is UI/model/network boundary. `idempotentHint` permit reuse is D-21/D-27/D-37 overlap.
- Threat result: success requires a single annotation flip to change a fixed host security decision for an existing trusted B operation, B expected deny/confirm, independent append-only commit, strict actual-effect recomputation rejection and benign utility. UI/log/model text, user approval, A-owned effects and B rejection do not count.
- D-41 closes annotation/effect-hint binding for the checked range as NO-GO, retaining only an unverified external-host audit question. The next bounded axis is tool identity/name shadowing binding; no model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP tool identity/name shadowing binding screen — 2026-11-13

- Four bounded subagents completed literature, fixed-source, candidate and threat checks. No service, model, experiment, claim registration or EVIDENCE number was produced.
- Literature result: strict direct coverage `0/8`; Docker MCP Gateway, WeKnora and LangChain cover bare/composite-name overwrite or wrong dispatch; IBM covers collision/DoS; Applied Sciences shows same-name multi-server defense; OpenAI Agents shows qualified-name rejection/namespace. These block broad novelty but do not provide the B-side ledger chain. `direct=0` is not novelty proof.
- Implementation result: exact target source trees/locks/commit objects are unavailable. Historical VS Code records show refresh plus explicit invoke; mcp-agent has server-name/namespaced connections and explicit call; SDKs are transport/session layers. Local `cra_mcp` is single-server and has no B ACL/effect ledger.
- Candidate result: TS-1 registry definition shadow, TS-2 approval epoch shadow and TS-3 dispatch target/source shadow all lack static A/B collision consumer and trusted B witness; they also risk D-21/D-28/D-35/Q7 overlap.
- Threat result: success requires A legal same-name metadata, fixed identity/approval consumer, actual B dispatch, A-derived expected-deny ACL, independent B commit, strict full tuple rejection and benign namespaced utility. UI/model ambiguity, A-owned effects, transport misrouting, dynamic stale and ordinary collision do not count.
- D-42 closes tool identity/name shadowing for the checked range as NO-GO, retaining only an unverified external multi-server host question. The next bounded axis is MCP external-content code-execution boundary; no model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## R4 MCP external-content code-execution boundary screen — 2026-11-13

- Four bounded subagents completed literature, implementation, candidate and threat checks. No service, model, code runner, paper code, experiment, claim registration or EVIDENCE number was produced.
- Literature result: INFUSE and CIBER cover the broad external/indirect content→Agent code/shell→sandbox effect; new MCP-specific CE-MCP arXiv:2602.15945 directly covers discovery artifact/tool metadata/tool output/exception→code execution in runtime/sandbox. Thus first-mechanism framing is taken; only a narrow single-exposure/unknown-registry/no-feedback/G-T-X-E evaluation condition remains uncertain.
- Implementation result: local cra_mcp is ordinary model function-calling plus ToolBox text results; no code artifact parser, dedicated code tool, trusted sandbox runner, independent state oracle, authorization ledger or server-self-execution monitor. Design files are static proposals; Q1 canary is a parser mock.
- Candidate result: V1 content→artifact→constrained code→sandbox, V2 pre-execution gate control and V3 ordinary-MCP/server negative control all fail the fixed runner/oracle gate; no candidate is registered.
- Threat result: future success requires `unauthorized(E) ∧ X ∧ valid_chain(G,T,X,E) ∧ ¬server_self_execution`, with content hash, artifact hash, episode/sandbox IDs, source-read witness, sink commit, utility and false-trigger controls. Current environment cannot produce these observations.
- D-43 closes code-execution boundary for the checked local range as NO-GO, retaining only an unverified protocol-screen question. The next bounded axis is MCP prompt lifecycle/handler binding; no model calls, services, attack runs, ASR measurements or EVIDENCE entries occurred.

## Rules learned

- The 54-paper matrix is summary-level evidence. Full-text verification is required before a paper number or novelty claim enters the paper.
- The first probe varies evidence order only; automatic memory and downstream aggregation are separate causal factors.
- A mock result is a probe signal, not evidence that a real LLM agent is vulnerable.
- A full-text result can pre-empt a broad mechanism after experiments pass; Trust Cascade directly covers provenance/authority loss and trust reclassification at natural-language delegation boundaries, so P4 must be positioned around a typed/schema conversion delta or be closed.
