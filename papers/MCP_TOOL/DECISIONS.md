# Decisions

本文件只追加，不覆盖历史决定。

## D0 — 2026-11-13 — initialize

Decision: 使用分阶段、多角色、文件交接的 auto research 流程。

Rationale: 单个 Agent 直接读取全部论文会产生粗读、上下文污染和事后合理化。研究流程必须把检索、粗读、精读、baseline、idea、实验和写作分开。

Model allocation:

- Gemini 3.8 Flash：文献宽搜、初筛、聚类和批量整理；
- 6.1 Sol：代码、baseline、实验和执行；
- Opus：核心论文、威胁模型、idea 终审、falsification 和 claim 审计。

Reversal trigger: 如果某一阶段的模型输出在抽样审计中持续出现不可接受的事实错误，则降低其权限并把该阶段交给 Sol 或 Opus。

