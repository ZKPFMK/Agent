# VPI-Bench：面向计算机使用智能体的视觉提示词注入攻击

**原标题：**VPI-BENCH: VISUAL PROMPT INJECTION ATTACKS FOR COMPUTER-USE AGENTS  
**攻击方法：**Visual Prompt Injection（VPI，视觉提示词注入）  
**年份与会议：**2026，ICLR。  
**原文：**[本地 PDF](./26_iclr_vpi_bench.pdf)。

## 摘要

拥有完整系统访问权限的计算机使用智能体（Computer-Use Agents，CUA）能够实现强大的任务自动化，但由于可以操纵文件、访问用户数据和执行任意命令，也带来了重大的安全与隐私风险。以往研究主要关注基于浏览器的智能体和 HTML 层面的攻击，而 CUA 的漏洞仍未得到充分研究。

本文提出了一个端到端的威胁模型：在黑盒场景下，视觉提示词注入（Visual Prompt Injection，VPI）操纵 CUA 执行未经授权的操作或泄露敏感信息，从而覆盖从注入到造成危害的完整攻击链。随后，我们提出 VPI-Bench，这是一个包含 306 个测试用例的基准，覆盖五个广泛使用的平台，用于评估智能体在 VPI 威胁下的鲁棒性。

每个测试用例都是某个网页平台的变体，具备交互性，部署在真实环境中，并包含以视觉方式嵌入的恶意提示词。实证研究表明，在某些平台上，当前 CUA 和浏览器使用智能体（Browser-Use Agents，BUA）分别可能以最高 51% 和 100% 的比例受到欺骗。实验结果还表明，现有防御方法只能带来有限改善。这些发现凸显了开发稳健且具备上下文感知能力的防御措施的必要性，以确保多模态 AI 智能体能够在现实环境中安全部署。

**代码与演示：** <https://github.com/cua-framework/agents>  
**数据集：** <https://huggingface.co/datasets/VPI-Bench/vpi-bench>
