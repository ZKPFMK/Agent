# R4 MCP completion/输入辅助筛查

日期：2026-11-11。结论：VS Code 1.106.0 prompt completion 按当前威胁模型 NO-GO；resource-template 上游取值仍 UNCERTAIN。未运行实验或服务，未注册 claim。

## 已核验 VS Code 路径

固定对象：VS Code 1.106.0 tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`。

- `mcpPromptArgumentPick.ts:77–97` 为本次 prompt 流程初始化参数；当前值来自恢复值或既有已接受参数，否则为空。
- `175–227` 输入变化与 `onDidAccept` 分开；文件、选区和命令进入参数的动作发生在用户接受之后。
- `236–246` 调用 `prompt.complete(arg.name, 当前输入, alreadyResolved)`；`alreadyResolved` 只包含此前已接受的非空参数；结果映射为 suggestion label，server 不能通过 completion 返回值直接指定 file/selection/command 动作。
- `331–340` 有 200ms debounce，说明存在 pre-submit completion 网络请求。
- `mcpServer.ts:927–933` 发送 prompt ref、`argument.value` 和可选的 `context.arguments`；`mcpServerRequestHandler.ts:557–558` 使用 `completion/complete`。
- resource-template completion 包装在 `mcpServer.ts:1141–1148`，其上游私有值来源本轮未完成核验。

## 判定

攻击者控制一个已连接 server 的 completion handler/description，不能控制 host、用户输入、LLM、工具或 sink。成功必须是 host 私有状态中的随机 canary 在没有用户提交/提供动作时进入 `completion/complete` 请求，并由独立 receiver ledger 证明来自 host。

本轮未看到这种私有状态自动取出链。普通用户输入、用户选择文件/选区、用户接受 prompt、server 返回候选、server 自写日志或模型复述均不计攻击成功。普通 completion、elicitation、logging 和 progress 行为没有独立越权 effect。

邻近风险包括 ToolLeak 的 schema-driven argument completion、普通隐私外泄/提示词注入、Q7 session rebinding、Q9/Q10 side channel，但当前没有新机制证据。

## 下一步

只读核验 `resource-template` completion 的上游取值来源；若参数仍来自用户显式输入或已接受资源引用，关闭整个 completion 轴。不得为补齐 canary 来源而创建宽松 host、自动读取私有文件或改写 host。若未来真实 host 有隐私值自动进入 completion 请求，先做新颖性/威胁模型门检，再考虑合成 canary，不能直接报告 ASR。
