# ATTACK-RESEARCH — ACL 2027 Agent Attack research

This project uses `agent-attack-v1`. The external corpus is read-only; all project conclusions must point to a
source row, raw trial log or explicit inference label.

## Current scope — MCP attack screening, 2026-11-10

The user requested a subagent-assisted search for an effective MCP attack research direction. The bounded question is whether one attacker-controlled MCP input or protocol interaction produces an independently observable unauthorized action in an owned sandbox, beyond a matched naive baseline, without sacrificing legitimate task completion. No mechanism or high success rate is assumed.

Primary surface: A external interaction through MCP. B internal state or C composition is secondary only when an intermediate causal state is independently observed. Read-only source corpus and paper locations remain those recorded below. Candidate novelty and real implementation reachability must pass before a fresh synthetic pilot; no new model experiment is currently authorized by a passed gate.

Current synthesis: [R4-MCP-SYNTHESIS-2026-11-10.md](./R4-MCP-SYNTHESIS-2026-11-10.md) plus dated screens through [R4-MCP-CODE-EXECUTION-BOUNDARY-SCREEN-2026-11-13.md](./R4-MCP-CODE-EXECUTION-BOUNDARY-SCREEN-2026-11-13.md). D-43 closes MCP external-content code-execution boundary for the checked local range and V1/V2/V3 as NO-GO; INFUSE/CIBER and MCP-specific CE-MCP arXiv:2602.15945 cover the broad mechanism, while local code lacks a fixed runner/oracle/G-T-X-E chain. The next bounded question is MCP prompt lifecycle/handler binding. The project remains in R4 without a selected thesis or experiment. Reopening any closed axis requires a pinned implementation, independent protected-effect witness and fresh mechanism distinct from its recorded nearest work; no general source expansion or model trial is implied.

I1, P4 and Q1/C4 remain closed as paper directions. Their logs and original protocols are retained. The I1 question, variable ledger and probe arms below are historical; they must not be resumed as the current MCP experiment. Current execution remains limited to project-owned synthetic canaries, no external effects, no real secrets, no production targets and no publication.

## User-directed focused review — 2026-11-11

The user requested auto-research of `papers/10_MCP攻击/自适应工具链与Agent行为扩展_研究构想.md`. This bounded R0/R1/R4 literature and design review is complete, with separate local-paper, public-literature and threat/design reports under `reviews/adaptive-toolchain-2026-11-11/`. `REPORT.md` is the coordinator synthesis; D-20 rejects the broad new-autonomous-attack framing and retains only an UNCERTAIN evaluation question under restricted attacker knowledge and neutral real failure. Four local papers and eleven public papers were checked at relevant full-text-section level, not comprehensively reproduced. The review does not select a thesis, reopen I1/P4/Q1, register an effectiveness claim, authorize a new evaluation spend or change the safety boundary. Its question is whether one fixed external-content input under restricted attacker tool knowledge has a remaining, measurable delta in victim replanning and unauthorized effects beyond strong matched baselines.

## Historical profile — I1 (closed; not the current execution plan)

- **profile:** `agent-attack-v1`
- **research question:** Under a query-only attacker that controls the order of synthetic, individually true evidence fragments, does automatic memory plus downstream summary aggregation create a persistent false causal belief that is absent or weaker under random order, no memory or no aggregation?
- **primary surface:** `B internal cognition`
- **secondary surface:** `C collaboration`; `A external evidence` is the controlled input channel, not an additional attacker capability
- **corpus root:** `/Users/dj/Documents/paper/Agent/research_attack_ideas`
- **corpus matrix:** `/Users/dj/Documents/paper/Agent/research_attack_ideas/paper_matrix.csv`
- **paper source tree:** `/Users/dj/Documents/paper/Agent/papers` (read-only; no PDFs copied into this project)
- **KB:** `/Users/dj/Documents/paper/Agent/research_attack_ideas/paper_inventory.md` as a summary-level positioning view
- **target venue / deadline:** ACL 2027 main conference through ARR / 2027-01-04; current ACL/ARR checklist pending R0 completion
- **compute and API budget:** local OpenAI-compatible gateway `http://127.0.0.1:3425/v1`; model route `auto/gpt-6.1-sol`; temperature 0; max output 256; ≤$50 equivalent and ≤2 CPU-hours for the pilot
- **kill date:** 2026-11-14

## Scope and safety

### In scope

- local deterministic/mock agents, synthetic event graphs and offline summaries;
- evidence ordering, automatic memory writes, memory reset, downstream summary sharing and exact belief/canary probes;
- intermediate logs for local truth, inferred causal edge, memory entry, downstream repetition and utility.

### Out of scope

- real users, real credentials, real personal data, production pages, public MCP registries,
  live third-party services and irreversible tool actions;
- direct database writes, model-weight changes, system-prompt modification or real tool execution;
- deployable prompt payloads, real-world misinformation campaigns or claims about production systems.

### Stop and rollback

- **stop when:** 30 episodes, 3 seeds per first probe cell, 20 message/round steps per episode, or 1 CPU-hour;
- **rollback:** reset the synthetic episode and memory store between trials; remove only the project-local pilot directory if a run is invalid;
- **canary policy:** only fixed strings `CANARY_A` and `CANARY_B`; record whether a local function was called, never an external side effect;
- **redaction policy:** no real names, URLs, credentials, personal data, code execution or working external payloads in logs or git.

## Shared attack chain

```text
synthetic evidence fragments
  -> ordered context and summary retrieval
  -> causal interpretation and planning
  -> downstream summary/message routing
  -> memory entry or state change
  -> false-edge belief probe, canary choice, repetition and recovery
```

The first probe releases only **evidence order**. Later blocks independently release memory persistence and
summary aggregation. Model/backend, event graph, task, fragment contents, prompt, budget and seeds remain fixed.

## Evidence policy

- `full-text-verified`: page, section, table or figure checked;
- `abstract-verified`: the imported local summary explicitly supports the field;
- `inference`: this project's cross-paper interpretation;
- `unverified`: source missing or insufficient.

The imported matrix is summary-level. Its A07/A21 records remain unverified. No paper number is treated as a
project measurement. Project rates require raw JSONL, a command, environment metadata, `n` and a 95% interval.

## Automation boundary

### The research agent may

- normalize the supplied matrix, map the attack chain, compare mechanisms and draft gap/idea artifacts;
- generate synthetic event graphs and run the bounded mock probe;
- compute exact state metrics and preserve failed trials.

### The researcher must decide

- whether the cross-surface gap is sufficiently novel after full-text and public novelty checks;
- whether a mock effect merits a real-model pilot;
- the final threat-model wording, statistical interpretation, generalisation and release decision.

## Variable ledger

| id | surface | habit-fixed variable | values / range | fixed controls | primary metric | status |
|---|---|---|---|---|---|---|
| V-B1 | B | evidence order before automatic summarisation | random / chronological / narrative | same facts, graph, task, backend, seed and budget | false causal-belief rate | selected for R5 block 1 |
| V-B2 | B | memory persistence | off / auto-write / write-then-clear | selected order, task, backend, seed and budget | memory contamination and persistence | queued |
| V-C1 | C | downstream aggregation | none / summary only / summary + provenance | selected order and memory policy | downstream repetition rate | queued |

## Required arms

For the first probe:

1. clean random-order, no-memory, no-downstream baseline;
2. naive narrative-order condition at the same fragment and message budget;
3. candidate narrative-order plus automatic memory and downstream summary;
4. surface-matched chronological-order control with the same number of fragments;
5. memory-reset and provenance-preserving controls in the later block.

The first block must not claim a full cascade until the memory and downstream factors are separately ablated.

## Graph and handoff

`RESEARCH-GRAPH.md` is authoritative for node state. `progress.md` records every check and failed direction.
The first handoff after R0 is the summary-level evidence crosswalk; the first scientific handoff after R4 is a
bounded R5 probe with clean, naive, candidate and mechanism-control arms.
