# Agent Smith：一张图像即可指数级快速越狱一百万个多模态大语言模型智能体

**原标题：**Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast  
**攻击方法：**Infectious Jailbreak（传染式越狱）  
**年份与会议：**2024，ICML。  
**原文：**[本地 PDF](./24_icml_agent_smith.pdf)。

## 摘要

多模态大语言模型（multimodal large language model，MLLM）智能体可以接收指令、捕获图像、从记忆中检索历史信息，并决定使用哪些工具。然而，红队测试工作已经表明，对抗性图像或提示词能够使 MLLM 越狱并产生不符合安全要求的行为。

在本文中，我们揭示了多智能体环境中一个更加严重的安全问题，并将其称为传染式越狱（infectious jailbreak）。攻击者只需使单个智能体越狱，无需进一步干预，几乎所有智能体就会以指数速度受到感染并表现出有害行为。

为验证传染式越狱的可行性，我们模拟了包含最多一百万个 LLaVA-1.5 智能体的多智能体环境，并采用随机两两聊天作为多智能体交互的概念验证实例。结果表明，只需将一张具有传染性的对抗图像输入任意随机选中的智能体的记忆中，就足以实现传染式越狱。

最后，我们推导出一个简单原则，用于判断某种防御机制能否从理论上抑制传染式越狱的传播；但如何设计满足这一原则的实用防御方案，仍有待进一步研究。

**代码：** <https://github.com/sail-sg/Agent-Smith>
