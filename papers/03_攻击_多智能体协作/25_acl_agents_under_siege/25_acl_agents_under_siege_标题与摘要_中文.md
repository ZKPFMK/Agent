# Agents Under Siege：利用优化提示词攻击破解实用型多智能体大语言模型系统

**原标题：**Agents Under Siege: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks  
**攻击方法：**Permutation-Invariant Adversarial Attack（置换不变对抗攻击）  
**年份与会议：**2025，ACL（第 63 届年会，长论文）。  
**原文：**[本地 PDF](./25_acl_agents_under_siege.pdf)。

## 摘要

关于大语言模型（large language model，LLM）安全性的讨论大多集中于单智能体场景，但多智能体 LLM 系统依赖智能体之间的通信和分布式推理，因此带来了新的对抗风险。

本文创新性地关注具有现实约束的多智能体系统，例如有限的 token 带宽、消息传递延迟和防御机制。我们设计了一种置换不变的对抗攻击，在存在延迟和带宽约束的网络拓扑中优化提示词分布，从而绕过系统内部的分布式安全机制。

我们将攻击路径建模为最大流最小费用问题，并结合新颖的置换不变规避损失（Permutation-Invariant Evasion Loss，PIEL），利用基于图的优化方法，在最大化攻击成功率的同时最小化被检测的风险。

我们在 Llama、Mistral、Gemma、DeepSeek 等多种模型以及 JailBreakBench、AdversarialBench 等数据集上开展评测。结果表明，与传统攻击相比，我们的方法最高可达到 7 倍的攻击效果，揭示了多智能体系统中的关键漏洞。此外，我们证明包括 Llama-Guard 和 PromptGuard 各种变体在内的现有防御无法阻止该攻击，凸显了开发面向多智能体系统的专用安全机制的迫切需求。
