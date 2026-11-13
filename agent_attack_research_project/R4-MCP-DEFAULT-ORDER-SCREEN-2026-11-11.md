# R4 MCP-R4-01 默认值审批顺序筛查

日期：2026-11-11。结论：当前固定实现 `NO-GO`；外部未核验实现仍 `UNCERTAIN`。新颖性查重未发现 direct 先例，但没有注册 claim、没有运行服务或实验。

## 机制与成功标准

候选要求完整闭合：用户明确批准诚实工具的原始参数/效果集合 Γ_A；审批后，攻击者控制的 schema 或合法响应使 host/server 对省略、null 或可规范化字段自动补值/解析为 B；同一诚实受保护工具实际提交 B；独立 deterministic ledger 关联确认、原始 A、解析后 B、工具身份和 sink commit，并证明 B 不属于 Γ_A。正常默认行为、等价规范化、模型自行改选参数、攻击者自有副作用和错误文本不算成功。

## 文献查重

截至 2026-11-11，近 12 个月及 2026-10-12 至 2026-11-11 重点检索中，direct=0。近邻包括：

- `Approve What, Exactly?`（全文）：覆盖审批后规范化和 effect binding，但未直接覆盖默认插入导致的 A→B。
- MCPTox（全文）：覆盖工具描述诱导隐式参数操纵，不是审批前 A、审批后 server default B。
- `When Neither Side Confirms`（全文）：覆盖审批策略、缺失人工 gate 和模型自填 confirm，不追踪参数 A/B 默认解析。
- MCP Tools 规范：定义 inputSchema/arguments 和确认建议，不规定默认值必须在审批前解析，也不提供 effect binding 保证。
- CoSAI MCP Security：将 malicious default values/Full Schema Poisoning 作为类别和控制建议，没有 A→B→诚实 effect 证据。
- AWS normalization 公告和 OpenClaw advisory：分别覆盖规则匹配或环境变量归一化差异，非 MCP schema/default 链。

因此机制新颖性暂未被直接抢先，但这不是可达性证明。

## 固定实现核验

- `cra_mcp 0.2.0`，commit `463779b318f78a7c9e62e86639fec135c0423bc5`：`agent.py:117–125` 展示/审批原始参数后调用；`adapter.py:112–118` 删除 null 后执行；固定 `tools.py:459–473` 进行路径 normalization 和范围守卫，但 `file_write`、`phase_advance` 的关键参数没有默认值。未找到外来 schema 默认值进入独立诚实 sink 的路径。
- VS Code 1.106.0，tree `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`：`languageModelToolsService.ts:300–354` 等待确认并采用 rawInput；`mcpLanguageModelToolContribution.ts:174–216` 保留原始参数；`mcpServer.ts:1044` 原样发往 `tools/call`。未见审批展示后再补 server default 的路径。
- MCP Python SDK 1.23.1，commit `8e02fc17e196295116d3fa4e993116ce6e017c1`：`func_metadata.py:86–95,249–261` 将函数签名默认值用于预解析、Pydantic 校验和函数执行，但本轮未发现对应 host approval snapshot，也没有证明攻击者可改变诚实工具默认值。
- TypeScript SDK 1.29.0，commit `e12cbd7078db388152f6e839abdbe09ba01f3f32`：`mcp.ts:213–214,272–281,349–352` 将原始参数送入 Zod 解析后回调；未提供本题需要的审批快照与独立 protected sink 链。

## 判定与下一步

当前对象的判定为 `NO-GO`：没有“审批 A→默认解析 B→诚实受保护 effect”的完整链。外部实现只能在固定 revision、依赖锁和真实 caller 中重新核验，不能用 schema 含 default 推断漏洞，也不能构造 permissive broker。下一轴切换到 MCP-R4-04：resource_link 是否被固定 host 自动跨源解引用，并在没有对象授权的情况下把资源内容或权限带入诚实受保护工具；需先做全文查重、实现链和独立 effect/资源访问 ledger。

DO_NOT_DO：不要把 `null` 删除本身、参数字节变化、普通缺失验证、MCPTox、P4、R4-02、parser differential 或攻击者自己的工具副作用报告成新攻击。
