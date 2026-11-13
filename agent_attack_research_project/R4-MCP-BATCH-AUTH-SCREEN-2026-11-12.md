# R4 MCP batch/bulk tool-call item authorization 绑定筛查

日期：2026-11-12。状态：screen pending；未注册 claim、未运行服务或实验。目标是检查 host/client/server 的合法批量工具调用或批量资源请求是否把一次整体审批/授权错误地应用到 batch 内不同 item，导致其中一个 item 越过对象/tenant/action ACL。

## 成功标准与边界

攻击者只能控制已连接 MCP server 返回的合法 batch schema/response 或一次正常任务中的 synthetic item list；不能修改 host/client/tool code/schema/config、审批者、B token、sink 或 ledger。成功必须同时满足：

1. host 展示/批准 batch A，或按一次整体 policy 执行 batch；
2. batch 中 item B 的对象、tenant、action 或 recipient 不在 A 的授权集合内；
3. honest protected tool/server 实际提交 B，独立 item-level ledger 记录 approval、object/tenant/action、ACL 和 commit；
4. strict per-item authorization/reference checker 阻断 B，benign batch utility 保持。

排除 R4-02 approval inheritance、P4 provenance、parser differential、普通 parameter poisoning、task/session ID、批处理本来就逐 item 授权的正常语义、攻击者自有副作用和无 sink 的模型/文本效果。

## 待核验链

`batch schema/result → host approval/policy → per-item expansion/dispatch → item ACL/tenant/action check → protected sink ledger`。

需固定一个实际支持 batch/array arguments 或 multi-tool call 的 host/client/server revision 与依赖锁，核对 approval snapshot 是否含每个 item、item expansion 是否在审批后、是否有独立 ACL/ledger。若只有普通数组参数、模型生成错误 item 或已有 R4-02/参数污染语义，立即关闭；不得构造 permissive batch broker。

## 有界源码核验结果

- `cra_mcp 0.2.0` commit `463779b318f78a7c9e62e86639fec135c0423bc5`：`server.py:43–50` 单工具注册；`adapter.py:106–127` 单 `name,args→call_tool`；`agent.py:107–125` 可遍历多个模型 tool calls，但逐调用审批/执行；array 只用于 schema 递归，不是 batch dispatch。
- VS Code 1.106.0 tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`：`languageModelToolsService.ts:300–354` 一次 rawInput 确认；`mcpLanguageModelToolContribution.ts:174–216` 保留原参数；`mcpServer.ts:1044` 发单个 `tools/call`；未见 batch schema/item expansion。
- TypeScript SDK 1.29.0 单 `callTool`；transport batch 仍逐条派发。Go SDK v1.6.0 对新版本拒绝 JSON-RPC batch；client/server 仍单调用。官方 conformance server 没有 batch schema、tenant/object ACL 或 protected sink。
- 本地 `.cra/events.jsonl` 只有 ts/actor/action/target，不是 item approval/ACL/commit ledger；没有 `approval snapshot→expansion→item ACL→sink` 链。

结论：固定对象 `NO-GO`；普通数组、多个独立 calls 和 JSON-RPC transport batch 不构成本轴。外部 compound operation 仍未泛化，但不应构造 broker。下一轴切换为 resource subscription/update binding；无实验、claim 或 EVIDENCE。
