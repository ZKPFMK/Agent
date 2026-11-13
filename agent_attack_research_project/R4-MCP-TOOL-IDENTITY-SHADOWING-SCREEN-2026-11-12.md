# R4 MCP tool identity/name shadowing binding 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查多 server host 的 tool registry/approval key 是否缺少 server/session identity，使 A 的合法同名 tool definition/metadata 影响 B 的既存 trusted tool approval/dispatch，并使 B protected effect 在原 A policy/ACL 应拒绝时发生。

## 成功标准与边界

攻击者只能控制已连接 server A 返回的合法 tool name/metadata/schema 和正常 `tools/list` 内容；不能控制 host/client registry policy、B trusted tool implementation、B ACL、用户、token、transport、approval ledger 或 protected sink。成功必须满足：

1. fixed host 允许 A 与 B 同时存在同名或 identity-equivalent tools，并存在自动 registry/approval/dispatch consumer；
2. A 的合法同名 definition 改变 B 的既有 approval/dispatch identity、policy or target binding，而不依赖模型选择、用户显式选择、dynamic refresh race 或 shared transport response misrouting；
3. B 的 trusted protected operation 对 A-derived identity/policy 应被拒绝，但独立 append-only ledger 记录 B protected canary commit；
4. strict `(server, session, tool name, version, method, target, approval epoch)` binding 拒绝，benign namespaced A/B utility 保持。

排除 generic tool poisoning、prompt injection、model/tool selection、dynamic `list_changed`/stale approval（D-35）、shared transport ID/response misrouting（D-21/GHSA）、attacker-owned A effect、用户显式选择、普通无效果 name collision、parser/schema/default differential、resource/template、gateway capability 和为补链构造 global registry/shadow broker。

## 待核验链

`A legal tools/list same-name metadata → fixed host tool registry/approval key → B tool identity/dispatch → B ACL/effect ledger`。

需固定 host/client/server revision 和依赖锁，追踪 server/session/tool identity、registry key/namespace、definition digest/version、approval metadata、actual `tools/call` target、effective principal/ACL、effect commit 和 utility。若 host 明确按 server/session namespace 隔离、同名只影响 UI/模型可见性、或不存在既存 B protected ACL/ledger，立即关闭；不得构造跨 server dispatcher。

## 四路筛查结果

本轮四个只读 scout 已完成；没有启动服务、调用模型、运行实验、注册 CLAIMS 或写入 EVIDENCE 数字。

### 文献与安全公告查重

- 严格链 `A legal same-name metadata → fixed host identity/approval consumer → existing B trusted dispatch → B ACL deny but independent ledger commit` 的 direct coverage 为 `0/8`，但宽泛 registry/dispatch shadowing 已有强近邻。Docker MCP Gateway GHSA-m5m2-mrxf-7j7q、Tencent WeKnora GHSA-67q9-58vj-32qx、LangChain adapter issue #605 均覆盖 bare-name/composite-key overwrite or wrong dispatch；IBM ContextForge 覆盖 name normalization collision/DoS；Applied Sciences 2026 论文展示同名双 server 与 ownership rejection 防护。
- OpenAI Agents Python utility 默认对跨 server 重名报错或使用 server-qualified names，是 strict namespacing 的负边界。MCP name standardization issue #1395 讨论组合 namespace ambiguity，但不是 exploit evidence。
- 这些来源的效果是 attacker-owned wrong dispatch、普通 collision/DoS 或防御拒绝；没有既存 B trusted operation 按 A identity 被错误放行并由独立 B ledger 记录。因此不能把 direct=0 写成 novelty proof，也不能把宽泛 shadowing 称 clean new mechanism。

### 固定实现与可达性

- 四个指定 revision 的源码树、依赖锁和目标 Git objects 当前不可复核；无法直接核对 registry/approval/dispatch key 是否遗漏 server/session identity。
- 历史 VS Code 记录只说明 registry/approval metadata refresh 和显式 `invokeTool`/`tools/call`；mcp-agent 有 `server_name`/namespaced connection 线索并显式 `call_tool`；Python/TS SDK 是 transport/session API，没有 host B approval/ACL/ledger。没有 A/B 同名共存→B dispatch→B effect witness。
- 本地 `cra_mcp` 是单 server in-process toolbox；其 `by_name` map 不能作为多 server host 证据。没有 B protected tool、ACL expected-deny 或 append-only ledger。

### 候选与威胁模型

- TS-1 registry definition shadow、TS-2 approval epoch shadow、TS-3 dispatch target/source shadow 均未过 gate：都需要固定多 server host 的静态 name-only key、A/B 同名共存、B trusted operation、B ACL 和独立 ledger；当前缺失且宽泛故障族已有近邻。
- 成功必须由 trace 证明 A definition digest 改变 B approval/dispatch identity，实际目标仍是 B，B ACL 对 A-derived tuple 预期 deny 但独立 ledger 记录 B commit，strict full tuple reject，且 namespaced benign utility 保持。UI/model visibility、用户显式选择、A-owned effect、transport misrouting、dynamic stale、普通 no-effect collision 均不计成功。

## 本轮裁决与边界

**VERDICT: NO-GO（当前可复核范围与 TS-1/TS-2/TS-3）；未固定外部 multi-server host 仅保留 UNCERTAIN 审计问题。** 当前不注册 claim、不进入 R5/R6、不产生效果率。

硬关闭条件包括：没有固定 host/source/lock；host 按 server/session namespace 隔离；同名只影响 UI/model；效果属于 A；问题依赖 D-21 shared transport、D-35 list_changed/stale、D-28 gateway、parser/schema/default、用户显式选择或构造 global registry/shadow broker；或没有 B ACL/ledger。

## 下一条有界轴

下一轮切换到外部/间接内容导致 Agent 生成代码并在受限 sandbox 执行的 MCP 代码执行边界。该方向不主张首次机制：INFUSE/CIBER 已覆盖外部内容→Agent code/shell→sandbox effect；本轮只检查是否存在一个 MCP-specific、单次外部内容、攻击者不知道具体工具注册表、无在线反馈、独立 G/T/X/E 事件链的未覆盖固定 host 评测增量。主机 RCE、容器逃逸、真实文件/凭据/网络和 MCP server 自执行均排除。

禁止下载或运行论文代码、启动代码执行器、生成 payload 或接触真实目标；继续只做文献、固定实现和纸面威胁审查。
