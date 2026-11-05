# 针对基于大语言模型的多智能体系统的知识产权泄露攻击

**原标题：**IP Leakage Attacks Targeting LLM-Based Multi-Agent Systems  
**攻击方法：**MASLEAK  
**年份与发布形式：**2025，arXiv 预印本。  
**原文：**[本地 PDF](./25_arxiv(preprint)_ip_leakage.pdf)。

## 摘要

大语言模型（large language models，LLM）的快速发展推动了多智能体系统（Multi-Agent Systems，MAS）的出现，使其能够通过协作完成复杂任务。然而，MAS 的架构及智能体之间的交互十分复杂，也引发了人们对知识产权（intellectual property，IP）保护的重大担忧。

本文提出 MASLEAK，一种用于从 MAS 应用中提取敏感信息的新型攻击框架。MASLEAK 针对一种现实的黑盒场景：攻击者事先不了解 MAS 的架构或智能体配置，只能通过公开 API 与 MAS 交互，提交攻击查询 q，并观察最终智能体的输出。

受计算机蠕虫传播并感染易受攻击网络主机的方式启发，MASLEAK 精心构造对抗性查询 q，诱导、传播并保留来自每个 MAS 智能体的响应，从而泄露一整套专有组件，包括智能体数量、系统拓扑、系统提示词、任务指令和工具使用情况。

我们构建了首个包含 810 个应用的 MAS 应用合成数据集，并在包括 Coze 和 CrewAI 在内的现实 MAS 应用上评估 MASLEAK。结果表明，MASLEAK 能够高效提取 MAS 的知识产权：在大多数情况下，系统提示词和任务指令的平均攻击成功率达到 87%，系统架构的平均攻击成功率达到 92%。最后，我们讨论了研究发现的影响及潜在防御方法。
