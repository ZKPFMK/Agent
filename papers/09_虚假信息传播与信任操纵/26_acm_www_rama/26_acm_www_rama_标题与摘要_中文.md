# RAMA：用于多模态事实核查的检索增强多智能体错误信息检测框架

**原标题：**RAMA: Retrieval-Augmented Multi-Agent Framework for Misinformation Detection in Multimodal Fact-Checking  
**作者：**Shuo Yang；Zijian Yu；Zhenzhe Ying；Yuqin Dai；Guoqing Wang；Jun Lan；Jinfeng Xu；Jinze Li；Edith C. H. Ngai  
**年份与会议/期刊：**2026，Companion Proceedings of the ACM Web Conference 2026（WWW Companion）  
**本地 PDF：**[本地 PDF](./26_acm_www_rama.pdf)  
**原文链接：**<https://doi.org/10.1145/3774905.3796483>；<https://arxiv.org/abs/2507.09174>  
**版本说明：**本文使用 arXiv 公开版本；Crossref 已确认正式版本 DOI 为 10.1145/3774905.3796483。  

## 摘要或内容概述

本文提出 RAMA，一个利用检索增强和多 Agent 交叉核验来检测多模态错误信息的框架。不同 Agent 负责将图像和文本主张转化为检索查询、比较多来源证据并执行事实核查，再通过多模型 ensemble 汇总最终判断。实验表明，RAMA 在多模态错误信息基准上具有较好的检测性能。

## 研究问题

如何结合多模态检索、跨来源证据聚合和多 Agent ensemble，提高错误信息事实核查的可靠性？

## 方法

使用战略查询生成、权威来源交叉核验、证据聚合和多模型多提示 ensemble，分别处理图像、文本及其联合主张。

## 主要发现

检索增强和交叉核验扩大了证据覆盖，多 Agent 与多模型互补能够提升检测稳健性。

## 研究意义

提供攻击论文之外的检测侧基线，可用于评估证据投毒和传播攻击的可检测性。
