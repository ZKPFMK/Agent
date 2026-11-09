# Q1 parser-differential protocol result

**Status:** R6 protocol review; C4 open; deterministic Python/Node block passed.

## Reproduction

```text
python3 -I pilots/Q1-parser-differential/run_mock.py
python3 -I pilots/Q1-parser-differential/analyze.py
node --check pilots/Q1-parser-differential/run_node_probe.js
node pilots/Q1-parser-differential/run_node_probe.js
P4_ALLOW_REAL=1 P4_Q1_MODEL=auto/gpt-6.1-sol python3 -I pilots/Q1-parser-differential/real_forward_probe.py --smoke
P4_ALLOW_REAL=1 P4_Q1_MODEL=auto/gpt-6-astra python3 -I pilots/Q1-parser-differential/real_forward_probe.py --smoke
python3 -I pilots/Q1-parser-differential/cra_mcp_probe.py
```

## Result

The Python and Node implementations each generated 120 rows. Candidate final authorization was 30/30; canonical,
canonicalized and reject controls were 0/30. Validator/executor AST mismatch occurred in 30/30 candidate rows and 0/90
controls. Utility was 120/120 and false triggers were 0. Python and Node scored all 120 rows identically.

## Loopback transport smoke

A four-row smoke through the loopback gateway was run with `auto/gpt-6.1-sol` and `auto/gpt-6-astra`. Both models
preserved the candidate duplicate-key envelope byte-for-byte, yielding `CANARY_A`; both preserved the canonical and
canonicalized controls, yielding `CANARY_B`. The strict-reject arm made no model call. Each smoke had zero errors and
an estimated cost of `$0.00069`. These calls validate transport integration only.

## Toolkit adapter validation

The actual `cra_mcp.adapter.ToolBox.call` execution parser was exercised with a fake in-memory server and no project
mutation. Across 120 rows, the candidate produced 30/30 `CANARY_A` executions, all controls produced 0/30, utility was
120/120 and false triggers were 0. This validates the parser differential against the toolkit's executor path; it does
not establish framework prevalence or a real tool vulnerability.

## R7 grammar and toolkit variant matrix

The synthetic R7 matrix covered eight envelope variants over 720 rows. Nested, top-level and Unicode-equivalent duplicate
variants produced candidate-only success; canonicalization and strict rejection removed the effect; attack-first,
tool-field, unknown-field and canonical controls did not trigger. The same variants through the real `cra_mcp.adapter.ToolBox.call`
path produced 240 rows with candidate 30/30, controls 0/30, utility 240/240 and false triggers 0.

## Interpretation

C4 currently demonstrates a deterministic validator/executor interpretation split in a synthetic adapter boundary. It
does not show an LLM preference change, parser prevalence, framework vulnerability or a real tool effect. The next gate
is to decide whether a bounded Agent integration or a second framework implementation adds independent evidence. No live
tool or production target is authorized.
