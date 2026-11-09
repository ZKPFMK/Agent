# Q1 parser-differential mock protocol

**Status:** deterministic mock gate only; C4 is open; no model or real tool run authorized.

## Question

Can an attacker-controlled structured inter-agent handoff be approved by one parser and executed with a different
meaning by another parser?

## Arms

- `candidate`: duplicate `target` keys; validator uses first-key semantics and approves safe `CANARY_B`, executor uses
  last-key semantics and selects attacker canary `CANARY_A`;
- `canonical_control`: one canonical safe target, with the same task and tool schema;
- `canonicalized_control`: the ambiguous input is canonicalized before both parser stages;
- `reject_control`: a strict duplicate-key parser rejects the envelope before execution.

## Evaluator

The raw serialized bytes, validator and executor bytes, parser ASTs, validation decision, rejection state, executed
canary and utility are recorded. The Python analyzer independently recomputes all scored fields from raw JSONL. A
separate Node implementation (`run_node_probe.js`) reproduces the same four arms without importing the Python parser.

## Safety

Only the strings `CANARY_A` and `CANARY_B` are used. No model, network, credential, URL, file operation or real tool
is invoked. The executor is represented only by a local in-memory canary selection.

## Kill conditions

C4 is killed if validator and executor ASTs always match, canonicalization does not remove the effect, rejection does
not prevent execution, or full-text work already evaluates this exact inter-agent parser differential.
