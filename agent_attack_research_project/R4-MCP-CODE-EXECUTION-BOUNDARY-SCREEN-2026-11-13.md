# R4 MCP external-content code-execution boundary 筛查

日期：2026-11-13。状态：screen pending；未注册 claim、未运行服务、模型、论文代码或实验。目标不是重新提出“外部内容可诱导代码执行”，而是检查是否存在一个 MCP-specific、可审计且尚未被 INFUSE/CIBER 覆盖的窄评测增量：单份低信任外部 MCP 内容、攻击者不知道精确工具注册表、无在线反馈，是否能在固定 MCP host/runner 中使 Agent 生成并提交代码，在受限 sandbox 产生独立合成 canary effect。

## 成功标准与边界

攻击者只能控制一次由正常 MCP/tool-result 通道摄入的合成外部内容；不能控制用户任务、系统提示、模型、host、工具注册表、代码 runner、sandbox、授权表、canary 或日志 oracle，也不能观察中间轨迹或追加反馈。固定 host 必须已有 Agent loop、准确 code/shell 或受限 code tool 描述、runner 和独立状态 oracle；攻击者不得直接写 sink。

必须分层记录并独立关联：

- `G`：Agent 生成可解析代码 artifact；
- `T`：Agent 主动向 code/shell tool 提交该 artifact；
- `X`：可信 runner 在指定 sandbox 中执行该 artifact；
- `E`：独立 oracle 观察到预注册合成状态变化。

主效果仅在 `unauthorized(E) ∧ X ∧ valid_chain(G,T,X,E) ∧ ¬server_self_execution` 时成立。模型文本、tool call 尝试、执行成功文本、MCP server 自己的副作用、普通工具调用、真实文件/网络/凭据、宿主机 RCE 或容器逃逸均不计成功。

## 必须与既有工作区分

- INFUSE 已覆盖外部环境表面→Agent shell→Docker 执行→文件/网络等独立副作用；CIBER 已覆盖工具输出/反馈→代码生成→Docker code interpreter→文件/进程状态。因此本轴不能声称首次机制。
- MCP-SafetyBench 的 user-side MCE、MSB 的真实 MCP 工具副作用、Parasites/MCP-UPD 的合法工具链/隐私外发，不能替代 `G→T→X→E` 代码执行证据。
- A11 Prompt handler 的 server-side 自执行、generic prompt injection、tool poisoning、D-29 contract/effect、task/roots/identity/annotation 等已筛查方向均排除。

## 待核验链

`single A-controlled external MCP content → fixed host Agent planning → generated artifact G → explicit code-tool submission T → sandbox runner execution X → independent synthetic effect E`。

需固定 host/client/server/runner revision、依赖锁、工具能力图、内容 hash、任务/授权表、artifact parser、runner ledger、state oracle、server-self-execution monitor 和 matched controls。若没有固定 MCP code runner、只产生普通 tools/call、只复现 INFUSE/CIBER、或独立 oracle 不存在，立即关闭；不得构造 payload、runner 或 canary 只为让链成立。

## 四路筛查结果

本轮四个只读 scout 已完成；没有运行服务、模型、论文代码、代码 runner 或实验，没有生成 payload、注册 CLAIMS 或写入 EVIDENCE 数字。

### 文献与机制查重

- 严格 `single external MCP content → G → T → X → independent E` 的宽机制已被 INFUSE、CIBER 和新增 MCP-specific CE-MCP（arXiv:2602.15945）直接或强近邻覆盖，因此“首次外部/间接内容诱导 Agent 生成并执行代码”是 NO-GO/TAKEN。
- CE-MCP 的 discovery artifact/tool metadata/tool output/exception 可进入代码生成/重生成并在 runtime/sandbox 执行，是本轮最强 MCP-specific competitor；但它不是本 screen 的严格合取：多种攻击 surface、post-query discovery、异常/结果重生成，未单独证明 single exposure、未知精确 registry、无在线反馈和完整独立 G/T/X/E ledger。
- INFUSE/CIBER 已提供外部内容→shell/code→Docker→独立状态的完整强近邻；MCP-SafetyBench/MSB/AgentDojo/AgentDyn/Parasites 分别覆盖普通 MCP 工具/状态效果、动态规划或合法工具链，但不能替代代码 runner 证据。检索受 OpenReview/DBLP/S2 限制，`direct=0` 不是 novelty proof。

### 固定实现与可达性

- 本地 `cra_mcp` 只有普通 function-calling loop、工具调用和文本结果，没有固定 Agent-generated artifact parser、dedicated code tool、sandbox runner、independent state oracle 或 server-self-execution monitor。
- `lib/agentattack/runner.py`、`crbench/runner.py` 和 Studio runner 是试验调度/进程管理，不是 MCP code runner；Q1 parser pilot 的 canary 是 fake server/parser memory path，不是 G/T/X/E 代码执行链。
- 设计文件中的 G/T/X/E、授权表和 ledger 是未来协议定义，不是现有运行时证据；没有版本/锁/源码哈希可固定的 victim host/runner bundle。

### 候选与威胁模型

- V1 `single content → Agent artifact → constrained code tool → sandbox canary`：只能作为未来评测协议条件，当前因无 runner/oracle NO-GO；宽机制已被 INFUSE/CIBER/CE-MCP 覆盖。
- V2 同链路加 pre-execution authorization gate：依赖 V1 的缺失链，只能作为未来防御 control，不是当前候选。
- V3 ordinary MCP tool/server boundary negative control：普通 `tools/call`、server self-execution 或文本成功不满足 G/T/X/E，当前也没有独立 oracle。
- 成功必须同时有 `unauthorized(E) ∧ X ∧ valid_chain(G,T,X,E) ∧ ¬server_self_execution`，artifact hash、episode/sandbox ID、source-read witness、sink commit 和独立授权表可重算。当前这些都不存在。

## 本轮裁决与边界

**VERDICT: NO-GO（宽机制已被 INFUSE/CIBER/CE-MCP 覆盖；当前本地无固定 MCP runner/oracle；V1/V2/V3 均未闭合）。** 本轮不注册 claim、不进入 R5/R6、不产生效果率。

即使未来取得 runner，本轴也只能作为 MCP-specific 评测协议收窄：single ingestion、unknown exact registry/schema、no attacker feedback、固定能力图和 G/T/X/E deterministic oracle；不能声称新攻击机制。主机 RCE、容器逃逸、真实文件/网络/凭据、直接 user injection、恶意 server 自执行和普通工具效果均排除。

## 下一条有界轴

下一轮切换到 MCP prompt lifecycle/handler boundary：检查固定 host 是否把 A 的合法 `prompts/get`/prompt handler 结果、role/content/argument metadata 自动提升为受信 system/instruction/context 或触发 downstream protected operation，且没有原始 server/session/source/approval binding。该轴必须排除通用 prompt injection、A11 server-side handler 自执行、用户显式选择 prompt、completion、sampling、elicitation、普通文本返回和模型自发工具选择；没有固定 host prompt consumer、B ACL/ledger 立即关闭。

禁止调用真实 prompt handler、启动服务、生成注入内容或运行模型；继续只做文献、源码和纸面威胁审查。
