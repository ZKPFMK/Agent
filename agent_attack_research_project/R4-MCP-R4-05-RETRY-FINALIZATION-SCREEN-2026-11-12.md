# R4 MCP-R4-05 trusted retry/finalization binding 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查低信任 MCP server 是否能通过合法 cancellation/retry/finalization 交互，使固定 host/client 重提交一次已经批准的 trusted protected call，或把一次 approval/effect permit 错误复用于第二次 protected effect，且该效果超出原授权。

## 成功标准与边界

攻击者只能控制已连接低信任 server A 的合法响应、进度/取消相关协议事件或 server-side timing；不能控制 host/client、trusted tool B、B ACL、approval ledger、token、用户、网络传输或 protected sink。成功必须同时满足：

1. host 对一次明确的 trusted B effect 形成可审计的 approval/permit；
2. A 的合法协议行为触发 host 的 retry/finalization/resubmission 路径；
3. 第二次或变更后的 B protected effect 被独立 append-only ledger 记录，且不应由原 approval 覆盖；
4. strict/reference exactly-once/permit binding 拒绝该路径，正常 retryable A utility 保持；成功不是重复传输、日志、A 自有副作用、普通 cancellation residue 或 B 允许的幂等重试。

排除 D-21 已关闭的广义 effect-history/receipt/notification framing、TRAP/GHSA 已覆盖的 replay/misbinding、FCD handler drift、普通网络重传、取消后无权限承诺的残留效果、攻击者自有工具重复写、用户明确批准的第二次调用、以及为补齐链条而创建 retry broker/weak approval state/permissive finalizer。

## 待核验链

`A legal response/progress/cancel → fixed host retry/finalizer consumer → approval/permit reuse or changed effect selector → trusted B protected sink → independent effect ledger`。

需固定 host/client/server revision 和依赖锁，追踪 approval snapshot、request/call identity、retry reason、attempt number、method/args/target/principal、finalization state、B ACL 和 ledger commit。若 host 没有自动重试/重提交、每次 retry 都重新审批/重新绑定，或没有独立 B protected sink，立即关闭；不得构造弱 broker。

## 四路筛查结果

本轮四个只读 scout 已完成；没有启动服务、调用模型、运行实验、注册 CLAIMS 或写入 EVIDENCE 数字。

### 文献查重

- 公开核验结果为 `direct=0/8`、`near=5/8`、`excluded adjacent=3/8`；没有来源同时证明“低信任 MCP server 的合法 cancellation/retry/finalization → 固定 host 复用既有 permit → trusted B protected effect 第二次提交”。最近 30 天机器检索受限流/解析错误影响，不能把索引失败当作 exhaustive novelty proof。
- AID-Guard、CapLease、Permission to Retry 直接覆盖 approval/recovery/effect-count 的防御边界；When Tool Calls Succeed but Workflows Fail 覆盖 retry/abort/late effect；TRAP/GHSA 覆盖 replay/misbinding；FCD 覆盖 descriptor/handler/epoch drift；这些阻止广义 effect-history/replay 新颖性，但没有给出本轮窄 host-event→permit-reuse witness。
- MCP cancellation 规范是 best-effort，未承诺 rollback、exactly-once 或自动重提交；规范说明不是攻击证据。

### 固定实现

- VS Code 的既有固定-source记录显示原 request/server 回调、单次 `tools/call`、raw-input approval，未发现 server progress/final/cancel 自动回流 `invokeTool` 或将同一 approval 改投 B；当前源码快照不在工作树，不能把记录升级成新的逐行证据。
- mcp-agent 记录显示 upstream/session/request identity 绑定和当前请求清理；没有 server event 触发另一工具或另一 upstream 的 host 重提交。Python/TypeScript SDK 是显式 transport/handler API，不提供 host approval snapshot、自动 retry/finalizer、B ACL 或 effect ledger。当前 fixed source 缺失时保留证据等级，不外推为所有 host 安全。
- 本地 `cra_mcp` 是单工具循环，没有 retry/finalizer、attempt identity、trusted B、B ACL 或独立效果账本；不能作为受害拓扑，也不能新建这些组件来制造候选。

### 候选与威胁模型

- C-1/R4-05-1 `attempt-blind permit reuse` 或同一非幂等 effect 的第二 semantic attempt：若只是 transport duplicate、普通幂等重试、D-21 replay 或 D-27 cancel residue，立即关闭；当前没有第二个独立 B commit witness，NO-GO。
- C-2/R4-05-2 `cancel-terminal permit survival` 或 retry selector 改变后复用 p0：只有取消后形成与原调用语义不同的独立 finalization effect，或 host 内部 selector 变化而 snapshot 未失效时才可能成立；当前无固定 finalizer/selector witness，UNCERTAIN/NO-GO。
- C-3/R4-05-3 `retry-selector snapshot staleness`：要求 target/effect 由 host 自有 retry policy 改变，而不是用户、LLM、普通参数、MRTR、dynamic registry 或 URI 输入；当前不存在 host→B protected effect 链，UNCERTAIN/NO-GO。
- 成功必须有原始 p0 approval、独立 semantic attempt、expected effect scope、B ACL、B protected append-only ledger、strict/reference permit binding 和 benign retry utility。日志、UI、receipt、late final、模型文本、A 自有副作用和普通 transport retry 均不计成功。

## 本轮裁决与边界

**VERDICT: NO-GO（已核验固定对象与三个候选）；未核验外部 host 仅保留 UNCERTAIN，不能升级为新颖性或可达性通过。** R4-05 不进入 R5/R6，不注册 claim，不产生效果率。

硬关闭条件包括：没有现有 host 自动 retry/resubmission/finalizer；每次 retry 重新审批和绑定；效果是同一幂等调用、网络重传、迟到结果、普通 cancellation residue 或 A 自有写入；没有固定 trusted B 和独立 ledger；或只能通过构造 retry broker、weak approval state、permissive finalizer、跨 client transport、B sink/ACL 来补齐链条。

## 下一条有界轴

下一轮切换到尚未筛查的 MCP task-augmented request/task-result handle binding：检查固定 host/client 是否把 A 的合法 task handle、`tasks/get`/`tasks/result` 或延迟结果自动绑定到 B 的 session/tenant/object/protected effect，且缺少原始 request/approval/source 绑定。该方向必须排除 MRTR requestState、普通异步任务重放、transport ID misbinding、effect-history、dynamic tools 和攻击者自有任务；若没有固定 task consumer、B ACL 和独立 ledger，立即关闭。

禁止构造 task broker、跨 session handle resolver、弱状态缓存、受害 B 或 protected sink 来制造链条；继续只允许 owned/local/sandbox、合成数据和无副作用 canary。
