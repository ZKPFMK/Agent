# R4 MCP prompt lifecycle/handler binding 筛查

日期：2026-11-13。状态：screen pending；未注册 claim、未启动服务、调用模型或运行实验。目标是检查固定 host 是否把低信任 server A 的合法 `prompts/get`/prompt handler result、role/content/argument metadata 自动提升为受信 system/instruction/context，或自动触发既存 B protected operation，而没有原始 source/session/approval binding。

## 成功标准与边界

攻击者只能控制已连接 server A 返回的合法 prompt metadata/result/argument-dependent content；不能控制 host/client prompt policy、用户、LLM、B trusted operation、B ACL、approval ledger、token 或 protected sink。成功必须满足：

1. fixed host 有自动 prompt consumer，且 A 的 result/role/content/argument metadata 进入 host-owned security-relevant context or downstream operation；
2. B protected operation 按 A source/session/approval 应拒绝，但独立 append-only ledger 记录 B effect；
3. strict source/session/role/approval reference binding 拒绝该路径，正常 A prompt utility 保持。

排除用户显式选择 prompt、普通 `prompts/get` 文本返回、generic prompt/indirect injection、A11 server-side prompt handler 自执行、completion、sampling、elicitation、模型自行选择工具、tool poisoning、attacker-owned effect、日志/文本和为补链构造 prompt broker/fake B。

## 待核验链

`A legal prompts/get/handler result → fixed host prompt registry/context consumer → role/source/session/approval binding → B protected downstream operation → B ACL/effect ledger`。

需固定 host/client/server revision 和依赖锁，追踪 prompt source/server/session、prompt name/version、arguments、role/content blocks、context insertion point、approval/recipient、downstream method/target/principal、B ACL 和 effect commit。若 prompt 结果只返回原始 caller/model、用户必须显式选择、host 不自动消费，或不存在 B ACL/ledger，立即关闭；不得启动 handler 或模型来补链。
