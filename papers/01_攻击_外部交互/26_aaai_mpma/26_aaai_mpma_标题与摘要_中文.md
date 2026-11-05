# MPMA：针对模型上下文协议的偏好操纵攻击

**原标题：**MPMA: Preference Manipulation Attack Against Model Context Protocol  
**攻击方法：**MCP Preference Manipulation Attack（MPMA，MCP 偏好操纵攻击）  
**年份与会议：**2026，AAAI。  
**原文：**[本地 PDF](./26_aaai_mpma.pdf)。

## 摘要

模型上下文协议（Model Context Protocol，MCP）为大语言模型（large language models，LLM）访问外部数据和工具提供了标准化的接口映射，改变了工具选择的范式，并推动了 LLM 智能体工具生态的快速扩张。然而，随着 MCP 得到越来越广泛的采用，第三方定制 MCP 服务器也暴露出潜在的安全漏洞。

本文首先提出一种新的安全威胁，并将其称为 MCP 偏好操纵攻击（MCP Preference Manipulation Attack，MPMA）。攻击者部署定制的 MCP 服务器，操纵大语言模型，使其相较于其他竞争 MCP 服务器优先选择该服务器。这可能为攻击者带来经济收益，例如付费 MCP 服务产生的收入，或免费服务器产生的广告收入。

为实施 MPMA，我们首先设计了直接偏好操纵攻击（Direct Preference Manipulation Attack，DPMA）：将操纵性词语和短语插入工具名称与描述中，从而取得显著的攻击效果。然而，这种直接修改很容易被用户发现，隐蔽性不足。为解决这些局限，我们进一步提出基于遗传算法的广告偏好操纵攻击（Genetic-based Advertising Preference Manipulation Attack，GAPMA）。GAPMA 采用四种常用策略初始化工具描述，并结合遗传算法（Genetic Algorithm，GA）提升攻击的隐蔽性。

实验结果表明，GAPMA 能够在较高攻击有效性与隐蔽性之间取得平衡。我们的研究揭示了开放生态中 MCP 的一个关键漏洞，也表明亟需开发稳健的防御机制，以确保 MCP 生态的公平性。

**代码：** <https://github.com/hanbaoergogo/MPMA>
