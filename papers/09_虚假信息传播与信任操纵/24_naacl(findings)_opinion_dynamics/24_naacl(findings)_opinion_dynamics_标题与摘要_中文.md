# 使用基于 LLM 的 Agent 网络模拟意见动力学

**原标题：**Simulating Opinion Dynamics with Networks of LLM-based Agents  
**作者：**Yun-Shiuan Chuang；Agam Goyal；Nikunj Harlalka；Siddharth Suresh；Robert Hawkins；Sijia Yang；Dhavan Shah；Junjie Hu；Timothy Rogers  
**年份与会议/期刊：**2024，Findings of NAACL  
**本地 PDF：**[本地 PDF](./24_naacl(findings)_opinion_dynamics.pdf)  
**原文链接：**<https://aclanthology.org/2024.findings-naacl.211/>  

## 摘要或内容概述

本文使用由大语言模型驱动的 Agent 网络模拟意见形成和变化过程，研究网络结构、角色设定和提示词如何影响群体意见。实验发现，LLM Agent 对科学正确答案存在一定的内在偏向；在提示词中加入确认偏差后，系统可以出现意见碎片化。研究说明，Agent 的先验倾向与交互设定会共同改变信息传播结果。

## 研究问题

网络结构、角色设定和确认偏差如何共同影响 LLM Agent 的意见形成与碎片化？

## 方法

构建由 LLM Agent 组成的社会网络，改变 Agent persona、交互网络和提示词中的认知偏差设定，并比较意见分布、共识和碎片化。

## 主要发现

LLM Agent 对事实正确答案有一定趋向，但确认偏差和网络交互可以放大分歧并形成碎片化意见。

## 研究意义

为后续错误信息传播实验提供了没有主动攻击者的意见动力学基线。
