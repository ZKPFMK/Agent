# Source Paths

本工作区使用已有文件作为只读输入，不复制 PDF、私人笔记或第三方代码。

## 现有 MCP 论文

```text
/Users/dj/Documents/paper/Agent/papers/10_MCP攻击
```

其中已经有 MCP attack、MCP security、tool invocation prompt security、MCP safety benchmark、MCPtox、MPMA 等材料。先读取其中已有的标题/摘要/Introduction 笔记，再决定哪些论文需要重新精读。

## 现有 Agent Attack Research 项目

```text
/Users/dj/Documents/paper/Agent/agent_attack_research_project
```

这个目录提供已有的：

- Agent attack taxonomy；
- literature matrix；
- MCP candidate screening；
- threat model；
- attack chain；
- evidence ledger；
- claims；
- baseline 和 experiment 结构。

工作区中只引用这些路径，不把它们复制进 `MCP_TOOL`。

## Agent Attack Research toolkit

```text
/Users/dj/Documents/paper/Agent/Agent-Attack-Research
```

需要复用已有命令、模板或检查器时，先读取其 `AGENTS.md`、`CLAUDE.md` 和 `SPEC.md`。

## 外部材料的处理

- 公开论文可以记录 metadata、链接和本地阅读笔记；
- 不把有版权的 PDF 提交到新的仓库；
- 不把真实攻击 payload、凭据、个人数据和生产系统日志写入工作区；
- API、网页、registry 和服务端实验必须有明确授权；
- 不能通过复述搜索摘要代替全文核查。

