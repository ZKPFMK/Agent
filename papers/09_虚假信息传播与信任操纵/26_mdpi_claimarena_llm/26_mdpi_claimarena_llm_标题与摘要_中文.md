# ClaimArena-LLM：审计多智能体 LLM 辩论中虚假因果归因的对抗性传播

**原标题：**ClaimArena-LLM: Auditing Adversarial Propagation of False Causal Attributions in Multi-Agent LLM Debates  
**作者：**Catalin Anghel；Andreea Alexandra Anghel；Antonio Stefan Balau；Marian Viorel Craciun；Adina Cocu；Simona Moldovanu；Cristian Sandu  
**年份与会议/期刊：**2026，Machine Learning and Knowledge Extraction  
**本地 PDF：**[本地 PDF](./26_mdpi_claimarena_llm.pdf)  
**原文链接：**<https://www.mdpi.com/2504-4990/8/10/327>  

## 摘要或内容概述

本文构建多智能体辩论环境，审计错误因果命题如何在 Agent 之间传播。作者使用 100 个合成因果事件，比较对抗性辩论和全诚实辩论，追踪错误因果主张、证据引用、来源谱系和最终审计结果。实验发现，攻击者可以维持预设的错误目标；错误目标对调查者和最终审计者的影响具有角色差异，最终 LLM 审计器也可能被上游污染。

## 研究问题

错误因果归因如何通过多智能体辩论传播，并污染最终的 LLM 审计器？

## 方法

构建 100 个合成因果事件和 investigator、honest analyst、adversarial analyst、auditor 四类角色，进行对抗与全诚实条件下的 1,460 次验证运行。

## 主要发现

对抗分析者维持预设错误目标的平均忠实度为 97.6%；对抗暴露提高调查者和审计者对错误目标的归因，且最终审计器不能被视为独立安全屏障。

## 研究意义

把因果正确性、传播、语义来源和最终审计分开评估，为多 Agent 辩论的过程级审计提供指标。
