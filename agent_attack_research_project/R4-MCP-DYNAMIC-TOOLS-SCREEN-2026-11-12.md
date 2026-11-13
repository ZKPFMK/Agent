# R4 MCP dynamic tool registration/list-changed 绑定筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查 server 的合法 tool registration/list-changed 更新是否让 host 在旧审批/缓存状态下自动加入或执行新的受保护工具，或把 A server 的工具更新错误应用到 B/session/tenant。

## 成功标准与边界

攻击者控制已连接 MCP server A 的合法 `tools/list` response、tool metadata 和 `notifications/tools/list_changed` 时序；不能控制 host/client/LLM、B server、审批者、ACL、sink 或 ledger，不能将真实凭据作为工具参数。成功必须满足：

1. host 收到 A 的合法 tool update/list change，并自动改变可执行工具集合或审批 metadata；
2. 新工具/更新后的 tool 在没有新列举、用户确认或 exact approval 的情况下让 honest protected sink 执行未授权 effect，或更新错误应用到 B/session/tenant；
3. 独立 ledger 记录 source server/session/tool version、approval snapshot、arguments、ACL 和 protected commit；strict registration/cache/source binding 阻断，benign utility 保持。

排除普通 tool poisoning/metadata injection、dynamic registration 仅改变可见性、模型自行选择新工具、跨-client GHSA、parser、P4、approval inheritance、攻击者自有工具 effect 和日志/文本。

## 待核验链

`A tools/list/list_changed → host tool registry/cache update → approval/policy snapshot → tool discovery/selection → honest protected sink`。

需固定支持 dynamic registration/list_changed 的 host/client/server revision 和依赖锁，追踪 registry key、server/session binding、version/epoch、approval cache invalidation、tool invocation 和 ACL/effect ledger。若 host 只重新列举而不自动执行、每次调用仍重新审批，或工具集合变化本身没有 protected effect，立即关闭。不得构造 permissive registry。

## 有界源码核验结果

- VS Code 1.106.0 tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e26357`：`mcpServerRequestHandler.ts:371–373` 消费 `notifications/tools/list_changed`；`mcpServer.ts:863–876` 自动 `tools/list`，`:813–821` 更新 primitive cache；`mcpLanguageModelToolContribution.ts:124–154` 重注册/删除 host tool，`:106–120,174–196` 重算 approval metadata；但 list_changed 不触发 invoke，实际执行仍需显式 `invokeTool`/`tools/call`。缓存/approval 可能按 definition/tool ID 和连接 nonce 绑定，但没有 protected ACL/effect ledger。
- mcp-agent 0.2.6 `f62d849350816588b1c6294e7914bbe4d8b84072`：显式 `refresh/list_tools` 和 namespaced map；通知仅记录，无 list_changed 自动处理或自动执行。
- Python SDK 1.23.1 tag `8e02fc17e196295116ce6e0171c7`：显式 `tools/list`、schema cache 和 `call_tool`；无专用 list_changed host consumer。TS SDK 1.29.0 `e12cbd7078db388152f6e839abdbe09ba01f3f32`：调用方显式启用 autoRefresh 后回调，SDK 本身没有 host approval/ACL/sink。

结论：固定对象 `NO-GO`；dynamic registry refresh 不形成 `list_changed→旧审批→未授权 protected effect` 链。下一轴切换 resource-template URI 变量绑定；不运行实验或服务。
