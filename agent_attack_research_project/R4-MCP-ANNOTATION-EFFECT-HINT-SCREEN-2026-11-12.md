# R4 MCP tool annotation/effect-hint binding 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查固定 host 是否把低信任 server A 返回的合法 tool annotations（`readOnlyHint`、`destructiveHint`、`idempotentHint`、`openWorldHint`）当作 approval/dispatch 安全事实，而不重新验证实际 tool effect，导致 A 控制的 annotation 改变对既存 trusted B protected operation 的审批或执行范围。

## 成功标准与边界

攻击者只能控制已连接 server A 返回的合法 tool metadata/annotations 和正常工具实现声明；不能控制 host/client approval policy、用户、B trusted tool、B ACL、protected sink、token、ledger 或实际 B effect implementation。成功必须满足：

1. fixed host 自动消费 annotation，并让单一 annotation 变量改变 approval/dispatch/confirmation/ACL scope；
2. A 的 annotation 声明与实际 B protected synthetic operation 不一致，B ACL/approval 按真实 effect 应拒绝或要求确认，但 protected effect 被独立 append-only ledger 记录；
3. strict/reference effect evaluator 重新计算真实 effect 并拒绝 annotation-only path，同时正常 benign tool utility 保持。

排除 generic tool poisoning、prompt injection、模型选择、D-29 broad contract/effect escape、用户明确批准、attacker-owned tool/effect、host 完全忽略 annotations、普通 UI label/日志差异、schema/default/parser differential、真实文件/网络/凭据和为补链条构造 permissive approval broker。

## 待核验链

`A legal tools/list metadata+annotation → fixed host annotation consumer → approval/confirmation/dispatch decision → trusted B actual effect → B ACL/effect ledger`。

需固定 host/client/server revision 和依赖锁，追踪 tool annotation source/version、approval decision、actual method/args/target/principal、B ACL、effect commit 和 utility。若 annotation 只是 advisory UI metadata、host 每次按真实 tool/effect 决定、或不存在 B protected ACL/ledger，立即关闭；不得把“标注不准确”直接升级为攻击成功。

## 四路筛查结果

本轮四个只读 scout 已完成；没有启动服务、调用模型、运行实验、注册 CLAIMS 或写入 EVIDENCE 数字。

### 文献与安全公告查重

- 严格链 `A legal annotation → fixed host security consumer → annotation-driven approval/dispatch → trusted B effect that B ACL should deny → independent ledger` 的 direct coverage 为 `0/8`；但宽泛的“annotation 不可信、可能影响 confirmation/auto-approval、必须执行时重验”已被 MCP 规范、官方 annotations 说明、OWASP、ToolHive policy 文档和强近邻 approval 研究覆盖。`direct=0` 不是新颖性证明。
- 最强近邻 *When Neither Side Confirms*（arXiv:2611.02527）测量 destructive approval fail-open/间接 prompt injection，但不操纵 annotation 字段，也没有 A annotation→trusted B 独立账本链。Dynatrace GHSA-pqh8-p93p-2rx7 是 read-only hint 与参数注入的 adjacent advisory；ToolHive annotations-as-policy 文档是实现/防御启示，不是 exploit。
- `readOnlyHint`、`destructiveHint`、`idempotentHint`、`openWorldHint` 的规范和 OWASP testing guidance 都要求将 server annotations 视为不可信并在调用时按真实 effect/参数/主体授权；这限制了宽泛 novelty 表述。

### 固定实现与可达性

- 四个指定 revision 的源码树、依赖锁和目标 commit 对象当前都不可复核；没有字段级 annotation parse→security gate→B effect 的固定源码 witness。
- 既有 VS Code 记录只证明 registry/approval metadata refresh、raw-input confirmation 和显式 `tools/call`；没有证明四个 annotation 字段映射到不可绕过的 ACL/dispatch gate、actual-effect revalidation 或 trusted B ledger。mcp-agent/SDK 记录是显式 list/call/transport API，也没有 host annotation security consumer。
- 本地 `cra_mcp` 的 `readOnlyHint`/`destructiveHint`→`is_write`/`is_destructive`→confirmation 是同一单工具箱内的替代实现，没有 connected A、trusted B、B ACL 或独立 ledger，不能外推到固定对象。

### 候选与威胁模型

- AH-1/TM-1 `destructiveHint=false` 或 `readOnlyHint=true` confirmation/approval downgrade：只有固定 host 把 annotation 当作 security-relevant permit/dispatch state，且相同 canonical call 触发既存 B protected effect 时才可能成立；当前无 host witness、B ACL 或 ledger，UNCERTAIN/NO-GO。
- AH-2/TM-2 `readOnlyHint=true` admission into state-changing B：若实际 effect 与 annotation 不一致但 annotation 不改变 host decision，就是 D-29 broad contract/effect escape，NO-GO/high overlap。
- AH-3/TM-3 `openWorldHint=false` suppresses world/egress gate：若无独立 host gate则是 UI/模型 metadata；若通过 network/recipient/URI 则落入已关闭资源/auth/SSRF轴，NO-GO。
- `idempotentHint` 复用 permit/retry 也不新增第四候选；它落入 D-21/D-27/D-37 effect-history/replay/retry，除非未来有 annotation-only 且第二个独立 B semantic commit 的固定 witness。
- 成功必须有预先存在 trusted B、B ACL expected deny/confirm、独立 append-only effect ledger、strict effect recomputation reject 和 benign utility。UI、日志、模型文本、用户批准、A-owned effect、B handler denial 和 host 忽略 annotation 均不计成功。

## 本轮裁决与边界

**VERDICT: NO-GO（当前 fixed-source range 与 AH-1/AH-2/AH-3）；未固定外部 host 仅保留 UNCERTAIN 审计问题。** 宽泛 annotation/approval 机制已被近邻和防御规范覆盖；当前无 claim、无 R5/R6、无效果率。

硬关闭条件包括：host 不读取 annotations 或只用于 UI；固定 host 源码缺失；annotation 翻转不改变 security decision；每次调用按真实 effect 重验；不存在 B ACL/independent ledger；或只能通过 D-29 contract/effect、generic tool poisoning、模型选择、用户批准、retry/replay、网络资源或构造 broker/fake B 补齐链条。

## 下一条有界轴

下一轮切换到尚未单独归档的 MCP tool identity/name shadowing binding：检查多 server host 的 tool registry/approval key 是否缺少 server/session identity，使 A 的合法同名 tool metadata 影响 B 的既存 trusted tool approval/dispatch，且 B protected effect 被错误放行。该轴必须排除 generic tool poisoning、dynamic list_changed/stale approval（D-35）、shared-transport response misrouting（D-21/GHSA）、attacker-owned A effect、用户显式选择和普通 tool-name collision 无效果情形；没有预先存在的 B ACL/ledger 立即关闭。

禁止构造 global tool registry、shadow broker、假 B sink、真实工具或生产 host；继续只允许 owned/local/sandbox、合成工具和无副作用 canary。
