# 当真相分散时：错误信息如何使基于 LLM 的多智能体系统偏离集体事实恢复

**原标题：**When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems  
**作者：**Chenfei Yan；Zeyang Yue；Feifei Zhao；Erliang Lin；Lu Jia；Haibo Tong；Mingyang Lyu；Chengyi Sun；Yi Zeng  
**年份与会议/期刊：**2026，arXiv 预印本  
**本地 PDF：**[本地 PDF](./26_arxiv(preprint)_when_truth_distributed.pdf)  
**原文链接：**<https://arxiv.org/abs/2608.03421>  
**版本说明：**使用 arXiv 公开预印本版本。  

## 摘要或内容概述

本文研究事实分散在不同 Agent 的局部观察中时，一个关键证据持有者的虚假证词如何影响集体事实恢复。作者提出 ForesightSafety-TIDE，在 120 个五 Agent 物体移动环境中配对比较全诚实协作与单个关键证据持有者欺骗，追踪多阶段投票、证词采纳和证据根谱系。实验显示，聚合事实恢复率从 72.50% 降至 14.17%；恶意 Agent 离开后，错误证词仍可能继续传播。

## 研究问题

当完整事实分散在多个 Agent 的局部观察中时，关键 Agent 的虚假证词会如何影响集体事实恢复？

## 方法

构建局部观察共同决定唯一终点的五 Agent 环境，配对比较诚实和欺骗条件，分析投票、证词采纳与证据根谱系。

## 主要发现

单个关键证据持有者的欺骗显著降低事实恢复率，虚假证词有时比真实证词更容易被采纳，并可在恶意 Agent 离开后残留。

## 研究意义

揭示分布式事实聚合中的关键证据节点风险，为证词权重、证据根和退出后的清理机制提供依据。
