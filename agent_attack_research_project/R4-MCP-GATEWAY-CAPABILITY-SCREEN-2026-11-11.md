# R4 MCP gateway capability subject/audience/purpose 绑定筛查

日期：2026-11-11。状态：screen pending；未注册 claim、未运行 gateway、模型或实验。目标是检查多租户 MCP gateway 是否把一个 server 返回的 opaque capability/ref 在跨 server/tenant 转发时错误绑定到实际 effect。

## 成功标准与边界

攻击者是普通 synthetic tenant A 或已接入 gateway 的第三方 server，只能控制 A 自己返回的 capability/ref 和合法工具结果；不能读取 B 的 token、gateway 私钥、B server/database 或直接写 ledger。固定本地 gateway 的授权 tuple 为 `(subject, issuer, audience, purpose, expiry, session_id)`。

成功必须满足：A 仅被授权访问 A；gateway 接受 A 返回的 ref 后，在跨 server/tenant 转发时实际以错误 subject/audience/purpose/issuer 访问 B 的 protected canary；B 的独立 effect ledger 记录 read/write；reference verifier 和 strict audience-bound gateway 对同一 ref 拒绝；benign A task utility 保持。仅 alias/name collision、session rebinding、token passthrough、invalid-token error、模型选错工具、攻击者自有 effect 不算成功。

## 重点区分

- Q7 identity collision/agent alias/session smuggling：已关闭，不重包装。
- P4 provenance/authority laundering：仅来源或信任标签丢失不算本轴。
- 普通 OAuth/token passthrough 或 gateway configuration error：需有具体 capability tuple 到 B effect 的独立链，否则关闭。
- 仅构造没有真实部署约束的 permissive broker 不算实现证据。

## 待核验链

`attacker ref → gateway parser/store → issuer/subject/audience/purpose/expiry check → cross-server dispatch → B object ACL → protected canary ledger`。

优先检查 GatewayBench、MCP gateway/security specs 和一个固定本地/公开 gateway 实现；如果没有多租户 capability/ref 转发或没有 independent effect sink，立即关闭。所有后续工作仅限 owned/local/sandbox、synthetic tenants 和内存 canaries。

## 有界筛查结果

- 文献查重：8 个来源 direct=0，但 HCP v2、衰减 token、state handle hijacking、MCP authorization 和 ABAC 已覆盖绑定、逐跳 audience、权限衰减与 token passthrough 原则；MCPHub 的跨租户读取是 serverName IDOR，GatewayBench 测工具暴露/注入，不是本轴的 A-owned ref→B effect。
- 固定实现：本地 `cra_mcp` commit `463779b318f78a7c9e62e86639fec135c0423bc5` 的 `server.py:43–52` 绑定单 project，无多租户 ref。GatewayBench `2610.23449v1` 是研究评测，不提供可审计生产 gateway commit。PRECINCT commit `a1fe87c117e091f1e70ad3ac1523ace8e0835b02` 有 `handle_store.go:75,112` 的随机 ref、过期和 owner 检查，`gateway.go:1630,1653,1667` 比较 SPIFFE owner；但 `gateway.go:813,817,965` 的 dispatch 使用固定 upstream/config，未见 ref 解封到另一 server、B 对象 ACL 和 protected effect ledger。store 缺 issuer/audience/session，ToolName 不强制 purpose。
- 测试对照：PRECINCT `handle_dereference_test.go:69,106` 只检查过期/错误 owner；219–274 是测试自身 handler，不是生产 handler 的 strict/reference 对照。没有同 ref 的 B effect ledger。
- 结论：固定对象 `NO-GO`；外部 gateway 仍未泛化。只有在固定真实跨 server ref consumer 和 B ACL/sink 源码同时存在时才能重开；不要构造 permissive broker。下一轴切换为非 filesystem declared contract 与实际 effect/data-flow。
