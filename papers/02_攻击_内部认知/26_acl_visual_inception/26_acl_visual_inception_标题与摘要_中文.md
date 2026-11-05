# Visual Inception：通过多模态记忆投毒破坏智能体推荐系统的长期规划

**原标题：**Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning  
**攻击方法：**Visual Inception（视觉入侵）；防御框架：COGNITIVEGUARD  
**年份与会议：**2026，ACL（第 64 届年会，长论文）。  
**原文：**[本地 PDF](./26_acl_visual_inception.pdf)。

## 摘要

从静态排序模型发展到智能体推荐系统（Agentic Recommender Systems，Agentic RecSys），使 AI 智能体能够维护长期用户画像，并自主规划服务任务。尽管这一范式转变提升了个性化能力，却也引入了一个漏洞：系统对长期记忆（Long-term Memory，LTM）的依赖。

本文揭示了一种名为“Visual Inception”的威胁。不同于旨在立即造成误分类的传统对抗性攻击，Visual Inception 将触发器注入用户上传的图像（例如生活方式照片），使其成为系统记忆中的“休眠智能体”。当这些遭到投毒的记忆在未来规划过程中被检索出来时，就会劫持智能体的推理链，在没有提示词注入的情况下，将其引导至攻击者设定的目标（例如推广高利润产品）。

为缓解这一威胁，我们提出 COGNITIVEGUARD，一种受人类认知启发的双过程防御框架。该框架包括用于清理感知输入的系统 1 感知净化器（基于扩散模型的净化），以及用于检测记忆驱动规划异常的系统 2 推理验证器（反事实一致性检查）。

在模拟电子商务智能体环境中的大量实验表明，Visual Inception 的目标命中率（Goal-Hit Rate，GHR）约为 85%；COGNITIVEGUARD 可将这一风险降至约 10%，并提供可配置的延迟权衡：轻量模式约为 1.5 秒，完整顺序验证约为 6.5 秒。在本文设置下，该防御不会造成质量下降。延迟统计采用单独核算方式：查询时开销不包括一次性的上传时预处理。
