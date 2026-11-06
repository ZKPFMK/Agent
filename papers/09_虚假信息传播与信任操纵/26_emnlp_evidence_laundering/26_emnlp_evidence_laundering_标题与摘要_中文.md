# 证据洗白：深度研究 Agent 将相关来源误认为独立证据

**原标题：**Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence  
**作者：**Ruihua Zhou；Hao Huang；Yijie Zheng；JiaTang Luo；Yunpeng Li；Yuling Liu；Dan Du  
**年份与会议/期刊：**2026，EMNLP  
**本地 PDF：**[本地 PDF](./26_emnlp_evidence_laundering.pdf)  
**原文链接：**<https://aclanthology.org/2026.emnlp-main.509/>  

## 摘要或内容概述

本文研究深度研究 Agent 是否会把多个相关、重复或改写的来源误认为彼此独立的证据。作者将同一虚假主张发布到多个改写网页，构造单来源、相关来源簇和表面独立来源等场景，并控制 Agent 对这些来源的检索曝光。结果表明，Agent 可能给经过“洗白”的相关来源簇赋予接近真正独立来源的可信度；结构化的来源溯源门控可以降低这一问题。

## 研究问题

深度研究 Agent 能否识别来源之间的相关性，还是会把重复信息误判为独立证据？

## 方法

构造共享同一虚假主张的改写网页和来源簇，比较单来源、相关来源和表面独立来源下的检索、证据聚合与最终判断。

## 主要发现

相关或复制来源常被误认为相互独立，来源溯源门控能够降低证据洗白造成的置信度膨胀。

## 研究意义

揭示多来源一致性假设的脆弱性，为深度研究 Agent 增加 provenance 检查提供依据。
