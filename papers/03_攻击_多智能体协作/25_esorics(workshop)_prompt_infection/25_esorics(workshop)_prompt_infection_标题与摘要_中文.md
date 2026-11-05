# Prompt Infection：多智能体系统中的大语言模型间提示词注入

**原标题：**PROMPT INFECTION: LLM-TO-LLM PROMPT INJECTION WITHIN MULTI-AGENT SYSTEMS  
**攻击方法：**Prompt Infection（提示词感染）  
**防御方法：**LLM Tagging  
**年份与发布形式：**2025，ESORICS Workshop。  
**原文：**[本地 PDF](./25_esorics(workshop)_prompt_infection.pdf)。

## 摘要

随着大语言模型（large language models，LLM）日益强大，多智能体系统——即多个 LLM 协作完成复杂任务的系统——正越来越多地应用于现代人工智能应用。然而，大多数安全研究仍然集中于单智能体 LLM 的漏洞，其中包括提示词注入攻击：嵌入外部内容中的恶意提示词会诱骗 LLM 执行非预期或有害操作，从而破坏受害应用。

本文揭示了一种更加危险的攻击向量：多智能体系统中的大语言模型间提示词注入（LLM-to-LLM prompt injection）。我们提出提示词感染（Prompt Infection），一种能够在相互连接的智能体之间自我复制恶意提示词的新型攻击，其行为类似计算机病毒。

该攻击会带来严重威胁，包括数据窃取、诈骗、错误信息传播和系统范围的破坏，并且能够在系统中悄无声息地传播。大量实验表明，即使智能体不公开共享全部通信内容，多智能体系统仍然很容易受到攻击。

为应对这一问题，我们提出 LLM Tagging，一种防御机制。将其与现有安全措施结合后，能够显著缓解感染传播。随着多智能体 LLM 系统得到越来越广泛的采用，这项工作凸显了开发先进安全措施的迫切需求。
