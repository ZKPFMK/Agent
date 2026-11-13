# R4 MCP initialize 版本/能力协商降级筛查

日期：2026-11-11。状态：screen pending；尚无 claim、实验或服务。只读门检目标是判断恶意 server 能否通过协议合法 `initialize` 响应，让固定 host 接受较弱版本/能力状态，并执行严格参考 client 会拒绝的本地无副作用 canary。

## 成功标准与边界

攻击者只控制已连接 MCP server 的 initialize response，包括 protocolVersion、capability flags 和公开协商字段；不能控制 host/client 源码、用户任务、模型、其他 server、审批策略或真实工具。完整成功必须同时有：

1. host 接受低于预设最低版本或关闭安全相关能力；
2. 该握手状态改变后，host 的授权、响应处理或 protected action 与 strict/reference client 不同；
3. 独立 trace evaluator 记录 handshake、最终 negotiated state 和本地 synthetic canary effect。版本字段不同、展示字段变化、拒绝/解析错误或没有 action 差异不算攻击成功。

禁止使用 duplicate keys/Unicode/parser ambiguity、DNS/transport hijack、tool poisoning、普通 capability spoofing 或 server 自有副作用；这些分别属于 Q1/transport/metadata 近邻。

## 待核验问题

- 新版 MCP 是否仍存在 host 可接受的版本回退或双时代 fallback；旧版 initialization negotiation 不能外推到 2026-07-28 版本。
- capability flags 是否只影响 feature availability，还是改变审批、response validation、resource/authorization state machine。
- 至少两个固定 host/client 是否对同一合法低版本 response 有不同安全 action；若所有 host fail-closed 或只改变可用功能，候选关闭。
- 严格 reference state machine、最低版本 pinning、能力单调性检查和握手后重新验证是否消除差异。

后续四路子 agent 只读查重、实现和威胁审查完成后，才决定 NO-GO/UNCERTAIN/GO。不得为制造 downgrade 另写 permissive host，也不得连接真实第三方服务或生产 MCP。

## 有界筛查结果

- 文献与规范查重：没有发现“合法 initialize 响应 → 协商状态改变 → 诚实 host 授权/响应验证/受保护 action 改变”的 direct 攻击证据，但已有机制级规范/防御覆盖最低版本、legacy fallback、能力 feature gate 和 transcript binding，因而不能称为 clean novelty。
- 固定源码筛查：Python/TypeScript SDK 检查版本支持集合或 outputSchema，不存在由合法低版本关闭授权检查的路径；VS Code 保存 handshake 结果但未把返回版本接入审批或本地执行 gate；能力消费只影响工具枚举、通知和日志。现代 2026-07-28 每请求版本探测先于旧式 initialize，单条响应不能改变时代探测。
- 候选挖掘：0 个存活变体。版本差异、缺失 feature、解析错误、authority/transport spoofing、session DoS、server 自有副作用均被排除。OWASP/MCPS 防御建议和 Go SDK header/body 优先级问题不能替代 protected-effect witness。
- 结论：当前方向 `NO-GO/UNCERTAIN`；没有注册 claim、没有运行实验。若重开，只能固定 dual-era host/client、server SDK 和依赖锁，追踪 discover→initialize→version/capabilities→authorization middleware→response validator→tool executor，并证明低版本/缺能力专属安全分支造成诚实 canary effect。

下一轴：streaming/notification/cancel 的 canonical 在途状态机；必须排除 parser ambiguity、stale-state、timing covert channel、普通失败/日志和攻击者自身 effect。
