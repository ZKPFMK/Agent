# Imprompter：诱骗大语言模型智能体不当使用工具

**原标题：**Imprompter: Tricking LLM Agents into Improper Tool Use  
**攻击方法：**Imprompter  
**年份与发布形式：**2024，arXiv 预印本。  
**原文：**[本地 PDF](./24_arxiv(preprint)_imprompter.pdf)。

## 摘要

大语言模型（Large Language Model，LLM）智能体是一种新兴的计算范式，将生成式机器学习与代码解释器、网页浏览、电子邮件以及更广泛的外部资源等工具相结合。这类基于智能体的系统代表了个人计算的发展方向。本文为基于智能体的系统奠定安全基础，并揭示了一类新的、可自动生成的混淆对抗提示词攻击。这类攻击会破坏与大语言模型智能体连接的用户资源的机密性与完整性。

我们展示了如何利用提示词优化技术，在已知模型权重的情况下自动找到这类提示词，并证明这些攻击能够迁移到生产级智能体。例如，我们针对 Mistral 的 LeChat 智能体实现了一种信息外泄攻击：该攻击分析用户的对话，提取其中的个人可识别信息（personally identifiable information，PII），并将其格式化为有效的 Markdown 命令，最终把这些数据泄露到攻击者的服务器。在端到端评测中，该攻击的成功率接近 80%。

我们开展了一系列实验来刻画这类攻击的有效性，发现它们能够稳定地攻击 Mistral 的 LeChat、ChatGLM 和 Meta 的 Llama 等新兴智能体系统。这些攻击支持多模态场景；我们分别展示了文本-only 和图像领域中的攻击变体。真实产品上的代码和演示视频见：<https://imprompter.ai>。
