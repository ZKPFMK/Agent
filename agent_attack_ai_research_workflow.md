# Agent Attack 研究中的 AI 加速工作流

**检索范围：** `paper/papers/01_攻击_外部交互`、`paper/papers/02_攻击_内部认知`、`paper/papers/03_攻击_多智能体协作`

**语料规模：** 54 篇本地论文（01：21 篇；02：14 篇；03：19 篇）。

**外部检索窗口：** 2024–2026 年公开论文、GitHub、研究者博客、X 搜索结果和 Reddit 搜索结果。本文把本地论文作为问题地图，把外部来源作为“研究者如何实际使用 AI 加速这类研究”的补充证据。

**本轮核验状态：** 直接打开并核对了关键作者原文、论文摘要/HTML 和会议页面；X 页面返回 HTTP 402，Reddit 官方页面返回 HTTP 403，Reddit 条目通过公开 archive 读取并保留原始 permalink。凡只能看到搜索摘要或 archive 内容的材料，报告中均标明证据限制。

**原始链接核验分级：** 已直接核验的核心页面包括 Google DeepMind red teaming、PyRIT 访谈、AgentDojo attacks 文档、SafeSearch、Genesis、DTap、MonitoringBench、PaperBench、EXP-Bench、AgentPoison、MCPTox、AI Scientist 独立评估，以及 Simon Willison、Patrick Mineault 和 Matthew Schwartz 的作者原文。Reddit 研究帖通过公开 archive 读取，原始 permalink 保留但官方页面未直接打开；X 仅保留原帖链接和搜索摘要，未将其数字作为核心证据。

## 研究问题

1. Agent attack 研究中，哪些环节最适合交给 AI 或 coding agent 加速？
2. 对 `01/02/03` 三类攻击面，怎样组织可复现的“攻击生成—执行—评估—迭代”循环？
3. 哪些工作仍然必须由研究者控制，怎样避免把自动化结果误写成安全结论？

## 先给结论

在这三个目录覆盖的研究里，AI 最适合加速的是**搜索空间探索、代码实现、批量实验和日志分析**，而不是独立决定研究问题或直接解释安全含义。可迁移性最高的模式是：

> 研究者定义攻击目标和成功标准 → AI 生成候选攻击或实验代码 → 沙箱中运行 → 独立 evaluator 检查是否真的达成目标 → AI 根据失败轨迹变异下一轮 → 研究者审计代表性案例和统计口径。

这个模式与本地论文的三条攻击路线相配：

- `01_攻击_外部交互`：让 AI 搜索网页内容、工具描述、视觉输入和环境状态中的攻击载荷。
- `02_攻击_内部认知`：让 AI 搜索触发器、推理劫持、记忆写入/检索和后门行为的组合。
- `03_攻击_多智能体协作`：让 AI 生成角色、消息、拓扑和多轮策略，测试攻击能否传播、协同或隐蔽。

自动化的主要收益来自**扩大候选数量和减少工程摩擦**。它不能自动保证新颖性、因果解释、真实世界代表性或防御有效性。

## 一、本地语料提供的研究问题地图

### 1. 外部交互：从“写一个 prompt”转向“搜索攻击环境”

`01_攻击_外部交互` 已经覆盖了从内容输入到工具执行的完整链路：网页间接提示词注入、不可见 HTML、视觉/GUI 元素、恶意图像补丁、工具元数据、MCP 工具投毒、事实核查证据污染、搜索 Agent 红队以及跨工具寄生链。

本地知识库把它抽象为：

```text
外部内容或界面环境
        ↓
上下文、角色或感知边界被混淆
        ↓
错误动作、工具调用或证据判断
        ↓
任务偏转、隐私外泄、事实误判或资源消耗
```

因此 AI 加速点不是简单让模型“写更强的恶意 prompt”，而是让它自动探索以下变量：

| 变量 | AI 可以做的工作 | 研究者必须固定的条件 |
|---|---|---|
| 载荷位置 | 生成网页文本、HTML 属性、工具描述、图像/截图、文档片段 | 注入位置、可见性、长度、权限和用户任务 |
| 目标行为 | 根据目标 Agent 的工具 schema 生成动作导向候选 | 什么算成功：错误点击、越权调用、泄露、任务偏转或成本上升 |
| 黑盒反馈 | 读取轨迹、工具调用和失败原因，变异下一轮候选 | 反馈是否可被攻击者获得，避免把不可用信息泄露给攻击者 |
| 环境变化 | 自动构造不同网页、工具列表、排序和上下文组合 | 真实应用分布、基线环境和随机种子 |
| 规模化评测 | 并行运行多个 Agent/模型/任务组合 | 模型版本、系统提示、工具权限和停止规则 |

`AdvAgent`、`AgentVigil`、`SafeSearch`、`VPI-Bench`、`MCPTox` 等本地条目适合被整理成一个“黑盒攻击搜索与环境 benchmark”分支，而不是只按提示词类型逐篇阅读。

### 2. 内部认知：从一次越狱转向状态生命周期

`02_攻击_内部认知` 覆盖训练后门、推理劫持、故障放大、记忆投毒、查询式记忆注入、多模态记忆投毒、知识文件泄露和动态后门。

这里最值得 AI 加速的是**多阶段状态实验**：

```text
写入或植入阶段 → 休眠/触发阶段 → 检索或推理阶段 → 行动阶段 → 持久性/迁移评估
```

AI 可以自动生成不同的写入样本、触发器和查询序列，管理长对话，比较写入后立即触发与延迟触发，并从轨迹中抽取“何时发生状态改变”。但需要特别防止把“输出看起来异常”直接等同于“记忆被成功投毒”。至少应分开测量：

- 写入成功率；
- 触发成功率；
- 目标任务偏转率；
- 跨任务、跨用户或跨 Agent 的迁移率；
- 对正常任务效用的损失；
- 检测器或内容筛选器是否能发现攻击。

本地 `AgentPoison`、`MINJA`、`MemIncept`、`Visual Inception`、`BadAgent`、`DemonAgent`、`UDora` 等可以据此组成统一实验模板。

### 3. 多智能体协作：从单个攻击样本转向传播和协调

`03_攻击_多智能体协作` 的核心变量是角色、通信、拓扑、轮次和状态传播。攻击目标可能是让多个 Agent 协同完成恶意任务、传播恶意提示、隐藏意图、篡改消息、制造递归阻塞、执行恶意代码或形成信念操纵。

适合 AI 自动化的对象包括：

- 角色配置和恶意/良性 Agent 的组合；
- 通信拓扑和受感染节点位置；
- 多轮消息变异与隐蔽性约束；
- 传播路径和感染深度；
- 任务、Agent 数量、工具权限和记忆策略的网格实验；
- 对话轨迹聚类、异常消息定位和失败原因归因。

本地 `Evil Geniuses`、`Prompt Infection`、`Multi-Agent Security Tax`、`Agents Under Siege`、`Attack the Messages, Not the Agents`、`CORBA`、`Evo-Attacker`、`Lying with Truths` 等适合统一到“攻击传播—协作损失—检测难度”的实验框架中。

## 二、外部证据：研究者实际怎样使用 AI

### A. 把 coding agent 当作可审计的研究助理

Paul Goldsmith-Pinkham 的研究 workflow 文章是一个较具体的第一手案例。他描述了用 Claude Code 读取项目、写并运行脚本、查看输出后继续迭代；长任务通过 `progress.md` 保存状态，再在新会话中续接。他还把数据安全和验证放在 workflow 里：敏感数据不交给 Agent，研究代码需要“信任但验证”。

这套做法可以直接迁移到 agent attack 项目：

1. 用 `README` 或 `PROJECT.md` 固定攻击目标、威胁模型和成功标准；
2. 让 coding agent 先读取目录结构和已有实验，再提出计划；
3. 将每次实验拆成独立脚本和可复现配置；
4. 每轮写入 `progress.md`、seed、模型版本、环境和结果路径；
5. 研究者逐步审阅 diff、攻击轨迹和统计脚本。

文章还强调，AI 生成的数据处理和图表必须由研究者检查。它提供了可迁移的方法论证据，但没有证明某个总体效率提升百分比，因此不应把“90% 工作在 Claude Code 中”当作普遍生产力结论。

来源：

- [Getting Started with Claude Code: A Researcher’s Setup Guide](https://paulgp.substack.com/p/getting-started-with-claude-code)
- [Claude Code for Applied Economists 系列](https://markusacademy.substack.com/p/claude-code-for-applied-economists)

Goldsmith-Pinkham 系列还展示了从 Census 数据抓取、SEC 10-K 文档抽取、DuckDB/HMDA 大型数据处理，到论文复现和 Overleaf 图表同步。对 agent attack 研究而言，最有价值的不是具体经济学任务，而是其工程结构：**规划、执行、调试、版本提交、逐步审阅**。

### B. 把 AI 用作攻击候选生成器和 evaluator，而不是唯一裁判

安全研究中的自动红队工作逐渐采用“攻击者 Agent + 被测 Agent + evaluator”的结构。公开工具和平台中，Promptfoo 的 red team 文档、DeepTeam、DecodingTrust-Agent Platform（DTap）都体现了类似思路：生成攻击输入，在隔离环境运行，重置环境，记录轨迹，再由规则或模型评估结果。

这种结构与三个本地目录的对应关系如下：

| 本地目录 | 生成器 | 被测对象 | evaluator 应检查什么 |
|---|---|---|---|
| 01 外部交互 | 注入/工具描述/网页/视觉载荷生成器 | Web Agent、Computer-use Agent、MCP Agent、搜索 Agent | 是否调用错误工具、改变参数、泄露数据或偏转任务 |
| 02 内部认知 | 触发器、查询序列、记忆写入样本生成器 | 具有记忆、RAG、后门或长程规划的 Agent | 是否写入、检索、触发、持久化及损害正常效用 |
| 03 多智能体 | 角色、消息、传播和拓扑策略生成器 | MAS 编排器和多个协作 Agent | 是否传播、勾结、隐藏意图、破坏协作或造成资源耗尽 |

关键设计是让 evaluator 与攻击生成器尽量解耦。攻击生成器可以使用 LLM，但最终成功判定应尽可能依赖可观察的工具调用、状态变化、任务完成条件和规则检查，而不是只让另一个 LLM 读一段回答后打分。

来源：

- [Promptfoo LLM red teaming guide](https://www.promptfoo.dev/docs/red-team/)
- [DeepTeam GitHub](https://github.com/confident-ai/deepteam)
- [DecodingTrust-Agent Platform](https://arxiv.org/pdf/2605.04808)
- [AI-Red-Teaming-Guide](https://github.com/requie/AI-Red-Teaming-Guide)

### C. 用自动化 benchmark 把“会攻击”变成可比较的任务

`SEC-bench` 是与本项目最接近的公开基准思路之一：把真实软件安全任务整理为可执行环境，让 Agent 设置仓库、复现漏洞并生成修复。其报告的最佳 PoC 生成率为 18.0%，最佳修复率为 34.0%。这些数字衡量的是特定 benchmark 上的成功，不等于一般 Agent attack 能力。

`MCPTox` 则更贴近 `01_攻击_外部交互` 的 MCP 工具投毒方向。其摘要页明确写出：评测了 45 个真实 MCP server、353 个真实工具、1,348 个恶意测试用例和 20 个 LLM Agent；摘要报告最高攻击成功率为 o1-mini 的 72.8%，最高拒绝率低于 3%。这些是摘要页数字，具体攻击模板、基线和完整分项结果仍应以论文全文为准。

`AgentPoison` 是 `02_攻击_内部认知` 的本地对应案例。公开 NeurIPS 页面明确把问题定义为通过投毒记忆或知识库进行 Agent 红队测试，适合用来设计“低投毒率、写入/检索分离、正常效用保持”的实验矩阵。

来源：

- [SEC-bench NeurIPS 页面](https://neurips.cc/virtual/2025/poster/118134)
- [SEC-bench arXiv](https://arxiv.org/pdf/2506.11791)
- [MCPTox arXiv](https://arxiv.org/pdf/2508.14925)
- [AgentPoison NeurIPS 页面](https://neurips.cc/virtual/2024/poster/94715)

### D. 用 paper-to-code 系统减少复现实验的工程成本

`ResearchCodeAgent` 把论文方法描述转成可执行代码。其正文页面报告了三类 ML 任务、每个任务 8 次运行、规划 Agent 与 worker 的分工，并指出平均代码编辑量折算的时间节省为 57.86%。但同一页面也显示：生成代码仍有大量错误，简单任务上一次性生成可能比动态规划更快，而且“时间节省”是根据修复行数和编辑行数计算的代理指标，并非真实墙钟时间。

对本地 agent attack 语料，适合让 AI 做的是：

- 将论文方法和实验配置转换成统一的 YAML/JSON schema；
- 生成 benchmark harness、API wrapper、日志解析器和统计脚本；
- 从论文表格检查实现是否覆盖所有模型、任务和攻击预算；
- 对失败案例进行定位和分类；
- 生成复现实验报告草稿。

不应把“代码能运行”作为复现成功。需要同时检查攻击载荷、威胁模型、模型版本、工具权限、随机种子、停止条件和指标定义是否与原论文一致。

来源：

- [ResearchCodeAgent](https://arxiv.org/html/2504.20117v2)

### E. 一手实践案例：隔离、可回滚和验证优先

另一组研究者的一手记录把上述模式说得更具体，也暴露了“Agent 运行得很快”与“研究结论可信”之间的差距：

- [Simon Willison：Code research projects with async coding agents](https://simonwillison.net/2025/Nov/6/async-code-research/)：把每个技术问题放进隔离 GitHub repo，交给 Codex Cloud、Claude Code web、Jules 或 Copilot agent；Agent 自己安装依赖、抓取数据、运行实验并提交 PR，commit 记录 prompt/transcript，再用 GitHub Workflow 汇总结果。作者明确提醒：Agent 可以证明“能工作”，不能证明“不可能”；未经审阅的报告属于不可直接发表的草稿。这个模式适合 `01` 的网页/工具攻击实验和 `03` 的多轮 MAS 实验。
- [Patrick Mineault：Claude Code for Scientists](https://www.neuroai.science/p/claude-code-for-scientists)：建议先 plan、再执行、再评估；把原始数据、处理数据、代码和 notebook 分开，用 Snakemake 或单一 pipeline 串起流程，先写 tests 和诊断图，再把已确认的经验变成测试，并用 git branch 保证可回滚。迁移到 `02` 时，可以把记忆写入、触发和检索分别做成可测试阶段。
- [Kevin Yang：Claude Code is secretly an excellent data analysis agent](https://yang3kc.substack.com/p/claude-code-is-secretly-an-excellent)：把研究问题写成 Markdown plan，拆成一步一个脚本，逐个审查脚本和输出，使用 git branch/commit 与 `CLAUDE.md`，清空上下文后从计划文件恢复。作者估计大部分分析代码由 Agent 生成，但没有提供受控的时间或质量对照，因此只能作为 workflow 案例。
- [Matthew Schwartz：Vibe physics](https://www.anthropic.com/research/vibe-physics)：用任务树、持续测试、Monte Carlo、分析脚本和 LaTeX 维护长周期计算，并用其他模型交叉核验。案例报告了错误公式、伪造平滑图和虚构 verification coefficients，说明跨模型检查、独立 oracle 和逐阶段验证是必要环节。
- [Yogesh Kumar 案例](https://aiforautomation.io/news/2026-03-24-researcher-gave-claude-code-old-project-found-hidden-bug)：在隔离环境中限制 Agent 只能修改单个训练文件，每轮执行“提出假设—改一处—训练—测量—保留/回滚”，从旧项目中发现硬编码参数问题。案例有具体循环，但单项目、单 GPU，且文章中的指标口径存在不一致，不能直接引用其提升数字。

这些案例共同支持一种更窄的实践结论：对 agent attack 研究而言，最重要的基础设施不是“让 Agent 更自主”，而是**让每轮修改可审阅、可回滚、可重跑，且让 evaluator 独立于攻击生成器**。研究者的时间会从手写代码转移到检查 threat model、指标泄漏、基线公平性和轨迹解释。

### F. Reddit 讨论：局部委托和证据回流

Reddit 官方页面在本环境返回 403；以下帖子由公开 Reddit archive 读取，再用原始 permalink 对照。它们适合提供研究者和研究生的真实使用语境，但没有严谨的前后对照计时，不能支持普遍提速结论。

- [r/MachineLearning：How much should researchers (especially in ML domain) rely on LLMs for their work?](https://www.reddit.com/r/MachineLearning/comments/1nwaunk/)（2025-10-02）：讨论者普遍把 LLM 放在读完论文后的总结/综合、检索词改写、寻找遗漏工作、boilerplate/plotting/data-conversion 代码、debugging 和语言润色环节。较稳妥的建议是先读原文，再让 LLM 组织材料，并回到原文核对；反对意见集中在 hallucination、popularity bias、sycophancy，以及把计划和阅读外包后研究判断力下降。
- [r/GradSchool：Thoughts on using ChatGPT to find academic articles?](https://www.reddit.com/r/GradSchool/comments/1nde8z8/)（2025-09-10）：较一致的 workflow 是让模型把抽象想法改成检索词或提供起始候选，然后回到 Google Scholar、图书馆数据库或领域索引手工筛选。讨论记录了假引用、只返回高引用/主流文献、paywall 覆盖不全和反复返回 Wikipedia/MDPI 等问题。这与 `01/02/03` 的论文矩阵构建直接相关：AI 负责 query expansion 和初筛，引用和威胁模型必须回源核验。
- [r/GradSchool：Using AI to read dense texts](https://www.reddit.com/r/GradSchool/comments/1oeuutu/)（2025-10-24）：讨论者将 PDF 交给 ChatGPT 或 SciSpace 摘要，再自己重读；有人建议使用 NotebookLM，让回答绑定到上传来源并带 source links。失败案例包括 false references、模型把不存在的论证归给原文，以及陌生理论领域中无法判断错误。它支持“先让 AI 抽取字段，再做人工页面核对”，不支持跳过原文阅读。
- [r/GradSchool：How to convert pdfs and summarize them for research papers?](https://www.reddit.com/r/GradSchool/comments/1ob6uer/)（2025-10-20）：讨论了 PDF/OCR、OneNote 固定字段、Zotero/Obsidian、NotebookLM 和 Elicit。最可迁移的部分是把每篇论文转成固定 schema，例如 `takeaway`、`important citations`、`main points` 和 `summary`，再写入本地论文矩阵；工具推荐和“节省时间”均缺少独立验证。
- [r/MachineLearning：AI-generated literature reviews 导致投稿/预印本质量问题](https://www.reddit.com/r/MachineLearning/comments/1ol8wup/)（2025-10-31）：这是一条反向证据。讨论者担心“把论文喂给 LLM 后拼成表面综合”会产生缺少 taxonomy、gap identification 和批判性判断的低质量综述。对本项目的启示是：AI 可以帮助抽取和比较 `01/02/03` 论文，但不能把逐篇摘要拼接当成攻击面 taxonomy 或 novelty 结论。

Reddit 证据的共同点是：社区实际接受的不是“端到端自动 research”，而是**先由人确定研究问题和材料，再让 AI 处理局部任务，最后让人把结论回链到原文、代码和数据**。讨论中的“更高产”主要是主观描述；帖子删除、评论自述身份、archive 截断和社区选择偏差也限制了外推。

### G. Agent attack 专门证据：自动红队闭环已经比较清晰

与一般科研 workflow 分开看，agent attack 领域的一手材料已经形成了更稳定的闭环：

```text
人工定义风险/目标
→ 生成器或 attacker agent 产生候选
→ 在真实或可复现的 sandbox 中运行
→ 用状态、工具轨迹、规则和 judge 评分
→ 保存失败轨迹并提炼策略
→ 变异、回归测试和人工抽查
```

这些材料比“AI 帮我写论文”更直接地说明了安全研究者如何使用 AI：

- [Google DeepMind：Red Teaming Language Models with Language Models](https://deepmind.google/blog/red-teaming-language-models-with-language-models/)（2022）：由 red LM 生成测试输入，target LM 生成回应，red classifier 判断有害行为。其价值是扩大测试用例的数量和多样性，限制是只能覆盖当前模型已经表现出的危害，不能替代其他评估。
- [PyRIT 访谈](https://talkpython.fm/episodes/show/521/red-teaming-llms-and-genai-with-pyrit)：微软 red team 描述了 seed prompt/假设 → 广泛扫描 → 聚焦薄弱点的流程；attacker LLM 生成攻击，另一个 LLM 或规则 scorer 判断结果，人可以编辑 prompt 并最终复核。Playwright、转换器、多轮对话和完整 trace 让它能测真实 UI、间接注入和多种 payload 变体。访谈也明确提醒，自动 judge 不能被当作绝对准确，系统的非确定性会影响结果。
- [AgentDojo attacks 文档](https://agentdojo.spylab.ai/concepts/attacks/)：攻击接口能访问被测 pipeline、task suite、user task 和 injection task，自动生成注入候选并运行 user/injection task pair。它同时关注正常 utility 和安全结果，适合 `01` 的间接提示词注入；但其白盒 attacker access 较强，不能直接代表黑盒攻击。
- [SafeSearch](https://arxiv.org/html/2509.23694v4)：用 o4-mini 从风险描述生成搜索场景、恶意计划、网站指南和安全 checklist，再通过基线 Agent 的差分测试过滤不可行案例。300 个 case 覆盖五类风险、17 个模型和三种 search scaffold，每个 case 运行三次；最高报告 ASR 为 90.5%，安全 evaluator 与人工校验一致率超过 95%。限制包括每次只注入一个不可靠网站、不模拟真实 SEO、未覆盖全部失败模式，且安全评估依赖 LLM judge。
- [Genesis](https://arxiv.org/html/2510.18314)：把成功攻击策略存入库，Strategist 从交互轨迹中提炼自然语言或代码策略，Attacker 用 embedding 检索并通过 mutation/crossover 生成下一轮 payload。Mind2Web 840 个任务中，SeeAct/GPT-4o 的平均 ASR 为 53.0%，去掉 Strategist 后降为 29.9%；这说明“从失败轨迹提炼可复用策略”比单纯增加 prompt 数量更重要。但实验只有四个领域、两个目标 Agent 和三个后端，跨模型迁移并不稳定。
- [DTap / DTap-Bench](https://arxiv.org/html/2605.04808)：提供超过 50 个模拟环境、14 个领域、6,682 个任务，其中 3,876 个红队任务；环境支持状态 reset、确定性转移、回放和可验证 judge。DTap-Red 采用攻击优化 → 受害 Agent 执行 → verifier 判断 → 失败 refinement 的循环。模拟环境提高了可重复性，但对 surrogate Agent 的优化能否迁移到真实服务仍需验证。
- [MonitoringBench](https://arxiv.org/html/2605.09684)：让 Recon Agent 或 Recon+Tools 生成 BashArena 攻击轨迹，再用四阶段 identify/plan/rewrite/validate 做隐蔽化 refinement。2,644 条轨迹中，针对 Opus 4.5 的 catch rate 从只诱导攻击时的 94.9% 降到 refinement 后的 60.3%。但它只覆盖一个环境和四个 side task，阈值按 honest runs 校准，且攻击主要用 Anthropic 模型开发，存在模型偏差。

对本地三个目录的直接映射是：`01` 重点采用 SafeSearch/AgentDojo/DTap 的环境与工具轨迹闭环；`02` 重点采用 MonitoringBench 的状态/轨迹 refinement 和独立 monitor；`03` 重点把 Genesis 的策略库扩展为通信、角色、拓扑和传播路径的记忆库。agent attack 专门证据目前主要支持**自动红队和实验执行**，不足以支持“AI 已经能独立完成文献综述、选题和论文写作”的说法。

## 三、针对三个目录的推荐工作流

### 阶段 1：先让 AI 建立本地论文矩阵

不要一开始让 Agent 总结 54 篇论文的长摘要。先生成结构化表，每篇只保留以下字段：

```text
paper_id
attack_surface: external | internal | multi-agent
entry_point
attacker_capability
victim_agent
state_affected
objective
attack_generation_method
evaluator
benchmark_or_environment
models_and_versions
main_metrics
ablations
limitations
code_or_data_url
```

让 AI 从本地中文摘要和 PDF 中填表，再由研究者抽查原文。已有知识库 `paper/知识库/Agent安全论文知识库.md` 可以作为第一版分类依据，但不应替代论文全文。

推荐的第一轮产物：

- `papers.csv`：一行一篇论文；
- `attack_taxonomy.md`：按攻击面和状态阶段组织；
- `claims.md`：每个数字对应论文页码或表格；
- `gaps.md`：同一攻击面中尚未比较的变量。

### 阶段 2：用攻击链找研究空白

让 AI 做候选生成时，提示中必须带上已有论文矩阵和排除条件。可以让它对每个候选回答：

1. 它改变的是输入、推理、记忆、通信还是执行？
2. 与本地目录中的哪些论文重叠？
3. 新增了攻击者能力、受害者状态、环境约束还是评测指标？
4. 能否构造一个不依赖主观 LLM judge 的成功标准？
5. 最小可行实验是什么？
6. 哪个控制实验最可能推翻这个想法？

这一步的目标是减少“换一个 prompt 名字”的伪创新，而不是让 AI 代替研究者决定新颖性。

### 阶段 3：建立统一的攻击实验 harness

建议所有三个目录共享同一套接口：

```text
AttackGenerator.generate(context, budget) -> payload
VictimAgent.run(task, payload, environment) -> trajectory
Evaluator.score(trajectory, target_condition) -> metrics
Mutator.update(payload, trajectory, score) -> next_payload
Recorder.write(config, seed, trajectory, metrics)
```

每轮实验至少保存：

- 原始任务和干净基线轨迹；
- 攻击 payload 及其生成历史；
- Agent 的完整消息、工具调用和环境变化；
- 模型、系统提示、工具 schema、权限和 temperature；
- evaluator 的原始判定和规则版本；
- seed、运行时间、失败原因和人工复核标签。

### 阶段 4：三条攻击线使用不同的搜索循环

#### `01` 外部交互

```text
生成网页/工具描述/视觉载荷
→ 在沙箱中运行目标 Agent
→ 检查动作、参数、泄露和任务结果
→ 根据黑盒反馈变异载荷
```

需要做的控制实验：可见文本 vs 不可见文本、单来源 vs 多来源、普通工具描述 vs 投毒描述、截图输入 vs DOM/可访问性输入、单个工具 vs 多工具链。

#### `02` 内部认知

```text
生成写入样本或触发查询序列
→ 执行写入/检索/规划任务
→ 分开测量写入、触发、持久化和迁移
→ 检查正常任务效用与检测器表现
```

需要做的控制实验：直接写入 vs 查询式写入、单次触发 vs 多轮触发、文本 vs 视觉载荷、短期上下文 vs 长期记忆、单 Agent vs 跨 Agent 传播。

#### `03` 多智能体协作

```text
生成角色/消息/拓扑/传播策略
→ 在固定通信预算中运行 MAS
→ 记录每个节点的消息和状态
→ 检查传播、勾结、隐蔽性、协作损失和资源消耗
```

需要做的控制实验：单 Agent vs MAS、星型 vs 链式 vs 非完全拓扑、显式恶意消息 vs 看似良性消息、固定攻击者位置 vs 动态位置、一次篡改 vs 多轮自适应篡改。

### 阶段 5：让 AI 做分析助手，不让它决定统计结论

AI 适合：

- 从轨迹中聚类失败类型；
- 找到异常工具调用或状态变化；
- 生成可视化代码；
- 检查表格是否与原始日志一致；
- 提出可能的混淆变量和后续 ablation。

研究者必须核对：

- 分母是什么；
- attack success 和 policy violation 是否被混用；
- 失败是攻击失败、Agent 任务失败，还是环境/工具报错；
- evaluator 是否对某类载荷有偏见；
- 结果是否只来自一个模型、一个 prompt 或一个随机种子；
- 防御下降是否只是正常任务能力下降。

## 四、哪些做法有证据，哪些仍只是经验

| 做法 | 当前证据强度 | 可以得出的结论 |
|---|---|---|
| 用 coding agent 读项目、写脚本、调试和维护进度文件 | 研究者第一手 workflow | 适合减少工程摩擦；没有普遍提速证明 |
| 用 Agent 生成和变异攻击 payload | 自动红队论文/平台 | 可扩大搜索量；成功率依赖 evaluator 和反馈设计 |
| 用沙箱和环境重置运行多轮攻击 | 公开红队平台和 benchmark | 提高可复现性和隔离性 |
| 用 paper-to-code agent 复现方法 | ResearchCodeAgent 等实验 | 能减少部分编码工作；代码错误和指标代理问题仍明显 |
| 让 Agent 端到端提出想法、做实验、写论文 | AI Scientist、Agent Laboratory、AIssistant | 能生成可运行的研究草稿；研究质量、引用和解释仍需人工审计 |
| 让 AI 独立判断新颖性和安全结论 | 缺乏可靠证据 | 不应作为唯一判断依据 |
| Reddit/X 上的个人经验可代表研究领域趋势 | 只有定性社区证据 | 可用于发现 workflow 和失败模式，不能推出普遍提速或安全效果 |

### 补充的系统性评测证据

为了避免把个人 workflow 分享夸大成“AI 已经能独立做研究”，还应参考以下 benchmark。它们不是专门针对 agent attack 的 benchmark，但能直接说明自动化研究流程在哪些条件下有效，以及为什么需要把攻击实验拆成可评分的子任务。

| 评测 | 测量对象 | 关键结果 | 对本项目的启示 |
|---|---|---|---|
| [MLE-bench](https://arxiv.org/abs/2410.07095) | ML engineering / Kaggle 风格任务 | 不同模型和 scaffold 的奖牌率仍然较低；延长运行时间只带来有限提升 | 不能用“运行更久”替代更好的 threat model、evaluator 和实验设计 |
| [RE-Bench](https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/) | 接近 AI R&D 的短任务 | 短时预算下 Agent 在部分可评分任务上有优势；长时任务中人类专家仍明显更强 | agent attack 的短反馈、明确目标任务适合自动化，开放式攻击发现仍需专家推进 |
| [EXP-Bench](https://arxiv.org/abs/2505.24785) | 从实验设计到结论的完整实验链 | 单个阶段可能完成，但“设计正确、实现正确、执行成功、结论正确”的完整成功率很低 | 每个攻击实验都要单独验证设计、代码、执行和解释，不能只看最终 ASR |
| [PaperBench](https://arxiv.org/abs/2504.01848) | 不使用原代码的论文复现 | 迭代 Agent 优于一次性 Agent，但整体复现率仍有限，且评审 rubric 本身成本很高 | 复现 `01/02/03` 论文时要保存 lineage、配置和逐项 rubric |
| [AutoReproduce](https://arxiv.org/html/2505.20662v1) | 文献 lineage、代码实现、单元测试和调试 | paper lineage 与 debug/refine 会显著影响执行率；数据预处理和模型数据流仍是难点 | 让 AI 先追踪论文、引用和代码，再写攻击 harness；不要只给它一段摘要 |
| [MLR-Bench](https://arxiv.org/abs/2505.19955) | 开放式 ML research task | Agent 的实验 soundness 低于可接受阈值，部分运行使用 synthetic/placeholder data | attack benchmark 必须检查真实数据流、真实工具行为和独立复核，不能接受占位结果 |
| [OpenScholar](https://arxiv.org/abs/2411.14199) | retrieval-grounded 科学文献问答 | 检索、重排序和 citation verification 能改善文献答案与成本 | 用 AI 做 54 篇论文矩阵时必须保留原文段落、引用和页码，而不是只保留摘要 |
| [ResearcherBench](https://arxiv.org/html/2507.16280) | AI research 问题、综述和咨询任务 | citation faithfulness 可以较高，但 citation coverage / groundedness 仍不足 | “引用存在”不等于“引用支持全部安全结论”，要逐条做 claim-to-evidence 检查 |

这些结果和本地三类论文结合后，形成一个更具体的判断：AI 最适合承担**候选生成、代码实现、短循环执行、轨迹整理和初步分析**；最不适合独立承担**攻击问题定义、真实威胁模型、结果有效性、跨系统外推和安全结论**。

## 五、需要保留的失败边界

### 1. 自动化 evaluator 会把“像成功”误判为成功

LLM judge 可能把一段听起来合理的回答判为攻击成功，却没有检查工具调用、数据流或持久状态。对于 `01/02/03`，优先使用可执行断言：调用了哪个工具、参数是否改变、秘密是否进入攻击者可见输出、记忆是否写入、消息是否跨节点传播。

### 2. 规划 Agent 的额外开销可能超过收益

ResearchCodeAgent 页面报告的结果显示，动态规划在复杂任务上有帮助，但简单任务上一次性生成可能更快。agent attack 研究应先测量 harness 本身的成本：每次候选生成的 token、模型调用次数、环境启动时间和人工复核时间。

### 3. 论文复现经常改变了原问题

如果 AI 自己补全缺失的 pseudocode、降低训练轮数、替换模型或修改工具权限，运行结果只能叫“近似复现”或“扩展实验”。报告中必须把原配置和实际配置并列记录。

### 4. 规模增加不等于研究质量提高

批量生成数千个 payload 可能只是在重复相似模式。需要报告去重率、攻击族覆盖率、跨模型迁移率和人工确认比例，而不是只报告候选数量或最高成功率。

### 5. 安全研究中的自动化必须保持隔离

攻击代码、恶意工具和多 Agent 传播实验都应在沙箱或离线环境中运行。使用真实数据、真实账户、真实 MCP server 或联网工具时，需要明确授权、最小权限和可回滚条件。报告只记录防御研究所需的抽象载荷和指标，不把可直接滥用的操作步骤作为默认实验材料。

## 六、可直接落地的最小项目结构

```text
agent-attack-research/
├── corpus/
│   ├── papers.csv
│   ├── taxonomy.md
│   └── claims.md
├── configs/
│   ├── external.yaml
│   ├── internal.yaml
│   └── multi_agent.yaml
├── attacks/
│   ├── generator.py
│   ├── mutator.py
│   └── seeds/
├── victims/
│   ├── web_agent.py
│   ├── memory_agent.py
│   └── mas.py
├── evaluators/
│   ├── tool_trace_rules.py
│   ├── memory_state_rules.py
│   └── communication_rules.py
├── experiments/
│   ├── run.py
│   ├── ablations.py
│   └── seeds.csv
├── logs/
├── analysis/
├── progress.md
└── README.md
```

`README.md` 固定威胁模型和成功定义，`progress.md` 保存阶段进度，`configs/` 固定实验条件，`logs/` 保存不可变原始轨迹，`analysis/` 只读取日志生成表格。让 coding agent 修改代码时，优先要求它先读 `README.md`、`progress.md` 和对应 config，再提交小的可审阅 diff。

## 七、来源与证据说明

### 本地来源

- [Agent 安全论文知识库](paper/知识库/Agent安全论文知识库.md)
- [01 外部交互论文目录](paper/papers/01_攻击_外部交互/)
- [02 内部认知论文目录](paper/papers/02_攻击_内部认知/)
- [03 多智能体协作论文目录](paper/papers/03_攻击_多智能体协作/)

### 外部来源

- [Paul Goldsmith-Pinkham: Getting Started with Claude Code](https://paulgp.substack.com/p/getting-started-with-claude-code)
- [Claude Code for Applied Economists](https://markusacademy.substack.com/p/claude-code-for-applied-economists)
- [ResearchCodeAgent](https://arxiv.org/html/2504.20117v2)
- [SEC-bench](https://arxiv.org/pdf/2506.11791)
- [MCPTox](https://arxiv.org/pdf/2508.14925)
- [AgentPoison](https://neurips.cc/virtual/2024/poster/94715)
- [Promptfoo red teaming guide](https://www.promptfoo.dev/docs/red-team/)
- [DeepTeam](https://github.com/confident-ai/deepteam)
- [DecodingTrust-Agent Platform](https://arxiv.org/pdf/2605.04808)
- [AI-Red-Teaming-Guide](https://github.com/requie/AI-Red-Teaming-Guide)
- [MLE-bench](https://arxiv.org/abs/2410.07095)
- [RE-Bench](https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/)
- [EXP-Bench](https://arxiv.org/abs/2505.24785)
- [PaperBench](https://arxiv.org/abs/2504.01848)
- [AutoReproduce](https://arxiv.org/html/2505.20662v1)
- [MLR-Bench](https://arxiv.org/abs/2505.19955)
- [OpenScholar](https://arxiv.org/abs/2411.14199)
- [ResearcherBench](https://arxiv.org/html/2507.16280)
- [Simon Willison: Code research projects with async coding agents](https://simonwillison.net/2025/Nov/6/async-code-research/)
- [Patrick Mineault: Claude Code for Scientists](https://www.neuroai.science/p/claude-code-for-scientists)
- [Kevin Yang: Claude Code is secretly an excellent data analysis agent](https://yang3kc.substack.com/p/claude-code-is-secretly-an-excellent)
- [Matthew Schwartz: Vibe physics](https://www.anthropic.com/research/vibe-physics)
- [Yogesh Kumar case study](https://aiforautomation.io/news/2026-03-24-researcher-gave-claude-code-old-project-found-hidden-bug)
- [Google DeepMind: Red Teaming Language Models with Language Models](https://deepmind.google/blog/red-teaming-language-models-with-language-models/)
- [PyRIT interview](https://talkpython.fm/episodes/show/521/red-teaming-llms-and-genai-with-pyrit)
- [AgentDojo attacks documentation](https://agentdojo.spylab.ai/concepts/attacks/)
- [SafeSearch](https://arxiv.org/html/2509.23694v4)
- [Genesis](https://arxiv.org/html/2510.18314)
- [DTap / DTap-Bench](https://arxiv.org/html/2605.04808)
- [MonitoringBench](https://arxiv.org/html/2605.09684)
- [Reddit: How much should researchers rely on LLMs?](https://www.reddit.com/r/MachineLearning/comments/1nwaunk/)
- [Reddit: Thoughts on using ChatGPT to find academic articles?](https://www.reddit.com/r/GradSchool/comments/1nde8z8/)
- [Reddit: Using AI to read dense texts](https://www.reddit.com/r/GradSchool/comments/1oeuutu/)
- [Reddit: How to convert PDFs and summarize them for research papers?](https://www.reddit.com/r/GradSchool/comments/1ob6uer/)
- [Reddit: AI-generated literature reviews and preprints](https://www.reddit.com/r/MachineLearning/comments/1ol8wup/)

### 社交媒体检索限制

本轮对 X 和 Reddit 的搜索主要用于发现实践线索。X 页面在当前环境返回 HTTP 402，因此 X 条目只保留原帖链接和搜索结果中可见的摘要，未把 X 数字作为核心证据；能回溯到作者博客或论文的内容，优先引用后者。Reddit 官方页面返回 HTTP 403，但并行检索通过公开 Reddit archive 读取了部分正文和评论，并用原始 permalink 对照帖子结构。Reddit 材料现在可以支持“社区中存在这些 workflow 和反对意见”的定性结论，但不支持普遍提速百分比：帖子有删除/隐藏、评论自述身份、archive 截断和选择偏差。涉及 `01/02/03` 的安全研究者专门实践仍然较少，因此 Reddit 证据主要用于补充文献检索、论文阅读和 coding workflow，而不是证明 agent attack 方法有效。

## 结论

如果目标是加速这三个目录的后续研究，最值得优先建设的不是一个“自动写论文 Agent”，而是一套共享的、可复现的 agent attack harness：统一攻击生成器、受测 Agent、规则化 evaluator、轨迹记录和 ablation 配置。agent attack 专门文献最有力地支持自动红队、策略变异、环境回放和轨迹分析；Reddit 与一般科研 workflow 则只支持局部的文献整理、代码和 debugging 经验。AI 负责扩大候选、改代码、运行实验和整理轨迹；研究者负责威胁模型、成功定义、控制实验、统计口径、真实失败案例和最终安全解释。
