# MCP 攻击研究：R4 子代理初筛汇总

日期：2026-11-10。协调者：pi-orchestrator（主会话）。

**本轮结论：UNCERTAIN / 不进入实验。** 四个子代理已完成候选挖掘、公开文献核对、本地知识库定位和威胁模型预审。目前没有候选同时通过新颖性与真实实现可达性检查。没有注册新攻击主张，没有运行模型试验、攻击用例或 MCP 服务，也没有产生本轮 ASR 数据。

## 1. 本轮研究目标与输入

用户要求聚焦 MCP 攻击，使用子代理寻找有效的研究方向。有效性必须以可复现的测量证明，不能从攻击名称、伪代码或人为构造的脆弱代理中推定。当前工作继续现有 R4；I1、P4、Q1/C4 的关闭决定保持有效。

输入包括 `STATE.md`、`ATTACK-RESEARCH.md`、`RESEARCH-GRAPH.md`、`progress.md`、`PAPER-GOAL.md`、本地 54 篇 A/B/C 矩阵、`papers/10_MCP攻击` 的论文及公开规范/源码。外部论文目录和知识库保持只读。

## 2. 子代理交付与证据边界

| 角色 | 已交付内容 | 持久化位置 / 证据边界 |
| --- | --- | --- |
| idea-miner | 四个候选的释放变量、对照、评估器和终止条件 | 主会话中的 hand-back；未生成独立报告文件。本汇总保存经审查的候选及结论，不将其全部建议视为事实 |
| lit-scout | 候选公开文献/规范核对；effect-history 线索的有界跟进 | 主会话中的 hand-back；来源见下文。全文核验结果由该 agent 报告，协调者未逐篇重新阅读全文 |
| kb-curator | 本地论文近邻、既有方向覆盖及候选重叠判断 | [KB 报告](./R4-SCOUT-kb-mcp-2026-11-10.md)；广义机制重叠不是每个窄接口都已直接被测量 |
| threat-modeler | 可达性、权限边界和实验伪成功检查；实际 toolkit 源码定位 | [威胁模型预审稿](./R4-SCOUT-threat-mcp-2026-11-10.md)及后续 hand-back 修正；协调者另行核对 `cra_mcp/agent.py:87–130` |

本地报告是初筛材料，不能自动升级为已证实漏洞、完整新颖性结论或论文贡献。

## 3. 候选的协调结论

| ID | 待检验机制 | 本轮结论 | 依据及未解决问题 |
| --- | --- | --- | --- |
| MCP-R4-01 | 主机先审批原始参数，服务器后解析默认值，导致实际效果超出审批范围 | UNCERTAIN | 有参数默认值相关实现线索，但尚未证明实际效果超出用户批准范围。effect binding 已覆盖广义问题；需要在真实实现中隔离默认值解析顺序这一差异 |
| MCP-R4-02 | 普通结构化结果自动成为下游调用参数，并继承上游审批 | NO-GO（当前表述） | 与 P4 的来源/授权升级及既有跨工具参数操纵重叠；已读 toolkit 不存在假设中的自动字段绑定及审批继承路径。不能为获得成功率另写一个自动放权的 broker |
| MCP-R4-03 | 客户端分别校验 `structuredContent`、向模型传递不一致的 `content` | NO-GO（当前 toolkit）；外部实现未核验 | 有界只读检查确认 `ToolBox.call` 运行时只提取 `content` 文本；双字段 fallback 仅在测试辅助函数中，未发现两个真实安全消费者或授权/执行分叉。不能将此结论外推到未固定版本的外部 SDK/host |
| MCP-R4-04 | 工具返回的 `resource_link` 被自动跨源解引用并获得额外权限 | UNCERTAIN | 缺少真实 host 自动解引用、跨源传播权限或跳过对象授权的代码路径；容易退化为 P4、一般 confused deputy 或 SSRF |
| MCP-R4-05 | 低信任服务器控制时序，诱发可信工具在一次授权下重复产生效果 | UNCERTAIN | effect-history 已有理论分类；未找到跨信任重试/重复审批复用的实际 witness。取消后的副作用不自动等于漏洞，攻击者自己的工具重复写也不是权限突破 |

另外的版本/能力降级、sampling、gateway capability 和非文件系统 contract/effect 方向，只保留为预审线索；均未通过真实实现和新颖性门槛。高层目标诱发自主工具链也尚不能仅凭不指定工具名就与已有工作区分。

## 4. 淘汰优先候选的代码依据

`Agent-Attack-Research/lib/mcp/cra_mcp/agent.py` 中：

- 第 104 行每轮调用模型，获取本轮模型生成的动作；
- 第 117–125 行取本次工具名/参数，按配置判断本次调用是否需要审批，再调用工具；
- 第 128 行将工具结果追加为 tool message。

这段代码不能支持“结构化结果字段自动绑定到下游参数并继承审批”的假设。审批并非覆盖所有调用；是否询问由配置和工具分类决定，但这同样不能证明上游批准凭据被下游复用。

需要区分：模型依据错误数据选择了错误参数、工具使用自身既有权限、下游缺少对象级授权、以及审批凭据真正跨调用复用。它们不能合并成一个未经核验的新机制。

## 5. 对原始 scout 报告的修正

1. `prompts/get` 在某些框架中未暴露，不足以推断 `sampling/createMessage` 也未暴露。威胁模型预审稿中对 sampling 可用性的推断不作已验证事实使用。
2. MCP 取消与副作用回滚不能混为一谈。必须先确认被测系统明确承诺的权限或执行保证；取消后出现效果本身不算越权证据。
3. 重复效果必须来自独立、诚实的受保护工具，且超出实际授权范围。恶意服务器在自己的实现中重复写入不满足该条件。
4. idea-miner 对 MCP-R4-02 的优先推荐已被后续源码和文献审查否决。该推荐不再代表当前研究方向。
5. 没有搜索命中、没有跑过 LLM、增加一种协议字段或换模型/工具数量，都不足以单独支持新颖性。

## 6. 有界只读实现检查结果

后续由一个独立只读 source-check agent 核对当前 toolkit。结论：**MCP-R4-03 在该实现中 NO-GO**；外部 SDK/host 未核验，不能据此断言普遍安全或存在同类漏洞。

- `lib/mcp/cra_mcp/adapter.py:106–127` 的 `ToolBox.call` 调用 server 后，只从 `res.content` 提取文本并返回字符串，没有读取 `structuredContent`。
- `lib/mcp/cra_mcp/agent.py:104–128` 每轮取模型新调用；审批取决于当前工具分类和配置，随后调用 `box.call`，将字符串结果追加为 tool message。没有结果双表示参与不同安全决策的代码路径。
- `lib/mcp/tests/test_server.py:24–29` 存在 `structured_content` / 文本 fallback，但只用于测试断言，不能作为两个部署安全消费者的证据。
- `mcp>=2.0,<3` 是依赖范围，不是固定 SDK 版本。该 agent 没有据此声称验证了 SDK 内部或任意外部 host。

本次检查没有调用模型、启动服务或运行攻击。协调者另行记录了两个关键本地源文件的 SHA-256：

| 文件 | SHA-256 |
| --- | --- |
| `cra_mcp/agent.py` | `83a493ac04d1d3cada5e98a52163e87fcc1e6f95c1c1f60e7ff97f96fe6c368d` |
| `cra_mcp/adapter.py` | `5e28cd0797db159f280975fa140f4986eb73b37bd6af96f25e4a05d6e8970e79` |

**重开条件：**固定一个外部 SDK/host 的准确版本和源码哈希，找到同一合法响应被两个实际 consumer 用于不同安全决策的路径，并先证明独立授权/执行状态差异；同时排除 Q1 和既有 post-wire semantic-change 研究覆盖。只有满足这些条件，才注册主张、交给 falsifier，并考虑合成 canary 试验。不再重复当前 content-only toolkit 检查。

## 7. 可追溯来源

以下章节定位来自 lit-scout 的全文核验报告，来源内容与推断分开使用：

- [MCP Tools 规范](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)：工具调用、结构化结果及兼容性表示要求；不证明客户端存在安全分叉。
- [MCP Resources 规范](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)：资源访问和客户端处理；不承诺自动跨源解引用。
- [Approve What, Exactly?](https://arxiv.org/html/2610.21063v1)，§2.2、§5.1–5.3：实际 effect descriptor 和执行绑定，构成参数审批方向的重要近邻。
- [A2M](https://arxiv.org/html/2609.26761v1)，§3.1、§3.3、§4.3：工具返回对后续工具及参数的影响。
- [MCPTox](https://ojs.aaai.org/index.php/AAAI/article/download/40895/44856)，§3.1：P3 隐式参数篡改。
- [When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary](https://arxiv.org/html/2609.15397v1)，§2–§5：effect histories、重试重复效果及取消残留等异常；未提供本轮所需的跨信任攻击 witness。
- [MCP Python SDK cancellation 文档](https://py.sdk.modelcontextprotocol.io/v2/handlers/cancellation/)：取消处理的实现指导，不是攻击结果。
- [项目原 P4 关闭记录](./R6-P4-screening-2026-11-08.md)、[Q1 关闭记录](./R7-Q1-screening-2026-11-08.md)。

## 8. 检查与交接

- 项目结构检查：待运行。
- P0 门检：待运行；研究主张及当前会议要求尚未闭合，不应被标记通过。
- 新增实验 / 测量：无；`CLAIMS.md`、`EVIDENCE.md` 不新增研究结果。
- 当前状态：保留 R4，下一工作是有界、只读的真实实现检查。
- 不得执行：重启已关闭方向、把 toy broker 成功当作模型漏洞、连接生产/第三方受害系统、发布工作载荷、宣称高 ASR 或未经核验的新颖性。
