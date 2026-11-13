# R4 MCP 控制面筛查：2026-11-11

## 结论

本轮由 3 个子 agent 并行完成：文献/规范 scout、idea-miner、threat-modeler。结论为 **NO-GO/UNCERTAIN**：没有候选同时满足具体机制缺口、真实实现可达、独立安全状态/效果 witness 和非循环威胁模型。没有注册 claim、没有运行模型、没有启动 MCP 服务、没有运行攻击或 ASR 测量。

## 筛查范围

- `initialize` 协议版本/能力协商与双时代 fallback；
- server-initiated `sampling/createMessage` 与 elicitation；
- roots、resources、prompts 生命周期和自动上下文纳入；
- streaming、notification、cancel、timeout、retry 的在途状态；
- 多租户 gateway 的 subject/audience/purpose 绑定；
- 非文件系统 declared contract 与实际 effect/data-flow。

已避开 I1、P4、Q1/C4、R4-02、R4-03，以及普通工具投毒、偏好操纵、响应注入、SOPE、签名木马和一般隐私/授权复刻。

## 结果

| 方向 | 结论 | 原因 |
|---|---|---|
| 版本/能力降级 | UNCERTAIN | 新版规范使用每请求版本，旧版才有初始化协商；尚无固定双时代 host/client 证明 fallback 改变安全 gate 或受保护 effect |
| Sampling/elicitation | UNCERTAIN | 规范允许反向请求，但必须固定 host 验证上下文、审批和 response recipient；当前本地工具包没有 host callback/taint/回传链 |
| Roots/resources/prompts 生命周期 | NO-GO（当前本地实现） | 本地 `server.py` 只注册资源和 prompt；没有真实 host 自动获取、上下文注入或绕过审批的执行路径。外部 host 只能标 UNCERTAIN |
| Stream/cancel/retry 状态 | UNCERTAIN | MCP cancellation 是 best-effort，没有 rollback/exactly-once 承诺；迟到 effect 不自动是漏洞，恶意 server 自己重复 effect 是循环访问 |
| Gateway audience/purpose | NO-GO（当前本地实现） | 没有多租户 gateway、opaque capability/ref 或 audience/purpose tuple 绑定路径；外部实现需独立源码证据 |
| 非文件系统 effect contract | UNCERTAIN | 需要 schema-valid 调用通过审批后到达未授权 DB/network/message sink 的真实 benign server；现有 filesystem laundering、approval 和 hidden-code 工作是近邻 |

## 关键来源

- [MCP versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md#protocol-version-negotiation)：新版本不再采用旧式初始化协商，不能直接把旧版 downgrade 假设外推到新实现。
- [MCP sampling](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)：允许 server 请求 sampling，但需要具体 host 的授权与上下文路由证据。
- [MCP elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)：涉及用户同意和状态绑定，但没有证明具体 host 存在授权复用。
- [MCP cancellation](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md#transport-specific-cancellation)：取消/断开不等于回滚或 exactly-once。
- [MCP resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)：资源如何进入上下文由应用决定，不能从规范推导自动跨源授权。
- [MCP security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)：已覆盖一般 confused deputy/token passthrough。
- [When Tool Calls Succeed but Workflows Fail](https://arxiv.org/html/2609.15397v1)：定义 effect-history 异常，但未提供本轮所需的跨信任 runtime attack witness。
- [Filesystem Capability Laundering](https://arxiv.org/abs/2610.22301)：覆盖文件系统 contract/effect 不一致，限制了泛化表述。
- [GatewayBench](https://arxiv.org/abs/2610.23449)：覆盖 gateway 架构与安全评估边界。

## 本轮最小下一步

不要继续重复本地 toolkit 审查，也不要为任一候选构造宽松 broker。下一轮应从一个不同于上述控制面族的攻击轴开始，并先由子 agent 做 full-text/public pre-emption；候选需有独立 deterministic evaluator 和 benign utility path。若仍无候选通过，保留 NO-GO 记录并继续换轴。
