# 谁是内鬼？大语言模型多智能体系统中隐藏意图的恶意智能体建模与检测

**原标题：**Who’s the Mole? Modeling and Detecting Intention-Hiding Malicious Agents in LLM-Based Multi-Agent Systems  
**攻击范式：**隐藏意图攻击（Intention-Hiding Attacks）  
**检测框架：**AgentXposed  
**年份与发布形式：**2025，arXiv 预印本。  
**原文：**[本地 PDF](./25_arxiv(preprint)_whos_the_mole.pdf)。

## 摘要

由大语言模型驱动的多智能体系统（LLM-based Multi-Agent Systems，LLM-MAS）在协作解决问题方面展现出卓越能力。然而，部署这类系统也会引入新的安全风险。现有关于基于 LLM 智能体的研究主要考察单智能体场景，而多智能体系统的安全性仍在很大程度上未得到研究。

为弥补这一空白，我们系统研究了 LLM-MAS 中的隐藏意图威胁。我们设计了四种具有代表性的攻击范式，在保持高度隐蔽性的同时，悄然破坏任务完成效果，并在集中式、去中心化和分层通信结构下对其进行评估。

实验结果表明，这些攻击具有很强的破坏性，并且能够轻易规避现有防御机制。为应对这些威胁，我们提出 AgentXposed，一种受心理学启发的检测框架。AgentXposed 基于 HEXACO 人格模型，通过心理特质维度刻画智能体，并借鉴 Reid 审讯技术这一用于诱导隐藏意图的结构化方法。

通过结合渐进式问卷探测和基于行为的智能体间监控，该框架能够在恶意行为发生之前主动识别恶意智能体。在六个数据集上，针对本文提出的攻击和两种基线威胁开展的大量实验表明，AgentXposed 能够有效检测多种形式的恶意行为，并在多种通信设置下保持较强鲁棒性。
