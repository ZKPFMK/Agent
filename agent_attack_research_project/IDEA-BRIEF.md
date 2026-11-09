# IDEA-I1 — truthful evidence to persistent causal error

**Status:** dead for the preregistered order/adjacency mechanism; retained as a negative boundary result
**Proposer:** idea-miner / pi-orchestrator
**Date:** 2026-11-07

## One-sentence hypothesis

Under TM-I1 and a single local synthetic evidence agent, changing only the order of individually fact-verified
fragments changes the false-causal-belief rate because order alters the agent's global causal interpretation. The
full I1 cascade is killed if the order effect does not survive a paired control, if local fact truth is below 100%,
or if memory and downstream blocks add no measurable state difference.

## Position

- primary surface: B internal cognition
- secondary surface: C collaboration; A external evidence is a controlled input channel
- nearest corpus / KB papers: C18, B10, B13, C19; adjacent B02, C04, C07, C12
- evidence level of the source comparison: abstract-verified summaries plus project inference; full text pending
- one-line delta: measure the sequence `true fragments -> inferred false edge -> automatic memory -> downstream repetition`
  with local-truth, memory-reset, provenance and no-aggregation controls instead of reporting a single ASR
- why this is more than changing a model, prompt, dataset, topology or agent count: the first probe releases one
  habit-fixed evidence-order variable and defines intermediate state checks; later blocks release memory and
  aggregation separately under the same synthetic facts and budgets

## Threat model and safety

- attacker goal: control the order of a set of synthetic evidence fragments in an authorized offline sandbox
- knowledge: black-box with respect to the victim's internal belief and memory implementation; knows the synthetic
  fact pool and task interface
- capabilities: choose an ordering and presentation schedule only; no weight, system-prompt, database, tool or
  network access; at most one ordered evidence episode per trial
- access point and why reachable: a project-owned evidence/retrieval adapter supplies the ordered fragments to the
  local test agent; this is a sandbox interface, not a real website or service
- victim system and state: one deterministic/mock evidence agent; block 1 has no persistent memory or downstream
  agent; later blocks add a fixed local memory module and two downstream summary agents
- allowed environment: local Python process, synthetic event graphs, fixed canaries and JSONL traces
- synthetic data / canary: 30 planned episodes from 6–10-node causal graphs; fixed `CANARY_A` / `CANARY_B`
- out of scope: real information, users, secrets, websites, MCP servers, external model APIs, code execution and
  claims about deployed agents
- stop and rollback: stop at 30 episodes, 3 seeds per condition, 20 steps per episode or 1 CPU-hour; reset the
  episode and memory state between trials; preserve failed logs

## Released variable

- variable id: V-B1
- values / range: random order / chronological order / narrative order / narrative order with bridge swap
- fixed conditions: same graph, fragment text, local truth oracle, task, backend, prompt, message budget and seed
  pairing; memory off and no downstream agent in block 1
- expected mechanism: order changes which locally true fragments are combined into a non-existent causal edge
- intermediate state to log: local truth verdict, ordered fragment IDs, inferred edge, confidence, task utility and
  failure class

## Probe design

| arm | condition | purpose | fixed controls |
|---|---|---|---|
| clean | random order; no memory; single agent | no-attack baseline | same facts, graph, task, backend and seed |
| naive | chronological order; no memory; single agent | natural-order baseline at equal budget | same facts, graph, task, backend and seed |
| candidate | narrative order selected from the same facts; no memory; single agent | test the order mechanism | same facts, graph, task, backend and seed |
| mechanism-control | candidate order with the two bridge fragments swapped | remove the hypothesised causal bridge while preserving surface and length | same facts, graph, task, backend and seed |
| defense | provenance-preserving atomic facts plus causal-independence check | later block only; test a static defense | same selected order and task |
| adaptive-defense | attacker knows the provenance/independence check | later block only; do not run before defense is validated | same budget and task |

- evaluator: deterministic event-graph oracle for local truth; exact structured false-edge probe; no LLM judge
- primary metric: false-causal-belief rate, k/n, Wilson 95% CI
- secondary metrics: local fact truth rate, normal task utility, confidence calibration, false-trigger rate,
  memory contamination, persistence after reset, downstream repetition, runtime and token-equivalent cost
- seeds: 0, 1, 2 for the first 30-episode pilot; paired across arms
- resource limits: 30 episodes, 20 steps, no network, 1 CPU-hour
- raw trace path: `pilots/I1-memory-cascade/trials.jsonl`
- analysis command: `python3 code/analyze_probe.py pilots/I1-memory-cascade/trials.jsonl`

## Gate results

- Gate A freed assumption: neighboring work commonly fixes evidence order, or measures order and memory in
  separate papers; I1 releases order first and records the fixed conditions in this brief
- Gate B anomaly versus naive: mock-only PASS, but local-gateway C2 failed; narrative 17/30 versus random 14/30, exact paired p=0.607239
- root-cause intervention: bridge-swap was 23/30, higher than narrative 17/30; the preregistered adjacency mechanism is not isolated
- control result: clean 0/30, chronological 5/30, narrative 17/30, random 14/30, bridge-swap 23/30; all parse/utility/local-truth checks passed
- judge / rule validation: exact local truth and structured-output checks; no LLM judge used
- strongest falsifier: model sensitivity to statement direction or surface semantics, model snapshot drift, or post-hoc selection; the control failure blocks memory/downstream expansion

## Verdict

- [x] kill the preregistered order/adjacency mechanism: primary comparison and bridge-swap control failed
- [x] keep as a negative result and local-gateway boundary; no memory/downstream expansion
- [ ] advance to a new idea only after a fresh gap, claim, protocol and control matrix

## Provenance

- source files and hashes: `PAPER-MATRIX.csv`; corpus SHA-256 `5c2e7fc2b465660adc9eec9a0634c07debb175993eab058de6af34f4e1e51359`; `candidate_ideas.md`; `experiment_plan.md`
- code commit: no project commit yet; source toolkit nested repository is at its current working tree
- model/backend and snapshot: no external model; deterministic local mock backend to be recorded by R5
- config: `ATTACK-RESEARCH.md` variable ledger V-B1
- decision record: D-1 exploratory scope; D-3 local-gateway pilot; D-4 closes I1; C1 weakened; C2 refuted; no memory/downstream run
