# STATE

phase: P0
status: initialized
project: MCP_TOOL
created: 2026-11-13
research_window: 2023-11-13..2026-11-13
topic: MCP and tool-use agent security
lead_model: 6.1 Sol
judgment_model: Opus
scout_model: Gemini 3.8 Flash
source_paths: SOURCE-PATHS.md
contract: RESEARCH-CONTRACT.md

## Current objective

建立 MCP/tool-use agent security 的近三年文献地图，完成核心论文精读，确定一个可在本地或 sandbox 中验证的研究问题，并通过 baseline、cheap probes、正式实验和 falsification 形成可复现论文结果。

## Current gate

- [ ] RQ1/RQ2/RQ3 已冻结
- [ ] 攻击面和 threat model 已冻结
- [ ] API/Token/计算预算已填写
- [ ] 安全边界和 kill criteria 已填写
- [ ] 文献时间窗已确认

## Active tasks

| id | owner | task | output | status |
|---|---|---|---|---|
| P0-1 | 6.1 Sol | 根据现有 MCP 材料提出 2–3 个可测 RQ | `RESEARCH-CONTRACT.md` 草稿 | pending |
| P0-2 | Gemini Flash | 从 `10_MCP攻击` 和现有项目生成 paper inventory | `PAPER-MATRIX.csv` | pending |
| P0-3 | Opus | 审查 RQ、范围和安全边界 | `DECISIONS.md` | pending |

## Resume rule

恢复工作时先读本文件，再读 `DECISIONS.md`、`LITERATURE.md`、`CLAIMS.md` 和 `EVIDENCE.md`。不要从聊天记忆推断当前阶段。

