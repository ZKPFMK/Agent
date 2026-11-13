# H2 sampling 会话/接收者错绑：固定源码核验

日期：2026-11-11。状态：UNCERTAIN；未运行代码、服务或模型，未注册 claim。

## 固定版本

- `mcp-agent` 0.2.6，commit `f62d849350816588b1c6294e7914bbe4d8b84072`
- `modelcontextprotocol/python-sdk` 1.23.1，commit `8e02fc17e196295116d3fa4e993116ce6e017c1`（固定对象由 scout 提供；若继续研究需重新核对 SHA 字符串）
- mcp-agent `uv.lock` 锁定 mcp 1.23.1，wheel SHA256：`3ce897fcc20a41bd50b4c58d3aa88085f11f505dcc0eaed48930012d34c731d8`

## 已核验路径

- `app_server.py:375–391` 克隆请求 Context，将 session 写入 `bound_context.upstream_session`，再设置 ContextVar；`426` 重置。
- `core/context.py:117–151` 优先解析请求绑定 session；`248–276` 克隆时清空旧 upstream。
- `mcp_agent_client_session.py:103–126` 将实例 Context 交给 sampling handler；`340–364` 从 `self.context.upstream_session` 转发并原样返回。
- `sampling_handler.py:217–259` 新建 sampling LLM，`server_names=[]`，输入为请求 `messages/systemPrompt`，`use_history=False`；未找到另一会话历史自动加载。
- `sampling_handler.py:145–201` 使用独立 UUID 请求/响应审批，metadata 保存参数或结果；无 human handler 时直接通过；有 upstream 时直接转发。
- Python SDK `shared/session.py:194–201,256–281` 的 pending key 为每个 Session 实例内的 request id；`490` 按该实例表取响应。
- `client/session.py:555–563` 使用原 responder 回应；`shared/session.py:134–136,337–349` 保留原 request id 并写回对应 session 流。

## 结论

没有证据证明：

1. B 会话的私有上下文进入 A 的 sampling 请求；或
2. B 的 sampling 响应被发送给 A；或
3. A 的审批被 B 复用，或相反。

`upstream_session` 的赋值/切换和 per-session pending 表说明实现有绑定机制，但未读到 host 自有 connection manager、filtered stdio client 和固定上游 sampling 的完整端到端路径。因此不能把“缺少显式 recipient tuple”升级为错绑漏洞，也不能把 `includeContext` 参数存在升级为隐私泄露。

## 下一最小检查

只读补读同一提交的 connection manager 的 session factory/接收任务 ContextVar 继承、`filtered_stdio_client` 和一个固定上游 sampling 实现。如果没有 `B context → A request/response` 的完整链，关闭 H2；如果只是 identity/session rebinding，归入已关闭 Q7；如果需要模型遵循 server 文本，归入普通注入。不得创建宽松模拟 host，也不得运行 canary 实验。
