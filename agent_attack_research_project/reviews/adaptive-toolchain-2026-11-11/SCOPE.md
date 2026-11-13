# 自适应工具链构想：本轮调研边界

日期：2026-11-11。用户请求：使用 auto research 调研《自适应工具链与Agent行为扩展_研究构想.md》。本轮任务为文献核查、近邻对比和研究设计。

## 输入与来源

- 用户原稿：`/Users/dj/Documents/paper/Agent/papers/10_MCP攻击/自适应工具链与Agent行为扩展_研究构想.md`。
- 原稿 SHA-256：`63ca1233a225b6ea87ed6ed07857c4c7568bcdd4de593089a830f4df233f413c`。
- 项目：`/Users/dj/Documents/paper/Agent/agent_attack_research_project`；已按顺序读取 `STATE.md`、`ATTACK-RESEARCH.md`、`RESEARCH-GRAPH.md` 和 `progress.md`，并检查现有定位/文献/决策。
- 自动研究入口：`/Users/dj/.claude/skills/agent-attack-research/SKILL.md`；按 R0/R1/R4 的有界节点执行。本次没有启动定时循环。
- 原稿和外部论文语料保持只读；报告及各节点材料均留在本项目。

## 有界问题

初始问题是：在攻击者只能一次控制一份外部内容、看不到具体工具注册表及执行中间结果的条件下，既有工作是否已经覆盖受害 Agent 自行将高层越权目标映射为多工具行动，并在工具不可用时选择替代路径？该问题的宽泛新攻击定位已被收窄。

用户进一步明确其提到的 A11 是《When MCP Servers Attack》中的 **A11 Prompt Logic Attack**。因此新增并优先区分两个问题：

1. **A11 原义**：用户选择 MCP Prompt 后，Prompt handler 是否在 MCP Server 运行环境中执行预先写入的恶意代码；该阶段不一定需要 LLM。
2. **Agent 代码执行链**：外部内容是否导致目标/逻辑漂移，Agent 生成并提交 code/shell 调用，在受限 sandbox 中执行并产生独立 canary 效果；这不是 A11 handler 自执行，也不等于主机 RCE。

代码执行增量文献和设计见 `CODE-EXECUTION-LITERATURE.md` 与 `CODE-EXECUTION-DESIGN.md`。INFUSE/CIBER 已提供沙箱代码执行链先例；未知注册表、一次外部曝光、无攻击者反馈、未指定 code-tool 路径和主机/生产 RCE 的完整组合仍未建立。原先的故障替路降为次要扩展。“低显著性”暂作为独立后续变量，不能预先声称隐蔽、有效或新颖。

## 工作所有权

| 节点 | 所有者 | 独立输出 | 范围 |
|---|---|---|---|
| 本地近邻 | kb-curator | LOCAL-PRIOR.md | MCP-UPD 等原论文的方法和威胁模型核对 |
| 公开文献 | lit-scout | WEB-LITERATURE.md | 跨 MCP/通用工具 Agent 的公开新颖性筛查 |
| 设计审查 | threat-modeler | DESIGN-REVIEW.md | 变量混淆、独立判据、最小对照和否决条件 |
| 语义核查与合成 | 主协调 | MCP-SEMANTICS.md、REPORT.md | 固定版官方 MCP 语义、本地循环适用范围及最终综合 |

只有主协调写共享台账。上述节点不注册新的有效性 claim，不改 `EVIDENCE.md`，不将研究方案标记为已测结果。

## 完成判据

1. 对原稿中 MCP-UPD 的对比逐项给出有出处的修订建议。
2. 对主要近邻记录证据等级、实际重叠和未验证部分。
3. 给出一条可证伪主问题、等强基线、可观察状态判据和最小下一步。
4. 将论文新颖性判断与可行性、评测价值分别表达。
5. 保留节点报告，校验链接/哈希，追加研究图与进度记录。

本轮没有授权或执行新的攻击实验、付费模型评测、真实账户操作、对外发布或向服务上传私有构想。研究助手及子代理自身的推理不计作受害模型实验，其用量费用本报告不估算。
