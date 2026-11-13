# R4 MCP canonical streaming/notification/cancel 状态机筛查

日期：2026-11-11。状态：screen pending；未注册 claim、未运行服务或实验。只读目标是判断一个已连接 server 是否能仅控制自己合法 canonical response/notification/cancel 时序，使固定 host 对同一 logical call 产生 duplicate 或 post-cancel 的诚实受保护 effect。

## 成功标准与边界

攻击者控制自己 pending call 的合法 response stream、progress/log notification、final result、延迟和取消相关时序；不能伪造其他 request ID、修改 host/client/LLM/用户任务/诚实工具或 sink，不能写 ledger。禁止 duplicate keys、Unicode/parser ambiguity、跨 session stale state、revoked checkpoint、DNS/transport hijack 和 timing covert channel。

候选成功必须有：

1. canonical event sequence 在协议语义上合法；
2. host 的 pending-call FSM 对同一 request/logical call 从 pending→terminal/cancel/commit 出现违反一次性或终态规则的转移；
3. 独立 fake-tool effect ledger 记录 `effect_count>=2` 或 cancel/timeout 后的诚实 protected commit；
4. benign task utility 保持，strict/reference FSM 对同一序列拒绝第二次 commit。

重复文本、progress/log、失败、成功消息、模型复述、攻击 server 自己的副作用不算 effect。

## 待核验问题

- MCP cancellation 是 best-effort，不能从“取消后仍有结果”直接推断 rollback 或越权；必须有固定 host 的 exactly-once/commit 语义或明确安全保证。
- streaming/notification 的 event ID、request ID、terminal state、timeout/retry 是否在真实 host 中被消费为执行状态，而非只进日志或模型上下文。
- P18/P21、effect-history、TRAP、CapLease 和已有任务/重放工作是否已经直接覆盖 candidate；若是，关闭。
- 至少一个固定 host/client 的代码链必须从 canonical response/notification 进入 honest protected sink；不可为了成功写 permissive broker。

四路子 agent 完成文学查重、源码、候选和威胁模型后再决定 NO-GO/UNCERTAIN/GO。所有后续测试只能使用 owned/local/sandbox 和内存 canary。

## 有界筛查结果

- 文献查重：P18/P21 主要是元数据/社会工程测试；effect-history、TRAP、CapLease、Limbo、Recovery 覆盖重复、取消、迟提交、重试和恢复近邻，但没有 direct 的 response-only canonical FSM 攻击实证。当前 broad framing `UNCERTAIN/NO-GO`，不能称 clean novelty。
- 候选挖掘：数值 progress 到 100% 后 final 只影响 UI 或缺 sink；旧版断流恢复重入依赖已取消的 Last-Event-ID/旧版恢复语义或一般 retry/idempotency；0 个候选进入实验。
- 固定源码：VS Code、TypeScript SDK、Python SDK、mcp-agent 均在 final/cancel/timeout 时清理 pending/handler，迟到 final 走 unknown ID 或被忽略；progress 只回调/日志；工具 retry 只重试原工具。MCP server 的 progress/final 不回流 `invokeTool`，没有 honest sink、approval snapshot 和 effect ledger 链。固定 Python SDK tag 应为 `8e02fc17e196295116d3fa4e993116ce6e0171c7`，项目旧记录的更长 SHA 不存在。
- 结论：当前固定实现 `NO-GO`；取消 best-effort、远端副作用 exactly-once 和 rollback 均未由 MCP 保证。若重开，只能固定真实 host 的 commit/finalizer/受保护 sink 并证明 reference FSM 会阻断额外 commit；不得构造 permissive broker。

下一轴：gateway capability 的 subject/audience/purpose/expiry 绑定；必须排除 Q7 identity collision、P4 provenance laundering 和普通 token passthrough。
