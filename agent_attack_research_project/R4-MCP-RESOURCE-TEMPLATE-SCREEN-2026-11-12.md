# R4 MCP resource-template URI variable binding 筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查合法 resource template expansion 是否把 A-controlled URI variable 解析到 B tenant/object 的 protected resource，且固定 host/client/server 未在 template/source/ACL 边界上重验。

## 成功标准与边界

攻击者只能控制已连接 server A 返回的合法 `resources/templates/list` template 或正常任务中的 synthetic variable value；不能控制 host/client、B server/database、用户、ACL、token、审批者或 ledger。成功必须满足：

1. fixed host/application 按 A 的合法 template 展开变量；
2. expansion 实际选择 B origin/tenant/object/resource，B ACL 本应拒绝但 protected synthetic resource read/sink commit 发生；
3. independent ledger 记录 template URI, variable, source server/session, canonical expanded URI, B ACL and effect；strict source/template/origin/tenant binding 拒绝且 benign A utility 保持。

排除 resource_link、SSRF、path traversal、filesystem capability laundering、pagination/cursor、ordinary resources/read、public resources、URI display、token passthrough、P4 provenance和攻击者自有资源。

## 待核验链

`resources/templates/list(A) → host template registry/URI expansion → canonical URI/source/tenant binding → resources/read or protected tool → B ACL/effect ledger`。

需固定支持 resource templates 的 host/client/server revision 和依赖锁，追踪 template source/authority、variable encoding/canonicalization、registry/cache key、read dispatch 和 B ACL。若 host 不自动展开、只向原 server read、或不存在 B protected ACL/sink，立即关闭；不得构造 permissive URI resolver。

## 四路筛查结果

本轮四个只读 scout 已完成；没有启动服务、调用模型、运行实验、注册 CLAIMS 或写入 EVIDENCE 数字。

### 文献查重

- `exact direct = 0`：未找到把 `resources/templates/list(A) → host 自动展开 → source/template/origin/tenant 错绑 → B protected resource → ACL 应拒绝但 effect 发生` 作为同一 MCP 机制实证评测的来源。
- 近邻已足以阻止宽泛新颖性表述：MCP Object-Authz Lab S8 覆盖 resource URI 中的 tenant/object 选择；The Stochastic Deputy 覆盖模型控制 tenant/resource scope；n8n-MCP advisory 覆盖真实跨租户 protected-resource 访问；OWASP/RFC 6570/RFC 8707 覆盖 URI/template、tenant/audience 和 confused-deputy 风险或防御。它们没有证明本轮窄链，但说明“URI/template 选择另一租户对象”本身不是新机制。
- 证据边界：这些近邻的 threat model、实现和指标不能合并成当前项目的 ASR；最近 30 天没有 exact hit 也不能单独证明新颖性。

### 固定实现

- TypeScript SDK v1.29.0 的 `listResourceTemplates()` 只返回模板，`UriTemplate.expand()` 是调用方工具定义，`readResource({uri})` 需要调用方显式提供具体 URI；SDK 没有 host-side 自动展开、跨 source/tenant ACL 或 effect ledger，因此该实现为 NO-GO。
- VS Code 1.106.0 与 mcp-agent 0.2.6 的固定源码在当前本地工作树不可复核；不能把旧记录或规范语义当作它们的本轮 template consumer 证据。已有只读线索显示 VS Code resource URI 保留 server definition，mcp-agent/SDK 以显式 API 为主，但不足以升级为完整全集合结论。
- 本地 `cra_mcp` 是单 project、固定资源、显式 read/tool loop，没有多租户 template consumer；不能作为受害 host，也不能为补齐链条而构造 broker、resolver、B ACL 或 ledger。

### 候选与威胁模型

- RT-1 `variable-source binding omission`：若 host 将 B-context 变量作为无来源字符串交给 A template，可能落到 B object；当前没有固定自动展开和现成 tenant router，且容易退化为 P4 provenance/普通 BOLA，UNCERTAIN/NO-GO。
- RT-2 `bind-before-canonicalize timing`：要求真实两阶段 pre-canonical authorization 与 post-canonical dispatch；不能使用非法编码、path escape、parser differential、SSRF 或 malformed URI。当前没有两阶段 witness，NO-GO pending witness。
- RT-3 `source-blind template-registry key`：要求已有 host-wide template registry 的 key 遗漏 source/session/tenant 并选择 B 的既有 handler；当前没有 registry→B ACL→protected effect 链，且与 Q2/Q7/D-28/D-35 高度重叠，NO-GO。
- 独立 evaluator 必须由 B synthetic reader/sink 写 append-only ledger，重算 expansion/canonicalization 并绑定 source/session/tenant；completion、URI、日志、模型意图、普通 read、B handler 拒绝和 attacker-owned effect 均不计成功。当前不存在可用的固定 B protected witness。

## 本轮裁决与边界

**VERDICT: NO-GO（已核验实现与三个候选）；整体保留 UNCERTAIN 仅用于未固定外部 host，不构成新颖性或可达性通过。** 资源模板轴关闭，不进入 R5/R6，不注册 claim，不产生效果率。

硬关闭条件包括：host 只展示 template/返回 completion/要求调用方显式 read；只向原 A server 读取；跨任意 authority 才能触发（SSRF）；变量直接选择 tenant/object（普通 BOLA）；缺少预先存在的 A/B source/session/tenant 隔离、B ACL、protected synthetic ledger；或只能证明 URI、completion、日志、模型文本和普通资源读取。

## 下一条有界轴

下一轮只筛查尚未关闭的 `MCP-R4-05` 窄问题：低信任 server 控制 cancellation/retry/finalization 时，固定 host 是否会把一次已批准的 trusted protected call 重新提交或重复提交到独立受保护 sink，并错误复用原 approval/effect permit。该问题必须与 D-21 已关闭的广义 effect-history、TRAP/GHSA replay、普通 cancellation residue、FCD handler drift、攻击者自有重复效果和网络时序区分；没有固定 host 的重提交路径或独立受保护 ledger 就立即关闭。

禁止为补齐路径而创建 retry broker、弱审批状态、宽松 finalizer、跨 client 连接或受害 sink；继续只允许 owned/local/sandbox、合成数据和无副作用 canary。
