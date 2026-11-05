# AgentDojo：用于评测大语言模型智能体提示词注入攻击与防御的动态环境

**原标题：**AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents  
**年份与会议：**2024，NeurIPS（Datasets and Benchmarks Track）。  
**原文：**[本地 PDF](./24_neurips(datasets-benchmarks)_agentdojo.pdf)。

## 摘要

AI 智能体旨在将基于文本的推理与外部工具调用相结合，以解决复杂任务。然而，AI 智能体容易受到提示词注入攻击：外部工具返回的数据可能劫持智能体，诱使其执行恶意任务。为衡量 AI 智能体的对抗鲁棒性（adversarial robustness），我们提出 AgentDojo，这是一个面向使用工具处理不可信数据的智能体的评测框架。

为适应攻击与防御不断演进的特点，AgentDojo 被设计为一个可扩展的环境，用于设计和评测新的智能体任务、防御方法以及自适应攻击（adaptive attacks），而非一套静态测试集。我们在该环境中设置了 97 个贴近实际的任务（例如管理邮件客户端、浏览网上银行网站或进行旅行预订）、629 个安全测试用例，以及文献中的多种攻击与防御范式。

我们发现，AgentDojo 对攻击与防御双方都构成了挑战：最先进的大语言模型即使在没有攻击的情况下，也无法完成许多任务；现有提示词注入攻击能够破坏部分安全属性，但无法破坏全部安全属性。我们希望 AgentDojo 能够推动对 AI 智能体新设计原则的研究，使其能够可靠且稳健地完成常见任务。

**项目主页：** <https://agentdojo.spylab.ai>
