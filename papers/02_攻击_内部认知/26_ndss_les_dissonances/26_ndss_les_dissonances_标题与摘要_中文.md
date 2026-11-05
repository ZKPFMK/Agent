# Les Dissonances：工具池赋能大语言模型智能体中的跨工具窃取与污染

**原标题：**Les Dissonances: Cross-Tool Harvesting and Polluting in Pool-of-Tools Empowered LLM Agents  
**攻击方法：**Cross-Tool Harvesting and Polluting（XTHP，跨工具窃取与污染）  
**扫描工具：**Chord  
**年份与会议：**2026，NDSS Symposium。  
**原文：**[本地 PDF](./26_ndss_les_dissonances.pdf)。

## 摘要

大语言模型（large language model，LLM）智能体是由 LLM 驱动的自主系统，能够借助一组工具进行推理和规划以解决问题。然而，在 LLM 智能体中集成多个工具，也带来了安全管理工具、确保工具兼容性、处理依赖关系以及保护智能体任务工作流控制流等方面的挑战。

本文首次对多工具 LLM 智能体中的任务控制流开展系统性安全分析。我们发现了一种新型威胁——跨工具窃取与污染（Cross-Tool Harvesting and Polluting，XTHP）。该威胁包含多个攻击向量，攻击者可以先劫持智能体任务的正常控制流，再收集并污染 LLM 智能体系统中的机密或私人信息。

为了解这一威胁的影响，我们开发了 Chord，一种动态扫描工具，能够自动检测现实世界中容易受到 XTHP 攻击的智能体工具。我们评估了来自两个主流 LLM 智能体开发框架 LangChain 和 Llama-Index 的 66 个真实工具，结果发现其中 75% 容易受到 XTHP 攻击，凸显了这一威胁的普遍性。
