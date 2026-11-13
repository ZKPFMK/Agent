# MCP_TOOL Auto Research Workflow

## 0. 核心原则

这套流程把“读论文、想 idea、写代码、跑实验和写论文”拆成有状态的阶段。每个阶段都有：

1. 固定输入；
2. 明确输出；
3. 独立上下文；
4. 可检查的 Gate；
5. 失败后的返回路径。

任何 Agent 都不能用结果倒推研究故事。`RESEARCH-CONTRACT.md` 写好后，成功信号、失败信号、ablation 预期和主要 metric 不能为了配合结果而修改。确实需要修改时，创建带版本号的 contract，并在 `DECISIONS.md` 说明原因。

## 1. 阶段总览

| 阶段 | 名称 | 主模型 | 关键产物 | 通过条件 |
|---|---|---|---|---|
| P0 | Scoping | 6.1 Sol + Opus | `STATE.md`, `RESEARCH-CONTRACT.md`, `ETHICS.md` | 问题、范围、指标、预算和安全边界明确 |
| P1 | Corpus discovery | Gemini Flash | `LITERATURE.md`, `PAPER-MATRIX.csv`, `refs.bib` | 多视角检索、去重、引用验证完成 |
| P2 | Broad reading | Gemini Flash + Sol | `notes/clusters/`, paper cards | 所有候选论文有可追溯的粗读记录 |
| P3 | Canonical selection | 6.1 Sol + Opus | `CORE-READING-LIST.md`, `DECISIONS.md` | 经典性、相关性、影响力和可复现性有依据 |
| P4 | Deep reading | Opus 主导，Sol 辅助 | `notes/papers/`, `GAP-MATRIX.md` | threat model、方法、实验和局限逐项审计 |
| P5 | Baseline | 6.1 Sol | `baselines/MANIFEST.md`, `experiments/probes/` | 至少一个可运行 baseline 或记录复现差异 |
| P6 | Ideation | Gemini Flash → Sol → Opus | `IDEAS.md`, `CLAIMS.md` | 每个 idea 有 prior-art delta 和 kill switch |
| P7 | Research contract | Opus + Sol | `RESEARCH-CONTRACT-vN.md` | hypothesis、成功/失败信号和 ablation 预期冻结 |
| P8 | Cheap probes | 6.1 Sol | `experiments/probes/` | 低成本实验杀死明显错误方向 |
| P9 | Full experiments | 6.1 Sol | `experiments/runs/`, `EVIDENCE.md` | 配置、seed、日志和 metric 完整 |
| P10 | Falsification | Opus + 6.1 Sol | `CLAIMS.md`, `REVIEWS.md` | 关键 claim 经反证、控制和归因 |
| P11 | Paper | 6.1 Sol 起草，Opus 审计 | `paper/` | 每条 claim 和数字都能追溯到证据 |

P10 可以返回 P6、P8 或 P9。没有通过 P10 的 idea 不得进入论文。

## 2. P0 Scoping

在任何搜索之前，填写：

```text
研究对象：
研究问题 RQ1/RQ2/RQ3：
时间窗：
攻击面：
攻击者能力：
受害系统：
主要 metric：
最小 baseline：
计算预算：
模型预算：
安全边界：
kill date：
```

研究问题要能被实验回答。例如：

```text
RQ1：MCP tool metadata 中的哪类可见性或身份信号会改变 agent 的 tool selection？
RQ2：跨工具组合是否会形成单个工具测试无法发现的攻击？
RQ3：现有 tool sanitization 防御在自适应攻击下是否仍然有效？
```

P0 的 Gate：

- 不是只有主题，而是有可测的研究问题；
- 有明确的 attacker capability；
- 有 naive attack 和最小 defense baseline；
- 规定了何时停止一个方向；
- 攻击只在授权的本地或 sandbox 系统中执行。

## 3. P1 Corpus discovery

Gemini Flash 分成五个相互独立的搜索视角：

1. MCP-specific：`MCP security`, `MCP attack`, `malicious MCP server`；
2. Tool-use：`tool poisoning`, `tool shadowing`, `tool output injection`；
3. Agent security：`agent tool misuse`, `privilege escalation`, `credential exfiltration`；
4. Adjacent security：`indirect prompt injection`, `confused deputy`, `supply chain`, `capability security`；
5. Evaluation/defense：`agent security benchmark`, `tool-use defense`, `adaptive attack`.

每个视角执行：

```text
核心关键词
→ 同义词扩展
→ venue/author/benchmark 定向搜索
→ 相关工作向后追溯
→ cited-by 向前追溯
→ 最近 12 个月补搜
```

Gemini 只负责候选发现和元数据，不负责判断论文已经证明了什么。所有候选进入 `PAPER-MATRIX.csv`，每条记录至少包含：

```text
paper_id, title, authors, year, venue, url, code_url,
attack_surface, threat_model, target, evidence_type,
relevance, canonicality, reproducibility, duplicate_of, status
```

P1 的 Gate：

- 每个搜索视角都有结果或明确记录为空；
- 论文完成去重；
- 预印本和正式版本已归并；
- 论文元数据经过验证；
- 没有把搜索摘要当作实验事实。

## 4. P2 Broad reading

粗读不是让 Agent 写长摘要，而是让它为每篇论文生成 [PAPER-CARD.md](templates/PAPER-CARD.md)。

粗读只读：

- title；
- abstract；
- introduction；
- threat model 或 problem setup；
- conclusion；
- related work 中最相关的几篇。

粗读阶段必须回答：

```text
它攻击什么？
攻击者有什么权限？
攻击入口在哪里？
主要贡献是什么？
有没有真实实验？
有没有代码？
和当前 RQ 的关系是什么？
是否进入精读池？
```

Gemini 负责首轮 card。Sol 对高相关论文抽查，重点检查 Gemini 是否把“作者声称”误写成“实验已经证明”。

P2 的 Gate：

- 每篇论文都标注 `skimmed`、`selected` 或 `excluded`；
- 排除原因可追溯；
- 论文之间已经形成 cluster；
- 没有把一篇论文的数字或结论复制到另一篇论文。

## 5. P3 Canonical selection

进入精读池的论文不只按引用量排序。使用以下五项：

```text
相关性：是否直接对应 RQ？
经典性：是否定义了问题或攻击范式？
影响力：是否成为后续工作的 baseline？
证据质量：是否有真实实验、代码或漏洞复现？
差异性：是否覆盖了文献地图中的关键空白？
```

建议保留三类论文：

- 3–5 篇定义问题或攻击范式的经典论文；
- 3–5 篇最接近当前 RQ 的最新论文；
- 2–4 篇相邻领域的机制或防御论文。

Opus 只审计最终精读名单，不重新浏览整个候选池。

## 6. P4 Deep reading

每篇核心论文单独建立一个 session，并写入 [DEEP-READ.md](templates/DEEP-READ.md)。

精读分四轮：

### Round A：结构

建立论文地图，不做价值判断：

```text
问题 → 威胁模型 → 方法 → 实验 → 结论 → 局限
```

### Round B：技术

逐项重建：

- threat model；
- attacker knowledge/capability；
- system boundary；
- attack path；
- tool routing 或 message flow；
- 防御假设；
- 算法和伪代码；
- 关键实现细节。

### Round C：证据

为每个重要 claim 建立：

```text
claim → section/table/figure → evidence → limitation
```

没有定位证据的内容标为 `UNVERIFIED`。

### Round D：反例

要求 Agent 试图推翻论文：

- naive attack 是否已经达到同样效果；
- 是否只在一个模型或框架上成立；
- 是否有数据泄漏；
- 是否测试了 adaptive attacker；
- 防御是否只针对已知 payload；
- 结果是否依赖特殊 prompt、temperature 或 judge；
- threat model 是否把攻击者权限写得过强。

Opus 负责 Round C 和 Round D。Sol 负责代码、配置和实验细节核对。Gemini 不负责核心论文的最终理解。

## 7. P5 Baseline

先复现 baseline，再想 idea。baseline 记录在 `baselines/MANIFEST.md`：

```text
paper_id
repository
pinned_commit
model_snapshot
dataset_version
framework_version
run_command
expected_result
observed_result
discrepancy
```

复现任务放在独立的 Sol session 或后台进程中，不污染主研究上下文。远程实验使用 `tmux`，每次运行保存环境、配置、seed、日志和 commit。

P5 通过条件：

- baseline 至少能运行；
- 不能复现时写清楚差异；
- 已知的 naive attack 和简单 defense 已经实现；
- 后续 idea 有可比较的基线。

## 8. P6 Ideation

Gemini Flash 生成候选 idea，但只能读取：

```text
LITERATURE.md
核心论文精读结论
GAP-MATRIX.md
baseline summary
```

它不能读取同一轮中其他 idea 的完整讨论，以减少锚定效应。

每轮生成 5–10 个 idea，并使用 [IDEA-CARD.md](templates/IDEA-CARD.md)。

Sol 对每个 idea 做工程可行性和廉价实验设计。Opus 做最终安全性、novelty 和威胁模型审计。

每个 idea 必须有：

- 一句话机制；
- 与最近工作的明确差异；
- attacker capability；
- naive baseline；
- 最小可证伪实验；
- kill switch；
- 预期失败信号；
- 不得只是已有攻击的重新命名。

## 9. P7 Research contract

进入实现前冻结 [RESEARCH-CONTRACT.md](RESEARCH-CONTRACT.md)：

```text
hypothesis
success signals
independent failure signals
ablation expectations
baseline
datasets
model families
metrics
seeds
cost budget
kill criteria
```

成功信号和失败信号必须分开写。失败信号不能只是“没有成功”，还要覆盖：

- 证明大小或延迟恶化；
- 只在单一模型上有效；
- 换 seed 后消失；
- naive attack 已经达到同样效果；
- 防御只在非自适应攻击下有效；
- 攻击成功但破坏了任务 utility；
- 结果无法复现。

## 10. P8–P9 Probes and experiments

先做低成本 probe，再进行全量实验：

```text
P8.1 parser/route probe
P8.2 naive attack control
P8.3 one-variable sweep
P8.4 second model family
P8.5 defense sanity check
P8.6 judge validation
```

只有廉价 probe 支持机制假设，才进入正式实验。

正式实验至少记录：

- 攻击成功率；
- benign utility；
- false trigger；
- latency；
- token/API cost；
- stealth 或可检测性；
- 不同模型和框架；
- naive baseline；
- 至少一个防御；
- 自适应攻击；
- n、seed 和置信区间。

实验数字只能从 `EVIDENCE.md` 进入论文。

## 11. P10 Falsification

Opus 负责关键 claim 的反证，Sol 负责补充实验。每个 claim 都必须在 `CLAIMS.md` 中有状态：

```text
open
survived
weakened
refuted
```

至少执行：

```text
naive baseline attack
stronger baseline
judge swap
model swap
framework swap
adaptive defense
budget-matched control
```

如果结果只在某个模型、某个框架或某个 threat model 下成立，就把 claim 改写为更窄的 `weakened`，不能保留原来的普遍表述。

## 12. P11 Writing

写作顺序：

```text
claims registry
→ evidence table
→ figures
→ method
→ experiments
→ related work
→ introduction
→ abstract
```

论文 Agent 只能使用已经通过审计的 claim、数字和引用。它不负责重新发明实验结果，也不负责从记忆补充引用。

