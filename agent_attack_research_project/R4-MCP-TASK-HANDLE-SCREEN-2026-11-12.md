# R4 MCP task-augmented request/task-result handle binding 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查 MCP task-augmented request/task-result 机制（若固定实现实际支持）是否把 A 的合法 task handle、`tasks/get` 或 `tasks/result` 结果自动绑定到 B 的 session/tenant/object/protected effect，而没有持续绑定原始 request、approval、source 和 ACL。

## 成功标准与边界

攻击者只能控制已连接 server A 返回的合法 task metadata/result/handle 或正常异步任务状态；不能控制 host/client task registry、B server/database、ACL、token、approval ledger、用户、transport 或 protected sink。成功必须满足：

1. fixed host/client/server 已支持 task-augmented request、task handle 查询或 task result retrieval，并且存在自动 consumer，而不是只提供显式 application API；
2. A 的合法 handle/status/result 经 host 自动解析或续接，实际选择 B session/tenant/object/protected tool/resource；
3. B ACL 按原 A source/session/approval 应拒绝，但独立 append-only ledger 记录 protected read/commit；
4. strict/reference handle binding 拒绝该路径，同时正常 A 异步任务 utility 保持。

排除 MRTR `requestState`、普通异步任务重放、transport JSON-RPC ID misbinding、effect-history/replay、dynamic tools、resource-template、pagination、普通 task polling、用户显式跨 session 查询、公开任务、日志/文本/模型意图和攻击者自有任务效果。

## 待核验链

`A legal task-augmented request/result → host task registry/handle resolver → source/session/tenant/object/approval binding → tasks/get or tasks/result → B protected effect ledger`。

需固定 host/client/server revision 和依赖锁，追踪 task handle issuer/source/session、original request id、method/args/target/principal/tenant、TTL/expiry、registry/cache key、task result consumer、B ACL 和 effect commit。若 MCP task 仅由 server/client 显式 API 转发、没有自动 resolver/consumer、或不存在 B protected ACL/sink，立即关闭；不得构造 task broker、弱缓存或多租户 victim。

## 四路筛查结果

本轮四个只读 scout 已完成；没有启动服务、调用模型、运行实验、注册 CLAIMS 或写入 EVIDENCE 数字。

### 机制与文献查重

- 任务机制是真实存在的，但必须区分协议时代：2025-11-25 experimental Tasks 有 `tasks/get`、`tasks/result` 和 `tasks/cancel`；2026-07-28 移入 `io.modelcontextprotocol/tasks` extension，终态结果由 `tasks/get` 携带，`tasks/result`/`tasks/list` 移除，并增加 `tasks/update`。
- 广义跨 session task handle/object 访问已被直接覆盖：Python SDK GHSA-hvrp-rf83-w775/CVE-2026-52870 覆盖 task enumerate/read/result-message consumption/cancel；TypeScript SDK GHSA-22jm-h49p-29qw 覆盖共享 `InMemoryTaskStore` 的跨 session list/read/cancel。复现这些 advisory 不是新贡献，也没有证明 B application object 或 protected effect 越权。
- C# SDK 的自动 polling/settling helper 和 VS Code task polling issue 只证明“task lifecycle 自动消费”作为实现模式存在；没有固定 A→automatic consumer→B protected effect witness。RAC 只覆盖相邻 workflow authorization drift。规范中的 task isolation/authentication 是防御语义，不是攻击结果。

### 固定实现与可达性

- 当前本地没有四个指定 revision 的可复核源码或依赖锁；不能用 Python SDK 1.30.0/2.3.0 缓存、`cra_mcp`、普通 `task_id` 字段或旧 handoff 摘要替代固定证据。
- 历史 TypeScript 线索提到 task store 按 `taskId` 索引、`tasks/result` 可 drain queued messages，但没有证明不同用户连接共享 store、没有 host 自动 B consumer、没有 source/session/tenant/approval 绑定和独立 B ledger。C# polling helper 若按文档工作，也只是把同一 A tool 的最终 `CallToolResult` 返回原始 caller。
- 当前固定实现集合没有证实 `A legal task handle/result → host automatic resolver → B session/tenant/object ACL → protected effect`；因此实现层不能升级为 GO。协议存在本身不构成固定 host 可达性。

### 条件候选与威胁边界

- H1 `issuer/session/tenant-blind task registry`：若固定 host 自动 resolver 以 opaque handle 选中 B context，strict tuple binding 应拒绝；当前没有 cross-session resolver、B ACL 或 ledger，且已知 SDK advisory 覆盖较宽的 task-store isolation，blocked/NO-GO。
- H2 `terminal-result to B selector rebinding`：若 host-owned auto-settle 把 A terminal result 直接变成 B object/tool/effect selector，且不经过用户/模型/应用显式调用，才与 ordinary result flow 区分；当前没有这样的 consumer，且容易退化为 P4/approval inheritance/参数或 URI 流，blocked/NO-GO。
- H3 `status/expiry terminal permit survival`：若 terminal/expiry transition 自动触发 B effect 且复用旧 permit，需独立 B ledger；该形态直接重叠 D-37 retry/finalization、D-21 replay 和普通 late/cancel residue，当前 NO-GO/DO_NOT_REOPEN。
- 成功必须有原始 R0 approval、A-issued handle、自动 consumer、B ACL 按原 tuple 应 deny、实际 B protected commit、独立 append-only ledger、strict handle/source/approval/expiry binding 拒绝和 benign utility。task state/read/cancel/queue access、模型文本、日志、普通 polling、用户显式 read 与 A 自有副作用均不计成功。

## 本轮裁决与边界

**VERDICT: NO-GO（广义机制已被 GHSA 直接覆盖；窄自动 B-consumer 链未证实）；固定实现缺失部分保留 UNCERTAIN，但不构成 claim 或实验许可。** 本轮是对既有 task lifecycle screen 的协议版本和已知 advisory 补核，不重开已关闭的 task ID isolation 方向，不进入 R5/R6。

硬关闭条件包括：只存在显式 `tasks/get`/`tasks/result` API；自动 polling 只把 A 结果返回原始 caller；跨 session 只有 task data/control；缺少既存 B ACL、protected sink 和 independent ledger；或需要构造 task broker、跨 session resolver、弱 cache、多租户 victim 来补齐链条。

## 下一条有界轴

下一轮切换到尚未筛查的 MCP authorization resource-indicator/token-audience binding：检查固定 HTTP host/client 是否会把已连接 server A 的合法 `401` challenge 或 protected-resource metadata 解释为 B resource/audience，并将 A 的 token/approval 发送到 B protected synthetic endpoint，且缺少 origin/resource/audience binding。该方向必须排除 SSRF、attacker-owned token sink、普通 OAuth phishing、transport redirect、gateway capability、handshake downgrade 和真实凭据；没有固定 metadata consumer、B ACL/audience denial 和独立 receiver ledger，立即关闭。

禁止接触真实 token、真实账户、第三方服务或生产 OAuth；只允许 owned/local/sandbox、合成 token 和无副作用 canary。
