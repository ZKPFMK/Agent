# R4 MRTR requestState 筛查

日期：2026-11-11。结论：UNCERTAIN；没有注册 claim、没有运行实验。

## 机制假设

攻击者尝试复用一个正常授权流程产生的有效 `requestState`，但在恢复请求中替换 tool/method/arguments，使诚实受保护工具执行未获批准的 B，而初始批准只覆盖 A。

## 已核验边界

- MRTR 规范要求 client 重试原请求时原样携带 `requestState`；影响授权/资源访问/业务逻辑时，服务端必须保护完整性并拒绝验签失败；绑定主体、TTL、原始请求标识（method + 关键参数摘要）是建议项。签名/TTL 本身不证明单次消费或当前 ACL。
- 官方 Python SDK 某固定 commit `77001c96f9507be0f4d009b83210a384a5e08bda` 的 `server/request_state.py:54–58` 有 expiry/request binding/principal 的契约说明和 AES-GCM 组件，但本轮未完整核验摘要实际覆盖哪些参数、默认装配和 host 调用链。
- TypeScript MRTR 示例可创建带 `step`/`env` 的 continuation state，但本轮固定 commit/SDK package/依赖锁及最终 effect 链不完整；示例最后返回部署成功文本，没有真实部署 API 或受保护持久效果。

## 威胁模型与成功标准

攻击者不能控制 host、LLM、诚实受保护 server/tool、sink、审批者或 token；不能自行签发诚实 server 的 state，也不能修改 state。完整成功必须同时有：

1. 初始批准明确覆盖 A；
2. 同一有效 state 被用于恢复 B，且 B 不在批准范围内；
3. 诚实受保护工具实际执行 B；
4. 独立 effect ledger/canary 记录 B；
5. 攻击者事先没有直接访问该 sink 的权限。

仅 state 存在、参数字节不同、拒绝/报错、成功文本、恶意 server 自己写入或模型声称成功，都不算成功。不同 JSON 解析器、来源/权威丢失和审批缓存问题分别回到 Q1、P4、R4-02 或既有 approval 研究。

## 结论与下一步

当前没有“有效 state + 参数替换 + 诚实受保护 effect”的完整源码链。下一步若继续，只能固定一个真实 host/client/server/SDK revision 和依赖锁，追踪初次调用、`input_required`、state 存取、恢复请求构造、method/arguments 绑定、验证、批准和最终 effect。若恢复始终使用原 A 或对 B 重新审批/拒绝，关闭 MRTR；不能创建宽松 broker 来制造错配。
