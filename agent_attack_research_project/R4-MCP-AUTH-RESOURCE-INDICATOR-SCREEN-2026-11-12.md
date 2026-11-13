# R4 MCP authorization resource-indicator/token-audience binding 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查 MCP HTTP authorization flow 中，已连接 server A 返回的合法 `401` challenge 或 protected-resource metadata 是否能使固定 host/client 把合成 token/approval 错送到既有 B protected synthetic endpoint，且缺少 origin/resource/audience binding。

## 成功标准与边界

攻击者只能控制已连接 server A 的合法 authorization challenge、`WWW-Authenticate` 参数或其 protected-resource metadata；不能控制 host/client token store、authorization server、B server、B ACL/audience policy、token signing key、用户、网络 proxy、receiver ledger 或真实 credentials。成功必须满足：

1. fixed HTTP host/client 自动消费 A challenge/metadata，并按其 resource indicator/audience 形成或选择 token/authorization route；
2. A 的合法 metadata 导致该 token/approval 被发送到预先存在的 B protected synthetic endpoint，B 对 A origin/resource/audience 应拒绝但 independent ledger 记录 token acceptance 或受保护 canary effect；
3. strict origin/resource/audience checker 拒绝该路径，正常 A authorization utility 保持；synthetic token 仅用于 owned/local/sandbox，无真实身份或第三方服务。

排除 SSRF、任意 URL fetch、attacker-owned token sink、OAuth phishing/CSRF、transport redirect/hijack、gateway capability、initialize downgrade、普通 token passthrough、用户主动改变 resource、真实 token/account/endpoint 和规范建议本身。

## 待核验链

`A legal 401/metadata → fixed host/client protected-resource metadata consumer → resource indicator/audience/token selection → B synthetic authorization endpoint/resource → B ACL/effect ledger`。

需固定 host/client/server revision 和依赖锁，追踪 A origin、metadata URL/issuer、resource indicator、token audience/subject、redirect/route、B decision、effective principal、canary commit 和 independent receiver ledger。若 client 不自动追随 metadata、每个 token audience 正确绑定、或不存在既存 B protected endpoint/ledger，立即关闭；不得构造 permissive OAuth broker 或 fake redirector。

## 四路筛查结果

本轮四个只读 scout 已完成；没有接触真实 token/账户/第三方服务，没有启动服务、调用模型、运行实验、注册 CLAIMS 或写入 EVIDENCE 数字。

### 文献与安全公告查重

- 严格完整链的 direct 命中为 `0/8`；近邻为 `8/8`。MCP authorization security/discovery 规范、RFC 8707、RFC 9728 已覆盖 resource/audience/issuer 绑定的防御边界。
- 三个 MCP SDK advisory 已覆盖 metadata/issuer/origin confusion：Rust rmcp GHSA-33F5-2C5Q-WGWJ、Python GHSA-qx49-fqc8-xw99、TypeScript GHSA-6qxp-vccf-f47h。它们的结果是 token/credential 被送到攻击者自有端点，属于本 screen 明确排除的 attacker-owned sink/credential exfiltration，不是既存 B audience 应拒绝但接受的 protected effect。
- Zero-Trust Authorization and Discovery for Enterprise MCP 是相邻授权评测，不含 A challenge→B audience-denied acceptance→independent ledger 链。近期索引受限和解析失败不构成 exhaustive novelty proof；`direct=0` 不能写成新颖性证明。

### 固定实现与可达性

- VS Code 1.106.0、mcp-agent 0.2.6、Python SDK v1.23.1、TypeScript SDK v1.29.0 的固定源码/依赖锁在当前工作树不可复核；没有本轮 authorization challenge、protected-resource metadata、resource indicator、token cache/key、issuer/audience 或 B effect 的源码 witness。
- 本地 `cra_mcp` 只有静态 Bearer challenge/Host allow-list，没有 protected-resource metadata discovery、RFC 8707 resource indicator、issuer/audience token route 或 B receiver；不能作为固定 OAuth host 或 B witness。
- 规范中的 `401 → resource_metadata → authorization server → token → retry` 只证明 protocol discovery semantics，不证明 A metadata 能改变 receiver 到 B；client 正确实现应回到原 A resource。

### 候选与威胁模型

- AI-1 `origin-stripped resource-indicator auth-cache key`：只有固定 client 的 auth/approval cache 缺少 scheme+authority/origin，且已有 B route/ledger 时才可能成立；当前没有 cache witness，且容易退化为 D-36 URI/cache 或 D-28 tuple confusion，UNCERTAIN/NO-GO。
- AI-2 `post-challenge metadata tuple 未重绑定`：只有同一自动授权 transaction 在 A challenge 后继续使用既存 B issuer/resource/audience tuple，并且不依赖跨源 metadata fetch/redirect 时才可能成立；当前没有 transaction witness，UNCERTAIN/NO-GO。
- AI-3 `challenge-origin-blind audience selector`：若 A 直接指定 B audience、AS 错发 audience、token 只是 passthrough 或通过 redirect/SSRF 才到 B，分别是普通 OAuth 配置错误或排除项；NO-GO。
- 成功必须由独立 receiver ledger 记录 B token acceptance/protected canary commit，B 对 A origin/resource/audience 预期 deny，strict/reference binder reject，且 benign A authorization utility 通过。A 收到 token、A 日志、receipt、401/403、模型文本和 B 拒绝均不算成功。

## 本轮裁决与边界

**VERDICT: NO-GO（当前 fixed-source range 与 AI-1/AI-2/AI-3）；未固定外部 host 仅保留 UNCERTAIN 审计问题。** 没有注册 claim、没有进入 R5/R6、没有生成效果率。

硬关闭条件包括：没有固定自动 metadata consumer；token audience/resource/issuer 已正确绑定；client 始终回到 A；B endpoint/ACL/independent receiver ledger 不存在；或只能通过 SSRF、redirect、OAuth phishing、普通 token passthrough、攻击者自有 sink、真实凭据、弱 B verifier 或新建 broker 补齐链条。

## 下一条有界轴

下一轮只筛查尚未完成的 MCP roots boundary binding：低信任 server A 的合法 `roots/list` 请求或根相关上下文消费，是否使固定 host 将 B workspace/tenant 的 root capability 自动暴露给 A 之外的受保护资源/工具，或使既有 trusted file operation 使用超出 A 授权的 root。该轴必须区别已关闭的“roots/list 一般披露”、普通文件读取、path traversal、resource-template、SSRF、用户显式共享 root 和攻击者自有文件效果；没有固定 host 自动 root consumer、B root ACL 和独立 canary ledger 就立即关闭。

禁止读取真实文件、真实 workspace、第三方服务或凭据；只允许 owned/local/sandbox、合成 root URI 和无副作用 canary。
