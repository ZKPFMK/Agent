# 良性多智能体系统中的错误信息传播

**原标题：**Misinformation Propagation in Benign Multi-Agent Systems  
**作者：**Jonas Becker；Jan Philip Wahle；Terry Ruas；Bela Gipp  
**年份与会议/期刊：**2026，arXiv 预印本  
**本地 PDF：**[本地 PDF](./26_arxiv(preprint)_benign_mas.pdf)  
**原文链接：**<https://arxiv.org/abs/2606.16710>  
**版本说明：**使用 arXiv 公开预印本版本。  

## 摘要或内容概述

本文研究没有恶意攻击者时，错误信息如何在良性多智能体辩论中持续存在、被纠正或被保留。作者构建 MINT，包含 10,278 条不同风格的 LLM 生成错误信息，在常识推理、知识问答和道德判断任务上评测三个开放权重模型。相关错误段落会使单个 Agent 的准确率下降约 0.12—0.43；当少数 Agent 读到错误信息时，辩论并不总能恢复正确答案。

## 研究问题

在没有恶意 Agent 的情况下，单个 Agent 接触错误上下文如何影响多智能体协作和集体纠错？

## 方法

使用 MINT 错误信息库，在统一协作协议下比较单 Agent、辩论和投票设置，控制错误信息风格、相关性及被误导 Agent 比例。

## 主要发现

相关错误上下文会显著损害单 Agent；少数被误导 Agent 也可能影响集体答案，投票和多数辩论并不保证纠错。

## 研究意义

提供“无主动攻击”基线，说明协作协议本身也可能让错误信息持续传播。
