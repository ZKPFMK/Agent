# 别再执着于提示词：面向大语言模型智能体红队测试的推理劫持与约束收紧

**原标题：**Stop Fixating on Prompts: Reasoning Hijacking and Constraint Tightening for Red-Teaming LLM Agents  
**攻击框架：**JailAgent  
**年份与会议：**2026，ACL（第 64 届年会，长论文）。  
**原文：**[本地 PDF](./26_acl_stop_fixating_prompts.pdf)。

## 摘要

随着基于大语言模型（large language model，LLM）的智能体在各个领域得到广泛应用，其复杂性也带来了新的安全威胁。现有红队测试方法大多依赖修改用户提示词，因而难以适应新的数据，并且可能影响智能体的性能。

为应对这一挑战，本文提出 JailAgent 框架，完全避免修改用户提示词。具体而言，JailAgent 通过三个关键阶段，隐式操纵智能体的推理轨迹和记忆检索：触发器提取（Trigger Extraction）、推理劫持（Reasoning Hijacking）和约束收紧（Constraint Tightening）。

借助精确的触发器识别、实时自适应机制和优化后的目标函数，JailAgent 在跨模型和跨场景环境中展现出优异性能。
