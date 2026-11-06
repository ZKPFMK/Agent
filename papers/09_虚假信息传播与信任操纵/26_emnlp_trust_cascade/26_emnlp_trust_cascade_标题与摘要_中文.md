# 通过来源抹除形成信任级联：多智能体委托如何破坏单智能体安全

**原标题：**Trust Cascade through Provenance Erasure: How Multi-Agent Delegation Breaks Single-Agent Safety  
**作者：**Yuxin Zhou；Xiao Ding；Tianle Chang；Ye He；Wenbin Zhang；ShangZhan Li；Yijia Meng；Wenyu Zang；Bibo Cai；Qi Shi  
**年份与会议/期刊：**2026，EMNLP  
**本地 PDF：**[本地 PDF](./26_emnlp_trust_cascade.pdf)  
**原文链接：**<https://aclanthology.org/2026.emnlp-main.1005/>  

## 摘要或内容概述

本文研究多智能体自然语言委托过程中，来源、权限和信任元数据如何丢失，并使下游 Agent 将低信任内容当成高信任消息。作者定义来源抹除现象，分析双 Agent 委托中的信任级联，并提出 Trust Boundary Auditor 进行检测。实验显示，格式标记、权限实体和来源归因在委托中可能大量丢失，八种开源模型上的级联攻击成功率为 33%—63%。

## 研究问题

消息在多轮委托和转述中丢失来源、权限与信任元数据后，是否会形成可利用的信任级联？

## 方法

设计双 Agent 及多 Agent 委托任务，追踪来源标记、权限实体和归因在消息传递中的保留率，并评估 Trust Boundary Auditor。

## 主要发现

委托过程会系统性抹除部分信任边界信息，导致下游 Agent 接受低信任内容；审计器能够检测大部分风险。

## 研究意义

把“消息内容安全”扩展到“来源和权限元数据安全”，为多智能体委托链设计审计机制。
