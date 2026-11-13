# 自适应工具链构想：公开文献核查

检索/阅读日期：2026-11-11。此文件由主协调根据已完成的 lit-scout 交接整理。原始网页/PDF、下载 URL 和阅读文本均保留在 `web-sources/` 的独立目录；主协调没有为本文件增加新一轮检索。方法事实与来源边界分开记录。

**结论：原稿宽泛的“新自主攻击机制”定位不建议继续；严格收窄的评测问题仍为 UNCERTAIN。** 高层恶意目标委托、多工具自主调用、任务相关包装、预先植入且无攻击者逐步反馈，都有明确近邻。本轮没有核查到某篇在同一设置下建立“严格未知工具注册表、单份外部内容、无后续攻击指令、中性真实故障后独立发现未指定替代路径、最终未授权效果”的完整证据；这不是全领域空白证明，也不是新颖性 gate 通过。

## 证据等级、范围及版本

本轮实际核查 **11 篇论文的方法或评测相关原文段落**，另核 Parasites/MCP-UPD 的公开版本元数据。核心阅读包括 AgentDojo、AgentDyn、MCP-ITP、FlowSteer、Context manipulation 的威胁模型与方法相关段落；没有宣称把全部论文所有正文、附录逐页精读。

为与项目统一，以下采用：

- `full-text-verified`：在公开原文定位了支持该具体事实的段落；不代表复现，也不代表整篇每页精读。
- `abstract-verified`：只有官方摘要支持。
- `inference`：本项目对证据的比较或解释。
- `unverified`：缺乏足够来源、运行日志或实现核对。文中“未建立”均属于此类，不能解释成方法不支持。

lit-scout 交接中的 A/B/C 分别为“原文段落/摘要或元数据/搜索线索”，这里不沿用该字母，避免与 A/B/C 攻击表面或 abstract 混淆。元数据核验只说明版本/书目信息，不能替代方法核验。

最终引用版本均不晚于 2026-11-11。AgentDyn 初读 v1 后已补读 2026-05-07 的 v3，以 v3 为最终依据；MCPTox 为 2026-09-29 的 v2；task-tampering 为 2026-11-05 的 v1。检索引擎的时间筛选曾返回窗口外记录，最终按官方版本历史筛选。

本文件不转述任何论文的 ASR 百分比，避免不同有效输出分母、模拟工具、预定攻击工具和系统指令条件被混在一起排名。

## 1. 对构想最重要的六组证据

### AgentDojo 已有高层目标委托与受害者选工具

来源：[AgentDojo v3，2024-11-24](https://arxiv.org/html/2406.13352v3)，§2、§§3.1–3.3、§§4.1–4.3、App.A/B.3、Fig.19。

`full-text-verified`：§2 明确受害者须“decide which tool(s) to call”；任务与攻击目标有对应环境状态检查；基线包括让受害者先完成恶意任务的 important-message，以及直接插入任务文字的 TODO，工具知识链是可选更强攻击，而非所有攻击都要预写每步函数调用。主协调额外核对了归档文本中受害者选工具及 TODO 基线段落。

`unverified`：§3.3/App.A 的接口可在每个 placeholder 返回内容，不能由此认证严格一次新摄入；§4.2 的知识消融是用户/模型姓名，不能当作目标工具注册表盲测。没有在本轮已核段落建立冻结载荷下的真实能力图变化与中性故障自主替路。

`inference`：原稿不能把“高层目标交给 Agent，由其自行选择合法工具”单独作为新机制；需要在知识和环境变化上明确更严格的可测量条件。

### AgentDyn 已研究动态规划和部分错误处理

来源：[AgentDyn v3，2026-05-07](https://arxiv.org/html/2602.03117v3)，§§3.2、4.1，App.B/D/F，Tables 6–7。

`full-text-verified`：动态规划要求受害者根据环境反馈实时调整策略；使用通用目标注入；附录有 push/pull 冲突和目录不存在的错误。部分冲突响应会指明后续 git 操作或 force 提示。因此“现有评测都没有错误后继续规划”的说法不成立。

`full-text-verified`：为减少动态操作中询问用户导致的效用下降，评测向系统消息加了自动完成且不请求确认的指令。主协调核对了归档文本中的这一选择。它必须作为比较条件保留，不能据其结果宣称自然部署的用户确认被绕过。

`unverified`：已核段落没有提供“首选能力真正失效，错误不含下一步建议，Agent 独立发现攻击文本未指定的另一能力路径”的完整同设置证据。动态状态和跨应用任务也不等于冻结载荷的严格工具盲迁移。

### MCP-ITP 的 adaptive 主要是攻击者优化

来源：[MCP-ITP v1，2026-01-12](https://arxiv.org/html/2601.07395v1)，§§3.2、4–5.2、Alg.1。

`full-text-verified`：攻击者可检查工具集，选择原工具及高权限目标工具；用 evaluator/detector 反馈迭代工具描述；目标用指定工具调用判断。这与受害 Agent 在未知工具环境中自行恢复是不同的自适应主体。

其 MDR 是特定检测器/有效输出下的指标，不能外推为真人发现率或完整轨迹审计发现率。跨模型泛化也不能写成跨工具能力图迁移。

### FlowSteer 是规划污染强近邻，但权限条件不同

来源：[FlowSteer v1，2026-05-12](https://arxiv.org/html/2605.11514v1)，§§3.2、4.1、5.1.2，App.E/F.1。

`full-text-verified`：在线通过用户任务提示接口提交单个提示，不持续查看运行中的工作流；主方法在构造前用 clean workflow、intermediate outputs、interaction traces 做画像。planner 实际重新生成角色、子任务和依赖，攻击者不是简单直接改图。黑盒替代也先探测角色/拓扑，再构造攻击。

`inference`：不能继承旧 Q6 的一句概要便认定它直接关闭当前完整条件。它的入口是用户任务提示，离线知识更强，主要评估最终输出偏离，不是低信任外部材料、未知 MCP 注册表与真实工具故障后的副作用见证。其 App.E.2 的 ASB-Bench 是改编任务并生成目标/参考解，不能直接当成 ASB 真实工具执行证据。

### 最新 task-tampering 削弱“预先植入、无观察、业务相关”的单独新意

来源：[Beyond Instruction Override / Task-Tampering v1，2026-11-05](https://arxiv.org/html/2611.07640v1)，§§1、3–4 及防御段落。

`full-text-verified`：攻击材料在执行前植入；攻击者只能改其角色可控制的外部材料，不能改用户/系统提示、看推理、拦截工具调用或改其他参与者材料，只知角色可知的公开环境结构，甚至不知道精确用户任务。工作重点是篡改既有任务所需的决定或值，不一定另加恶意任务。

`inference`：它并非当前高层附加越权目标及故障迁移的直接同设置证据，但“预置、无中途观察、表面贴合业务”各自已经不足以承担机制差异。

### 任务相关和流程合理化已有其他近邻

来源：[Context manipulation v1，2025-06-18](https://arxiv.org/html/2506.17318v1)，§§3–6；[TAB v1，2026-05-12](https://arxiv.org/html/2605.12233v1)，§§2–4.5。

`full-text-verified`：Context manipulation 区分 non-contextual、task-aligned、context-chained，后者把合法任务、中间目的、越权目标连接起来；其主要实验直接修改计划/历史，部分生成使用当前轨迹，权限强于单份外部资料。TAB 把 helpful cue 与额外 distractor 放在自然遇到的材料中，并操纵 blind/informed/targeted 的知识条件与相关性。

`inference`：这些近邻削弱“正常工作流措辞/任务相关性”本身的新意。它们不自动证明人类更难发现，也不能将有轨迹知识的结果当作无观察攻击者结果。

## 2. 十一篇有界对照矩阵

下表方法事实均有原文段落支持；严格条件的缺证据保持 `unverified`。同一作品的不同攻击子类不可合并成单一攻击权限。

| 工作、版本与方法位置 | 攻击者入口/知识 | 在线反馈 | 目标、受害者规划与环境变化 | 对本构想的重合与边界 |
|---|---|---|---|---|
| [InjecAgent，ACL Findings 2024](https://aclanthology.org/2024.findings-acl.624/)，§§2.1–2.3、3.1 | 修改外部工具响应字段；按已知工具生成并补齐任务参数 | 固定载荷，读取后响应有模型模拟 | 自然语言恶意任务、读→发送两阶段；首次合法调用被假定完成，非完整规划 | 外部目标诱导跨工具已有；严格工具盲与端到端故障替路未建立 |
| [AgentDojo v3，2024-11-24](https://arxiv.org/html/2406.13352v3)，§§3–4、App.A/B | 外部内容 placeholder；框架允许 API/任务知识 | 普通基线预置；Max 另取攻击最好结果 | 目标文本/TODO/important-message；有状态多工具自主执行 | 高层目标委托直接重合；一次新摄入、注册表盲和能力图迁移未建立 |
| [AgentDyn v3，2026-05-07](https://arxiv.org/html/2602.03117v3)，§§3–4、App.B/D/F | 现实第三方表面；网页例限制在广告位；严格未知工具未建立 | 默认预置，另有 scenario-adaptive 构造需分开 | 通用目标、动态反馈、冲突/路径错误；部分错误给下一步建议 | 动态规划已覆盖；中性真实故障后的未指定替代路径仍待核，且评测取消确认 |
| [ASB v4，2025-05-30](https://arxiv.org/html/2410.02644v4)，§§3.2、4.1 | 已知且可加入攻击工具；其他子类还可写用户/系统/记忆 | 多数模板预置 | 部分模板指定 Attack Tool 并强约束工具集；多场景/模型 | injected task 旧概念；不能把强控制工具集的结果视为弱攻击者自然规划 |
| [MCPTox v2，2026-09-29](https://arxiv.org/html/2508.14925v2)，§§3–4.1、5 | 恶意工具元数据；生成器拿到完整合法工具列表 | few-shot 与人工审核，非持续在线攻击反馈 | 触发+恶意动作+合理化；合法工具调用/参数评测 | 合法工具滥用、合理化已有；入口/知识更强，多服务器样本非同载荷迁移 |
| [MCP-ITP v1，2026-01-12](https://arxiv.org/html/2601.07395v1)，§§3–5 | 控制自有 server 描述，检查良性工具集并选目标 | 攻击构造用影子查询、检测/效果反馈 | 指定目标工具优化，跨模型泛化 | adaptive 主体不同；没有已核的真实失效多路径测试 |
| [FlowSteer v1，2026-05-12](https://arxiv.org/html/2605.11514v1)，§§3–5、App.E/F | 改用户任务提示；离线 workflow/trace 画像，或先黑盒探测 | 在线一个 prompt，构造前有侦察 | planner 重生角色/任务/依赖；跨模型/配置/拓扑 | 自组织规划污染强近邻；并非当前低信任入口与未知工具故障合取 |
| [Context manipulation v1，2025-06-18](https://arxiv.org/html/2506.17318v1)，§§3–6 | 直接写计划/历史；部分攻击生成看当前 trajectory | 有单次植入，但构造可知轨迹 | task-aligned/context-chained；逐步改计划、两代理架构 | 任务相关合理化已有；入口与观察能力更强 |
| [TAB v1，2026-05-12](https://arxiv.org/html/2605.12233v1)，§§2–4.5 | 自然环境材料，表面选择使用解题轨迹；知识有分层 | 环境预置，不是目标 Agent 在线持续调优 | cue 旁放 distractor；正常任务中额外行为；统一终端 scaffold | 相关性与额外行为切面已覆盖，不必恶意；非未知 MCP 替代链专项 |
| [Firewalls v2，2026-03-23](https://arxiv.org/html/2510.05244v2)，§§3、7–8 | 工具输出 IPI；强 cascade 有 tool-knowledge/语义欺骗/defense-aware mutator | Stage 3 用成败和防御反馈迭代，应与冻结攻击分开 | 沿 AgentDojo/tau 环境执行；跨基准 | 强必要防御/评测近邻；其 adaptive 结果不能当弱无反馈攻击效果 |
| [Task-tampering v1，2026-11-05](https://arxiv.org/html/2611.07640v1)，§§1、3–4 | 一处角色可控外部材料，知公开结构、不知确切任务、无中间轨迹 | 主威胁模型预植；检测优化改写另列 | 篡改原任务决定/值，有状态工具环境、多影响原语 | 无中间观察和任务相关操纵已有；附加高层目标/未知故障迁移仍不同 |

## 3. 公平比较、版本与代码线索

- [Parasites 官方记录](https://arxiv.org/abs/2509.06572) 为 v5，2026-05-01，注明 IEEE S&P 2026；早期题名不同。本节点只核公开元数据，方法结论由 `LOCAL-PRIOR.md` 承载。攻击者不必预知配置，与研究者分析工具能力不能混为一谈。
- MCPTox v2 摘要/介绍报告的用例数与同版 Table 1 三类计数之和不一致；MCP-ITP 又采用后者。未来比较必须固定数据文件版本，不能替作者默默统一。此处只记录计数来源冲突，不引用成功率。
- Firewalls §7.2 批评 ASB 的工具集构造、工具响应与参数无关、判定较粗。这是该论文作者的审查结论，本轮没有运行 ASB 复现；足以要求审计，不能直接当成已证实的本项目复现结论。
- AgentDojo §4.3 已指出初始 tool-filter 在不能提前计划工具，或同一工具集也能完成攻击时失效。该动态性与防御矛盾本身也不是新发现。
- 名称、参数名、描述改写和跨模型/服务器结果，都不能直接认证真实能力拆分/合并与中间表示变化下的迁移。

可用代码/防御线索仅核到论文或公开页所给链接，没有克隆、安装、运行或签署公平比较：

| 工作 | 代码/项目页 | 本轮辨认的防御线索 |
|---|---|---|
| InjecAgent | https://github.com/uiuc-kang-lab/InjecAgent | ReAct 安全提示与微调对照；注意模拟执行/有效输出分母 |
| AgentDojo | https://github.com/ethz-spylab/agentdojo | delimiters、detector、sandwich、tool filter；状态判定可参考 |
| AgentDyn | https://github.com/leolee99/AgentDyn | 提示/检测及 CaMeL、Progent、DRIFT 等；取消确认条件须保留 |
| ASB | https://github.com/agiresearch/ASB | 防御跨多攻击面，不能全算 IPI 防御 |
| MCPTox | https://github.com/zhiqiangwang4/MCPTox-Benchmark | §5 多为候选防御讨论，不能冒称都已实测 |
| MCP-ITP | 专用方法代码本轮未核到 | AI-Infra-Guard、Oracle；MDR 非用户/日志发现率 |
| FlowSteer | 专用方法代码本轮未核到 | FlowGuard 与 MAS 防御；最终输出 judge 不是工具效果 oracle |
| Context manipulation / TAB | 方法专用代码发布未独立确认 | Secure/Sandwich；TAB 列 Spotlighting、RUP、SIC、PromptArmor、TaskShield、Firewall |
| Firewalls | https://firewall-defenses.github.io/ | Minimizer/Sanitizer；修订基准与强反馈攻击应分组 |
| Task-tampering | https://github.com/amazon-science/task-tampering-prompt-injection | 信任层级提示、检测移除、DRIFT、Progent 等 |

## 4. 实际检索轴及未覆盖部分

检索只发送公开学术主题，没有发送用户构想、私有路径或私人材料。代表性实际查询包括：

```text
"prompt injection" "tool agnostic" agent
"prompt injection" "high-level goal" tools
"goal-conditioned" "prompt injection" agent
"prompt injection" "task-aligned" agent
"prompt injection" "unknown tools"
"prompt injection" "replanning" tool failure
"prompt injection" "tool failure" attack arxiv
"prompt injection" "semantic" "tool" transfer unknown
"prompt injection" "tool" "replanning" after:2025-11-11 before:2026-11-12
"prompt injection" "tool" "substitution" after:2025-11-11 before:2026-11-12
"prompt injection" "tool-agnostic" after:2026-10-12 before:2026-11-12
"prompt injection" "dynamic" "tools" after:2026-10-12 before:2026-11-12 arxiv
"prompt injection" "goal" "delegation" "tools" after:2026-10-12 before:2026-11-12
```

另逐名检索种子论文、FlowSteer 与 Context manipulation，沿相关工作追到 Firewalls 和规划隔离，再核对截点前一周的 task-tampering。11 篇是去重后实际核方法的数量，不是检索返回总数。没有穷举 Semantic Scholar/DBLP/ACL/OpenReview 全部 API 或全量 cited-by，不能写成全面排除先行工作。

失败/降级记录：

- AAAI 出版页 access denied，MCPTox 方法证据改用官方 arXiv v2；没有据此声称出版原文不存在。
- 一份硕士论文的搜索线索提到高层目标/工具 schema，WebFetch 只返回 PDF 二进制，未核正文，不计论文数量或证据。
- SecureGARD 等近月防御只达到搜索线索，未用于支持效果；不明镜像及未核版本日期记录不计结论。
- TAB 首次下载 TLS 失败，后取得显式 v1；AgentDyn 已从初读 v1 补核 v3。

## 5. 本地阅读工件

以下目录均在 `web-sources/` 下，每个目录含 `source-text.txt`、`source-url.txt` 及 `source.html` 或 `source.pdf`。原始下载与衍生文本分别记录；不从下载目录执行代码，文本处理使用 Python `-I`。

| 工作 | 独立目录 | 核读范围 |
|---|---|---|
| InjecAgent | `injecagent-acl-1fe50e87/` | §§2–3.1，局部 |
| AgentDojo | `agentdojo-1f993b9c/` | §§2–4、App.A/B，核心 |
| AgentDyn 最终 v3 | `agentdyn-v3-d6448ab0/` | §§3–4、App.B/D/F，核心 |
| ASB | `asb-801adc32/` | §§3.2、4.1，局部 |
| MCPTox | `mcptox-75437a85/` | §§3–4.1、5，局部 |
| MCP-ITP | `mcp-itp-87551812/` | §§3–5.2，核心 |
| FlowSteer | `flowsteer-7ca31b42/` | §§3–5、App.E.1/E.2/F.1，核心 |
| Context manipulation | `context-manipulation-528080a0/` | §§3–6，核心 |
| TAB | `task-alignment-3afaa38f/` | §§2–4.5，局部 |
| Firewalls | `firewalls-d7d6309f/` | §3、§§7–8，局部 |
| Task-tampering | `task-tampering-049f480d/` | §§1、3–4 及防御段，局部 |

AgentDojo 与 ASB 的下载 URL 未显式写版本号，但原件头部标识最终核对版本；上方公开引用采用显式版本 URL。下载材料有缓存价值，不表示本轮已核实现与所有实验配置。最终完整性检查见 [CHECKS.md](CHECKS.md)。

## 6. 剩余问题与下一节点

**可考虑的方向一：严格知识约束下的能力图迁移。** 在目标环境生成前冻结攻击内容，构造者只知道能力类别与目标约束，没有目标工具表；改名只是表面控制，另测试能力拆并、中间表示变化或路径变化，并事先证明正常任务和目标效果仍结构可达。它可能贡献严格泛化测量，而不是一种已成立的新提示注入机制。

**可考虑的方向二：中性真实故障后的无提示越权恢复。** 不允许错误携带下一步建议、替代工具名或新恶意内容，检查受害者在预设失败后是否自行选择未指定替代路径并产生真实越权效果；同时要有无可行路径和正常可用对照，以及同等授权的良性恢复任务。若只有带提示的错误才能完成，降回已知引导式恢复。

主协调建议先选第二个问题，以名称变化为单独控制；不一次同时开放能力图变化、任务相关性和所有检测指标。一次修改、一份对象、一次新摄入与后续 history 反复可见的定义见主报告，不能把标准 history 重放当作攻击者第二次在线反馈。

VERDICT: UNCERTAIN；宽泛“首次自主组链/低显著性新攻击”定位不支持。
INPUTS: 原构想、STATE、KB 定位及公开来源；原构想 hash 见 SCOPE.md。
OUTPUT: 本文件及上表 11 组下载/阅读工件。
CHECK: lit-scout 完成指定原文段落核查；主协调完成关键归档文本抽查与最终工件审计，结果见 CHECKS.md。没有运行论文代码或模型试验。
EVIDENCE: 各节固定版本、具体方法节及归档文本。
BLOCKERS: 严格合取尚无完整来源或可重算结果；没有全量被引遍历；没有注册表知识隔离、故障干预或效果 oracle 的实现证据。
NEXT: 对 MCP-UPD/AgentDojo/AgentDyn 做书面逐条件对照，冻结一个主问题与测量合同，保持 R4，不直接开实验。
DO_NOT_DO: 不把检索完成当创新通过；不写此前都是固定脚本、不写名即工具无关、低显著性即低发现率；不混淆攻击者优化与受害者恢复；不重开 I1/P4/Q1。
