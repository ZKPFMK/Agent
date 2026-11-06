# Evo-Attacker：面向大语言模型多智能体系统长期工具攻击的记忆增强强化学习

**原标题：**Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS  
**攻击方法：**Evo-Attacker；Attack-Flow GRPO  
**年份与会议：**2026，ACL。  
**原文：**[本地 PDF](./26_acl_evo_attacker.pdf)。

## 摘要

基于大语言模型的多智能体系统（LLM-MAS）通过编排专业化智能体和外部工具，在解决复杂任务方面展现出卓越能力，但对工具输出的隐式信任也形成了关键攻击面。现有工具攻击受到领域特异性或固定静态模板的限制。

为应对这些挑战，我们提出 Evo-Attacker，将工具攻击建模为一个自我演化、记忆增强的强化学习过程。Evo-Attacker 构建动态攻击记忆，并通过审慎推理检索对抗模式，在关键时刻制定并执行修改干预策略。

此外，我们提出 Attack-Flow GRPO，利用终端结果优化中间推理步骤，从而应对长期交互中的信用分配难题。全面实验表明，Evo-Attacker 持续优于基线方法，展现出良好的泛化和演化能力，也凸显了开发工具安全防护措施的迫切需求。
