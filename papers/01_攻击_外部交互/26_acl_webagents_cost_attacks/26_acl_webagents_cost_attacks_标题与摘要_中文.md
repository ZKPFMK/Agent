# 当效率成为漏洞：针对 WebAgent 的计算成本攻击

**原标题：**When Efficiency Becomes a Vulnerability: Computational Cost Attacks on WebAgents  
**攻击方法：**Computational Cost Attack（CCA，计算成本攻击）；CostBomb  
**年份与会议：**2026，ACL（第 64 届年会，长论文）。  
**原文：**[本地 PDF](./26_acl_webagents_cost_attacks.pdf)。

## 摘要

WebAgent 已展现出自主完成复杂网页任务的强大能力，但其计算效率方面的漏洞却很少受到关注。攻击者可以向网页中注入恶意提示词，诱使 WebAgent 生成不必要的长篇推理过程并承担过高的计算成本；我们将这种攻击称为计算成本攻击（Computational Cost Attack，CCA）。

为了在现实的黑盒环境中系统研究这一漏洞，本文提出 CostBomb，一种“生成—选择”式攻击框架。该框架利用大语言模型生成多样化的对抗性提示词，并使用强化学习增强的选择器识别最有效的扰动。

在多个真实世界网页基准上的大量实验表明，现有 WebAgent 很容易受到 CCA 攻击：在不影响任务成功完成的情况下，其计算成本会大幅增加。我们的研究揭示了 WebAgent 鲁棒性中一个被忽视的维度，并强调了开发具备效率感知能力的防御措施的迫切需求。
