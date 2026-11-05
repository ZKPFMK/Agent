# 传染式越狱捣乱者让诚实城镇陷入混乱

**原标题：**A Troublemaker with Contagious Jailbreak Makes Chaos in Honest Towns  
**攻击方法：**Adversarial Replication Contagious Jailbreak（ARCJ，对抗性复制传染式越狱）  
**评测任务：**Troublemaker Makes Chaos in Honest Town（TMCHT）  
**年份与会议：**2025，ACL（第 63 届年会，长论文）。  
**原文：**[本地 PDF](./25_acl_contagious_jailbreak.pdf)。

## 摘要

随着大语言模型的发展，它们被广泛用作各个领域的智能体。记忆是智能体的关键组成部分，用于存储重要信息，但也容易受到越狱攻击。现有研究主要关注单智能体攻击和共享记忆攻击，而现实场景通常使用彼此独立的记忆。

本文提出 Troublemaker Makes Chaos in Honest Town（TMCHT）任务，这是一个大规模、多智能体、多拓扑结构的文本攻击评测框架。TMCHT 让一个攻击者智能体尝试误导整个智能体社会。我们识别出多智能体攻击面临的两项主要挑战：（1）非完全图结构；（2）大规模系统。我们将这些挑战归因于一种称为“毒性消失”（toxicity disappearing）的现象。

为应对这些问题，我们提出对抗性复制传染式越狱（Adversarial Replication Contagious Jailbreak，ARCJ）方法。该方法优化检索后缀，使投毒样本更容易被检索；同时优化复制后缀，使投毒样本具备传染能力。

我们在 TMCHT 中证明了该方法的优越性：在线形拓扑、星形拓扑和 100 智能体设置下，性能分别提升 23.51%、18.95% 和 52.93%。研究结果揭示了广泛使用的多智能体架构中潜在的传染风险。
