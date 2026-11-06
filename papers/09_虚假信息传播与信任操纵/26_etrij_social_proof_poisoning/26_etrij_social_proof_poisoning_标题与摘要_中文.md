# LLM 多智能体社会中的数据投毒：社会证明驱动金融协商中的集体决策失败

**原标题：**Data poisoning in LLM multiagent societies: Social proof drives collective decision failure in financial deliberation  
**作者：**Jeongsu Park；Yuji Lim；Geonwoo Kim；Taehyeon Yun；Moohong Min  
**年份与会议/期刊：**2026，ETRI Journal，48(5): 783–795  
**本地 PDF：**（未获得公开 PDF）  
**原文链接：**<https://doi.org/10.4218/etrij.2026-0186>  
**版本说明：**官方 PDF 地址已核对，但 Wiley 页面和 PDF 在当前环境被 Cloudflare/HTTP 403 拦截；作者 GitHub 仓库公开了实验代码和数据，但未包含论文 PDF。  

## 摘要或内容概述

本文研究单个恶意成员能否先建立声誉，再利用社会证明和伪造数据操纵多智能体金融讨论。实验在七 Agent 的金融协商环境中设置一个恶意 Agent，它依次建立信任、注入伪造数据并制造紧迫感。结果显示，恶意 Agent 仅占 14% 时，集体准确率可从 87.5% 降至 52.5%；公开标记无法追溯到官方记录的主张后，准确率可恢复到 85.8%。

## 研究问题

一个少数恶意 Agent 如何利用声誉、同伴背书和时序策略，把伪造数据转化为群体决策失败？

## 方法

在 Moltbook 金融协商测试床中比较七 Agent 的诚实与数据投毒条件，控制网络拓扑、模型家族和系统级 provenance 标记防御。

## 主要发现

攻击通过社会证明而非提示词注入实现；崩溃具有结构性并跨模型出现，公开标记不可追溯主张能够恢复大部分准确率。

## 研究意义

说明多智能体安全需要系统级来源核验和信任边界，而不能只依赖单 Agent 提示词对齐。
