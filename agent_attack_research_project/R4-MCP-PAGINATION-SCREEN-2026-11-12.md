# R4 MCP pagination/cursor 跨边界绑定筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是判断 host/client 是否错误地把一个 server/method/session 的 opaque `nextCursor` 自动带入另一个 server/method/session，导致 honest protected resource/tenant 的未授权读取。

## 成功标准与边界

攻击者只能控制已连接 MCP server A 返回的合法 `nextCursor` 和分页响应时序；不能读取/签发 honest B 的 cursor secret、控制 host/client、B server/database、用户、审批者或 ledger。成功必须由独立 ledger 证明：A cursor 被 host 自动送到 B 或错误 method/session；B 返回的 protected synthetic tenant/resource/object 超出 A 授权；strict per-server/per-method/per-session cursor binding 拒绝；benign pagination utility 保持。

排除普通分页、invalid cursor error、公开列表、攻击者自有资源、server 自身循环、模型/提示词、task ID/session isolation 已知漏洞、parser ambiguity、SSRF/token passthrough 和没有 protected object effect 的 DoS。

## 待核验链

`A list/read → nextCursor store/cache → automatic next request → server/method/session/tenant binding → honest B resource ACL → independent read/effect ledger`。

需固定 host/client/SDK/server revision 和依赖锁，确认 host 是否自动分页、cursor key 是否包含 server/method/session、B 是否存在受保护 synthetic resource/tenant。若 host 不自动分页、cursor 只回原 server、或 B 以独立 ACL 拒绝，立即关闭；不得构造 permissive cursor store。
