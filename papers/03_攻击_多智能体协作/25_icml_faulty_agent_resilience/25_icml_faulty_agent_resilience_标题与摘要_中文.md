# 含故障智能体的大语言模型多智能体协作的韧性

**原标题：**On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents  
**故障模拟方法：**AUTOTRANSFORM、AUTOINJECT  
**防御机制：**Challenger、Inspector  
**年份与会议：**2025，ICML。  
**原文：**[本地 PDF](./25_icml_faulty_agent_resilience.pdf)。

## 摘要

基于大语言模型的多智能体系统通过让各自专注于特定领域的专家智能体进行协作，在各种任务中展现出强大能力。然而，笨拙甚至恶意的智能体——即在任务中频繁出错的智能体——对系统整体性能的影响仍未得到充分研究。

本文研究两个问题：（1）在不同下游任务中，面对故障智能体时，各种系统结构（例如 A→B→C 和 A↔B↔C）具有怎样的韧性？（2）如何提升系统韧性，以抵御这些智能体？

为模拟故障智能体，我们提出两种方法——AUTOTRANSFORM 和 AUTOINJECT，分别向智能体响应中引入错误。在四个下游任务和六个系统上的实验表明，“层次化”结构 A→(B↔C) 展现出更强的韧性，性能下降仅为 5.5%，而另外两种结构的性能下降分别为 10.5% 和 23.7%。

为进一步提升韧性，我们提出：（1）Challenger，在每个智能体中引入质疑其他智能体输出的机制；（2）Inspector，增加一个用于审查和纠正消息的智能体。Inspector 最多能够恢复故障智能体造成的 96.4% 错误。

**代码与数据：** <https://github.com/CUHK-ARISE/MAS-Resilience>
