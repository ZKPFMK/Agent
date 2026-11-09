# ATTACK-RESEARCH — ACL 2027 Agent Attack research

This project uses `agent-attack-v1`. The external corpus is read-only; all project conclusions must point to a
source row, raw trial log or explicit inference label.

## Active direction — P4 typed/provenance conversion

P4 tested whether an unsafe typed conversion at a two-agent handoff can upgrade one untrusted value into a trusted
authorization state. Its results are preserved as bounded protocol-level artifacts, but public pre-emption closed P4 as
an ACL paper candidate. Q1 then reproduced a known MCP parser mismatch across multiple local implementations; D-16
closed it as a paper candidate and preserved the outputs as regression evidence.

I1, P4 and Q1 remain recorded negative-boundary/protocol results. The active project has returned to R4 for a new
mechanism-level thesis.

## Profile

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
