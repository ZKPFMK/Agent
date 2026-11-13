# R4 MCP resource subscription/update 绑定筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查 server 的资源订阅与 `resources/updated` notification 是否被固定 host 错绑定到另一 server/session/URI/tenant，导致自动刷新过期授权下的受保护资源或把更新内容交给错误 protected tool。

## 成功标准与边界

攻击者控制已连接 MCP server A 的合法 resource subscription/update notification、URI metadata 和时序；不能控制 host/client、B server/database、用户、审批者、B token、sink 或 ledger。成功必须满足：

1. host 对 A 的合法订阅/URI 建立 pending subscription；
2. A 的 update notification 被自动映射到 B URI/session/tenant，或在订阅撤销/授权变化后仍刷新并提交受保护 B resource；
3. B ACL/authorization 本应拒绝，独立 ledger 记录 B protected synthetic object/tenant read or sink effect；strict source+session+URI+tenant binding 阻断；benign subscription utility 保持。

排除普通 `resources/updated` 文本、A 自有资源、显式 user `resources/read`、resource_link 跨源已关闭轴、cross-client transport GHSA、stale/revocation 已覆盖方向、DoS、日志和攻击者自有副作用。

## 待核验链

`resources/subscribe(A, URI) → host subscription/cache key → resources/updated(A, URI) → automatic refresh/read → B ACL/tenant/session authorization → independent protected effect ledger`。

需固定支持 subscription 的 host/client/server revision 和依赖锁，追踪订阅 key、URI canonicalization、server/session/tenant、unsubscribe/revocation 和自动 read/refresh；若 SDK/host 只转发通知、不自动读取，或每次显式重新授权，立即关闭。不得构造 permissive subscription broker。

## 有界查重与源码结果

- 文献查重：12 个月与最近 30 天 direct=0/8。MCP resources 规范将 interaction 设为 application-driven；TS/Python/Cloudflare 近邻只做通知/连接路由；OverServe 是请求放大/DoS，不是订阅错绑。
- VS Code 1.106.0 tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`：`mcpResourceFilesystem.ts:100–136` 的 `watch(uri)` 先解码原 server，再由该 server handler subscribe；`mcpServerRequestHandler.ts:365–370` 的 `resources/updated` 只触发事件；`mcpServerRequestHandler.ts:494–495` 与 `mcpResourceFilesystem.ts:274–276` 的 `resources/read` 是显式调用且仍绑定原 server。无 notification→自动 read、跨源 key、B ACL 或 protected ledger。
- TypeScript SDK 1.29.0 `e12cbd7078db388152f6e839abdbe09ba01f3f32`：`client/index.ts:575–583,716–725` 只校验 capability 并提供显式 read/subscribe/unsubscribe；无自动 refresh reader。
- mcp-agent 0.2.6 `f62d849350816588b1c6294e7914bbe4d8b84072`：`mcp_aggregator.py:730–810,1387–1449` 的 read/subscribe 需显式调用，按 server_name 选 connection；无自动更新读取器、tenant key 或 B sink。Python SDK v1.23.1 同样只有显式 API/通知转发；旧记录中 39 位 SHA 不能作为 commit。

结论：固定对象 `NO-GO`；没有 `A subscribe/update → host auto-read B → protected effect` 链。下一轴切换 dynamic tool registration/list-changed binding；不运行实验或服务。
