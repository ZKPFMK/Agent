# R4 effect-history / receipt / notification 筛查

日期：2026-11-11。结论：当前宽泛 framing 为 `TAKEN/NO-GO`；没有注册 claim、没有运行实验或服务。仅保留两个需要固定真实 host/client 代码路径的实现线索：`receipt→workflow promotion` 与 `notification→terminal commit`。

## 机制边界

本轮只考虑攻击者控制已连接 MCP server 的协议合法 response、receipt 或 notification 时序/元数据，固定 host 将其写入跨调用状态后，自动改变后续诚实工具的授权或受保护执行。攻击者不能控制 host、LLM、诚实工具、审批者、sink，也不能直接写 effect ledger。成功必须由独立 ledger 记录诚实工具的未授权 effect；模型复述、成功文本、日志、任务失败、攻击 server 自己的副作用和普通结果重放不计入成功。

保留的窄线索：

- `receipt→workflow promotion`：终态 receipt 被 reducer 错误解释为下一阶段 `ready`，进而触发诚实 B 工具；要求 B 不继承 A 的审批，且 B effect 独立可观察。
- `notification→terminal commit`：合法 notification 被错误解释为 pending call 的 terminal/commit，触发固定 finalizer 或诚实工具；要求真实 notification consumer 和严格 FSM 对照。

已淘汰的 `effect-history→retry/compensation` 与重复/迟到结果、取消后提交和恢复边界重叠；若效果只是攻击 server 自己重复执行，也不构成授权绕过。

## 固定源码核验

1. 本地 `cra_mcp 0.2.0`，commit `463779b318f78a7c9e62e86639fec135c0423bc5`：`agent.py:97,104–128` 将 A 的结果留在模型 `messages`，下一轮可由模型生成 B；审批只按当前 B 名称和 `is_write/is_destructive` 判定。`adapter.py:106–127` 不把 A 历史自动绑定到 B，event history 只作观测。
2. `mcp-agent 0.2.6`，commit `f62d849350816588b1c6294e7914bbe4d8b84072`：`sampling_handler.py:129–191,193–255` 只消费当前请求/结果并显式使用 `use_history=False`；`mcp_agent_client_session.py:334–358` 转发当前请求；`server/app_server.py:375–391,426` 绑定和清理当前 upstream session。未发现 effect-history 自动进入后续授权或诚实受保护 sink 的双消费者链。

结论：上述两个固定对象不支持攻击可达性；不能由模型间接链外推一般安全结论。若重开，只能补读同一 mcp-agent commit 的 session factory、workflow registry 的 resume payload 和固定工具执行器，寻找 `A effect→B authorization input→honest effect` 的完整链；不能构造 permissive broker。

## 文献与公开安全公告查重

有限公开检索覆盖 12 个月 arXiv 查询（8 个机制 query，38 个命中，最近 30 天 17 个；DBLP/Semantic Scholar 受限流，OpenReview 字段解析失败，故索引覆盖不完整）。已核验的最高相关来源：

- [TRAP](https://arxiv.org/abs/2610.16333)：全文直接覆盖真实 tool-result 在不兼容上下文中的 misbinding 与 replay；结果重放不构成新的 effect-history 攻击。
- [CVE-2026-25536 / GHSA-345p-7cg4-v4c7](https://github.com/modelcontextprotocol/typescript-sdk/security/advisories/GHSA-345p-7cg4-v4c7)：直接覆盖共享 transport/server 导致跨 client response、notification、sampling、elicitation 错路；修复版本为 1.26.0。
- [effect-history](https://arxiv.org/abs/2609.15397)：全文覆盖 MCP 外部效果异常，包括 duplicate、aborted、provisional 等类别；剩余只是具体 runtime witness。
- [RAC](https://arxiv.org/abs/2609.23498)：覆盖 MCP workflow authorization drift、accepted lineage/state 和 unsafe continuation 阻断。
- [CapLease](https://arxiv.org/abs/2608.01710)：覆盖 retry/replan/delegation/confirmation/crash 的 semantic replay 与持久 Issue–Prepare–Commit ledger。
- [Residual Authority Replay](https://arxiv.org/abs/2609.33910)：直接覆盖跨 task/session 的 approval 残留重放；不涉及 tool-result 字节，但覆盖授权重放子类。
- [Signed, Sealed, Leaked](https://arxiv.org/abs/2611.06585)：覆盖跨调用状态和 within-call mixing 的 MCP 隐私泄露；其能力是 tool code/manifest 控制，不是 response-only。
- [MCP MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)：规范直接要求 requestState 完整性、principal/TTL/origin-request binding，并提醒 single-use 需服务端消费；不是本项目的实证攻击。

## 判定与下一步

当前判定为 `TAKEN/NO-GO`，不是攻击效果结论。宽泛 effect-history、结果错绑、授权重放和跨调用状态泄露均已有直接或组合式覆盖。若继续，只能换到独立的 MCP sampling recipient/session binding 轴，或固定一个未被上述公告覆盖的 host/client/server revision，先完成源码链和新的全文查重；在候选 gate 通过前不得创建 broker、canary、模型调用或 ASR。

DO_NOT_DO：不要把 TRAP 的 FSER 当作 MCP ASR；不要把普通 prompt injection、stale state、P4 provenance、parser differential、task-ID 隔离或 approval inheritance 重新命名；不要将攻击 server 自己写 ledger、模型选择错误参数或单纯重复副作用报告为越权效果。
