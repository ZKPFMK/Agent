# DemonAgent：针对基于大语言模型智能体的动态加密多后门植入攻击

**原标题：**DemonAgent: Dynamically Encrypted Multi-Backdoor Implantation Attack on LLM-based Agent  
**攻击方法：**Dynamically Encrypted Multi-Backdoor Implantation Attack（动态加密多后门植入攻击）  
**年份与会议：**2025，Findings of EMNLP。  
**原文：**[本地 PDF](./25_emnlp(findings)_demonagent.pdf)。

## 摘要

随着基于大语言模型（large language model，LLM）的智能体越来越普及，植入用户查询或环境反馈中的触发器可能激活隐藏后门，引发人们对智能体安全漏洞的严重担忧。然而，传统后门攻击通常能够被分析智能体推理过程的安全审计检测出来，从而限制了智能体安全研究的进一步发展。

为此，我们提出一种新型后门植入策略，称为动态加密多后门植入攻击（Dynamically Encrypted Multi-Backdoor Implantation Attack）。具体而言，我们引入动态加密机制，将后门映射为良性内容，从而有效绕过安全审计。为了增强隐蔽性，我们进一步将后门分解为多个子后门片段。基于这些改进，后门能够显著绕过安全审计。

此外，我们提出 AgentBackdoorEval，这是一个用于全面评估智能体后门攻击的数据集。在多个数据集上的实验结果表明，我们的方法在保持 0% 检测率的同时，攻击成功率接近 100%，展示了其规避安全审计的有效性。我们的研究揭示了现有安全机制在检测高级攻击方面的局限性，凸显了开发更强大防御措施以应对后门威胁的迫切需求。

**代码与数据：** <https://github.com/whfeLingYu/DemonAgent>
