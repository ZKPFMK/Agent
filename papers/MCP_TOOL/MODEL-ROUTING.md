# Model Routing

## 1. 总策略

配额有限的模型用于高信息增益判断，配额充足的模型用于重复性执行。

```text
Gemini 3.8 Flash = breadth
6.1 Sol = execution
Opus = judgment
```

不得因为某个模型“看起来更聪明”就让它承担所有阶段。每个模型的输出必须通过文件交接和 Gate 检查。

## 2. Gemini 3.8 Flash

### 适合

- 多关键词、多来源文献搜索；
- 标题、摘要、Introduction 初筛；
- 文献去重和元数据整理；
- 论文聚类；
- 发现同义词和相邻术语；
- 从论文中提取候选 baseline、数据集和代码；
- 批量压缩日志；
- 生成候选 idea。

### 不适合独立决定

- 论文是否真正证明了某个安全结论；
- novelty 最终判断；
- threat model 是否合理；
- 实验结果是否足以支持 claim；
- 论文最终结论；
- 高风险攻击设计。

### 输入限制

每批只发送一个 cluster 或固定数量的 paper card。不要让 Gemini 同时看到整个论文库和所有历史讨论。

## 3. 6.1 Sol

### 适合

- 读取代码和论文方法细节；
- 复现 baseline；
- 运行和监控实验；
- 处理环境、依赖和日志；
- 设计 cheap probe；
- 检查配置、数据 split、seed 和 metric；
- 生成图表和结果报告；
- 将实验结果转换成 `EVIDENCE.md` 草稿。

### 不适合独立决定

- 最终 novelty；
- 最终论文 claim；
- 是否可以忽略异常结果；
- 是否可以在真实第三方系统上测试；
- 是否把失败结果解释成正面发现。

### 执行规则

所有长任务放在独立 session、后台进程或 `tmux` 中。主研究 session 只读取结果文件，不吸收完整安装日志和长输出。

## 4. Opus

### 适合

- 精读核心论文；
- 审计 threat model；
- 检查攻击机制是否真的新；
- 比较最接近的 prior work；
- 评审 idea card；
- 写和审 research contract；
- 设计 falsification；
- 审计 claim-evidence 对应；
- 最终决定 go、revise 或 kill。

### 使用限制

Opus 配额较少，因此不要让它：

- 搜索所有论文；
- 批量做摘要；
- 监控训练；
- 处理安装错误；
- 生成几十个初始 idea；
- 读取不在精读池中的全部 PDF。

## 5. 交接协议

模型之间不传递“上一段聊天上下文”，只传递以下文件：

```text
Gemini → LITERATURE.md / PAPER-MATRIX.csv / PAPER-CARD.md
Sol → baseline manifest / logs / EVIDENCE.md
Opus → deep-read verdict / decisions / claims audit
```

每次交接必须包含：

```text
任务
输入文件
输出文件
本次模型能做什么
本次模型不能做什么
停止条件
失败时返回哪一阶段
```

## 6. 预算建议

每个方向的默认预算优先级：

```text
文献搜索与粗读：Gemini 60%
baseline 与实验执行：Sol 25%
关键论文、idea 和反证：Opus 15%
```

如果一个 idea 连 cheap probe 都没有通过，不得消耗 Opus 做完整精读或长篇评审。

