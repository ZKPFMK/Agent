# 逐步欺骗：使用 LLM Agent 模拟从真实新闻到虚假新闻的演化

**原标题：**The Stepwise Deception: Simulating the Evolution from True News to Fake News with LLM Agents  
**作者：**Yuhan Liu；Zirui Song；Juntian Zhang；Xiaoqing Zhang；Xiuying Chen；Rui Yan  
**年份与会议/期刊：**2025，EMNLP  
**本地 PDF：**[本地 PDF](./25_emnlp_stepwise_deception_fuse.pdf)  
**原文链接：**<https://aclanthology.org/2025.emnlp-main.1330/>  

## 摘要或内容概述

本文模拟真实新闻在多轮传播和转述中逐步变成虚假新闻的过程。作者提出 FUSE，设置传播者、评论者、核验者和旁观者四类 Agent，并通过 FUSE-EVAL 从语言和语义维度测量真实性偏移。研究能够重现信息逐步失真的过程，并指出越早介入传播链，越有可能阻止错误信息继续演化。

## 研究问题

真实新闻如何在多轮转述、评论和核验中逐步演化为虚假新闻？

## 方法

构建包含 spreader、commentator、verifier 和 bystander 的多角色传播环境，配合层级记忆和 FUSE-EVAL 追踪语言与语义失真。

## 主要发现

内容会在多轮传播中产生累积性失真；较早的核验和干预比晚期纠正更有效。

## 研究意义

把错误信息传播建模为连续演化过程，为研究消息篡改和纠正时机提供了实验框架。
