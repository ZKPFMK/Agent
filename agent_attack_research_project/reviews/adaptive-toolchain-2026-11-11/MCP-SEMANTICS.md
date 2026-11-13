# MCP 语义与本地规划循环核查

日期：2026-11-11。范围：只读官方固定版规范及本地研究工具包；没有运行 Agent、工具服务器或模型评测。此检查不判断新颖性。

## 1. 官方规范直接支持什么

来源 S-MCP-T：[MCP 2025-11-25 Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)，本次通过 WebFetch 核对全文。

- **full-text-verified，User Interaction Model**：工具为 “model-controlled”；模型可依赖上下文和用户提示自动发现、调用工具。同时规范明确 “the protocol itself does not mandate any specific user interaction model”。所以不能把某一宿主的自主规划循环视为所有 MCP 系统的固定属性。
- **full-text-verified，Error Handling**：工具执行错误包含模型可用于 “self-correct and retry with adjusted parameters” 的反馈；客户端 **SHOULD** 将这类错误提供给模型。错误反馈和恢复是预期能力。该文本没有证明模型会寻找不同工具，也没有证明错误恢复会完成越权目标。
- **full-text-verified，User Interaction Model / Security Considerations**：规范建议让人能拒绝调用、对敏感操作确认。这里的 **SHOULD** 不是每个宿主已经实现不可绕过授权的证据。
- **full-text-verified，Tool**：来自非可信服务器的 annotations 必须视为不可信。元数据/描述的信任问题与用户当前的“正常工具返回的外部内容”入口应分别建模，不能在不同实验条件下偷偷更换攻击能力。

来源 S-MCP-A：[MCP 2025-11-25 Architecture](https://modelcontextprotocol.io/specification/2025-11-25/architecture)，本次通过 WebFetch 核对全文。

- **full-text-verified，Host**：Host “Enforces security policies and consent requirements”，处理授权、协调模型集成、聚合多个客户端的上下文。
- **full-text-verified，Design Principles 3**：服务器不应看见完整对话或其他服务器；跨服务器交互由宿主管理。这是架构责任划分，不能据此断言宿主不会被外部内容影响。

**inference：**用户构想的主要入口是间接提示词注入；MCP 是能力暴露和工具组合的承载环境。若主张“MCP 特有的新机制”，还需要在相同工具语义/授权政策下与普通函数调用宿主作对比，或指出具体 MCP 信任边界。仅使用 MCP SDK 不能自动获得协议层新颖性。

## 2. 本地循环实际提供什么

文件：`/Users/dj/Documents/paper/Agent/Agent-Attack-Research/lib/mcp/cra_mcp/agent.py`

- 工具包 HEAD：`463779b318f78a7c9e62e86639fec135c0423bc5`。
- 工作区有既有修改，以上 HEAD 不代表整个工作区的可重现快照；被检查文件本身 SHA-256 为 `83a493ac04d1d3cada5e98a52163e87fcc1e6f95c1c1f60e7ff97f96fe6c368d`。
- **full-text-verified，45–50 行**：SYSTEM 明确要求错误时阅读 violations 并修复原因；它同时要求先调用研究台账工具、不能自行跑 shell。这是研究助手，不是已适配本研究的通用受害 Agent。
- **full-text-verified，87–131 行**：每轮模型生成调用，循环执行 `box.call`，再把返回值追加为 tool 消息，直到模型结束或达到 `max_steps`。因此实验各注入条件应使用同一个反馈循环，不应单独为候选条件添加反馈。
- **full-text-verified，96 行**：工具列表在循环开始时取得。现有循环不能直接证明对执行期间工具注册表变化的适应；需要另行固定并验证宿主的列表刷新行为。研究“事先未知环境”和“执行中列表变化”应分开。
- **full-text-verified，120–125 行**：写入/破坏性操作有本地审批分支。关闭它再声称绕过用户确认，会改变威胁模型。
- **full-text-verified，12–13 行与 173–174 行**：该循环通过进程内 ToolBox 调用同一套研究工具，文件说明无需 MCP client。它不能单独作为真实 MCP 端到端运行的证据。

**inference：**可借鉴现有循环的日志与步数上限，但不应直接向研究项目工具注入载荷并调用其真实写入能力。后续需要只暴露合成业务工具的隔离适配器；若要称为 MCP 测量，还需要真实 MCP client/server transport，并保留 tools/list、tools/call、工具响应和宿主政策事件。

## 3. 本次核查的边界

- 没有验证任意生产宿主、当前最新 SDK 或任意模型会服从用户构想。
- 没有观察到攻击成功、权限提升、替代路径恢复、用户发现率或检测率。
- 官方固定版本支持的是能力/责任语义，不能代替宿主实现证据。

## Handoff

VERDICT: GO（语义核查完成；不表示创新、可行性或实验门槛通过）
INPUTS: 固定版官方规范 S-MCP-T/S-MCP-A；agent.py SHA-256 如上；原构想 SHA-256 `63ca1233a225b6ea87ed6ed07857c4c7568bcdd4de593089a830f4df233f413c`
OUTPUT: `reviews/adaptive-toolchain-2026-11-11/MCP-SEMANTICS.md`
CHECK: 官方两页已读取；本地 agent.py 已读取；`shasum -a 256` 返回 0；项目结构检查返回 0。结构 PASS 仅检查台账结构。
EVIDENCE: 上述规范标题及 agent.py 行号。
BLOCKERS: 尚无合成业务环境、MCP transport 适配和独立授权 oracle。
NEXT: 与本地/公开文献和独立实验设计审查合成，保持 R4。
DO_NOT_DO: 不运行研究写入工具作为受害工具；不将普通恢复能力或进程内 ToolBox 演示报告为 MCP 新攻击。
