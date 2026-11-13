# R4 MCP elicitation URL-mode consent/callback 绑定筛查

日期：2026-11-12。结论：`NO-GO`（检查对象）；未注册 claim、未运行服务或实验。URL-mode 机制在规范中有 consent/requestState/elicitationId 设计，但固定 VS Code、mcp-agent、Python SDK 没有 browser URL callback consumer 或 protected sink 链。

## 成功标准与边界

攻击者控制已连接 MCP server 发出的合法 `elicitation/create` URL-mode request、公开 URL/metadata 和 request 时序；不能控制 host、浏览器/用户、OAuth provider、诚实 sink、真实账户、审批者或 ledger，不能把真实凭据作为输入。成功必须由独立 ledger 证明：用户明确同意/提交的是 origin/session A，但固定 host 将 callback/result 交给 B origin/session/tenant，或没有新 consent 就让诚实 protected tool 产生 effect；strict/reference origin/state/nonce/tenant binding 阻断且 benign utility 保持。

排除普通 elicitation form、用户主动提交、URL phishing/SSRF、OAuth redirect/CSRF 通用漏洞、自动读取私有表单状态、server 自有副作用、日志/文本和 token passthrough。

## 文献查重

MCP 2025-11-25/2026-07-28 elicitation 规范、SEP-1036、MRTR 和 TypeScript SDK URL elicitation 文档已覆盖显式 consent、发起 client/user 绑定、requestState/elicitationId 完整性、completion 回原 client 与 Alice→Bob 错绑威胁场景；这些是规范/设计近邻而非 exploit。近 30 天未找到 URL-mode callback binding 的 direct 论文或公告。Claude Code URL-mode issue 是 host 不支持/取消，不是错 recipient effect；Inspector GHSA 是 OAuth callback→stdio RCE，非本题机制。结论：strict direct=0，广义 framing `overlap/taken: NO-GO`，不能从规范缺少统一 tenant/nonce/origin 算法直接宣称漏洞。

## 固定源码核验

- VS Code 1.106.0，tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`：`mcpElicitationService.ts:32–72,78–136` 是 QuickPick form；请求类型 `modelContextProtocol.ts:1492–1511` 只有 `requestedSchema`；`mcpServerRequestHandler.ts:327–328`、`mcpServer.ts:610–620` 将请求交给 form service；`mcpElicitationService.ts:284–295` 的 URL 只是 form 字段 `format:'uri'` 校验。没有 URL 展示/浏览器打开或 callback consumer。
- mcp-agent 0.2.6，commit `f62d849350816588b1c6294e7914bbe4d8b84072`：`mcp_agent_client_session.py:366–423` 可转发 URL/form，但 `:420–423` 只调用应用注入 callback；`elicitation/handler.py:89–94,139–168` 内置 handler 只读 form schema；`407–418` 复制 message/url/elicitationId/server_name，不传 requestState。无 origin/tenant/object ACL 或 protected sink。
- Python SDK 1.23.1 的真实 tag commit 为 `8e02fc17e196295116ce6e0171c7`：`client/session.py:147–155` 只有自定义 callback 才宣告 form+url；`types.py:1858–1880` 只有 url/elicitationId；`client/session.py:597–607` completion 默认 no-op。JSON-RPC request-id/session 路由不是 browser callback binding。

## 候选与判定

- E1 全局 pending 槽覆盖：`UNCERTAIN` 但无固定 host URL callback consumer，且 GHSA 已覆盖广义跨 client misroute；不进入实验。
- E2 completion 不等于 consent：`UNCERTAIN` 但无 host-owned protected sink，接近 effect-history/MRTR；不进入实验。
- E3 origin/tenant 元组遗漏：`NO-GO`，与 GHSA/MSRC callback/state/多租户绑定近邻直接重叠。

当前固定对象判定 `NO-GO`；外部实现不能泛化。若重开，只能固定真正支持 URL-mode 的 host/server/client，追踪 state/nonce/origin/session→browser callback→recipient/tenant ACL→protected sink，并使用独立 consent/effect ledger。下一轮转入 MRTR requestState 端到端绑定的最后有界源码/文献检查；不得构造 permissive host 或混用旧 TS SDK v2 与 2026-07-28 input-required 语义。
