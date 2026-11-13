# R4 MCP-R4-04 resource_link 跨源自动解引用筛查

日期：2026-11-11。结论：当前固定实现 `NO-GO`；外部 host 仍 `UNCERTAIN`，没有注册 claim、没有运行实验或服务。

## 成功标准与边界

攻击者仅控制已连接 MCP server 返回的合法 `resource_link`/URI 或 tool-result metadata；不能控制 host resolver、诚实资源服务、诚实 protected tool、审批者、sink、真实用户，不能直接读取目标资源或写 ledger。完整成功必须闭合：

`server link → host 自动 resolver/fetch → 跨源身份/凭据或对象授权错误 → 未授权资源读取或内容交给诚实 protected tool → 独立 effect`

独立 ledger 需记录源 server/session、URI authority、事前授权集合、实际身份、资源 hash/bytes 或 sink commit。普通 `resources/read`、URI 展示、攻击者自有资源、纯网络访问/SSRF、提示词注入、日志和 P4 provenance 不算成功。

## 文献查重

截至 2026-11-11 的近 12 个月与最近 30 天有界检索保留 8 个来源，均为 `near`，没有 direct 三段链：MCP Resources/Tools 规范只说明资源读取和 resource link 表示，不要求自动获取或传权；AWS AgentCore 警告恶意 URI 可指向内部端点/文件但没有末段 effect；Python SDK outputSchema 外部 `$ref` 公告不是 resource_link；Mecatl 资源 fetch 工具显式防 SSRF；COPEX、跨框架 tool poisoning、Filesystem Capability Laundering 覆盖资源注入、客户端边界或文件能力洗白。剩余 delta 不是“网络请求”，而是固定 host 的跨源身份/授权绑定错误。

## 固定实现核验

- VS Code 1.106.0，tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`：`mcpLanguageModelToolContribution.ts:280–306` 对图片 resource link 读取；`mcpTypes.ts:790–824` 强制绑定原 server ID；`mcpResourceFilesystem.ts:227–282` 只向该 server 发 `resources/read`。图片字节可进入模型，非图片主要保留 URI/MIME 引用；未见跨源回退、对象授权绕过或诚实 protected tool sink。
- mcp-agent 0.2.6，commit `f62d849350816588b1c6294e7914bbe4d8b84072`：`mcp_aggregator.py:734–778,900–904` 的 `read_resource` 是显式接口；`call_tool` 返回结果，没有自动 resource_link 解引用。
- Python SDK 1.23.1，commit `8e02fc17e196295116d3fa4e993116ce6e017c1`：`client/session.py:329–418` 校验并返回资源结果；TypeScript SDK 1.29.0，commit `e12cbd7078db388152f6e839abdbe09ba01f3f32`：`client/index.ts:716–784` 同样没有自动跨源 resolver。

## 判定与下一步

当前固定对象判定 `NO-GO`；外部实现不能由规范沉默推断。若重开，只能固定一个实际 host 的 `application/vnd.code.resource-link` 或等价 caller，追踪 URI→resolver→凭据/身份→对象 ACL→资源内容→诚实 sink，并用独立 ledger 验证。下一条未覆盖轴切换到 `initialize` 版本/能力协商降级；必须先做公共查重、固定 handshake 实现和 threat gate，未通过前不做实验。

DO_NOT_DO：不要把普通资源读取、链接展示、内部 URL/文件 fetch、SSRF、resource injection、攻击者自有资源或 P4 authority laundering 改名为新机制。
