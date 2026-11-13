# R4 MCP sampling tools/toolChoice/includeContext 筛查

日期：2026-11-11。结论：宽泛 framing `NO-GO`；窄实现问题 `UNCERTAIN`，但当前固定实现没有完整链。未注册 claim、未运行实验或服务。

## 成功边界

攻击者只能控制已连接 MCP server 发出的合法 sampling 请求及 server-owned 字段；不能控制 host、模型权重、诚实 host tool、审批者、sink、真实用户或私有数据，不能直接写 ledger。成功必须是 server-only 的 `tools`、`toolChoice` 或 `includeContext` 字段导致固定 host 执行未授权 honest host tool 或读取 host-private context，并由独立 deterministic ledger 记录 effect。sampling 文本、模型复述、server 自己的工具调用、日志和正常允许的 server 工具不计入成功。

## 固定源码核验

- VS Code 1.106.0，tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`：`mcpServerRequestHandler.ts:325–326` → `mcpServer.ts:604–609` → `mcpSamplingService.ts:58–108`。后者只用 `messages/systemPrompt` 构造模型输入，`options={}`，再收集并返回文本；`tools`、`toolChoice`、`includeContext` 未进入 host 工具执行器或私有上下文读取器。
- mcp-agent 0.2.6：`sampling_handler.py:217–259` 的工具集合为空（`server_names=[]`）并使用 `use_history=False`；已有 Python SDK 1.23.1 源码核验没有发现 sampling response 到诚实 host sink 的路径。
- 因此当前固定对象只剩“字段到 host executor/private reader 的连接”这一缺口，不构成可达性证据。

## 文献和公告查重

有限最终查重核验 MCP sampling 规范、GHSA-345p-7cg4-v4c7、Unit 42、Breaking the Protocol 和一个近期 MCP 近邻。规范明确 multi-turn tool loop 中 server 执行返回的 `tool_use`，`toolChoice=required` 约束模型生成而不授予 host 工具权限；`includeContext` 默认 none，并可被 client 忽略或受能力声明限制。GHSA 近邻是共享 transport/server 的跨 client sampling 错路，未覆盖三字段到 host protected executor/private reader 的新链。Unit 42 的 sampling PoC 是提示诱导恶意 server 自有工具调用；Breaking the Protocol 汇总 sampling 注入/上下文外泄，但没有字段到诚实 host effect 的完整实现链。四个来源均无本轮定义下的 direct 机制证据。

## 判定与下一步

宽泛“sampling 字段触发工具/读取上下文”已是正常语义、提示词注入或已有错路近邻，判 `NO-GO`。窄题“固定 host 错把 server-owned 字段接入 host executor/private reader”保留为 `UNCERTAIN`，但 VS Code 和 mcp-agent 不支持它；不应为了补链构造宽松 host。下一轮切换到 MCP-R4-01：host 先审批参数、server 后解析默认值，检查是否存在默认值解析顺序导致实际 effect 超出批准范围的固定实现和独立 effect witness。该轴必须排除 `Approve What, Exactly?`、MCPTox 隐式参数操纵、P4 provenance 和普通参数污染。

DO_NOT_DO：不要把 host 忽略 `includeContext` 当成漏洞；不要把模型越狱、sampling prompt injection、正常 toolChoice、攻击 server 自有副作用或 GHSA 错路改名为新攻击。
