# MIP against Agent：利用恶意图像补丁劫持多模态操作系统智能体

**原标题：**MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents  
**攻击方法：**Malicious Image Patches（MIPs，恶意图像补丁）  
**年份与会议：**2025，NeurIPS。  
**原文：**[本地 PDF](./25_neurips_mip_against_agent.pdf)。

## 摘要

近年来，操作系统（operating system，OS）智能体取得了快速发展，使视觉语言模型（vision-language models，VLM）能够直接控制用户的计算机。传统 VLM 通常被动输出文本，而 OS 智能体则能够根据单条用户提示自主执行计算机任务。OS 智能体通过捕获、解析和分析屏幕截图，并借助应用程序编程接口（application programming interfaces，API）执行鼠标点击、键盘输入等底层操作。由于能够直接与操作系统交互，OS 智能体的故障或遭到操纵可能立即造成切实后果。

在本文中，我们揭示了针对这类 OS 智能体的一种新型攻击向量：恶意图像补丁（Malicious Image Patches，MIPs）。MIP 是经过对抗性扰动的屏幕区域；当 OS 智能体捕获这些区域时，攻击者可以利用特定 API 诱使智能体执行有害操作。例如，攻击者可以将 MIP 嵌入桌面壁纸或发布在社交媒体上，诱使 OS 智能体外泄用户的敏感数据。

我们证明，MIP 能够跨越不同的用户提示和屏幕配置发挥作用，并且即使 OS 智能体正在执行良性指令，也能劫持多个不同的 OS 智能体。这些发现揭示了 OS 智能体中的严重安全漏洞；在这类系统广泛部署之前，必须谨慎解决这些问题。
