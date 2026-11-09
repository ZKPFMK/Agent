# R4 fresh candidate screen B — 2026-11-08

**Status:** no candidate authorized; all tested mechanisms have direct or near-direct current coverage

## Screened directions

### Q6 — dynamic task-graph rewrite / route-node injection

**Verdict:** pre-empted/overlap. FlowSteer studies planning-time decomposition, role assignment, dependencies and routing;
conjunctive prompt attacks study topology-dependent fragment composition; ControlValve and safe-topology work cover
transition constraints and graph invariants. No experiment is authorized from generic task-graph manipulation.

### Q7 — agent identity alias collision / entity rebinding

**Verdict:** pre-empted/overlap. Recent Agent Name Collision work directly studies human-readable agent aliases resolving
to the wrong agent, while A2A session-smuggling and identity standards cover message-to-entity binding. A new collision
matrix would need a distinct state transition beyond identity ambiguity.

### Q8 — revocation resurrection through stale shared state or checkpoint restore

**Verdict:** pre-empted/overlap. Revoked-but-still-authoritative memory, stale shared memory propagation, checkpoint
restoration and authority resurrection are directly covered by recent memory/authorization work and standards. No run.

### Q9 — compositional privacy-budget leakage across agents

**Verdict:** pre-empted/overlap. The Sum Leaks More Than Its Parts, AgentLeak, mutual-information/Rényi privacy work and
sequential multi-agent privacy-budget composition directly cover correlated per-agent outputs and global reconstruction.
No run.

### Q10 — timing/traffic covert channel between cooperating agents

**Verdict:** pre-empted/overlap. Secret collusion, covert storage/timing/behavioral channels, steganographic tool use and
collaboration fingerprinting cover the channel family. No run.

## R4 conclusion

The current public literature is closing the obvious cross-surface combinations faster than the local 54-paper corpus
suggested. The next R4 pass must search for a mechanism outside the already saturated families: provenance/authority
laundering, parser differentials, dynamic routing, stale state, privacy composition, covert communication, and ordinary
prompt/tool-channel variants are already screened or closed. No claim or model budget is authorized from this file.
