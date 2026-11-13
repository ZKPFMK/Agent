# R4 MCP 非 filesystem declared contract 与实际 effect/data-flow 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是判断一个 schema-valid、通过 host approval 的合法工具调用，是否因为非 filesystem 的 contract/effect 边界，在 benign server 中产生声明范围之外的网络、数据库、消息或租户 effect。

## 成功标准与边界

攻击者只能控制一次被受害者正常读取的 synthetic external record，使 agent 为既有 benign tool 生成 schema-valid 参数；不能修改工具代码、schema、server config、host、model、审批者或 sink。victim state 为 declared contract `C=(name,description,schema,annotations)` 与实际 effect `E=(db/network/message/recipient/tenant/object)`。

成功必须同时满足：

1. call 通过 schema/host approval，benign task utility 保持；
2. independent effect monitor 记录 synthetic canary 到达 contract 未授权的非 filesystem sink 或读取未授权 synthetic tenant/object；
3. effect 不是隐藏代码、签名木马、普通 model-selected 参数、filesystem capability laundering、SSRF、P4 provenance/authority laundering 或攻击者自有副作用；
4. strict effect-policy/reference checker 阻断该 effect，同时保留正常 utility。

## 重点区分

- Filesystem path/symlink/staging/capability laundering：已由 MCP-FSD 近邻覆盖。
- Hidden code/rug pull/signed tool：归 Signed Sealed Leaked/mcpvenom。
- Schema/parameter poisoning 或模型只生成越界参数但没有 sink effect：归 MSB/MCPTox/COPEX，不能算本轴。
- P4 authority/provenance 转换、普通 token passthrough、SSRF 和 logging/covert channel：排除。

## 待核验链

`synthetic external record → schema-valid arguments → host approval → benign tool dispatch → non-filesystem DB/network/message/tenant sink → independent effect ledger`。

需要固定一个真实 benign server/host revision 和依赖锁，确认 declared contract、实际 effect、对象/租户 ACL 和 effect monitor。若本地只有 filesystem 工具、隐藏代码或模型意图，没有非 filesystem 的完整 effect 链，立即关闭。所有后续工作仅限 owned/local/sandbox、synthetic tenant、fake DB、in-memory queue 和 loopback canary。

## 文献查重与边界结论

- AWS DocumentDB `GHSA-j694-4m5j-w8hc` 是 conditional-direct：authenticated `aggregate` 在默认 read-only 下接受 `$out/$merge` 并写入独立 DocumentDB；公告缺少完整 approval/ledger，但已击中广义 read-only contract→write effect。
- Tabularis `GHSA-xrx3-j98v-67x9` 是 direct：schema-valid `describe_table`/JSON-RPC 被当作 benign introspection，`table_name` 导致 stacked SQL，绕过 read-only/write approval 并对独立 SQLite 表 DROP/读写。它不是模型意图或攻击者自有 sink。
- Description-Code Inconsistency、ChainCaps、CXI 和 destructive-approval 工作是静态/防御/近邻证据；不能把 DCI 比例或 abstract 级 approval gap 当作本项目 ASR。

结论：广义“声明 benign/只读 contract→非 filesystem effect”已 `TAKEN/NO-GO`，不能注册新攻击 claim。只能保留统一评测/防御问题（effect sandbox、egress/recipient/purpose/tenant enforcement），不是新的攻击机制。当前不运行实验；下一轮切换到 MCP elicitation URL-mode consent/callback 绑定，避免重包装表单自动读取私有状态或普通 server elicitation。
