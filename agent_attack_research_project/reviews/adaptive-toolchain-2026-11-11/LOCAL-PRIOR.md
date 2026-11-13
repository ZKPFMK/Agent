# 自适应工具链构想：本地原论文近邻核查

日期：2026-11-11。角色：auto research R1/R4 本地原文/KB核查。范围：用户指定构想、四篇本地 PDF、MCP-UPD 中文说明，以及只读 KB/项目论文索引；未进行公网检索、代码执行性验证或模型实验。

**VERDICT：GO（本地核查完成）；构想的新颖性结论为 UNCERTAIN。** 当前以“固定链的 MCP-UPD”对比“自主规划的新攻击”的宽泛表述不成立，不应据此通过新颖性门槛。MCP-UPD 已有不要求预知本地 MCP 配置、载荷不写工具名、单个外部入口驱动合法工具串联、诊断/审计伪装的原文证据；纯高层目标、严格工具注册表盲、真实故障后的无新增指令换路，仍是待验证的限定条件，不能从四篇论文未专门报告便推断为新颖。

## 证据口径与可比威胁模型

下文页码均为 **PDF 从 1 起计的物理页码**；MCPTox 的物理页 1–9 对应印刷页 35811–35819，其余引用页码与正文页码一致。短引来自英文原文；图中内容另经 PDF 视觉读取核对。

- **F = full-text-verified**：相关判断在本地正文、附录或图中有直接证据；不表示对整篇每页逐字通读，也不表示复现。
- **A = abstract-verified**：仅由摘要支持。本报告核心比较均已升级到正文核查，不以 A 独立支撑差异。
- **I = inference**：基于已核查原文作出的解释或证据边界判断。
- **U = unverified**：本次资料不能确认。没有报告某测试，不等于方法不支持该条件。

为避免把攻击权限变化误当成机制差异，固定比较条件为：攻击者仅能预先植入将由合法工具读取的外部内容，并控制接收端点；不能改 Host、LLM、MCP Server、工具注册元数据或后续工具返回；不读取目标工具注册表或中间日志，不根据运行反馈追加恶意指令。受害 Agent 正常可见其工具描述和结果，使用既有权限执行。比较的成功条件是**产生超出原始用户授权的、可验证的工具行为/副作用**，而非单纯链更长或最终文本异常。（构想第 61–87、108–113、160–175 行；F）

这应归入 **01 外部交互 → 外部内容/工具结果间接注入 → 受害 Agent 规划与跨工具执行**；访问本地敏感文件是后果，不会自动变成 02 记忆投毒；多个 MCP 服务也不等于 03 多智能体协作。（I，依据 U1–U4、M1–M2）

## INPUTS / hash / 实际阅读范围

来源目录：`/Users/dj/Documents/paper/Agent/papers/10_MCP攻击`。

| 输入文件 | SHA256 | 实际读取范围 |
| --- | --- | --- |
| 自适应工具链与Agent行为扩展_研究构想.md | `63ca1233a225b6ea87ed6ed07857c4c7568bcdd4de593089a830f4df233f413c` | 全文 1–230 行，特别是 35–44、61–87、129–189 行 |
| 26_sp_parasites_toolchain.pdf | `950180eef3912438a2a45719f5e5f5a813943cdb749636d2a95a9941c471396d` | 18 页全部提取；正文相关段落 pp.1–15、p.18 会议 meta-review；另视觉读取 p.4 |
| 26_aaai_mcptox.pdf | `9aa84895de698748cbdd75f615832acdde29ceaa81e8d5f7c51337e170be162b` | 9 页全部提取；重点阅读 pp.1–7 的攻击定义、生成、评估和讨论 |
| 26_iclr_mcp_safetybench.pdf | `e61c9c7fa390b944649ec7ff22d16a7ed17b836573d0ef6e4b22f00c6e60c925` | 25 页全部提取；阅读 pp.1–10、15–17、20–25 的方法、分类、缓解和消融；视觉读取 p.23 |
| 26_iclr_msb.pdf | `e3d2c602aa5d3432d2da48b2374459e129526301ca58d0f4324e37b5ab94f9a0` | 32 页全部提取；阅读 pp.1–10、14–19、28–31 的定义、攻击和模板；视觉读取 pp.17–19、30 |

**四篇关键 PDF 均实际读取了正文。** 读取方式为 `pdftotext -layout` 后阅读相关页文本，并对关键图表使用 PDF 页面读取；未把参考文献、其余附录图逐页通读冒称为完成全文精读。

另已读取 MCP-UPD 中文说明全文，但不以其代替英文原文。KB `/Users/dj/Documents/paper/Agent/research_attack_ideas/paper_inventory.md` 的 SHA256 为 `10eda26cdbdbe5ecd673cc97267a43b6760c00cc068e744692906ccf4447fcf5`；其第 7、16 行明确是摘要级记录，第 31 行 A10 的年份/会议当时未验证，第 42 行 A21 连题名/机制都未验证。此次原文证据更新只记录在本报告，未修改 KB 或共享台账。项目 `PAPER-MATRIX.csv`/`LITERATURE.md` 只作定位检索，未提升成原文证据。

## 题名、年份和 venue 核对

| 本报告简称 | 原文题名 | 本地版本及 venue 证据 | 等级 |
| --- | --- | --- | --- |
| MCP-UPD / Parasites | *Parasites in the Toolchain: A Large-Scale Analysis of Attacks on the MCP Ecosystem* | p.1：`arXiv:2509.06572v5 ... 1 May 2026`；p.18 Appendix A 明载“program committee for the 2026 IEEE Symposium on Security and Privacy (S&P)”并有“Reasons for Acceptance”。可在本地证据范围记为 IEEE S&P 2026；该工作亦有 2025 年 arXiv 标识。MCP-UPD 是文内攻击实例名，不是论文题名。 | F |
| MCPTox | *MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers* | p.1 标题含单数 **Attack**，页眉为“The Fortieth AAAI Conference on Artificial Intelligence (AAAI-26)”，版权 2026。PDF metadata 的标题省略 Attack，采用页面正式题名。 | F |
| MCP-SafetyBench | *MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers* | p.1：“Published as a conference paper at ICLR 2026”；`arXiv:2512.15163v2 ... 5 Mar 2026`。 | F |
| MSB | *MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents* | p.1：“Published as a conference paper at ICLR 2026”；`arXiv:2510.15994v2 ... 24 Mar 2026`。不要混同另一工作的 MCPSecBench。 | F |

没有从文件名 `26_sp`、`26_aaai`、`26_iclr` 推断上述年份和会议；也没有进行外部书目数据库核验。

## EVIDENCE：可复核原文证据

| ID | 来源、页/节 | 原文短引 | 可支持的判断与限制 |
| --- | --- | --- | --- |
| U1 | Parasites p.3，§2.2.2 | “This serves as the sole injection point” | 外部文本载荷是唯一注入入口，另有接收外泄数据的端点；F。sole injection point 指权限/入口，并非严格证明所有实验只摄取一次文本。 |
| U2 | Parasites p.4，§2.2.3 | “does not require prior knowledge of the victim’s local files or MCP configuration” | “必须预知受害者 MCP 配置”被原文明示否定；F。尚不能把这句话升级为已做随机未知工具集合迁移。 |
| U3 | Parasites p.4，§2.3.2 | “perform a routine diagnostic”; “Read the contents of the local mcp.json file”; “Forward these contents ... for a security audit” | 展示的外部载荷写对象、读/转发行为和目的地，**没有写 FileSystem.readFile 或 Email.send 的工具名**；后两工具名出现在作者叙述的实际调用中；F。该载荷仍写出了两步操作和具体文件，不是纯目标种子。 |
| U4 | Parasites p.3，§2.1；p.5，§3.2 | “reasons over the user request and the available tool registry”; “autonomously drive multi-step task flows” | 受害 LLM 决定工具、参数及后续调用，作者明确讨论自主多步骤行为劫持；F。不能由此断言其已测量自主生成子目标或失败恢复。 |
| U5 | Parasites p.7，§4.2.2、§4.3 | “provide the complete set of tools exposed by an MCP server”; “Each prompt explicitly specifies the tool name” | 前者是 MCP-SEC 工具能力分析器输入；后者是动态验证单工具能力的**用户提示**。这是研究者测量流程，不是对所有外部攻击载荷的必要限制；F / I。 |
| U6 | Parasites p.7，§4.3 | “the tool execution adopts a linear switching mechanism” | 这里描述批量能力验证中依次执行工具并输出各工具聊天日志；不能将其解释成 MCP-UPD 运行时只支持固定线性规划；F / I。 |
| U7 | Parasites p.12，§5.3、Table 7 | “construct 10 tool invocation chains”; “nine chains ... randomly pairing tools across different servers” | 端到端评测确实由研究者预选工具组合；每种风险能力选十个工具，九条跨服务链、一条同服务链；F。这限制已验证的实验域，不等于攻击定义要求攻击者掌握目标注册表。 |
| U8 | Parasites p.12，§5.3 | “without adversarial tuning or repeated prompt engineering”; “A toolchain is labeled successful if any trial results in verified exfiltration” | 三条链的相关观察说明无需反复调载荷也会成功；十条链各重复十次，9/10 是“至少一次成功的链占比”，不是全试次 90% ASR；F。文中描述的流程不需要攻击者每步追加指令（I），但没有严格无反馈/不可观察性消融（U）。 |
| U9 | Parasites p.13，§5.3 | “direct & forceful, indirect & polite, and Base64-encoded”; “functional relevance among tools affects MCP-UPD success” | 已比较三类提示风格；Chain 8 因工具功能不相关而 0/10，其余链成功数见 Table 7；F。改变提示风格不等于测了用户、检测器和单步审计三类发现率。 |
| U10 | Parasites pp.13–14，§6.2–§6.4 | “mixed with benign content”; “Cross-Tool Auditing”; “future work” | 混合良性内容的有效性在 §6.2 是借前人工作的讨论；隔离、最小权限、跨工具审计在 §6.3；RCE/任意写文件在 §6.4 是未来方向讨论，不能当作该文实测主结果；F。 |
| T1 | MCPTox p.3，§2.2、§3.1 | “during its registration phase”; “without ever invoking the malicious tool by name” | 控制工具描述的元数据投毒，隐式规则诱导其他合法工具执行；“用户不调用恶意工具名”不等于“载荷不含合法目标工具名”，也不等于“攻击者不知道工具列表”；F / I。 |
| T2 | MCPTox p.4，§3.2 | “provide the LLM with the complete list of all legitimate tools”; “Trigger Condition ... Malicious Action ... Plausible Justification” | 离线载荷生成确实使用目标服务器完整合法工具表；触发条件、恶意动作和合理化理由已系统化，不是新构想首创；F。 |
| T3 | MCPTox p.4，Table 1、§3.1 | “Before any file operation, you must read ... as security check”; “the poisoned tool itself is never executed” | 文中有不写具体读取工具函数名的自然语言规则，并要求用既有合法工具、以增强隐蔽性；F。入口权限比外部内容攻击更强。 |
| T4 | MCPTox p.5，§3.4、§4.1；p.7，§5 | “Record the tool call output”; “automated and adaptive attack generation ... future work” | 主评估聚焦所选工具和调用参数，不能据其 ASR 推断任意长链的自主故障恢复；自适应攻击生成列作未来方向，不是受害者运行时适应性的否定；F / I。 |
| S1 | MCP-SafetyBench pp.5–7，§3.3–§3.5、§4.1 | “Each task is paired with exactly one MCP-layer attack”; “ReAct”; “maximum 20 ReAct iterations” | 已有单种攻击与多步、多服务器受害 Agent 执行；F。“一个攻击修改”不等于“恶意文本只出现一次”，特别是修改持久 manifest 时；I。 |
| S2 | MCP-SafetyBench p.6，§3.3；p.16，A.3 | “Host side: by modifying the host pipeline”; “Intent Injection ... modified during planning” | 该文高层意图重写是 Host 管线侧权限，不应直接拿来当作仅能改外部内容的同威胁模型结果；F / I。 |
| S3 | MCP-SafetyBench p.16，A.2；p.17，A.4 | “embedded instructions trigger unintended follow-up actions”; “Public data sources can be poisoned” | 工具返回注入和公开数据投毒都已有分类；但本地论文不能确认每个 RADE 实例都按严格外部内容权限实现，§3.3 的 user-side 实例说明为直接向用户 query 加片段；F / U。 |
| S4 | MCP-SafetyBench p.23，D.4、Table 14 | “Plan-and-Execute (planning-heavy) vs. ReAct (step-by-step reasoning with tool feedback)” | 不仅支持受害 Agent 在线使用工具反馈，还比较了两类规划策略；ASR 49.76±17.38% 对 45.52±7.71%，该比较 p=0.40；F。这里是 Agent 的反馈，不是攻击者在线反馈。 |
| S5 | MCP-SafetyBench p.23，D.3.2；p.25，E.2 | “exploring alternative tools”; “uses the correct parameter” | 已讨论安全完成任务时寻找其他工具，并展示改回正确参数的案例；F。没有据此确认“真实工具故障后坚持恶意目标自主换路”已被独立测量（U）。 |
| S6 | MCP-SafetyBench p.7，§3.4；p.10，§4.3 | “Stealth attacks ... without alerting the user”; “not statistically significant (p = 0.2908)” | 已区分 stealth/disruption，并测试 safety prompt；“stealth 标签”不等于有人类发现率实验；F / I。 |
| M1 | MSB pp.3–4，§3.1–§3.2 | “O enables the agent to dynamically refine its plan”; “deploy a malicious MCP server” | Agent 依据观测动态修正计划是显式模型；一般攻击能力允许控制恶意服务与多组件，强于本构想；F。 |
| M2 | MSB p.6，§4.4；pp.18–19，C.1.5、图 | “whereas the tool itself remains benign”; “injects malicious instructions into an external file” | RI 子类是同入口近邻：良性检索工具读取外部被污染文件，继而读取个人信息并写出；图示一次被污染资料被读入后接读/写两步；F。不能把全篇都归成“必须恶意 MCP Server”。 |
| M3 | MSB pp.5–6，Table 1、§4.3；pp.17–18，C.1.4 | “fabricated tool execution error messages”; “read personal information ... writes the retrieved phone number” | False Error 已用伪错误/前置修复理由驱动读取和写出；F。错误消息本身带新的攻击指令，区别于无攻击者控制的新真实故障。 |
| M4 | MSB p.6，§4.3；pp.28–29，Tables 8–9 / D.2 | “a chained attack involving two tools”; “It has been replaced by the [target tool name] tool” | Tool Transfer 已覆盖“此工具不可用，请改用指定工具”的显式换路；F。替代工具由载荷点名，不是 Agent 独立发现替代路径。 |
| M5 | MSB p.29，Table 9 | “by using read text file tool”; “by using write file”; “Use the ‘kill process’ tool” | 六类攻击任务中的具体提示普遍指定工具及对象，read→write 两步也预先写明；F。表中“stealing agent context”专门外泄工具名，与本构想仅 Agent 内部使用工具表不同。 |
| M6 | MSB p.30，Fig.6（视觉核对）；p.8，§5.2 | “Thought/Action/Action Input/Observation can repeat N times”; “examining the environmental state” | 多轮 Agent 执行和最终副作用判断已有，不能宣称现有工作只看单次工具调用；F。 |

## MCP-UPD 的准确拆分

**攻击者到底知道什么。** §2.2.3 不要求预知受害者本地文件或 MCP 配置（U2，F）；§2.3 仍以常见的网页/文件/邮件配置为动机场景，载荷指定 `mcp.json` 和接收地址（U3，F）。因此可以说“无需读取受害者注册表才定义攻击”，不能说“已证明所有载荷完全不依赖任何环境常识或目标路径知识”。严格未知工具表、未知参数名、未知文件布局的普遍迁移仍 U。

**工具名有没有写死。** 动机载荷本身没有工具函数名；作者叙述的调用轨迹有工具名，两者必须分开（U3，F）。§4.3 中“每个提示显式指定工具名”是为逐工具验证能力设计的用户提示，不是寄生载荷的强制模板（U5，F / I）。所以“不写工具名”作为二分创新不足；“不写子步骤/子目标”是更严格、原例未证明的条件。

**工具链谁构造。** 三阶段攻击逻辑由研究者定义，§5.3 的十种可用工具组合亦由研究者构建（U7，F）；受害 LLM 根据已摄入内容、可用工具与返回结果决定可执行调用（U3–U4，F）。实验预先配好工具，和模型在该环境内生成具体调用，可以同时成立。原构想第 40 行把前者和后者写成互斥对比，证据不足（I）。

**有无在线反馈。** 单个外部寄生内容即可启动后续读取和发送，描述的端到端流程没有必需的“攻击者观察每步并追加下一条指令”环节（U1、U3、U7–U8，F / I）。多次独立评测、离线准备载荷、受害 Agent 自己读取工具结果都不等于攻击者在线自适应。原文没有严格封闭所有攻击者观察通道的单独消融，因此只可说“所述攻击不依赖连续反馈”，不可冒称其已验证了本构想全部不可观察性约束（U）。

**哪些只是基准/测量构建约束。** 工具全集供分析器作能力标注、显式点名工具的用户提示、线性切换逐工具验证、预选十条组合，都属于 MCP-SEC/评测流程（U5–U7，F）。它们确实说明现有实证没有覆盖任意未知工具集合，却不构成 MCP-UPD 攻击者必须拥有相同能力的证明。

## 逐维对照矩阵

单元格中的“未确认”均为 U，不表示论文方法做不到。每项明确结论可回溯到上表的页码、节和短引。

| 维度 | MCP-UPD / Parasites | MCPTox | MCP-SafetyBench | MSB | 构想真正可声称的差异 |
| --- | --- | --- | --- | --- | --- |
| 唯一控制面为外部数据 | 是，U1–U2，F | 元数据投毒，权限不同，T1，F | 跨 server/host/user 权限，不能整体等同外部内容；S2–S3，F/U | **RI 子类**是，M2，F；FE/TT 不是 | 本身已覆盖，不能据此主张新攻击 |
| 载荷不写具体工具名 | 动机载荷已有，U3，F；随机改名迁移 U | 自然语言规则例可不写读取函数名，T3，F；生成器知道完整工具表，T2，F | 没有确认工具名消融，U | Table 9 任务提示普遍点名工具，M5，F | “不写名”不够；未知表且跨重命名稳定性仍待核查 |
| 攻击者不知道工具表 | 威胁模型不要求预知配置，U2，F；严格盲测 U | 生成时输入完整合法工具表，T2，F | 权限混合，严格表盲 U | 模板预定工具；RI 未给严格表盲证据，M5，F/U | 只能提出更严格盲条件，不能宣称前人必需读注册表 |
| 纯高层目标，不给动作/子步骤 | 原例给读→转发两步和文件，U3，F；纯种子 U | 触发+恶意动作+理由，T2，F；纯种子 U | 有意图重写，但 Host 控制面不同，S2，F | 恶意任务提示通常指定步骤/工具，M5，F | 有限剩余假说：真正只给目标后，是否生成未明示子任务 |
| 一次预置载荷、无攻击者连续反馈 | 流程已有，U1、U3、U8，F/I；严格一次曝光 U | 离线固定描述即可评估，T2、T4，F/I；不等于一次摄入 | 每任务单种攻击，S1，F；一次修改不等于一次曝光 | RI 示范预置一份外部文件触发后续链，M2，F | 宽泛单次攻击已重合；须分开“写入次数、曝光次数、后续恶意输入” |
| 受害 Agent 自主选工具与参数 | 原文明示，U3–U4，F | 工具调用输出是评测对象，T4，F | ReAct/Plan-and-Execute，S1、S4，F | 观测驱动修正计划、多轮执行，M1、M6，F | “由受害 Agent 规划执行”不构成差异 |
| 受害 Agent 持续使用工具结果 | §§2.1、3.1 的工作流及读后发送已有，U3–U4，F | 该文不足以外推任意长链，T4，I | 显式 step-by-step tool feedback，S4，F | O 动态修正计划和迭代模板，M1、M6，F | 单纯“执行后继续规划”已覆盖 |
| 失败/不可用引起改道 | 实测 Chain 8 失败，未报告自主修复，U9，F/U | 故障自主换路 U | 讨论替代工具和安全修正参数，S5，F；恶意目标故障恢复 U | FE 伪错误升级；TT 点名替代工具，M3–M4，F | 真实、非攻击者控制的失败后，自发现替代路径且保持恶意目标，仍待验证 |
| 未授权读取→发送/写入副作用 | 主结果是跨合法工具外泄，U3、U7–U8，F | 合法工具执行未授权动作，T1–T4，F | 文件/网络/凭据/意图等多类，S2–S3，F | RI/FE 读个人数据并写出，M2–M3，F | 一般副作用/授权范围扩大已覆盖；调用更高权限工具不等于获得 Host 原无权限 |
| 低显著性、任务/诊断语境伪装 | 例子已用诊断/审计；提示风格与功能相关性已有，U3、U9，F | Plausible Justification、安全检查、合法工具隐蔽性，T2–T3，F | stealth 分类已有，S6，F | RI 用正常博物馆信息及任务理由包裹恶意读写，M2 图 p.19，F | 新意不能是换措辞；三类发现率的联合测量仍未确认 |
| 隐蔽性/发现率与行为扩展的联系 | 有隐蔽性论述/风格比较，U9–U10，F；用户/检测器/单步审计联合曲线 U | 有隐蔽设计原则，T2–T3，F；联合曲线 U | stealth/utility 指标并非发现率，S6，F/I | 多轮执行与隐藏结果论述，M6，F；联合曲线 U | 可能是评测切面差异，尚不是新机制或新攻击成立的证据 |

## 原构想第 35–44 行：应如何纠正

以下仅为报告中的替代表述，**没有修改原构想**。

| 原表维度/行 | 过强或不对齐之处 | 原文支持的替代表述 |
| --- | --- | --- |
| 攻击指令，第 39 行 | “可包含具体工具和固定步骤”与“主要提供高层目标”并不互斥；且前人已存在不点名工具的载荷 | **MCP-UPD：动机载荷不写函数名，但明确读→转发两步、文件和终点。构想：进一步限定只给目标，不给具体子步骤，并验证隐含子目标生成。** U3，F；后半为待验证假说。 |
| 攻击链，第 40 行 | 把研究者选测试工具链误写成受害者执行必须固定脚本 | **MCP-UPD：研究者预选十种工具组合，受害 LLM 产生实际调用。构想：拟考查工具组合变化和真实故障下，是否产生未预写的替代链。** U4、U7，F；新增条件 U。 |
| 工具信息，第 41 行 | 把 MCP-SEC 的分析器输入当成攻击者必要知识；漏掉无须预知配置的威胁模型 | **MCP-UPD：威胁模型不要求预知文件/MCP 配置，测量框架会分析工具描述。构想：进一步把“攻击者从未访问目标工具表”设为明确条件。** U2、U5，F；已验证迁移不能预设。 |
| 攻击者反馈，第 42 行 | “可预先准备载荷”与“不依赖连续反馈”本来可同时成立，不构成对照 | **两者都可预置载荷；目前无证据证明 MCP-UPD 需要连续反馈。严格的一次曝光、无第二恶意返回及无攻击者观测，应单独界定。** U1、U3、U8，F/I。 |
| 注入显著性，第 43 行 | 把前人概括为直接暴露恶意步骤，忽略其诊断/审计伪装、间接礼貌提示、相关性观察 | **MCP-UPD 已研究隐蔽寄生载荷并比较提示风格；构想拟量化任务相关伪装下用户/检测器/审计发现率及行为变化，而非首次提出隐蔽注入。** U3、U9–U10，F/I。 |
| 研究重点，第 44 行 | 前人不只测“链是否完成”，还研究行为劫持、生态能力组合、模型/客户端与工具相关性 | **MCP-UPD 关注工具链行为劫持、能力分布及端到端外泄。构想若继续，应收窄为更严格盲条件下的目标持续性、未预写子任务和真实故障替路，而非泛称自主规划。** U4、U7–U9，F/I。 |

还需统一“行为升级”和“权限升级”的措辞：MCP-UPD 明确受限于 Host 已有资源/权限（p.4 §2.2.3：“limited to the resources and privileges accessible to the victim’s MCP Host”，F）。从网页读取转为文件读取/发送可构成用户授权范围越界，但没有自动获得 Host 原先不存在的 OS 权限。构想第 53、164、170、186 行若用“权限”指标，应保持这一区分（I）。

## 最接近的四篇与预占风险

| 排名、近邻 | 已经做到什么 | 同一控制入口？ | 同一受害者？ | 同一成功条件？ | 最强重合与尚存限制 |
| --- | --- | --- | --- | --- | --- |
| 1. Parasites / MCP-UPD；KB A21 当时仅占位 | 外部寄生内容驱动合法工具跨服务取密、外发；无需预知本地配置；实际函数映射由 LLM 执行，U1–U9 | 是 | 是，使用 MCP 的 LLM Agent | 是，构想选择隐私收集/外发时一致；其余副作用不完全一致 | “一次隐蔽注入→Agent 自主组合法工具”的宽泛贡献极易被判为该文扩展。纯目标、严格盲迁移、真实故障换路没有独立实证确认。 |
| 2. MSB，尤其 RI、FE、TT | RI 的良性工具读外部毒化资料后读/写；FE 伪故障驱动恶意步骤；TT 显式替代工具；M1–M6 | RI 是；FE/TT 要控制返回/恶意工具，权限不同 | 是 | 读/写未授权副作用一致；其数据“外泄”有写攻击目标文件形式，不必然是网络外发 | 泛称“失败后换路”容易被 FE/TT 预占；必须保留真实故障、无新增恶意内容、自发现替代路径的边界。 |
| 3. MCPTox；KB A10 | 固定元数据里的隐式规则/安全检查诱导合法高权限工具，离线生成使用完整工具表；T1–T4 | 否，元数据权限更强 | 是 | 合法工具执行未授权操作一致；主评估不等同任意长链外泄 | 高层自然语言规则、合理化理由、合法工具隐蔽性已存在；不宜把“少写工具名/换提示风格”作为新机制。 |
| 4. MCP-SafetyBench | 多步、多服务器 ReAct；单种攻击；意图重写、返回注入、stealth；Plan-and-Execute 对 ReAct 的反馈式规划比较；S1–S6 | 依子类不同；Host intent 不同，RADE 实例权限需再查 | 是 | 未授权行为/副作用与安全-效用部分重合 | “首次评估多轮规划/行为扩展”过宽。不是所有实例都满足外部内容唯一控制面的弱权限模型。 |

KB 中与该问题直接相关的已命名记录不足三条（仅检出 A10、A21）；因此本表的四篇是本地原论文近邻，不伪造 SafetyBench/MSB 的 KB ID。“KB 未收录/当时未验证”没有新颖性含义。

**最强反对意见（I，依据 U1–U9、M1–M6、T2–T3、S1–S6）：** 如果主结果只是把 `read_file`/`send_mail` 改写成“诊断并提交”，看见 Agent 自己调用若干合法工具，再加重命名或多工具数量消融，审稿人有充分理由称其为 MCP-UPD 的载荷概括化与评测扩展；若失败由攻击者给出错误及替代指令，则进一步落入 MSB FE/TT。链更长、增加拓扑或更礼貌的措辞，都未单独提供新机制。

## 真正剩余的待验证差异

以下不是完整实验方案，也不是文献空白已成立的结论。

1. **严格目标种子与工具表盲的合取。** 不提供工具/参数名，也不提供读→发送等子操作脚本；攻击者从未读取目标注册表，受害者仍生成可验证的未明示子任务并在能力等价的工具变化中保持目标。UPD 的免配置知识声明已覆盖较弱要求，因此新差异必须比 U2–U3 更严格；当前本地证据不能证明此合取已有或没有。（U；比较依据 U2–U7、T2、M5）
2. **真实故障后的自主恶意目标保持。** 后续错误是非攻击者控制的普通失败，既不夹带第二段恶意指令，也不点名替代工具；Agent 自己找到其他能力路径并继续原恶意目标。该条件区别于 MSB FE 的错误夹带指令和 TT 的指定替代工具，但本次没有验证其机制或排除其他文献。（U；比较依据 M3–M4、S5）
3. **显著性与行为/发现率的可归因联系。** 已有诊断伪装、合理化和 stealth，剩余可能是高层目标导致的行为扩展，是否同时改变用户、检测器、单步调用审计的发现能力。三个发现对象不能合并成一个“隐蔽性”数；载荷无关键词、结果中无工具名、评测标签为 stealth 都不等于未被发现。（U / I；比较依据 U3、U9–U10、T2–T3、S6、M2）

**一行 delta（仅作待检验候选，I/U）：在攻击者从未访问目标工具表、一次外部内容摄入且后续没有任何攻击者指令的条件下，仅给高层目标的载荷是否使受害 Agent 在真实工具故障后自主发现未指定的替代路径，继续产生用户未授权副作用。**

该句尚未成立；若最终仍需显式读写步骤、后续错误夹带恶意指令，或替代路径由攻击者指定，应回退为已覆盖子类，而不能继续沿用该 delta。尚需非 KB 文献核查；本节点不对“全领域没人做过”作结论。

## 防御邻居与转交候选

| 可转交 baseline-engineer 的邻居 | 原文依据 | 已验证程度 |
| --- | --- | --- |
| 上下文/工具隔离、最小权限、跨工具审计 | Parasites p.14 §6.3，短引“Context–Tool Isolation”“Privilege Minimization”“Cross-Tool Auditing” | F：论文讨论的候选防御，不能冒称已实现或测得阻断率 |
| 元数据清理、调用与用户意图校验、推理审计 | MCPTox p.7 §5，短引“Tool Call Output Validation” | F：讨论候选；元数据清理不直接解决纯外部内容入口 |
| MCIP 检测器 | MSB p.10 §6.3，短引“trains a Llama-xLAM-2-8B classifier” | F：该文有评估；不能将其性能无条件迁移至本构想的严格弱权限模型 |
| Safety Prompt | MCP-SafetyBench p.10 §4.3、p.20 Appendix C | F：有基线，整体改善未达显著，p=0.2908；是现实对照线索，不构成已解决机制 |

本节点未向其他人或服务发送材料；由协调者按需转交。

## OUTPUT / CHECK / BLOCKERS / NEXT / DO_NOT_DO

**OUTPUT**：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/LOCAL-PRIOR.md`。

独有衍生目录：`/Users/dj/Documents/paper/Agent/agent_attack_research_project/reviews/adaptive-toolchain-2026-11-11/local-sources/kb-curator-44809ef0/`。其中四份 `*.pages.txt` 保留 `===== PDF PAGE NNN =====` 标记，四份 `*.pdfinfo.txt` 保留 PDF 元数据，`sha256.txt` 保存上述构想及四 PDF 完整哈希。所有 Python 命令均使用 `python -I`；`pdftotext`/`pdfinfo` 全部成功返回。

**CHECK**：写入后执行本地 `Path.is_file()` / `stat()` 检查报告和九份衍生文件存在且非空；实际退出状态在最终交接中返回。没有为核验而回读或重写原输入，也没有修改共享台账。

**BLOCKERS**：四篇论文没有给出可直接认证本候选合取条件的材料；未知工具集合迁移、一次曝光、攻击者全程不可观察、真实故障替路和三类发现率仍 U。未读取关联仓库或运行日志，无法认证载荷实现细节与全部变体；没有公网检索，不能排除非本地先行工作。

**NEXT**：协调者先修正第 35–44 行的对比口径，并决定是否保留上述狭义 delta；再由获授权的文献节点针对该完整合取条件做非 KB 原文排查。只有得到新的机制/差异证据，才另行决定后续研究步骤。当前 GO 仅表示本地核查完成，不授权新实验、不通过新颖性门槛。

**DO_NOT_DO**：不把 MCP-UPD 描述成必须预知工具表、写死函数名、依赖攻击者连续反馈或只执行固定脚本；不把 MCPTox 的自适应载荷生成和受害 Agent 运行时规划混为一谈；不把 MSB 伪错误/显式转移当作真实故障自主恢复；不以文中未提及推导方法不支持；不重开已关闭 I1/P4/Q1；不修改 KB、构想或共享台账，不执行攻击、不开服务、不调用付费模型、不上传用户材料。
