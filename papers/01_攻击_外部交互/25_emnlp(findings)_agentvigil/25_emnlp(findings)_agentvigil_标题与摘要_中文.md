# AgentVigil：针对大语言模型智能体间接提示词注入的自动化黑盒红队测试

**原标题：**AGENTVIGIL: Automatic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents  
**攻击方法：**AgentVigil  
**年份与会议：**2025，Findings of EMNLP。  
**原文：**[本地 PDF](./25_emnlp(findings)_agentvigil.pdf)。

## 摘要

大语言模型智能体正面临一种关键的安全风险：间接提示词注入（indirect prompt injection）。这是一种复杂的攻击方式，通过操纵上下文信息而非用户的直接提示词，攻击智能体的核心——大语言模型。在本文中，我们提出 AgentVigil，这是一个通用的黑盒优化框架，旨在自动发现并利用不同大语言模型智能体中的间接提示词注入漏洞。

我们的方法首先构建高质量的初始种子语料库，然后采用基于蒙特卡洛树搜索（Monte Carlo Tree Search，MCTS）的种子选择算法，迭代优化输入，从而最大限度地提高发现智能体弱点的可能性。我们在 AgentDojo 和 VWA-adv 两个公开基准上评测 AgentVigil；针对基于 o3-mini 和 GPT-4o 的智能体，其攻击成功率分别达到 71% 和 70%，接近人工构造的基线攻击的两倍。

此外，AgentVigil 在未见过的任务和不同底层大语言模型之间表现出较强的迁移能力，在应对防御措施时也取得了有潜力的结果。除基准评测外，我们还将攻击应用于真实环境，成功误导智能体访问任意 URL，包括恶意网站。
