# R4 MCP sampling recipient/session binding 筛查

日期：2026-11-11。结论：`NO-GO`（当前固定实现与已知跨 client 错路）；未注册 claim、未运行实验或服务。mcp-agent 的持久连接管理仍有一个实现粘连线索，但尚无非 GHSA 的完整攻击链。

## 成功标准与边界

只考虑攻击者控制一个已连接 MCP server，发送合法 sampling/createMessage 请求或 metadata；攻击者不能控制 host、LLM、诚实 recipient/tool、审批者、sink、真实用户或另一会话，不能伪造 B 会话 ID、直接调用 sink 或写 ledger。成功必须同时满足：

1. 请求源为会话 A，host 实际将 sampling 请求、上下文或结果送到不同 recipient/session B；
2. B 的诚实受保护工具或 sink 产生 effect；
3. 独立 deterministic ledger 关联 origin/session/recipient/request/effect，并证明 A 没有覆盖该 effect 的有效授权。

模型生成文本、正常 callback、tool_use 文本、日志、成功消息、攻击 server 自己的副作用和普通 transport 跨 client 错路不计入新机制。

## 固定实现核验

- VS Code 1.106.0，tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`：`mcpServerRequestHandler.ts:318–342,420–426` 使用原请求 ID；`mcpServer.ts:604–609` 绑定原 server 回调；`mcpSamplingService.ts:59–80` 仅消费 server 提供的 messages/systemPrompt，未读取活动聊天历史；`mcpSamplingService.ts:222–248` 的 model hints 只在该 server 的 allowedModels 集合内匹配；`mcpSamplingLog.ts:98–133` 只是普通日志。没有跨会话 recipient/context/sink 链。
- mcp-agent 0.2.6，commit `f62d849350816588b1c6294e7914bbe4d8b84072`：`server/app_server.py:375–391`、`mcp_server_registry.py:174–186` 绑定 upstream；`mcp_agent_client_session.py:340–364` 按绑定 upstream 转发；Python SDK 1.23.1，commit `8e02fc17e196295116d3fa4e993116ce6e017c1` 的 `client/session.py:539–563` 与 `shared/session.py:134–136,337–349` 将响应送回原 session/id。`sampling_handler.py:217–259` 工具为空并使用 `use_history=False`；示例终点是文本，不是受保护 sink。
- mcp-agent 的 connection manager 按 server 复用并继承首建 ContextVar，但尚未发现从共享 manager 到 B 私有 context、A recipient 和诚实 effect 的完整链。若继续，只能补读一个真实 caller；不能构造宽松 host。
- TypeScript SDK 1.29.0，commit `e12cbd7078db388152f6e839abdbe09ba01f3f32`：单 transport/响应捕获和 stateless stream 约束已核验；旧共享 transport/server 的跨 client sampling 错路由由 GHSA-345p-7cg4-v4c7 覆盖，1.26.0 修复。

## 文献与公告查重

有界检索核验 8 个来源，覆盖近 12 个月、近 30 天和旧作追溯。GHSA 直接覆盖共享 transport/server 的跨 client sampling 错路；MCP sampling 规范允许或描述 context inclusion，但允许请求不等于错绑实证。`Breaking the Protocol`、Unit 42、Spectrum 与 `When MCP Servers Attack` 覆盖来源混淆、同会话污染、sampling 资源滥用或一般 callback 风险，未给出本轮定义之外的隔离 transport recipient-binding 机制；MCP 漏洞数据集没有该绑定案例；SEP-2567 讨论 sessionless/sampling 相关状态但不是攻击实证。

## 判定与下一步

当前固定实现判定为 `NO-GO`，不是“sampling 安全”的普遍结论。GHSA 覆盖的跨 client 错路不能重包装为新贡献；剩余 ContextVar/manager 粘连线索只有在固定真实 caller、B 私有上下文、A recipient 和诚实 effect 全部闭合时才可重开。下一轴切换为 sampling 请求中的 `tools/toolChoice/includeContext` 是否能让 host 将 server 请求升级为跨服务器工具调用或上下文读取；必须单独完成全文查重、固定实现核验和 threat gate，未通过前不运行实验。

DO_NOT_DO：不要把 `includeContext` 未被某个 host 使用当作漏洞；不要把模型越狱、sampling prompt injection、正常 allowed-model 选择、GHSA 错路、日志或成功文本当作独立 effect。
