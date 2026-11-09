# 研究质量检查

判定只使用：**通过**、**失败**、**未解决**。

| 节点 | 要求 | 判定 | 证据 |
|---|---|---|---|
| P0 | 三个目标目录存在 | 通过 | `phase1_scan.md`；目录扫描命令；A/B/C 均存在 |
| P0 | 论文目录、PDF、Markdown 统计 | 通过 | `phase1_scan.md`；A=21/21/19，B=14/14/14，C=19/19/19，另有 1 `.DS_Store` |
| P0 | 重复 PDF 检查 | 通过 | `phase1_scan.md`；54 个 PDF SHA-256 未发现相同哈希 |
| P0 | 缺失摘要记录 | 通过 | `phase1_scan.md`；A07、A21 明确列出 |
| P0 | 本地代码/日志/附录/批注核查 | 通过 | `phase1_scan.md`；目标目录只见 PDF、摘要 Markdown、`.DS_Store` |
| P1 | 54 篇均有唯一 ID | 通过 | `paper_inventory.md`、`paper_matrix.csv`；A01–A21、B01–B14、C01–C19 |
| P1 | CSV 必需列存在 | 通过 | `paper_matrix.csv`；包含 paper_id,title,category,year,target,threat_model,attack_surface,mechanism,required_capability,success_metric,baseline,limitations,source |
| P1 | 作者、年份、正文页码不确定处未猜测 | 通过 | `paper_inventory.md`；作者统一标未验证，A07/A10/A21 年份保留未验证 |
| P1 | 每条数字有本地来源 | 通过 | `paper_inventory.md`；数字均标摘要或摘要扩展；未声明逐页核对 |
| P1 | PDF 正文逐页核验 | 未解决 | 当前环境无 `pdftoppm`/可用 PDF 渲染器；`paper_inventory.md` 的证据边界说明；需要补充正文读取工具 |
| P1 | 外部链接代码已复现 | 未解决 | `phase1_scan.md`；仅记录摘要中的 URL，目标目录无本地代码 |
| P2 | 三类 taxonomy 有攻击面、威胁、机制、指标、防御、限制 | 通过 | `category_A_taxonomy.md`、`category_B_taxonomy.md`、`category_C_taxonomy.md` |
| P2 | 分类冲突和边界被记录 | 通过 | 各 taxonomy 的交叉边界；`paper_inventory.md`“目录与实际类别冲突” |
| P3 | A/B/C 统一比较 | 通过 | `category_comparison.md`；对象、能力、阶段、指标、防御、限制表 |
| P4 | A×B 空白引用论文 ID | 通过 | `cross_category_gaps.md`；A02/A05/A14/B04/B10/B12/B13 等 |
| P4 | A×C 空白引用论文 ID | 通过 | `cross_category_gaps.md`；A10/A19/C05/C10/C13/C16 等 |
| P4 | B×C 空白引用论文 ID | 通过 | `cross_category_gaps.md`；B02/B10/B13/C04/C07/C11/C19 等 |
| P4 | 三类链条与关键未验证条件 | 通过 | `cross_category_gaps.md`；外部→记忆→规划→传播→工具 canary |
| P5 | 候选想法不超过 5 个 | 通过 | `candidate_ideas.md`；4 个候选 |
| P5 | 每个想法有论文 ID、威胁模型、失败判据、防御 | 通过 | `candidate_ideas.md`；I1–I4 各有对应段落 |
| P5 | 文献事实/推断/假设有区分 | 通过 | `candidate_ideas.md` 开头规则；各想法标注“未经验证”或“增量” |
| P5 | 不把单样例或无防御描述当普遍有效 | 通过 | `paper_inventory.md` 证据边界；`candidate_ideas.md` 失败条件 |
| P6 | 九项评分和推荐等级 | 通过 | `idea_ranking.md`；I1=42、I2=40、I3=38、I4=34，均有等级 |
| P6 | 增量想法明确标记 | 通过 | `candidate_ideas.md` I2/I3/I4；`idea_ranking.md` 排除项 |
| P7 | I1/I2 有统计方法和样本数量 | 通过 | `experiment_plan.md`；90–150/60 起始 episode、paired bootstrap CI、配对检验 |
| P7 | I1/I2 有失败判据和反事实 | 通过 | `experiment_plan.md` 各实验“失败判据”“防御和反事实” |
| P7 | 实验限定授权沙盒 | 通过 | `experiment_plan.md` 共同安全边界；合成数据、canary、无网络/无外发 |
| P8 | 输出文件均可打开 | 通过 | 本次 `Write` 已成功创建；需最终 `find`/CSV 解析复核 |
| P8 | 关键正文页码/附录已核对 | 未解决 | `paper_inventory.md`；摘要级证据仍需补充正文解析后升级 |
| P8 | A07/A21 的分类、标题、年份和机制 | 未解决 | `paper_inventory.md`；只有 PDF 文件名线索 |
