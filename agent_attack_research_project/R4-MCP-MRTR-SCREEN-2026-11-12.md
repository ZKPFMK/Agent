# R4 MCP MRTR requestState 端到端绑定筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是判断一个合法 continuation request 中有效 requestState 是否可被攻击者在不修改 state 的情况下与 changed method/arguments/principal/session 错配，最终让诚实 protected tool 执行未获批准 B。

## 成功标准与边界

攻击者只能控制已连接 server 的合法 `input_required`/continuation 时序及恢复请求中的公开参数；不能签发/修改 requestState、控制 host/client、审批者、诚实 server/tool/sink、token 或 ledger。成功必须同时满足：

1. 初始请求 A 获得明确批准并产生完整性有效 requestState；
2. 恢复请求使用同一有效 state 但改变 method、关键 arguments、principal/session/tenant 或 approval scope 到 B；
3. 诚实受保护工具实际提交 B，且 B 不在 A 的授权范围；
4. 独立 ledger 关联原请求摘要、state、principal、验证结果、批准快照和 sink commit；严格绑定/reference verifier 拒绝；benign utility 保持。

state 存在、字节不同但被拒绝、成功文本、恶意 server 自有 effect、模型声称成功、正常重新审批和单纯 token replay 不算成功。不能构造 permissive broker 或弱签名 state 来制造错配。

## 待核验链

`initial request A → approval/input_required → requestState integrity/TTL/principal/origin binding → retry/resume request B → method/argument/tenant authorization → honest protected sink`。

必须固定一个真实 host/client/server/SDK revision 和依赖锁，核对 requestState 摘要实际覆盖哪些字段、是否 single-use、expiry、principal/session 绑定和恢复时的 approval。排除 P4 provenance、Q1 parser、R4-02 approval inheritance、task/session ID 已知漏洞和普通 stale state。若没有 valid state + changed args + honest effect 的完整链，立即关闭。
