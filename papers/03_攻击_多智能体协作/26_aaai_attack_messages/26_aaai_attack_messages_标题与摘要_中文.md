# 攻击消息，而非智能体：面向 LLM-MAS 的多轮自适应隐蔽篡改框架

**原标题：**Attack the Messages, Not the Agents: A Multi-round Adaptive Stealthy Tampering Framework for LLM-MAS  
**攻击框架：**MAST（Multi-round Adaptive Stealthy Tampering，多轮自适应隐蔽篡改）  
**年份与会议：**2026，AAAI。  
**原文：**[本地 PDF](./26_aaai_attack_messages.pdf)。

## 摘要

基于大语言模型的多智能体系统（large language model-based multi-agent systems，LLM-MAS）通过智能体之间的通信有效完成复杂且动态的任务，但对通信的依赖也引入了严重的安全漏洞。现有针对 LLM-MAS 的攻击方法要么破坏智能体内部，要么依赖直接且明显的说服，这限制了攻击的有效性、适应性和隐蔽性。

本文提出 MAST，一个旨在利用系统通信漏洞的多轮自适应隐蔽篡改框架。MAST 将蒙特卡洛树搜索（Monte Carlo Tree Search，MCTS）与直接偏好优化（Direct Preference Optimization，DPO）相结合，训练攻击策略模型，使其能够自适应地生成有效的多轮篡改策略。

此外，为保持隐蔽性，我们在篡改过程中施加语义相似性和嵌入相似性双重约束。在多种任务、通信架构和大语言模型上的全面实验表明，与基线方法相比，MAST 能够持续取得较高的攻击成功率，同时显著提升隐蔽性。

这些结果凸显了 MAST 的有效性、隐蔽性和适应性，也表明 LLM-MAS 亟需稳健的通信安全防护措施。
