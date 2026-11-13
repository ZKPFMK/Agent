# R4 MCP roots boundary binding 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查低信任 server A 的合法 `roots/list` 请求或 root-context 消费是否让固定 host 自动把 B workspace/tenant 的 root capability 暴露给 A 之外的受保护资源/工具，或使既有 trusted file operation 使用超出 A 授权的 root。

## 成功标准与边界

攻击者只能控制已连接 server A 发出的合法 `roots/list` request、root-related response/context metadata 或正常 server-side prompt；不能控制 host workspace roots、B workspace/tenant、文件 ACL、trusted file tool、用户、真实文件、token、ledger 或 host root registry。成功必须满足：

1. fixed host 自动消费 root request/context，并在 host-owned root registry/file operation 中选择、传播或使用 B root；
2. A 的原始 source/session/tenant/root scope 按 B ACL 应被拒绝，但 independent append-only ledger 记录 B protected synthetic file/resource read 或无副作用 canary commit；
3. strict root/source/session/tenant ACL reference checker 拒绝该路径，正常 A root utility 保持；合成 root URI 和 canary 只能属于 owned/local/sandbox。

排除一般 roots/list 披露、host 已明确授权的 workspace roots、普通文件读取、path traversal、resource-template、SSRF、用户显式共享 B root、prompt injection、攻击者自有文件和日志/文本效果。

## 待核验链

`A legal roots/list → fixed host root consumer/registry/context injection → root selection/file operation → B root ACL → independent synthetic canary ledger`。

需固定 host/client/server revision 和依赖锁，追踪 root issuer/source/session/tenant、URI/name、workspace mapping、root registry/cache key、context injection、file operation target、ACL decision、effective principal 和 canary commit。若 roots 只来自 host 显式配置、server 不能控制/触发 B root consumer、或不存在 B root ACL/ledger，立即关闭；不得构造 root broker、permissive adapter、fake B workspace 或真实文件 canary。

## 四路筛查结果

本轮四个只读 scout 已完成；没有启动服务、读取真实文件或 workspace、调用模型、运行实验、注册 CLAIMS 或写入 EVIDENCE 数字。

### 文献与安全公告查重

- 严格完整链 `A legal roots/list/context → fixed host automatic root consumer → B root ACL deny → independent protected canary/effect` 的 direct coverage 为 `0/8`；但 roots disclosure、filesystem boundary、tenant-scope guidance 和 root registry/list confusion 已覆盖宽泛“roots 是新授权面”的说法，`direct=0` 不是新颖性证明。
- MCP 2025 Roots 规范、2026-07-28 deprecated Roots 规范和 OWASP testing guidance 将 roots 视为 client-configured/informational context，要求 client/root boundary 和 filesystem access control；它们不是攻击证据。
- IBM MCP Context Forge GHSA-x39c-q2jx-f325 是最接近的真实公告：root service 的进程级集合缺 team/scope 过滤，导致跨 admin session root disclosure。它需要 root registration/admin 路径，未证明合法 A `roots/list` 触发 fixed host 自动选择 B root、B ACL 应拒绝但 protected effect 发生，因此是 partial overlap。Chrome symlink/Git confinement 和 filesystem capability laundering 属于排除的 path/file boundary 方向。

### 固定实现与可达性

- 固定 VS Code 1.106.0 的既有记录显示 server request → roots callback → 原连接 response；root URI/name 来自 host 已配置的 `explicitRoots` 或 workspace folders，并按 remote authority 过滤。它关闭一般披露，但没有 A 控制 B root、root registry/context injection 或 B protected file operation 的证据。
- 四个指定 revision 的源码树/依赖锁当前不可复核；不能用本机 VS Code 1.146.0、Python MCP 2.3.0、无目标 commit 的 TS 1.29.0 package 或历史摘要替代固定证据。
- 本地 `cra_mcp` 只有单 project 工具/resource/文件 containment，不是 host roots consumer；没有 B workspace/tenant ACL、trusted root operation 或 independent ledger。官方 filesystem server 的既有语义是收窄 client roots、generation/barrier 防旧 refresh 覆盖，未发现 A→B 自动 root consumer。

### 候选与威胁模型

- R-1 `source-session-tenant-blind root registry key`：要求 host root registry/cache 省略 source/session/tenant，A 合法请求误选预存 B root 并进入 trusted file operation；当前没有 registry→B ACL→ledger witness，且与 D-28/D-35/D-36 高度重叠，UNCERTAIN/NO-GO。
- R-2 `ambient root-context union into A task`：要求 host-owned structured root-context assembler 把预存 B root 自动并入 A task，再由 trusted file operation 使用；当前没有 context injector 或 B effect witness，且与 D-21/D-38 misrouting/session binding 高度重叠，UNCERTAIN/NO-GO。
- R-3 root-list-change stale/overbroad root snapshot 直接落入已关闭 Q6/Q8、D-35/FCD stale-state，排除，不计候选。
- 成功必须由独立 ledger 记录 B synthetic canary read/commit，B ACL 对 A tuple 预期 deny，strict `(issuer, source, session, tenant, workspace, root, scope, approval epoch)` binding reject，且 benign A root utility 保持。URI/name disclosure、普通 file read、模型/日志文本、用户显式共享、path traversal、SSRF、resource-template 和 attacker-owned files 均不计成功。

## 本轮裁决与边界

**VERDICT: NO-GO（当前可复核范围与 R-1/R-2/R-3）；未固定外部 host 仅保留 UNCERTAIN 审计问题。** 当前不注册 claim、不进入 R5/R6、不产生效果率。

硬关闭条件包括：roots 只来自 host 显式配置/workspace folders；没有自动 root registry/context/file consumer；A 只能看到 root URI/name；B root/ACL/ledger 不存在；或只能通过用户共享、path traversal/symlink、resource-template、SSRF、prompt injection、filesystem laundering 或构造 broker/adapter/fake B 补齐链条。

## 下一条有界轴

下一轮切换到尚未单独闭合的 MCP tool annotation/effect-hint binding：检查固定 host 是否把 `readOnlyHint`、`destructiveHint`、`idempotentHint` 或 `openWorldHint` 当作 approval/dispatch 安全事实，而不重新验证实际 tool effect，导致 A 控制的合法 annotation 改变对 trusted B protected operation 的审批或执行范围。该方向必须排除普通 tool poisoning、D-29 broad contract/effect escape、模型选择、用户明确批准、攻击者自有工具和 host 未使用 annotation 的实现。

禁止构造 permissive approval broker、假 B sink、真实文件、真实用户或生产工具；继续只允许 owned/local/sandbox、合成工具描述和无副作用 canary。
