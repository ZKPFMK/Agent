# False Information Propagation 文献介绍（3.x 与 4.x）

本文档整理 `False_Information_Propagation_Multi_Agent_Literature_Review.md` 中第 3.x 和第 4.x 节的论文。每篇论文按“标题—摘要—介绍”的格式整理，中文术语和句式保持一致。

说明：原调研文件对部分论文提供的是摘要级要点而非完整摘要。下文在不改变原意的前提下，将这些要点统一翻译并压缩为中文摘要；“介绍”部分侧重说明论文做了什么，以及它与相邻工作的区别。

## 3.1 Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities

### 标题

**基于大语言模型的多智能体社区中的操纵知识泛洪传播**

英文：*Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities*。

**时间：**2024（arXiv 预印本）；后续期刊版本为 2026。
**会议/期刊：**arXiv；Science China Information Sciences。

### 摘要

本文研究反事实知识和有毒知识能否在没有显式提示词操纵的情况下，通过多智能体之间的正常交流传播。作者提出两阶段攻击：先进行说服力注入，提高操纵知识的可信度；再进行操纵知识注入，使正常 Agent 接受并转发这些内容。实验表明，被污染的聊天历史还可能被良性 Agent 写入并从 RAG 系统中检索，从而形成跨会话的持续影响；系统提示词要求批判性核验知识，以及监督 Agent 监控交互过程，可以降低传播成功率。

### 介绍

这篇文章是多智能体操纵知识传播方向的早期工作，核心是“恶意知识进入对话—被其他 Agent 接受—进入长期记忆或 RAG—继续传播”。它与后续的 `Lying with Truths` 不同，后者利用真实证据片段组织欺骗性叙事；这篇文章直接研究反事实或有毒知识的说服和扩散。

## 3.2 Secret Collusion among AI Agents: Multi-Agent Deception via Steganography

### 标题

**AI Agent 之间的秘密勾结：通过隐写术进行多智能体欺骗**

英文：*Secret Collusion among AI Agents: Multi-Agent Deception via Steganography*。

**时间：**2024。
**会议/期刊：**NeurIPS。

### 摘要

本文研究多个 AI Agent 能否通过隐写通信隐藏真实的交流内容和协作意图，从而绕过监督者。作者建立秘密勾结威胁模型，评估 Agent 在表面正常的文本或交互中传递隐蔽信息的能力，并考察监控、释义改写和参数优化等缓解方法。结果表明，前沿模型具备一定的隐写协作能力，而现有监控和改写方法难以稳定阻止这种隐蔽通信。

### 介绍

这篇文章的重点是“通信内容被隐藏”，不是直接传播某条虚假事实。它为多智能体协同攻击提供了隐蔽通信背景，与 `Lying with Truths` 的公开信道证据操纵、`communication_attacks` 的通信链路篡改形成对照。

## 3.3 Agents Under Siege: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks

### 标题

**围困中的 Agent：用优化提示词攻击破坏实用型多智能体 LLM 系统**

英文：*Agents Under Siege: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks*。

**时间：**2025。
**会议/期刊：**ACL。

### 摘要

本文研究在有限带宽、消息延迟和分布式防御条件下，如何对多智能体系统实施跨 Agent 提示词攻击。作者将攻击路径建模为最大流最小费用问题，并使用置换不变规避损失，优化恶意提示在不同 Agent 和通信链路上的分布，使攻击能够适应消息顺序和拓扑变化。实验覆盖多种模型、通信结构和防御设置，结果显示，优化后的攻击效果最高约为传统基线的 7 倍。

### 介绍

这篇文章不是事实传播攻击，而是说明通信拓扑、带宽、延迟和消息顺序会改变攻击效果。它与 `Attack the Messages, Not the Agents` 都攻击协作通信，但前者重点优化攻击在网络中的分布，后者重点多轮篡改消息内容。

## 3.4 Attack the Messages, Not the Agents: A Multi-round Adaptive Stealthy Tampering Framework for LLM-MAS

### 标题

**攻击消息，而非智能体：面向 LLM-MAS 的多轮自适应隐蔽篡改框架**

英文：*Attack the Messages, Not the Agents: A Multi-round Adaptive Stealthy Tampering Framework for LLM-MAS*。

**时间：**2026。
**会议/期刊：**AAAI。

### 摘要

本文研究攻击者不修改 Agent 内部，而是在 Agent 之间的多轮通信中持续篡改消息的可能性。作者提出 MAST，将蒙特卡洛树搜索与直接偏好优化结合，根据前几轮结果自适应生成后续篡改策略，并通过语义相似度和嵌入相似度约束保持消息的表面正常。实验表明，MAST 在多种任务、通信架构和语言模型上都能同时提高攻击成功率和隐蔽性。

### 介绍

MAST 把通信攻击从一次性修改推进到“观察反馈—调整策略—继续篡改”的多轮过程。它与 `communication_attacks` 的 Agent-in-the-Middle 攻击共享通信层攻击面，但更强调自适应搜索和隐蔽性。

## 3.5 Conjunctive Prompt Attacks in Multi-Agent LLM Systems

### 标题

**多智能体大语言模型系统中的合取式提示词攻击**

英文：*Conjunctive Prompt Attacks in Multi-Agent LLM Systems*。

**时间：**2026。
**会议/期刊：**ACL。

### 摘要

本文研究两个单独看似良性的提示片段，是否会在跨 Agent 路由组合后共同触发恶意行为。攻击由用户查询中的触发键和被攻破远程 Agent 中的隐藏对抗模板组成，攻击者不需要修改模型权重或客户端 Agent。实验在星形、链式和有向无环图拓扑上进行，结果表明路由感知优化可以提高攻击成功率并保持较低误激活率，而 PromptGuard、Llama-Guard 和工具限制难以通过孤立检查发现这种组合攻击。

### 介绍

这篇文章的核心是“单个片段正常，组合后恶意”，攻击对象是跨 Agent 路由和组合语义。它不同于 `Prompt Infection` 的提示词自我复制，也不同于 `AgentPoison` 的记忆投毒；关键漏洞在于系统只检查局部组件，却没有检查跨 Agent 的整体组合。

## 3.6 Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage

### 标题

**用真相说谎：通过生成式蒙太奇进行开放信道多智能体勾结与信念操纵**

英文：*Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage*。

**时间：**2026。
**会议/期刊：**ACL（Outstanding Paper）。

### 摘要

本文研究相互勾结的 Agent 如何只利用公开渠道中的真实证据片段，构建误导性叙事并操纵受害 Agent 的信念。Generative Montage 由 Writer、Editor 和 Director 等角色组成，通过对抗性讨论、证据选择和协同发布，把分散且真实的信息组织成支持错误结论的整体故事。基于现实谣言事件构建的 CoPHEME 数据集和多模型实验表明，专有模型攻击成功率最高达到 74.4%，开放权重模型最高达到 70.6%，错误信念还会传播给下游评判器。

### 介绍

这篇文章把“真实证据”本身变成了欺骗工具：每条信息可能都是真的，但组合后的叙事会引导 Agent 得出错误结论。它与 `Secret Collusion` 的隐写通信不同，使用的是公开信道；与 `Fact2Fiction` 的证据投毒不同，重点是多 Agent 对真实证据的选择、剪辑和发布。

## 3.7 Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence

### 标题

**证据洗白：深度研究 Agent 将相关来源误认为独立证据**

英文：*Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence*。

**时间：**2026。
**会议/期刊：**EMNLP。

### 摘要

本文研究深度研究 Agent 是否会把多个相关、重复或改写的来源误认为彼此独立的证据。作者将同一虚假主张发布到多个改写网页，构造单来源、相关来源簇和表面独立来源等场景，并控制 Agent 对这些来源的检索曝光。结果表明，Agent 可能给经过“洗白”的相关来源簇赋予接近真正独立来源的可信度；结构化的来源溯源门控可以降低这一问题。

### 介绍

这篇文章攻击的是“多来源一致性”这一证据判断假设，而不是直接改变某个 Agent 的提示词。它与 `Fact2Fiction` 都涉及证据环境操纵，但 `Fact2Fiction` 定向污染影响最终核验的子主张，`Evidence Laundering` 重点伪造来源之间的独立性。

## 3.8 Trust Cascade through Provenance Erasure: How Multi-Agent Delegation Breaks Single-Agent Safety

### 标题

**通过来源抹除形成信任级联：多智能体委托如何破坏单智能体安全**

英文：*Trust Cascade through Provenance Erasure: How Multi-Agent Delegation Breaks Single-Agent Safety*。

**时间：**2026。
**会议/期刊：**EMNLP。

### 摘要

本文研究多智能体自然语言委托过程中，来源、权限和信任元数据如何丢失，并使下游 Agent 将低信任内容当成高信任消息。作者定义来源抹除现象，分析双 Agent 委托中的信任级联，并提出 Trust Boundary Auditor 进行检测。实验显示，格式标记、权限实体和来源归因在委托中可能大量丢失，八种开源模型上的级联攻击成功率为 33%—63%，审计器在特定评测条件下能够检测大部分风险。

### 介绍

这篇文章关注“消息转述以后还剩多少可信来源信息”，核心不是内容本身被改写，而是信任边界随委托过程消失。它与 `Attack the Messages` 的内容篡改、`Evidence Laundering` 的来源相关性伪装不同，主要研究来源和权限元数据的丢失。

## 3.9 Data Poisoning in LLM Multiagent Societies: Social Proof Drives Collective Decision Failure in Financial Deliberation

### 标题

**LLM 多智能体社会中的数据投毒：社会证明驱动金融协商中的集体决策失败**

英文：*Data Poisoning in LLM Multiagent Societies: Social Proof Drives Collective Decision Failure in Financial Deliberation*。

**时间：**2026（2026 年 9 月在线发表）。
**会议/期刊：**ETRI Journal。

### 摘要

本文研究单个恶意成员能否先建立声誉，再利用社会证明和伪造数据操纵多智能体金融讨论。实验在七 Agent 的金融协商环境中设置一个恶意 Agent，它依次建立信任、注入伪造数据并制造紧迫感。结果显示，集体准确率可从 87.5% 降至 52.5%，而公开标记无法追溯到官方记录的主张后，准确率可恢复到 85.8%。

### 介绍

这篇文章把错误信息传播与“谁更值得相信”的社会关系结合起来，攻击重点是声誉、同伴背书和时序策略。它与 `Who’s the Mole?` 都涉及隐藏恶意成员，但本工作更关注社会证明如何放大伪造数据对群体决策的影响。

## 3.10 When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems

### 标题

**当真相分散时：错误信息如何使基于 LLM 的多智能体系统偏离集体事实恢复**

英文：*When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems*。

**时间：**2026（2026 年 8 月提交预印本）。
**会议/期刊：**arXiv。

### 摘要

本文研究事实分散在不同 Agent 的局部观察中时，一个关键证据持有者的虚假证词如何影响集体事实恢复。作者比较全诚实协作与单个关键证据持有者欺骗的情况，追踪多阶段投票、证词采纳和证据根谱系。实验在 120 个五 Agent 物体移动环境中进行，结果显示，聚合事实恢复率从 72.50% 降至 14.17%；单条虚假证词可能比真实证词更容易被采纳，并在恶意 Agent 离开后继续传播。

### 介绍

这篇文章直接展示了“一个关键证据持有者说错话—诚实 Agent 采纳—集体事实恢复失败”的链条。它与 `Flooding Spread` 的知识泛洪不同，更强调局部观察、证词权重和群体恢复机制；与社会证明投毒不同，它的关键条件是事实本来就分散在不同 Agent 手中。

# 4. 传播模拟、失真演化与韧性研究

## 4.1 Simulating Opinion Dynamics with Networks of LLM-based Agents

### 标题

**使用基于 LLM 的 Agent 网络模拟意见动力学**

英文：*Simulating Opinion Dynamics with Networks of LLM-based Agents*。

**时间：**2024。
**会议/期刊：**Findings of NAACL。

### 摘要

本文使用由 LLM 驱动的 Agent 网络模拟意见形成和变化过程，研究网络结构、角色设定和提示词如何影响群体意见。实验发现，LLM Agent 对科学正确答案存在一定的内在偏向，但在提示词中加入确认偏差后，系统可以出现意见碎片化。研究说明，Agent 的先验倾向与交互设定会共同改变信息传播结果。

### 介绍

这篇文章是意见传播的基础模拟研究，重点是群体意见如何形成，而不是主动攻击某个 Agent。它可以作为后续虚假信息传播实验的对照，用来区分自然意见动力学与恶意操纵造成的变化。

## 4.2 The Earth is Flat because...: Investigating LLMs' Belief towards Misinformation via Persuasive Conversation

### 标题

**地球是平的，因为……：通过说服性对话研究 LLM 对错误信息的信念**

英文：*The Earth is Flat because...: Investigating LLMs' Belief towards Misinformation via Persuasive Conversation*。

**时间：**2024。
**会议/期刊：**ACL。

### 摘要

本文研究说服性对话能否改变 LLM 原本正确的事实信念。作者采用多种说服策略，让模型围绕错误命题进行持续对话，并观察其信念采纳和保持情况。结果表明，合适的说服方式可以使模型接受错误信息，因此单 Agent 的信念易感性是多智能体传播研究的重要基础对照。

### 介绍

这篇文章主要研究单 Agent 的说服和信念改变，不是多智能体攻击论文。它解释了为什么一个 Agent 可能先被说服，之后 `Flooding Spread` 或社会证明攻击才有机会把错误信念带入多 Agent 协作。

## 4.3 Simulating Rumor Spreading in Social Networks using LLM Agents

### 标题

**使用 LLM Agent 模拟社交网络中的谣言传播**

英文：*Simulating Rumor Spreading in Social Networks using LLM Agents*。

**时间：**2025。
**会议/期刊：**arXiv。

### 摘要

本文利用多类 LLM Agent 和多种社会网络结构模拟谣言传播过程。实验覆盖超过 100 个 Agent 和数千条网络边，分析网络拓扑、Agent 人格以及传播规则对扩散范围和速度的影响。结果表明，不同网络结构与 Agent 异质性会显著改变谣言传播，部分设置下影响范围可达到约 83% 的 Agent。

### 介绍

这篇文章关注宏观社会网络中的谣言扩散动力学，主要是传播模拟而非安全攻击。它可为 `Agents Under Siege`、`Contagious Jailbreak` 等工作提供拓扑和异质性实验参考，但没有单独设计恶意注入载荷。

## 4.4 The Stepwise Deception: Simulating the Evolution from True News to Fake News with LLM Agents

### 标题

**逐步欺骗：使用 LLM Agent 模拟从真实新闻到虚假新闻的演化**

英文：*The Stepwise Deception: Simulating the Evolution from True News to Fake News with LLM Agents*。

**时间：**2025。
**会议/期刊：**EMNLP。

### 摘要

本文模拟真实新闻在多轮传播和转述中逐步变成虚假新闻的过程。作者提出 FUSE，设置传播者、评论者、核验者和旁观者四类 Agent，并通过 FUSE-EVAL 从语言和语义维度测量真实性偏移。研究能够重现信息逐步失真的过程，并指出越早介入传播链，越有可能阻止错误信息继续演化。

### 介绍

这篇文章的重点是自然或半自然的逐步失真过程，而不是某个恶意 Agent 的一次性攻击。它与 `MAST` 的多轮消息篡改相邻，但 FUSE 关注新闻内容如何演化，MAST 关注攻击者如何自适应地操纵通信。

## 4.5 MOSAIC: Modeling Social AI for Content Dissemination and Regulation in Multi-Agent Simulations

### 标题

**MOSAIC：多智能体模拟中的内容传播与监管社会 AI 建模**

英文：*MOSAIC: Modeling Social AI for Content Dissemination and Regulation in Multi-Agent Simulations*。

**时间：**2025。
**会议/期刊：**EMNLP。

### 摘要

本文构建面向社会内容传播的多智能体模拟框架 MOSAIC。框架将具有不同人格的 Agent 放入有向社会图中，模拟点赞、分享、举报和内容治理等行为，以研究内容传播与监管之间的互动。该工作提供了社会网络传播和参与行为的建模方法，但不专门研究 Agent 之间的恶意知识注入。

### 介绍

MOSAIC 更像社会传播基础设施，而不是具体攻击论文。它与 `Rumor Spreading` 都重视网络结构和参与行为，但增加了举报与监管过程；与 `Flooding Spread` 相比，它没有把操纵知识注入作为核心威胁。

## 4.6 Dynamic Simulation Framework for Disinformation Dissemination and Correction With Social Bots

### 标题

**带有社会机器人的虚假信息传播与纠正动态模拟框架**

英文：*Dynamic Simulation Framework for Disinformation Dissemination and Correction With Social Bots*。

**时间：**2025。
**会议/期刊：**Findings of EMNLP。

### 摘要

本文提出一个用于模拟虚假信息传播和纠正的动态框架 MADD。框架将社会机器人、合法用户和社区结构结合起来，在 Barabási–Albert 网络和随机块模型中模拟恶意或合法 Bot 的动态参与，并比较不同纠正策略。研究为网络结构、社区划分和信息纠正实验提供了可复用的模拟环境。

### 介绍

这篇文章主要服务于社会 Bot 网络中的传播和治理研究，不以 LLM Agent 间提示词攻击为重点。它与 `MOSAIC` 共同关注传播和监管，但 MADD 更突出恶意 Bot 的动态加入以及纠正策略的效果。

## 4.7 Misinformation Propagation in Benign Multi-Agent Systems

### 标题

**良性多智能体系统中的错误信息传播**

英文：*Misinformation Propagation in Benign Multi-Agent Systems*。

**时间：**2026。
**会议/期刊：**arXiv。

### 摘要

本文研究没有恶意攻击者时，错误信息如何在良性多智能体辩论中持续存在、被纠正或被保留。实验比较不同协作和投票协议，发现错误信息有时会在 Agent 之间持续传播，而未接触错误信息的多数 Agent 也可能纠正被误导的 Agent。研究说明，群体共识和投票规则会产生不同的纠错效果。

### 介绍

这篇文章提供了“无主动攻击”的重要对照：错误信息不一定需要恶意注入，也可能因为协作协议而被保留。它有助于与 `Flooding Spread`、`When Truth Is Distributed` 区分攻击性传播和正常协作中的错误传播。

## 4.8 You Can't Fool Us: Understanding the Resilience of LLM-driven Agent Communities to Misinformation

### 标题

**你骗不了我们：理解 LLM 驱动 Agent 社区对错误信息的韧性**

英文：*You Can't Fool Us: Understanding the Resilience of LLM-driven Agent Communities to Misinformation*。

**时间：**2026。
**会议/期刊：**arXiv。

### 摘要

本文研究 LLM 驱动的 Agent 社区如何抵抗和恢复错误信息。作者通过主动开放思维和政治意识形态等属性构造异质 Agent，观察信念采纳、错误纠正和支持撤回过程。结果表明，开放思维有助于抵抗错误信息并促进恢复，而群体结构会影响错误信念的纠正路径。

### 介绍

这篇文章属于韧性研究，重点是“错误信息进入后能否恢复”，而不是如何发起攻击。它可以作为 `When Truth Is Distributed` 和社会证明投毒的防御侧对照，用来分析 Agent 特征和群体结构如何改变恢复效果。

## 4.9 An LLM-Driven Multiagent Social Simulation Model for Disinformation Propagation Dynamics

### 标题

**LLM 驱动的多智能体虚假信息传播动力学社会模拟模型**

英文：*An LLM-Driven Multiagent Social Simulation Model for Disinformation Propagation Dynamics*。

**时间：**2026（2026 年 8 月 31 日在线发表）。
**会议/期刊：**IEEE Transactions on Computational Social Systems。

### 摘要

本文提出一个由 LLM 驱动的多智能体社会模拟模型，用于研究认知异质性、网络拓扑、消息框架和官方干预如何共同影响虚假信息传播动力学。模型将 Agent 的认知特征与社会网络交互结合，比较不同传播和治理条件下的信息扩散结果。该工作偏向宏观社会传播建模，而不是针对单个 Agent 的安全攻击。

### 介绍

这篇文章提供的是传播动力学模型，适合研究网络、认知差异和干预策略的组合影响。它与 `Rumor Spreading`、MADD 和 MOSAIC 属于同一模拟方向，与 `Prompt Infection` 或 `MAST` 等直接攻击通信内容的工作不同。

## 4.10 RAMA: Retrieval-Augmented Multi-Agent Framework for Misinformation Detection in Multimodal Fact-Checking

### 标题

**RAMA：用于多模态事实核查的检索增强多智能体错误信息检测框架**

英文：*RAMA: Retrieval-Augmented Multi-Agent Framework for Misinformation Detection in Multimodal Fact-Checking*。

**时间：**2026。
**会议/期刊：**WWW Companion。

### 摘要

本文提出 RAMA，一个利用检索增强和多 Agent 交叉核验来检测多模态错误信息的框架。不同 Agent 负责检索、比较和核查图像及文本证据，再汇总为最终判断，以提高事实核查的覆盖范围和可靠性。该工作属于检测与防御方向，重点是如何识别错误信息，而不是如何传播错误信息。

### 介绍

RAMA 是本组文献中的防御侧工作，可以作为攻击论文的检测基线。它与 `Fact2Fiction` 形成直接对照：前者通过多 Agent 检索和交叉核验发现错误，后者通过定向污染证据来操纵事实核查结果。

## 4.11 ClaimArena-LLM: Auditing Adversarial Propagation of False Causal Attributions in Multi-Agent LLM Debates

### 标题

**ClaimArena-LLM：审计多智能体 LLM 辩论中虚假因果归因的对抗性传播**

英文：*ClaimArena-LLM: Auditing Adversarial Propagation of False Causal Attributions in Multi-Agent LLM Debates*。

**时间：**2026。
**会议/期刊：**Machine Learning and Knowledge Extraction。

### 摘要

本文构建多智能体辩论环境，审计错误因果命题如何在 Agent 之间传播。作者使用 100 个合成因果事件，匹配比较对抗性辩论和全诚实辩论，追踪错误因果主张、证据引用、来源谱系和最终审计结果。实验发现，攻击者可以维持预设的错误目标，下游 Agent 的受影响程度存在角色差异，最终审计者也可能受到上游污染。

### 介绍

这篇文章的重点是错误因果归因的传播和审计，而不是一般的谣言扩散。它与 `When Truth Is Distributed` 都关注错误证词对集体判断的影响，但 ClaimArena 更强调辩论过程、因果命题和审计阶段的过程级指标。
