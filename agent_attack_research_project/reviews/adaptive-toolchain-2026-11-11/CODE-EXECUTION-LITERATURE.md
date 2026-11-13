# CODE-EXECUTION-LITERATURE — 外部/间接提示词注入到代码执行的有界筛查

- 核验日期：2026-11-12
- 范围：只补充“外部或间接提示词/工具输出 → 目标或逻辑漂移 → Agent 自己生成并调用 shell、Python、code interpreter 或 MCP code tool → 代码真实执行 → 独立状态/网络/文件副作用判定”的公开文献证据。
- 明确区分：
  1. 沙箱内代码或 shell 执行；
  2. 主机或生产环境 RCE；
  3. 恶意 MCP Server/工具实现自身执行副作用；
  4. 只有工具调用或状态改变、没有受害 Agent 生成代码的攻击。
- 不复现论文代码，不构造或运行攻击载荷，不把搜索摘要当全文证据。全文证据优先使用官方 arXiv HTML；原文提取物保存在本文件末尾所列的独立目录。

## 结论

**结论：GO 作为一个有边界的代码执行风险评测问题；NO-GO 作为“首次发现外部材料能诱导 Agent 执行代码”的攻击机制。**

已经有全文证据证明，外部/间接内容可以影响代码 Agent 或终端 Agent 的决策，使其生成并执行 shell/Python 代码，并通过独立的容器状态、文件、进程、网络或测试脚本信号判定副作用：

- **INFUSE** 是与用户当前方向最接近的完整公开证据。它把攻击材料预置在 README、文件、配置、终端输出、错误信息、构建产物等环境表面；Agent 只有一个 shell 命令执行通道，但该通道可读写文件、运行 Python、安装包、访问网络和执行 git。它使用 Docker 隔离、完整轨迹、启发式状态验证和 LLM judge；启发式判据包括攻击者控制的网络请求、受保护文件修改、提交/凭据/外泄文件等具体伪迹。全文还给出一条“注入终端输出 → Agent 读取凭据 → 将凭据写入被追踪文件”的逐轨迹例子。其威胁模型不允许攻击者直接改系统提示、模型或用户输入；引擎同时支持 one-shot 与 persistent 变体。它已经覆盖了“外部材料 → 逻辑/目标漂移 → Agent 生成 shell 命令 → 沙箱中执行 → 独立副作用验证”。
- **CIBER** 也直接覆盖了完整链条，但攻击者权限更强。其 IPI 方法把工具输出或执行反馈替换为恶意内容；对需要推理的 Agent，论文明确描述恶意内容诱导 Agent 在下一步生成恶意代码。Agent 在 Docker 环境中生成并执行代码，评测同时读取文本响应和文件/进程状态，使用校验和、备份差异和进程树判定物理副作用。其攻击者是 grey-box，知道固定工具集、API 响应结构和一般系统提示，还可观察文本反馈和环境状态来细化攻击，因此不能当作“未知工具注册表、一次曝光、无反馈”的证据。
- **MCP-SafetyBench** 的 MCE（Malicious Code Execution）类别确实把“工具执行有害命令”列为攻击类型，并有机器可检查的 command-injection evaluator；但 v2 §3.3 明确，user-side 攻击是把 prompt-injection 片段直接放进用户 query。它不是外部低信任内容进入后的间接链条。其 server-side Tool Poisoning–Command Injection / FileSystem Poisoning 是被篡改的 MCP manifest 或 server 侧实现，不能直接解释为受害 Agent 自主生成代码。
- **MSB** 使用真实 MCP 工具和工作区状态，能测外部检索/工具响应诱导 Agent 调用攻击工具或合法工具，并用工作区状态判定目标是否达成；但其示例主要是显式指定攻击工具、工具转移、伪造错误和参数攻击。当前全文没有建立“外部材料 → 受害 Agent 生成未知代码 → code tool 执行 → 独立 canary”的完整证据。
- **AgentDojo** 已经测到外部工具输出诱导受害 Agent 选择多个工具并造成状态副作用，但工具是应用级 API，论文没有 shell/code interpreter 的实际执行通道。**AgentDyn** 增加了动态规划、有帮助的外部指令、冲突和路径错误，但本轮核到的 v3 没有把代码生成/代码工具执行作为攻击成功判据。
- **Parasites/MCP-UPD** 的本地全文节点已核到外部内容诱导合法 MCP 工具组成寄生链和隐私外泄，并且攻击者不必预知完整 MCP 配置；但本节点没有重读其本地 PDF，且现有证据重点是合法工具链和数据外发，不是受害 Agent 生成代码并由 code interpreter 执行。它应作为 MCP 合法工具副作用近邻，而不是代码执行链的完整先例。

因此，用户真正可以继续检验的窄问题是：在已有 INFUSE/CIBER 的沙箱代码执行链基础上，是否能在**更弱攻击者知识、单份低信任内容、无在线反馈、非固定攻击脚本、外部环境/工具能力变化**下保持代码执行及独立副作用。这个问题是评测协议和威胁模型收窄，不应写成尚无先例的代码执行攻击机制。

## 完整因果链核对表

| work / 版本 | 外部或间接内容 | 目标/逻辑漂移 | Agent 生成代码或 shell | 代码工具真实执行 | 独立副作用判定 | 环境级别 | 对本构想的含义 |
|---|---|---|---|---|---|---|---|
| **INFUSE**，arXiv v1，2026-10-14，全文 | 是。攻击者提前控制 README、文件内容、配置、错误/终端输出、归档等表面；不改系统提示、模型或用户输入。§A.2.1、§A.2.2 | 是。五类目标包含数据外泄、未授权修改、权限提升、系统破坏/安全绕过、供应链攻击；§3、§A.2.3 | 是。终端 Agent 每轮输出一个 shell 命令；可调用 shell、Python、包管理、HTTP、git；§3、App.E.1 | 是。每个 cell 在 Docker 中真实执行，记录 action/observation 以及读写/执行对象；§3.2 | 是。启发式检查网络请求、受保护文件、凭据、提交、外泄文件等；§3.2。G.3 有注入终端输出后读取凭据并写入跟踪文件的轨迹 | 隔离 Docker；restricted egress、只读 root、有限计算；没有主机逃逸证明 | **最强直接近邻**。已测完整“外部材料→shell执行→状态伪迹”，但不是 MCP，工具集合是单 Bash 原语；需要比较其 one-shot/static payload 与本构想的弱知识条件 |
| **CIBER**，arXiv v1，2026-02-23，全文 | 是，但 IPI 以替换工具输出/执行反馈的方式实现；§3.1、§3.3 | 是。攻击目标包括未授权执行、权限提升、持久化；IPI 可把恶意内容置入观察并改变后续代码生成；§3.1、§3.3 | 是。对 reasoning agent，恶意执行结果诱导下一步生成恶意代码；表1给出自然语言、代码描述、代码片段模态；§3.3 | 是。OpenInterpreter/OpenCodeInterpreter 在 Docker 中生成并执行代码，触发系统调用、文件操作、进程创建；§3.4 | 是。文本意图与物理状态双流判定；校验和、备份差异、进程树；§3.5 | Docker sandbox，论文讨论 RCE 风险，但本核验未发现主机/生产逃逸证据 | **直接支持代码执行链**，但攻击者 grey-box，知道固定工具集/API/提示模板，并可观察文本与环境反馈；不能支持严格盲注册表、一次无反馈条件 |
| **MCP-SafetyBench**，arXiv v2，2026-03-05，全文 | MCE 用户侧是直接用户输入；服务器侧还有 manifest/implementation 修改；§3.2、§3.3、App.A.4 | MCE/credential/RAC 等可造成目标偏离；server-side command injection 可篡改工具行为；但不是同一条外部内容→代码生成链 | MCE 的定义是“用户输入使工具执行有害命令”，没有核到受害 Agent 自己生成代码的独立证据；§A.4 | 有 real MCP server/多步工具执行和 command-injection evaluator，但不能据此断言 code interpreter 执行 | attack evaluator 检查特定攻击签名，execution-based；§3.5。没有核到独立 canary 作为 MCE 必要判据 | 真实 MCP 服务器和多服务器任务；不是主机 RCE 证明 | **MCE 可作标签/控制项**，不能作为外部间接代码执行的先例；要把 user-side direct attack 与 server-side malicious implementation 分开 |
| **MSB**，arXiv v1，2025-10-14；ICLR 2026 接收元数据，全文 | Retrieval Injection 把恶意指令从污染数据库经 benign tool response 带入；Prompt Injection/Tool Response 也可改变规划；§3.2、§4.3–4.4 | 是。可诱导 Tool Transfer、未授权数据访问、参数/工具偏离；攻击示例常明确指定攻击工具或 endpoint；§4.3、App.B | 没有核到 Agent 生成任意 Python/shell/code-tool 的判据；主要是调用真实 benign/malicious MCP tools | 是真实 MCP 工具执行，工作区含个人数据/SSH keys；但副作用来自工具调用，不等于受害 Agent 代码执行 | 工作区状态检查 attack task 是否完成；§5.1–5.2 | 真实 MCP 工具/服务器，非主机 RCE证明 | **真实工具副作用近邻**；可作为“工具执行≠代码执行”的边界控制 |
| **AgentDojo**，v3，2024-11-24；NeurIPS 2024，全文 | 是。外部工具输出 placeholders；§3.1、§3.3 | 是。外部内容可诱导攻击任务、多工具调用和状态改变；§4 | 否。公开环境是邮件、银行、旅行、Slack 等 curated API；未核到 shell/code interpreter | 是应用状态的模拟/受控工具调用，非任意代码执行 | 环境 state utility/security checks；§3.4 | 模拟的 stateful tool environment；非 RCE | 证明“外部材料能改变工具行为”，不能证明“外部材料能让 Agent 生成代码并执行” |
| **AgentDyn**，v3，2026-05-07，全文 | 是。网页广告位、邮件、文件、动态实体等；§3.2、App.B/D | 是。动态规划、helpful instructions、冲突和路径错误使规划改变；§3.2、App.D | 否。核到的攻击/防御是通用 IPI、文件/邮件/Web/Bank/GitHub 工具；未见 code interpreter 判据 | 有真实动态交互与工具执行，但不是代码生成执行链 | TSR/ASR 和状态任务检查；§3.5 | 动态 sandbox/多应用；非主机 RCE | 证明动态外部内容与多步规划风险，不能充当代码执行先例 |
| **Parasites/MCP-UPD**，arXiv 2509.06572，当前 v5 2026-05-01；本节点未重读本地 PDF | 本地全文节点报告外部内容单次预置并诱导合法 MCP 工具链；攻击者不要求预知 MCP 配置 | 是。读/收集/转发的高层流程可导致未授权隐私外发；本地节点 p4 §2.2.3、§2.3.2 | 未建立。现有证据不等于 Agent 生成 shell/Python/MCP code-tool 代码 | 合法 MCP 工具链执行和数据外发；不是 code interpreter 证据 | 外发/canary 类效果，具体代码执行副作用未核到 | MCP 工具链；主机 RCE未建立 | 作为 MCP 合法工具副作用近邻；不能把它写成代码执行论文 |
| AgentSentry，v2，2026-10-27，全文但属于防御论文 | 是。外部 email/document/web/retrieval artifact 进入状态；§III-B | 是。目标是未经授权高影响 action；攻击成功要求外部 effect 被提交；§III-B | 论文把 code-interpreter-style data exfiltration 作为背景/案例线索，但 AgentSentry 主实验是 AgentDojo，不是代码解释器攻击 benchmark；§I | 主实验工具执行有外部 effect；没有把代码生成执行作为独立攻击变量 | 攻击成功定义为 committed external-environment action；§III-B | 应用层 runtime + 黑盒远程 LLM；防御评测，不是 RCE研究 | 适合作为“如何将动作提交和外部副作用纳入判据”的防御近邻，不作为代码执行攻击数量 |

## 三类执行结果的边界

### 1. 沙箱内未授权代码执行

这条证据已经成立，且有两个不同角度：

- **CIBER** 的代码解释器循环直接生成并执行代码，使用 Docker 内的文件、进程和配置状态验证。其“Success”只要求容器状态被物理改变；因此是沙箱内真实副作用，而不是只看模型说了什么。
- **INFUSE** 的终端 Agent 直接产生 shell 命令，命令在 Docker 中执行。它同时提供 heuristic 和 LLM judge，且把“只提到注入内容”与“真正采取行动”分开。它的 attack registry 包含凭据/SSH/authorized-key、shell 启动文件、cron、包下载执行、网络 POST 等目标；本报告不复制这些载荷文本。

这两篇都说明，代码执行研究不能只统计“模型生成了危险代码”或“模型答应执行”，必须检查文件、进程、网络、提交或其他独立状态。它们也说明沙箱仅证明“受控运行时中的未授权执行”，不能证明攻击者已经取得宿主机或生产系统 RCE。

### 2. 真正 RCE

**本轮没有找到可把下列链条写成已证实的公开论文结果：外部间接提示词 → 受害 Agent 生成代码 → 代码工具突破隔离 → 宿主机/生产环境任意代码执行。**

CIBER 在相关工作和风险定义中使用“physical RCE”或 RCE 风险语义，但其实际执行模块是 Docker sandbox，状态判据是容器内部文件/进程等改变；INFUSE 同样明确写出 `Sandbox ≠ production` 的限制。MCP-SafetyBench 和 MSB 使用真实 MCP 服务器/工具，但本轮全文没有给出由间接外部材料触发的宿主机逃逸或生产 RCE 证据。不能把“shell 工具有权限”或“恶意 server 可执行”升级为 RCE。

### 3. 恶意 MCP Server 自执行

MCP 论文/基准中存在另一类链条：攻击者控制 MCP Server、工具描述、工具响应或工具实现，随后 server/tool 自己执行其实现中的副作用，或者诱导 Agent 调用已有高权限工具。这与“受害 Agent 自己生成代码并调用 code tool”不同。

- **MSB** 明确运行真实 benign/malicious MCP tools，攻击 tool 可能通过名称、描述、参数、响应和 retrieval 数据影响 Agent；工作区状态判定攻击任务。它能证明真实 MCP 工具副作用，但其 Prompt Injection、False Error、Tool Transfer 示例经常直接写出攻击工具/endpoint，不能等同于未知 code tool 的自主发现。
- **MCP-SafetyBench** 将 server-side Command Injection、FileSystem Poisoning、Tool Redirection 与 user-side MCE 分开；其 MCE 例属于直接 user query，server-side 则是 manifest/implementation 变更。必须按攻击面分别报告。
- **MCPTox/MCP-ITP**（原公开筛查）证明工具元数据可诱导 Agent 调用合法高权限工具；MCP-ITP 的攻击者知道良性工具集并用评估器/检测器反馈优化。它们不是 code interpreter 链，也不是未知注册表/无反馈证据。
- **Parasites/MCP-UPD**（本地节点证据）证明外部内容可诱导合法 MCP 工具组成寄生链并造成隐私外发；本轮没有把它扩写成代码执行或 RCE。

## “外部材料→代码执行→独立 canary”是否已被测到

按严格问题拆分：

| 条件 | 本轮证据 | 判断 |
|---|---|---|
| 外部/间接材料进入 Agent 上下文 | INFUSE 文件/配置/终端/错误/构建/网络表面；CIBER 工具输出/执行反馈；AgentDojo/AgentDyn 外部工具输出 | **已测** |
| 材料导致目标或逻辑漂移 | INFUSE 五类未授权目标；CIBER IPI/MPA/PBD；AgentDojo/AgentDyn 任务/状态偏离 | **已测** |
| 受害 Agent 自己生成 shell/Python/code-tool 调用 | INFUSE 单 Bash primitive；CIBER Think–Code–Execute 循环和 IPI 下后续代码生成 | **已测** |
| 代码/命令在受控运行时真实执行 | INFUSE Docker shell；CIBER Docker code interpreter | **已测** |
| 独立于语言回复的副作用判定 | INFUSE heuristic 文件/网络/提交/凭据等；CIBER checksum/diff/process probes；MCP-SafetyBench attack evaluator；MSB workspace state | **已测，但判据不同** |
| literal 独立 canary endpoint 作为每个攻击成功条件 | INFUSE 有 attacker-controlled network request/URL 目标，但不应概括为每个 cell 都有 literal canary；CIBER本轮核到的是容器状态探针；MCP-SafetyBench/MSB为 attack evaluator/workspace state | **部分；不能统一写成 canary** |
| 受害 Agent 使用未预先写出的替代 code/tool 路径 | 现有文献未在本轮核到该专项条件；AgentDyn 的动态工具重规划不等于 code-tool 迁移 | **未建立** |
| 攻击者不知道工具注册表/代码工具 schema | CIBER知道固定工具集；MSB/MCPTox/MCP-ITP通常知道或控制工具；INFUSE使用单 Bash primitive，不是未知 MCP registry | **未建立** |
| 只曝光一份外部内容、无攻击者在线反馈 | INFUSE registry支持 one-shot/static payload，但不是未知 registry；CIBER允许观察反馈并细化；MCP benchmark多为预置/固定任务 | **严格合取未建立** |
| 主机/生产 RCE 或沙箱逃逸 | 本轮没有全文证据 | **未建立** |

## 对原构想的有界定位

原构想中“外部提示词逻辑攻击能让 Agent 生成并执行未授权代码”已经有直接公开风险证据，不能写成首次机制。尤其应撤回以下表述：

- “此前工作只测工具调用，没有测 Agent 自己生成代码并执行”；INFUSE 和 CIBER 已直接反例。
- “工具名不写出就等于工具/代码能力未知”；CIBER 的固定工具集知识、MSB 的真实攻击工具与 MCP-ITP 的工具集访问说明两者不同。
- “沙箱内真实执行等于 RCE”；CIBER/INFUSE 都把隔离环境与生产安全边界分开。
- “外部材料导致工具调用成功就等于代码执行”；AgentDojo、MSB、MCP-SafetyBench 中许多结果是 API/工具或工作区状态副作用，必须和 Agent 生成代码区分。

如果继续，最小可检验 delta 应是**评测协议收窄**，而不是新的提示词类别：冻结单份、不包含工具名/参数/代码步骤的低信任内容；目标环境在注册后随机化；攻击者退出且不读取中间 trace；代码工具/能力图改变；只允许 Agent 根据自身工具描述和执行结果完成一次受控代码执行；使用容器状态和研究者控制的独立网络 canary 双重判定；再加入“只改变工具名”与“真实能力/路径改变”的分离对照。该设计是否能产生更强迁移或更低显著性，仍需实验，本文献筛查没有预先证明。

## 公开来源与证据等级

### A：官方公开全文，已核读相关方法/威胁模型/评测段落

1. **CIBER: A Comprehensive Benchmark for Security Evaluation of Code Interpreter Agents**，arXiv:2602.19547v1，2026-02-23。全文：
   <https://arxiv.org/html/2602.19547v1>
   - §3.1：攻击者目标、grey-box知识和四类入口；
   - §3.3：IPI 将工具输出/执行反馈变成后续恶意代码生成；
   - §3.4–3.5：Docker真实执行、文件/进程状态、checksum/diff/process probes；
   - 表1：自然语言、代码描述、代码片段与 IPI/MPA/PBD/DPI 组合。
   - arXiv元数据：<https://arxiv.org/abs/2602.19547>

2. **INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems**，arXiv:2610.20776v1，2026-10-14。全文：
   <https://arxiv.org/html/2610.20776v1>
   - §3：shell/code/package/network/git能力、攻击类别、Docker执行、双重评分；
   - §3.2：每轮一个 Bash 命令、启发式状态验证和 LLM judge；
   - §A.2.1–A.2.2：攻击者预先控制环境表面，不得修改 system prompt/model/user input；static/dynamic surfaces；
   - §A.2.3/Table 7：机器可验证的网络、文件、凭据、权限和系统破坏目标；
   - §G.3：终端输出注入后读取凭据并写入追踪文件的完整轨迹；
   - App.H/Limitations：明确隔离 sandbox 不等于 production。
   - 代码：<https://github.com/judydnguyen/infuse>
   - arXiv元数据：<https://arxiv.org/abs/2610.20776>

3. **MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers**，arXiv:2512.15163v2，2026-03-05。全文：
   <https://arxiv.org/html/2512.15163v2>
   - §3.2/Table 2：MCE、server-side Command Injection/FileSystem Poisoning/Tool Redirection 等攻击面定义；
   - §3.3：user-side attack 是将 injection 片段直接放入 user query；
   - §3.5：`check_command_injection_attack` 等执行式 attack evaluator；
   - App.A.4：MCE 例是 writable shell/file-editing 工具被要求产生有害命令；
   - §4：多步真实 MCP 任务及 attack/task 双标签。
   - 代码：<https://github.com/xjzzzzzzzz/MCPSafety>
   - arXiv元数据：<https://arxiv.org/abs/2512.15163>

4. **MSB: MCP Security Bench: Benchmarking Attacks Against Model Context Protocol in LLM Agents**，arXiv:2510.15994v1，2025-10-14；arXiv元数据注明 ICLR 2026 接收。全文：
   <https://arxiv.org/html/2510.15994v1>
   - §3.2：攻击者可控制恶意 MCP server、工具元数据、响应和外部资源；
   - §4.1–4.4：Prompt Injection、Tool Transfer、False Error、Retrieval Injection；
   - §5.1–5.2：真实 benign/malicious tools、工作区数据、workspace-state 评测；
   - App.B：攻击示例与实际工具调用链，但许多攻击显式指定 attack tool/endpoint。
   - 代码：<https://github.com/dongsenzhang/MSB>
   - arXiv元数据：<https://arxiv.org/abs/2510.15994>

5. **AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification**，arXiv:2602.22724v2，2026-10-27。全文：
   <https://arxiv.org/html/2602.22724v2>
   - §III-B：攻击者只能控制外部内容，攻击成功要求高影响 action 被提交到 external environment；
   - 这是防御论文，不把主实验当作 code-execution attack evidence；用于动作提交/副作用判据的参照。
   - 代码：<https://github.com/CyberGuardianAI/AgentSentry>
   - arXiv元数据：<https://arxiv.org/abs/2602.22724>

6. **AgentDojo**，arXiv:2406.13352v3，2024-11-24；NeurIPS 2024。此前报告已全文核读 §§3–4、App.A/B：
   <https://arxiv.org/html/2406.13352v3>
   - 已有外部工具输出→多工具/状态副作用；没有 shell/code interpreter 实际执行通道。

7. **AgentDyn**，arXiv:2602.03117v3，2026-05-07。此前报告已全文核读 §§3–4、App.B/D/F：
   <https://arxiv.org/html/2602.03117v3>
   - 已有动态规划、helpful instructions、冲突/路径错误；没有本轮可核的 code-generation/code-tool side-effect 链。

### B：本节点未重读全文，但已有本项目节点转交的公开/本地证据

8. **Parasites in the Toolchain: A Large-Scale Analysis of Attacks on the MCP Ecosystem**，arXiv:2509.06572v5，2026-05-01；页面注明 IEEE S&P 2026 接收：
   <https://arxiv.org/abs/2509.06572>
   - 本节点只核了公开版本元数据；本地全文节点报告已核对 p4 §2.2.3、§2.3.2、p12 §5.3：不要求先验 MCP 配置知识，外部内容可诱导读/转发链；未把该证据扩写为 code interpreter/RCE。

### C：只作检索线索，不作为本报告结论

- OpenSRE prompt-injection-to-RCE、厂商安全博客、搜索摘要中的“attacker shell”等非本轮全文学术证据；未写入矩阵结论。
- `paper_search.py` 的一次批量检索失败：OpenReview 结果作者字段为字典，脚本在解析时抛出 `TypeError`；官方 arXiv 下载和人工核读不受影响。未将该失败当作“无结果”。
- CIRCLE（arXiv:2507.19399）只作为 code-interpreter 资源耗尽近邻线索，未纳入主矩阵，因为本轮目标是外部/间接内容驱动的代码执行及独立副作用链。

## 本轮独有来源目录与阅读日志

本轮新增原始来源全部下载到独立目录，没有运行其中的代码或构建工具：

- CIBER：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/code-execution-sources/ciber-efd02893/source.html`
- INFUSE：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/code-execution-sources/infuse-4cca9639/source.html`
- MCP-SafetyBench：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/code-execution-sources/mcp-safetybench-b6ea973f/source.html`
- MSB：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/code-execution-sources/msb-2fe62dbc/source.html`
- AgentSentry v1/v2：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/code-execution-sources/agentsentry-b317c137/source.html`、`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/code-execution-sources/agentsentry-v2-34e2b285/source.html`
- CIRCLE（仅线索/局部）：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/code-execution-sources/circle-bc4b2b90/source.html`

提取文本：各目录中对应 `source-text.txt`。主核读者：literature-scout；日期：2026-11-12。CIBER、INFUSE、MCP-SafetyBench、MSB、AgentSentry 为官方 arXiv HTML 全文；AgentDojo/AgentDyn 为此前本报告已完成的官方 HTML 全文核读；Parasites 只采用本地全文节点转交的证据，不在本轮重复阅读。

## 对 coordinator 的 handoff

- **VERDICT：GO（仅作为代码执行链评测问题）；NO-GO（作为全新攻击机制）；严格主机 RCE：UNCERTAIN/无证据。**
- **INPUTS：** 原构想、旧公开筛查、AgentDojo/AgentDyn/Parasites/MCP 系列近邻；本轮新增 CIBER、INFUSE、MCP-SafetyBench、MSB、AgentSentry 全文。
- **OUTPUT：** 本文件；独有原始来源目录见上。
- **CHECK：** 已明确区分 sandbox code execution、true RCE、malicious MCP Server self-execution；未运行 payload、模型或论文代码。
- **EVIDENCE：** INFUSE 和 CIBER已测“外部/工具内容→Agent代码或shell→容器执行→独立副作用”；MCP-SafetyBench MCE主要是直接用户输入；MSB是真实 MCP 工具副作用但未建立受害 Agent 生成代码链。
- **BLOCKERS：** 没有来源在同一设置完整建立“严格未知 registry + 一次外部曝光 + 无反馈 + Agent自主生成未指定代码工具路径 + 主机/生产 RCE”。literal canary 不是所有论文的统一判据。
- **NEXT：** 若继续，只测冻结外部内容在能力/工具图变化下的代码执行迁移，并使用状态 verifier + 独立研究者控制 canary；先以 INFUSE/CIBER 作强基线，以 MCP-SafetyBench/MSB 作工具/服务器边界控制。
- **DO_NOT_DO：** 不写“首次实现外部提示词到代码执行”；不把沙箱状态改变称为主机 RCE；不把 MCE 直接用户攻击称为间接注入；不把恶意 MCP Server 自执行称为受害 Agent 生成代码；不把 MSB 的 tool transfer/false error 当作未知 code-tool 自主发现。
