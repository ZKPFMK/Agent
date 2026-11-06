# 代码中的阴影：探索基于大语言模型的多智能体软件开发系统的风险与防御

**原标题：**Shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems  
**攻击方法：**Implicit Malicious Behavior Injection Attack（IMBIA，隐式恶意行为注入攻击）  
**防御机制：**Adv-IMBIA  
**年份与会议：**2026，AAAI。  
**原文：**[本地 PDF](./26_aaai_shadows_in_code.pdf)。

## 摘要

基于大语言模型（large language model，LLM）的多智能体系统快速发展，显著简化了软件开发任务，使技术经验很少的用户也能开发可执行应用。然而，这类系统通过自然语言需求实现软件创作民主化的同时，也引入了尚未得到充分研究的重大安全风险。

我们识别出两种风险场景：恶意用户与良性智能体（Malicious User with Benign Agents，MU-BA），以及良性用户与恶意智能体（Benign User with Malicious Agents，BU-MA）。我们提出隐式恶意行为注入攻击（Implicit Malicious Behavior Injection Attack，IMBIA），展示多智能体系统如何被操纵，在表面良性的应用中生成隐藏恶意能力的软件；同时提出 Adv-IMBIA 作为防御机制。

在 ChatDev、MetaGPT 和 AgentVerse 框架上的评测显示，不同框架呈现出不同的漏洞模式。在 MU-BA 场景中，IMBIA 的攻击成功率分别达到 93%、45% 和 71%；在 BU-MA 场景中分别达到 71%、84% 和 45%。我们的防御机制显著降低了攻击成功率，尤其是在 MU-BA 场景中。

进一步分析表明，代码和测试阶段遭到破坏的智能体会带来更高的安全风险；同时，我们也识别出需要防范恶意用户利用的关键智能体。这些发现凸显了多智能体软件开发系统亟需稳健安全措施，并为实施有针对性且资源高效的防御策略提供了实践指南。

**代码：** <https://github.com/wxqkk0808/IMBIA>
