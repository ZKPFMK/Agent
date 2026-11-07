# 研究进度

## 已完成节点

- P0：扫描三个目标目录，统计 54 个论文子目录、54 个 PDF、52 个摘要 Markdown 和 1 个 `.DS_Store`。
- P0：发现 A07、A21 缺少摘要 Markdown；未发现目标目录内完全相同 PDF 哈希、本地代码、日志、附录或批注文件。
- P1：建立 A01–A21、B01–B14、C01–C19 唯一 ID，并生成 `paper_inventory.md`、`paper_matrix.csv`。
- P2：生成 A/B/C taxonomy 和 `category_comparison.md`。
- P3/P4：生成 `cross_category_gaps.md`，覆盖 A×B、A×C、B×C、A×B×C。
- P5/P6：生成 4 个候选想法和评分排序；I1/I2 推荐立即做最小实验，I3/I4 暂列后续。
- P7：生成 `experiment_plan.md`，包含 I1/I2 的样本、变量、统计、失败判据、安全边界和预期图表。

## 当前未解决

- PDF 正文逐页核对：环境缺少 `pdftoppm` 和可用系统 PDF 渲染工具；摘要是当前主要证据。
- A07、A21：只有 PDF 和目录名，标题、作者、年份、机制、结果均未验证。
- 代码/数据复现：摘要中的外部链接未下载或运行；目标目录无本地代码。
- 论文年份/版本：C03 等条目可能存在会议年份与本地版本/预印本年份差异，需要元数据核对。
- 具体作者、页码、表格、附录、置信区间和重复次数：摘要未提供或未逐页核验。

## 已生成文件

- `phase1_scan.md`
- `paper_inventory.md`
- `paper_matrix.csv`
- `category_A_taxonomy.md`
- `category_B_taxonomy.md`
- `category_C_taxonomy.md`
- `category_comparison.md`
- `cross_category_gaps.md`
- `candidate_ideas.md`
- `idea_ranking.md`
- `experiment_plan.md`
- `graph.md`
- `checks.md`
- `progress.md`

## 失败或排除的想法

- 只换模型、数据集、提示词的复现：排除为增量工作。
- 只增加 Agent 数量而不测传播、记忆、拓扑和反事实：排除为缺少机制证据。
- 直接串联现有外部注入、记忆投毒和通信攻击而不记录中间状态：排除为演示而非可证伪研究问题。
- I4 记忆放大协作拒绝：未排除，但因 C15 已直接研究 CORBA，暂缓并要求先做正文核对和资源上限验证。

## 下一步行动

1. 若能提供或安装可靠 PDF 文本/渲染工具，先补 A07/A21 和所有推荐想法所引用论文的正文页码、作者、附录和基线。
2. 对 I1 先做顺序效应和记忆持久性区块，不同时打开所有传播因素。
3. 只有 I1/I2 在配对对照和反事实下存活，才扩展到 I3 或多模型复验。
4. 将实际实验日志转成带命令、提交、机器和统计区间的证据行；当前没有实验结果，不得把预期写成结论。
