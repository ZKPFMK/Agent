# CORBA：基于大语言模型的多智能体系统中的传染式递归阻塞攻击

**原标题：**CORBA: Contagious Recursive Blocking Attacks on Multi-Agent Systems Based on Large Language Models  
**攻击类型：**Denial-of-Collaboration（DoC，协作拒绝）；COntagious Recursive Blocking Attacks（CORBA，传染式递归阻塞攻击）  
**年份与会议：**2026，Findings of ACL。  
**原文：**[本地 PDF](./26_acl(findings)_corba.pdf)。

## 摘要

基于大语言模型的多智能体系统代表了一种通过智能体协作解决复杂问题的有前景范式。然而，对开放式通信的依赖也暴露出一个根本性漏洞：协作过程本身可能被利用和破坏。

本文将这一类威胁形式化为协作拒绝（Denial-of-Collaboration，DoC）。不同于针对单个节点或服务的拒绝服务（DoS）攻击，DoC 攻击会破坏系统的协作结构，将通信拓扑转变为自我破坏机制，最终造成过度资源消耗和系统瘫痪。

我们提出传染式递归阻塞攻击（COntagious Recursive Blocking Attacks，CORBA）作为 DoC 的具体实例。CORBA 利用看似良性但能够递归传播的指令，迫使 LLM 多智能体系统陷入无意义的消息传递循环。由于攻击在语义上是良性的，因此能够轻易绕过针对行为或系统攻击检测能力不足的传统安全对齐机制。

在多种拓扑结构和模型上的大量实验表明，CORBA 能够实现系统瘫痪，而基线攻击无法做到这一点。我们的工作揭示了当前 LLM 多智能体系统安全中的新型 DoC 威胁，并为开发稳健且具备协作感知能力的防御机制建立了重要基线。

**代码：** <https://github.com/zhrli324/Corba>
