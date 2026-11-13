# MCP_TOOL Auto Research

这是一个面向 MCP、tool-use agent 和 agent security 的 falsify-first 自动科研工作区。

目标不是让一个 Agent 把论文总结成一段话，而是让多个角色按阶段协作，逐步完成：

```text
定义问题
→ 搜集近三年文献
→ 粗读并建立文献地图
→ 选择经典与最相关工作
→ 逐篇精读
→ 确定并复现 baseline
→ 生成候选 idea
→ 研究合同
→ 廉价探针
→ 正式实验
→ 反证与归因
→ 论文写作
```

当前研究时间窗默认从 **2023-11-13 到 2026-11-13**。如果研究问题改变，必须在 `STATE.md` 和 `RESEARCH-CONTRACT.md` 中更新时间窗与范围。

## 目录

```text
MCP_TOOL/
├── README.md
├── WORKFLOW.md
├── MODEL-ROUTING.md
├── SOURCE-PATHS.md
├── RESEARCH-CONTRACT.md
├── STATE.md
├── DECISIONS.md
├── LITERATURE.md
├── PAPER-MATRIX.csv
├── IDEAS.md
├── CLAIMS.md
├── EVIDENCE.md
├── REVIEWS.md
├── ETHICS.md
├── refs.bib
├── notes/
│   ├── papers/
│   ├── clusters/
│   └── debates/
├── baselines/
│   └── MANIFEST.md
├── experiments/
│   ├── probes/
│   ├── runs/
│   └── reports/
├── paper/
│   ├── figures/
│   └── sections/
├── prompts/
│   └── ROLE-PROMPTS.md
└── templates/
    ├── PAPER-CARD.md
    ├── DEEP-READ.md
    ├── IDEA-CARD.md
    └── EXPERIMENT-PLAN.md
```

## 研究对象

第一轮默认覆盖以下对象：

- MCP server 与 MCP client；
- tool description、tool schema、tool result、resource 和 prompt；
- tool-use agent 的规划、路由、记忆和权限边界；
- malicious tool、tool poisoning、tool shadowing、rug pull；
- indirect prompt injection 与 tool output injection；
- 跨工具攻击、权限提升、凭据窃取和数据外泄；
- MCP gateway、tool registry、动态工具发现和多 Agent handoff。

## 模型分工

模型策略见 [MODEL-ROUTING.md](MODEL-ROUTING.md)。

- `gemini-3.8-flash` 负责宽搜、去重、元数据整理、摘要初筛和日志压缩。
- `6.1 Sol` 负责主力执行、代码阅读、baseline 复现、实验编排和大多数中等难度分析。
- `Opus` 只用于高价值判断，包括核心论文精读、威胁模型、关键 idea 终审、反证和最终 claim 审计。

## 开始工作

1. 先阅读 [WORKFLOW.md](WORKFLOW.md)、[MODEL-ROUTING.md](MODEL-ROUTING.md) 和 [STATE.md](STATE.md)。
2. 根据 [SOURCE-PATHS.md](SOURCE-PATHS.md) 读取已有 MCP 论文和 Agent Attack Research 项目，不复制 PDF。
3. 填写 [RESEARCH-CONTRACT.md](RESEARCH-CONTRACT.md) 的研究问题、范围、成功标准和 kill criteria。
4. 只让 Gemini 先做文献搜集和初筛。
5. 通过阶段 Gate 后，再让 Sol 执行复现和实验。
6. 只把进入精读池和关键决策交给 Opus。

所有阶段之间通过 Markdown、CSV、JSONL 和实验日志交接，不通过一个持续膨胀的聊天上下文交接。

## 安全边界

攻击实验只能运行在本地系统、项目自有系统或明确授权的 sandbox/benchmark 上。不得向真实第三方 MCP 服务、公开 registry、真实用户、真实账户或生产环境发送攻击载荷。工作区只保存合成 payload、脱敏日志和可复现实验配置。

