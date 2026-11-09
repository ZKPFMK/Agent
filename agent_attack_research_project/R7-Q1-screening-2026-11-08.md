# R7-Q1 public pre-emption screen — 2026-11-08

**Status:** C4 closed as an ACL paper candidate; protocol reproduction preserved

## Direct implementation match

### MCP Go SDK message smuggling via case-insensitive JSON unmarshalling

Primary issue: <https://github.com/modelcontextprotocol/go-sdk/issues/805>  
Rule summary: <https://agentthreatrule.org/en/rules/ATR-2026-02350>

The verified issue describes the same security mechanism as C4 at an MCP boundary. A JSON-RPC `tools/call` request
contains case variants such as `name`/`Name` or `arguments`/`Arguments`. An upstream gateway or authorization layer
parses one spelling and approves it; a downstream Go SDK parser matches field names case-insensitively and uses the
replacement value. The result is an authorization/execution mismatch. The issue identifies parser layers in
`internal/jsonrpc2/messages.go` and `mcp/shared.go`, and reports a fix in go-sdk v1.3.1 using case-sensitive decoding.

**Decision.** C4's validator/executor parser differential is a controlled reproduction and generalization of an already
reported MCP implementation vulnerability. The Python, Node, `cra_mcp`, Sol and Astra artifacts remain useful as a
redacted protocol regression test, but they cannot support a novel ACL attack contribution under the current claim.

## Adjacent verified work

- **Output Constraints as Attack Surface:** <https://arxiv.org/abs/2503.24191>. Full-text check found grammar/schema
  constraint attacks, but not parser disagreement.
- **From Allies to Adversaries:** <https://aclanthology.org/2025.naacl-long.101/>. Tool selection/scheduling injection,
  not parser differential.
- **ToolSafe:** <https://aclanthology.org/2026.findings-acl.1850/>. Prompt-injection tool-call monitoring, not duplicate
  or case-variant JSON parsing.
- **Agent session smuggling:** <https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/>.
  Stateful A2A instruction smuggling, not serialization/parser disagreement.
- **ACP tool-call protocol:** <https://github.com/agentclientprotocol/agent-client-protocol/blob/main/docs/protocol/v2/tool-calls.mdx>.
  Provides structured tool-call status and raw input fields; it is a protocol reference, not evidence of the C4 attack.

## R7 decision

1. Close C4 as an ACL paper candidate because the exact authorization/execution parser mismatch is already reported and
   fixed in an MCP SDK.
2. Preserve C4's raw protocol, toolkit, Python/Node, transport and variant artifacts as a regression/negative-boundary
   record. Do not release working exploit payloads or frame the result as a new vulnerability.
3. Return to R4 for a new mechanism-level candidate. No additional C4 model matrix is authorized.
