# ObliInjection：面向多源数据大语言模型智能体的顺序无关提示词注入攻击

**原标题：**ObliInjection: Order-Oblivious Prompt Injection Attack to LLM Agents with Multi-source Data  
**攻击方法：**ObliInjection  
**年份与会议：**2026，NDSS Symposium。  
**原文：**[本地 PDF](./26_ndss_obliinjection.pdf)。

## 摘要

提示词注入攻击旨在污染大语言模型的输入数据，诱导其完成攻击者选择的任务，而不是预期任务。在许多应用和智能体中，输入数据来自多个来源，每个来源贡献整体输入中的一个片段。在这类多源场景中，攻击者可能只能控制部分来源并污染相应片段，同时通常不知道这些片段在输入中的排列顺序。现有提示词注入攻击要么假设全部输入数据来自攻击者控制的单一来源，要么忽略不同来源片段排列顺序的不确定性。因此，在涉及多源数据的领域中，这些攻击的成功率受到限制。

本文提出 ObliInjection，这是首个针对具有多源输入数据的大语言模型应用和智能体的提示词注入攻击。ObliInjection 引入了两项关键技术创新：顺序无关损失（order-oblivious loss），用于量化无论干净片段和受污染片段如何排列，大语言模型完成攻击者选择任务的可能性；以及 orderGCG 算法，该算法专门用于最小化顺序无关损失并优化受污染片段。

在覆盖不同应用领域的三个数据集和十二个大语言模型上开展的全面实验表明，即使输入数据的 6—100 个片段中只有一个片段遭到污染，ObliInjection 仍然非常有效。

**代码与数据：** <https://github.com/ReachalWang/ObliInjection>
