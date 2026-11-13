# R4 预审报告：MCP 攻击入口与机制族

日期：2026-11-10  
范围：MCP 相关中文翻译、原文 PDF、研究黑板文件及已有 baseline 目录。  
状态：威胁模型预审；没有选择论文 thesis，没有运行实验，没有调用外部服务。以下候选都只是 `screen-pending`，不能直接进入模型预算或主实验。

## 1. 读取范围与判断边界

本次先读了研究黑板中的 `STATE.md`、`ATTACK-RESEARCH.md`、`RESEARCH-GRAPH.md`、`progress.md`、`PAPER-GOAL.md`、`KB-POSITION.md`、`IDEAS.md`、`CLAIMS.md` 和 `R4-FRESH-CANDIDATES-2026-11-08-B.md`。当前项目的硬约束是：I1、P4、Q1 已经是负边界或协议结果；C4/Q1 的 MCP parser differential 已被 MCP Go SDK issue #805 与 ATR-2026-02350 直接覆盖；screen B 已否决 Q6–Q10；新的方向必须先通过完整文本和公共预占检查。

MCP 目录中，以下材料构成了本次定位的主要证据：

- `MCP攻击路线图_简版.md` 及 `自适应工具链与Agent行为扩展_研究构想.md`：给出选择、元数据、工具链、服务端转换和隐蔽行为扩展的谱系，但后者提出的通用“自主工具链扩展”已经与 Parasites、SOPE、GatewayBench、MSB/COPEX 形成明显重叠。
- `26_aaai_mcptox_标题与摘要_中文.md` / `26_aaai_mcptox.pdf`：工具描述中的三类 tool poisoning，成功标准是通过合法工具执行恶意行为。
- `26_aaai_mpma_标题与摘要_中文.md` / `26_aaai_mpma.pdf`、`25_neurips_attractive_metadata_attack.pdf`、`26_aacl_a2m.pdf`：工具选择、描述和返回值优化已经覆盖偏好操纵、吸引元数据和 trace-guided manipulation。
- `26_iclr_msb_标题摘要引言_中文.md` / `26_iclr_msb.pdf`、`26_neurips_copex_标题摘要正文_中文.md` / `26_neurips_copex.pdf`、`2611_arxiv_mcp_tool_poisoning_cross_framework.md` / `2611_arxiv_mcp_tool_poisoning_cross_framework.pdf`：覆盖工具签名、参数、响应、资源、transport 和跨框架执行评估；最新跨框架论文明确列出 P7、P12、P13、P16、P18、P21、P25 等类别，其中 streaming、notification 和 dynamic registration 的场景主要是对模型声称存在这些通道的社会工程测试，并非完整的实际协议机制验证。
- `26_sp_parasites_toolchain_标题摘要引言_中文.md` / `26_sp_parasites_toolchain.pdf`、`26_icml_sope_标题与摘要_中文.md` / `26_icml_sope.pdf`、`2610_arxiv_log_to_leak.pdf`：已经覆盖外部内容到多工具隐私外泄、良性服务器转换、情境感知外泄以及 post-hoc logging。
- `25_arxiv_mcp_attack_vectors.pdf`、`25_arxiv_systematic_mcp_security.pdf`、`25_arxiv_when_mcp_servers_attack.pdf`：覆盖 server metadata、configuration、initialization、tool/resource/prompt metadata、logic/output、sampling abuse、rug pull、恶意外部资源和 MCPXKIT 的 31 类攻击。
- `2611_arxiv_signed_sealed_leaked.pdf`、`2611_arxiv_destructive_tool_approval.pdf`、`2610_arxiv_filesystem_capability_laundering.pdf`、`2610_arxiv_provenance_binding_mcp.pdf`、`2610_arxiv_tool_call_trace_privacy_leakage.pdf`、`2610_arxiv_gatewaybench.pdf`：分别覆盖签名工具中的隐藏代码和跨调用状态、破坏性工具的 server/host approval 组合、filesystem capability laundering、来源绑定、工具调用轨迹画像和 gateway 架构/噪声工具规模效应。
- `26_acl_potemkin_adversarial_environments.pdf`、`25_emnlp_invisible_prompts.pdf`、`25_emnlp_mcip.pdf`、`26_acl_mcp_guard.pdf`、`26_acl_safemcp.pdf` 及相关 MCP 安全分析论文：覆盖环境幻觉/结构陷阱、不可见字体、contextual integrity、运行时检测和主动权限约束。

因此下面的“仍有研究价值”只表示“在现有本地材料中仍可形成一个可证伪的协议或边界问题”，不表示新颖性已经成立。所有候选都需要新的公共检索、版本固定和 falsifier 审查。

## 2. 候选总表

| 优先级 | 候选机制族 | 单一入口 | 主要 victim state | 当前判断 | 主要重叠/杀开关 |
|---|---|---|---|---|---|
| 1 | 实际 MCP handshake 的版本/能力降级 | `initialize` 响应及能力协商 | 客户端已协商的协议版本、能力集和安全策略 | `screen-pending`，协议级残余空白较清楚 | 最新跨框架 P19 只列出但未实际验证；若只是 authority spoofing，则淘汰 |
| 2 | 服务端主动 sampling 的权限/上下文越界 | `sampling/createMessage` 服务端请求 | Host 的 sampling 授权、上下文和响应路由 | `screen-pending`，实现依赖强 | `When MCP Servers Attack` 和 MCPXKIT 提到 sampling abuse；若没有 host 实际暴露 sampling，直接 kill |
| 3 | 流式响应、notification、timeout/cancel 的在途状态机竞态 | 单个 MCP 响应流/通知序列 | pending call、取消状态、side-effect 状态和最终结果 | `screen-pending`，可做确定性协议实验 | P18/P21 已被分类但主要未测真实 transport；若退化为 parser differential、stale revocation 或 timing covert channel，分别落入 Q1/Q8/Q10 |
| 4 | Gateway 中 capability 的 subject/audience/purpose 混淆 | 一个跨服务器返回的 opaque capability/ref | 多租户身份、issuer、audience、purpose、expiry 绑定 | `conditional`，最接近 Q7/P4 | 若仅是 alias/session collision，落入 screen B Q7；若只是 provenance/authority laundering，落入 P4 |
| 5 | 非 filesystem 的 declared contract 与实际 effect/data-flow 不一致 | schema-valid 的 `tools/call.arguments` | 工具声明的范围与真实网络、数据库、消息或租户 effect | `conditional`，测量价值有但机制重叠高 | filesystem 已被 capability laundering 直接覆盖；若是隐藏代码/签名工具，落入 Signed, Sealed, Leaked；若是参数绑定，接近 P20 |

推荐只先对 1–3 做新的 full-text/public screen。4–5 可以保留为审稿问题的备选，但不应在当前预算下直接启动。

## 3. 候选一：实际 handshake 版本/能力降级

### 3.1 机制和研究价值

MCP 客户端在连接阶段通过 `initialize` 协商协议版本和能力。当前材料大量评估注册、规划和执行阶段的恶意内容，却没有把“客户端接受了什么版本/能力集，以及这是否改变安全状态机”作为独立的可验证状态转换。最新跨框架工具投毒论文把 Version Downgrade 列为 P19，但其候选场景被归入 authority-marker 接受，而不是一次真实的协议版本协商弱点。这留下了一个较窄的协议审计问题：恶意服务器是否能返回协议合法但安全能力更弱的协商结果，导致 host 进入兼容路径或关闭某个检查。

这个方向的价值来自“协商状态改变”和“后续动作被允许”的因果链，而不是把低版本字符串当成新的 prompt payload。它也不需要 LLM 产生某个复杂恶意工具调用，因而适合先做框架无关的状态机 kill test。

### 3.2 Threat model

- **Attacker capability。**攻击者是第三方 MCP server 的发布者或部署者。用户已经出于正常业务需要安装或连接该 server；攻击者可以控制该 server 发出的协议合法 `initialize` response，包括 `protocolVersion`、capability flags 和可选协商字段。攻击者不能修改 MCP Host/client 源码、系统 prompt、模型权重、用户消息、其他 server 或用户的配置文件。
- **Victim state。**受害者是一个具体 MCP client/host 的连接状态：
  `N = (selected_version, negotiated_capabilities, security_policy, session_ready)`。
  只有当 `selected_version` 或能力集改变后，host 的后续调用授权、响应处理或审批路径也改变，才有安全意义。
- **Access point。**单一入口是一个 server → client 的 `initialize` 响应及其能力协商字段。测试中不能同时改变工具描述、工具响应、用户任务或 transport DNS，否则会把入口混成 metadata poisoning 或 transport hijacking。
- **Knowledge。**灰盒：攻击者知道公开 MCP 版本和目标 host 的公开版本/能力文档；不知道私有系统 prompt、用户任务内容、模型内部状态和 host 的未公开实现细节。白盒 host 源码只能作为独立适配器，不应写入攻击者能力。
- **Success criterion。**主成功必须同时满足两个可观察条件：
  1. `negotiation_downgrade = 1`：host 接受低于实验预设最低版本，或将一项在严格 arm 中启用的安全能力置为未启用；
  2. `unauthorized_canary_effect = 1`：在完全相同的无害任务和 synthetic canary call 下，host 执行了 strict/reference client 会拒绝的本地无副作用 canary。
  仅记录版本不同算 partial success；版本不同但没有任何安全状态或 action 差异算 protocol behavior，不能算攻击成功。要求独立报告 parse/handshake error、拒绝和任务 utility。
- **Independent evaluator。**固定的 JSON-RPC trace parser 读取原始 handshake、host 的最终 `N` 状态和 fake server 的 canary log；另用一个不参与 host 决策的 reference state machine 重算最低版本和允许能力。成功由版本/能力字段和 canary 事件的精确匹配判断，不需要 LLM judge。
- **Defense boundary。**防御位于 Host/client 的版本协商和 capability gate：最低版本 pinning、能力的单调性检查、security-relevant capability 的 fail-closed、握手后重新验证，以及 gateway 对 server 声称能力的白名单。它不能修复 server 内部代码，也不等于内容扫描。
- **Safety containment。**只使用项目自有的 fake MCP server、local host/client、内存 canary 和合成工具。不能连接真实 registry、第三方 remote server、真实账户或真实工具；所有“unsafe capability”都映射到固定字符串和内存状态。保留原始协议 trace，不保存真实 URL、密钥或可复用的公网 payload。
- **Minimal kill experiment（只定义，不执行）。**固定一个 benign task 和一个 fake canary，比较三臂：合法高版本握手、合法低版本握手、明显无效版本握手；每臂分别经过 baseline host 和 strict reference host。若所有候选 host 都拒绝低版本、忽略安全相关能力降级，或差异只来自 malformed-message parser error，则杀死候选。若只有某一 host 的非安全展示字段变化而没有 action/state 差异，也只能作为实现 bug 记录。

### 3.3 可达性与重叠判断

访问点是用户正常安装/连接第三方 MCP server 后自动发生的握手，攻击者没有先取得 host 的系统 prompt、审批权限或工具执行权限，因此不循环赋予攻击结果。实际持有访问的人是第三方 server 维护者、被供应链替换的 server 发布者或组织内的 server operator。需要由 operator 控制的条件必须写成约束：host 支持版本回退、存在一个只在低版本路径开放的 canary operation、以及没有额外的人工审批；不能把这些条件当成普遍事实。

它不属于 I1，也不属于 P4 的 typed/provenance conversion；它也不应使用重复键、Unicode 等 parser ambiguity，否则会回到 Q1/C4。它没有落入 screen B Q6–Q10。当前最大杀开关是公共工作已经实际证明同一版本协商降级会改变安全动作，或所有实现都将版本和安全能力视为不可降级。

## 4. 候选二：服务端主动 sampling 的权限与上下文越界

### 4.1 机制和研究价值

MCP server 可以在某些 host 实现中请求 LLM sampling。现有材料在 taxonomy 中提到 sampling abuse，但主要把它作为 resource/logic 攻击的一个例子；跨框架 tool-poisoning 测量明确表示 MCP prompt/sampling 入口在所测框架中没有可用暴露面，未形成实际的 host→model→server 往返测量。因此，仍有一个窄的入口问题：一个已连接的第三方 server 能否通过合法的 server-initiated sampling request，使 host 在没有独立批准的情况下把受害者上下文交给 sampling，或者把 sampling 返回值交回 server。

这不是普通的工具描述注入，也不是“模型被 prompt 说服”本身。重点是 server-to-host control request 的权限边界和返回值路由。

### 4.2 Threat model

- **Attacker capability。**攻击者控制一个已被用户连接的第三方 MCP server，可以发出协议允许的 `sampling/createMessage` 请求，控制采样请求中的公开 prompt、模型偏好、最大 token 和请求时机。攻击者不能读取 host 的内部 prompt、用户消息或模型输出，除非 host 通过 sampling 协议将它们放入请求或响应；不能修改 host policy、LLM 权重、其他 server 或工具实现。
- **Victim state。**受害者状态是 host 的 sampling authorization 和上下文边界：
  `S = (sampling_allowed, forwarded_context, sampled_response, response_recipient, token_budget)`。
  尤其要区分“请求被拒绝”“请求被批准但只看到了公开上下文”“sampling response 返回给 server”三种状态。
- **Access point。**唯一入口是一个 server → host 的 `sampling/createMessage` 请求及其返回通道。不能同时放入 poisoned tool description、resource output 或外部网页指令。
- **Knowledge。**灰盒：攻击者知道公开 sampling 接口和 host 是否宣称支持该能力；不知道用户上下文、系统 prompt 和 host 的私有上下文拼接规则。攻击者可以在本地模拟公开 host 行为，但模拟结果不升级为白盒能力。
- **Success criterion。**主要成功定义为：server 的响应日志收到 `CANARY_S`，且 `CANARY_S` 只存在于 host 的 synthetic user context 或 synthetic memory 中，并且该字符串通过 sampling response 回到了攻击者控制的 fake server。次级成功是 sampling 返回值导致 host 执行预注册的 local canary action。仅 sampling request 到达、仅消耗 token、或模型拒绝但解释了原因，都不算数据泄露成功；这些作为 partial/denied labels。
- **Independent evaluator。**fake server 记录 request/response 原始字段；host-side trace 记录 sampling policy decision、实际发送给模型的 context hash 和 response recipient；独立 evaluator 对 `CANARY_S` 做精确匹配，并检查该 canary 是否确实没有出现在请求外的其他输入中。无需 LLM judge。
- **Defense boundary。**防御位于 host 的 sampling gate，而不是工具描述扫描器：server 资格 allowlist、每次 sampling 的用户确认、上下文最小化/taint、禁止把 private context 传回未授权 server、token/rate budget 和 response recipient binding。该边界不能阻止 server 自己的恶意代码，也不等于对所有模型输出做语义审查。
- **Safety containment。**使用本地或项目自有模型、fake server 和 synthetic `CANARY_S`。sampling 只允许返回固定 canary 或无害短文本；不使用真实用户历史、真实系统 prompt、真实邮件、真实 credentials 或真实网络端点。所有 server response 只写入本地 trace。
- **Minimal kill experiment（只定义，不执行）。**为一个具体 host 建立 disabled、allowlisted-public-context、unrestricted-synthetic-context 三臂；同一 fake server 发出一条固定 sampling request，比较是否返回 `CANARY_S`、是否把结果路由给 server，以及 benign task utility。至少先确认目标 host 实际公开并实现 sampling。若没有任何可运行 host 暴露 server-initiated sampling，或所有 host 都在请求入口拒绝且该能力无法部署，则 kill 为“接口不可达”；若 only model follows an instruction but host never returns data，则不支持 sampling-boundary claim。

### 4.3 可达性与重叠判断

第三方 server publisher 在用户正常连接 server 后即可发送该协议请求，不需要预先拥有用户数据或 host 权限；但“host 支持 sampling”和“sampling request 能看到 private context”是 operator-controlled constraints，必须写成实验条件。`When MCP Servers Attack` 的 sampling abuse 和 MCPXKIT 的 resource/prompt taxonomy 是直接邻居；它们证明入口概念存在，不等于本候选的实际 host routing 机制已经成立。最新跨框架论文对 prompt/sampling 入口的未暴露说明，使它仍有测量价值，但公共 full-text screen 必须优先于任何模型预算。

它不属于 I1、P4 或 Q1，也不属于 screen B Q6–Q10。若最终只能通过 tool description 或 tool response 诱导模型自行调用工具，候选应降级为 MCPTox/MSB/COPEX 已覆盖的普通 injection；若目标只是 token 消耗，则是 DoS/资源滥用，需另立 claim，不能混入隐私外泄。

## 5. 候选三：流式响应、notification、timeout/cancel 的在途状态机竞态

### 5.1 机制和研究价值

MCP 论文已经大量研究“响应文本进入模型上下文”，但较少把一个正在执行的 call 看成一个有状态的协议对象：请求 ID、stream chunk、progress notification、cancel、timeout、final result 和 side effect 是否只允许一个合法顺序。最新跨框架论文把 Streaming Injection 和 Notification Injection 列为 P18/P21，但其四类传输相关场景明确是对所述 transport 机制的社会工程测试，而不是完整实现中的真实消息调度。COPEX 记录 protocol events 和 transport 状态，却不等于已经隔离并证明“取消之后的迟到结果”或“一个 logical call 产生两个 effect”。

最小而清楚的机制是 **in-flight duplicate/late-result acceptance**：server 只控制自己那条合法 response stream 的时序，不伪造其他 server 的消息、不改 JSON parser；如果 host 在一个 logical call 上产生两次 canary effect 或在 cancel 后提交 effect，问题属于客户端状态机/执行边界。

### 5.2 Threat model

- **Attacker capability。**攻击者运行一个已被用户连接的 MCP server，控制其自身 response stream 的时序、合法 progress/log notification、stream chunk、final result、延迟和重复发送。攻击者不能修改 host/client 代码、其他 server、LLM、用户任务或任意工具实现；不能伪造其他 request ID，除非该 ID 本来属于自己的 pending call。
- **Victim state。**受害者状态为一个 pending-call record：
  `P = (request_id, phase, cancel_flag, timeout, approval_state, committed_effects, final_result)`。
  每个状态变化必须在 host trace 中显式记录。跨 session 的缓存、revocation、checkpoint restore 不属于这个候选。
- **Access point。**唯一入口是该 server 对一个 MCP call 的 response stream/notification sequence。使用 canonical、单义的 JSON；不得用 duplicate key、Unicode 等字节歧义。
- **Knowledge。**灰盒：攻击者知道公开的 request/response/streaming protocol 和自己发起的 request ID；不知道 host 内部线程调度细节。若要测试 adaptive timing，攻击者可以知道 host 的公开 timeout，但不能读取内部日志。
- **Success criterion。**建议预注册一个主目标：同一个 logical call 只应产生一次本地 no-op canary effect；若 host log 或 fake tool log 记录 `effect_count >= 2`，且 benign task 仍完成，则 attack success。两个次级标签分别是 `post_cancel_effect=1` 和 `late_result_committed=1`。只看到重复文本、progress notification 或模型重复描述，不算成功；必须有 deterministic effect/state witness。
- **Independent evaluator。**fake tool server 的 effect ledger 记录每个 request ID 的执行次数；host-side FSM logger 记录 chunk、notification、cancel、timeout 和 commit；第三方 evaluator 对 request ID、时间窗和 effect count 做精确检查。无需 LLM judge，也不把最终自然语言回答当成功标准。
- **Defense boundary。**防御位于 MCP client/orchestrator 的 in-flight state machine：每个 request ID 一次性 commit、单调 sequence/event ID、cancel 后 terminal state、超时 fail-closed、幂等或 transactional tool wrapper，以及把 network response 与 side-effect commit 分开。它不能依赖 prompt scanner，因为竞态可以在模型不可见的 transport/client 层发生。
- **Safety containment。**所有 calls 进入项目自有的 in-memory fake tool；canary effect 只增加本地计数或写入临时 trial log，不写真实文件、不发真实网络、不连接真实 server。测试调度由本地 deterministic scheduler 控制，原始 sequence 和 host state 全部保留在项目外的实验目录。
- **Minimal kill experiment（只定义，不执行）。**固定一条 benign call 和四个 schedule：正常完成、重复 final chunk、cancel 后迟到 final、timeout 后迟到 final；分别在 baseline client 和 strict reference FSM 上运行。若两者都至多提交一次 effect，或差异只在 malformed parser，而 canonical event sequence 不会改变状态，则 kill。若需要跨 session revocation、checkpoint 恢复或长期记忆才出现效果，应停止并归入 Q8 stale-state，而不是扩大本候选。

### 5.3 可达性与重叠判断

第三方 server 只要被用户连接，就能决定自己发送合法响应的时间和顺序；这不要求 server 先取得 host 的系统 prompt、文件权限或模型控制权。自动执行、timeout、cancellation、idempotency 等是部署约束，必须按具体 host 记录，不能假设所有 host 相同。

该候选不属于 Q1/C4，因为没有 parser semantic split；canonical bytes 在 validator/executor 或 client/server 两端都应唯一解释。它也不属于 Q10，因为目标是一次 side effect/state commit，不是信息传输隐蔽性。如果使用 revoked state、恢复旧 checkpoint 或跨 session cache，则落入 screen B Q8。最新 P18/P21 和 COPEX 是直接邻居；候选的可保留 delta 只能是实际 protocol scheduler/state-machine execution，而不是再写一种 notification 文本。

## 6. 候选四：Gateway 中 capability 的 subject/audience/purpose 混淆

### 6.1 机制和研究价值

多租户 MCP gateway 可能把多个 server 的 opaque handle、资源引用或 delegated capability 转发给不同主体。一个较窄的研究问题是：gateway 是否只验证“这个 handle 格式正确/由某 server 返回”，却没有把 `subject`、`issuer`、`audience`、`purpose` 和 `expiry` 绑定到当前 tenant 和当前动作，导致 tenant A 的正常调用被转成 tenant B 的 canary 访问。它与工具名称冲突或 agent alias collision 不同，成功点是授权 tuple 的跨租户不一致。

这个候选的价值在于多租户 gateway 的授权审计，但它是本报告中最可能被现有 screen B/Q7 或 P4 杀死的方向。

### 6.2 Threat model

- **Attacker capability。**攻击者是一个普通 tenant 或一个已接入 gateway 的第三方 server publisher，只能控制自己 server 的返回值和自己 tenant 的 capability/ref；不能读取 tenant B 的 token、数据库、对方 server 或 gateway 私钥。
- **Victim state。**gateway 在每次跨 server 转发前保存的授权 tuple：
  `A = (subject, issuer, audience, purpose, expiry, session_id)`，以及最终执行的 tenant/resource。模型的语言判断不是 victim state。
- **Access point。**单一入口是 attacker-controlled server 返回的一个 opaque capability/resource reference，被 gateway 作为后续跨服务器调用的输入。不能同时操纵 human-readable agent name、session alias、memory entry 或 provenance label。
- **Knowledge。**灰盒：攻击者知道公开 gateway API 和自己 tenant 的 capability 格式；不知道 tenant B 的真实 token、内部 IDs 或私有数据。
- **Success criterion。**在两个 synthetic tenants A/B 和同一 benign task 下，只有 A 被授权；若 gateway audit log 显示 `subject=A` 的请求对 `audience=B` 的 synthetic resource 产生 read/write effect，且 B 的 `CANARY_B` 被返回或状态改变，则成功。仅返回 invalid-token error、名称显示错误或模型选择错误不算成功。
- **Independent evaluator。**gateway 的 append-only authorization log、每个 tenant 的 in-memory canary store 和 token verifier 的 reference implementation。由独立 evaluator 检查 `A` tuple 与实际 effect 的一致性，不使用 LLM judge。
- **Defense boundary。**gateway authorization layer：capability 必须绑定 issuer/subject/audience/purpose/expiry，跨 server forwarding 重新验证，禁止模型或 server 自己填写授权字段，tenant isolation 和 fail-closed。MCP metadata scanners 不覆盖这个边界。
- **Safety containment。**local gateway、两个 synthetic tenants、随机短期 capability、内存数据库和固定 canary；不使用真实 OAuth、真实云账户、真实 remote MCP 或公共 registry。所有 token 在 trial 后销毁。
- **Minimal kill experiment（只定义，不执行）。**建立 honest relay、attacker relay、strict audience-bound gateway 三臂；保持 tool schema、任务和 model-visible content 相同，只有 opaque ref 的 issuer/audience/purpose 关系变化。若 baseline 和 strict gateway 都拒绝跨租户 effect，或成功需要 attacker 直接读取 tenant B token，则 kill。若 payload 只是把 A 的名字换成 B 的名字，应判定为 Q7 identity collision，不再保留。

### 6.3 可达性与重叠判断

普通 tenant/第三方 server 可以在正常多租户工作流中返回自己的 capability/ref，不需要先拥有 tenant B 的授权；如果实验必须给攻击者 gateway 管理权限、数据库写权限或 tenant B token，则访问循环，候选无效。operator-controlled constraints 包括 gateway 必须允许跨 server delegation、存在 opaque ref 转发、且没有每跳 audience check。

这是最接近 screen B Q7 的候选：如果机制是 alias、name collision、session smuggling 或身份 rebinding，应明确关闭。它也接近 P4：如果只表现为 provenance/authority label 在 handoff 中丢失，应归入 P4 closure。只有当贡献是可独立验证的多租户 capability audience/purpose binding，且不依赖名字冲突或自然语言 provenance，才值得重新做 public screen。

## 7. 候选五：非 filesystem 的 declared contract 与实际 effect/data-flow 不一致

### 7.1 机制和研究价值

最新 `filesystem capability laundering` 已把“工具声明范围小于实际 filesystem effect”定义得很清楚，并报告了大量 filesystem 实例。因此，不能再把 path traversal、symlink、git staging 或一般文件访问写成新论文。仍可能有一条窄的测量方向：工具 schema/annotation 看起来只允许一个无害操作，但 schema-valid 的嵌套参数、回调、recipient、resource reference 或 server-to-server forwarding 让真实网络、数据库、消息或租户 effect 超出 declared contract；工具代码保持公开且没有隐藏 Trojan。

这更像一个 contract/effect audit benchmark，而不是独立攻击算法。它只有在能证明非-filesystem、非隐藏代码、非普通 parameter-binding 的新边界时才有价值。

### 7.2 Threat model

- **Attacker capability。**攻击者只能控制一个受害者正常会读取的外部记录，使 agent 为一个已经存在的合法工具生成 schema-valid 参数；攻击者不能修改该工具的代码、schema、server configuration、model 或 host。victim server 是有 bug 或过宽 effect 的 benign implementation，而非恶意签名工具。
- **Victim state。**工具的 declared contract/annotation 与真实执行 effect 的集合：
  `C = (name, description, schema, annotations)`，
  `E = (files, db rows, recipients, network destinations, tenant)`。
  目标是验证 `E(call) ⊄ Scope(C, deployment)`，且不是由隐藏 code 或 OS compromise 造成。
- **Access point。**单一入口是一次合法 `tools/call` 的 `arguments` 字段，参数值由 attacker-controlled external content 间接影响。不能同时改变 tool metadata、tool response、transport 或 server code。
- **Knowledge。**黑盒到灰盒：攻击者知道公开 schema 和 benign task，不知道私有数据；研究者为了构建 oracle 可以读取本地 server code，但这属于 evaluator knowledge，不自动授予攻击者。
- **Success criterion。**调用必须通过 schema/host approval，benign task utility 通过；独立 effect monitor 发现 synthetic canary 到达 contract 未授权的 network/DB/message sink，或读取了超出 deployment policy 的 synthetic tenant/object。只有“模型生成了越界参数”而没有 effect 是 intent-only partial result，不算 attack success。
- **Independent evaluator。**server-side effect ledger、local DB/queue/network sink 的 canary receipt 和 contract-policy reference checker；以 effect 和 sink event 判定，不用 LLM judge。
- **Defense boundary。**server/runtime 或 gateway 的 per-argument capability enforcement、effect sandbox、egress/data-flow allowlist、tenant/purpose binding。工具描述扫描只能发现文本风险，不能证明实际 effect 被限制。
- **Safety containment。**只用本地 fake DB、in-memory queue、loopback sink 和 synthetic tenant/file marker；不使用真实网络、真实消息、真实云凭证、真实数据库或真实 MCP registry。不能发布可复用的 path traversal、SSRF 或外泄 payload。
- **Minimal kill experiment（只定义，不执行）。**为一个 tool 构造 contract-equivalent control 和 suspected effect-divergent control，分别使用 clean argument 与由 synthetic external record 影响的 schema-valid argument；比较 baseline runtime 和 strict effect policy 的 canary receipt、benign utility 和 false trigger。如果只有 filesystem path escape，则归入 capability laundering 现有工作；如果必须植入隐藏 code，则归入 Signed, Sealed, Leaked/rug pull；如果只是模型填了不该填的参数而没有 effect，则 kill。

### 7.3 可达性与重叠判断

外部记录作者可以通过受害者正常的检索/阅读任务影响一次工具参数，不需要先拥有 server write 或 filesystem write 权限；但 server 必须已经存在真实的 effect/contract gap，且 host 会把该 call 发出。这些是实验约束，不应写成部署普遍事实。

此候选与 filesystem capability laundering 直接相邻，与最新跨框架 P20 Parameter Binding、Signed, Sealed, Leaked 的 hidden-code/data-flow、Destructive Tool Approval 的 annotation/approval 边界和 P4 的 authority laundering 都有重叠。若没有独立的非-filesystem机制、精确的 effect oracle 和 benign utility control，应关闭，不应以“更换文件为网络/数据库”宣称新颖。

## 8. 明确关闭或不应重新包装的方向

### 8.1 项目内已关闭

| 方向 | 关闭原因 | 处理 |
|---|---|---|
| **I1：truthful evidence order → memory → downstream causal error** | local-gateway C2 narrative 17/30 vs random 14/30，bridge-swap 23/30；主比较不显著且机制 control 更强。memory/downstream blocks 未授权。 | 只保留 negative boundary；任何“外部内容进入 memory 再传播”的普通版本也不能借 MCP 包装重新提出。 |
| **P4：typed/provenance conversion / authority laundering** | v2 与 Astra 复制都通过，但 Trust Cascade、multi-CaMeL、structured delegation、authority laundering 和 provenance-aware authorization 已直接覆盖广义机制。 | 只保留协议实验/负边界；候选四若变成标签或来源丢失，立即关闭。 |
| **Q1/C4：validator/executor parser differential** | Python、Node、`cra_mcp.adapter.ToolBox.call`、Sol/Astra transport smoke 全部复现；MCP Go SDK issue #805 与 ATR-2026-02350 已直接覆盖并修复。 | 不能再用 duplicate key、Unicode canonicalization、first/last-key 或 nested duplicate 变体。候选三必须使用 canonical bytes。 |

### 8.2 screen B 已关闭

- **Q6 dynamic task-graph rewrite / route-node injection。**FlowSteer、conjunctive routing、ControlValve 和 safe-topology work 已覆盖。候选三不能把 notification race 改写成动态任务图攻击。
- **Q7 agent identity alias collision / entity rebinding。**Agent Name Collision、A2A session smuggling 和 identity binding work 已覆盖。候选四只有在 subject/audience/purpose cryptographic binding 上形成新状态，否则关闭。
- **Q8 revocation/stale shared state/checkpoint resurrection。**候选三如果依赖 revoked capability、旧 checkpoint、跨 session stale memory 或 resurrection，应直接归入 Q8。
- **Q9 compositional privacy-budget leakage。**Sum Leaks More Than Its Parts、AgentLeak、mutual-information/Rényi privacy work 已覆盖。工具调用轨迹画像还被 `2610_arxiv_tool_call_trace_privacy_leakage.pdf` 直接研究；不能以 MCP trace 重新提出 privacy-composition thesis。
- **Q10 timing/traffic covert channel。**secret collusion、covert storage/timing/behavioral channels、steganographic tool use和 collaboration fingerprinting 已覆盖。候选三的 timing 只能作为协议竞态控制变量，成功必须是 duplicate/cancelled effect，不能是隐蔽通信。

### 8.3 MCP 目录中已直接覆盖的常规入口

以下方向没有清晰的机制级空白，除非研究目标改成一个明确的测量/防御边界，并通过新的 full-text screen：

- tool description/schema/response poisoning、preference manipulation、attractive metadata、A2M trace-guided manipulation；
- 外部网页/邮件/文档注入，固定多工具隐私外泄，Parasites/MCP-UPD、SOPE、Log-To-Leak；
- rug pull、server configuration abuse、initializer/backdoor、签名工具隐藏代码、跨调用 stash；
- filesystem path/symlink/staging capability laundering；
- destructive tool approval、server elicitation 与 host approval 缺失；
- resource/prompt metadata、logic、output injection 的一般版本；`When MCP Servers Attack` 已逐项列出 A7–A12，MCPXKIT 也已纳入 resource/prompt 族；
- generic gateway noisy-tool scaling、hierarchical discovery 和 tool injection；GatewayBench 已覆盖该 benchmark 轴；
- Potemkin 的 breadth belief drift 和 depth navigation trap；
- tool-call trace 的用户画像和跨 session 推断；最新 PrivacyTrace 已给出直接入口与独立 evaluator 形式。

## 9. 预审结论与下一步门槛

当前没有足够证据选择一个论文 thesis。若继续 R4，优先顺序应是：

1. 对候选一做 MCP 版本/能力协商的公共 full-text screen，并先确认至少两个可运行 host/client 的实际 handshake 行为；
2. 对候选三做 streaming/notification/cancellation 的实现级 full-text screen，重点查清最新跨框架论文的 P18/P21 是否仅为 prompt-level claim；
3. 对候选二做 host sampling 能力的实现清单，若没有至少一个真实可运行的本地/项目-owned host，则立即 kill；
4. 候选四和五只在前面三项都失败后作为测量型备选，不得直接声称新攻击机制。

无论选哪一项，最小 evidence bar 都必须包括：协议原始 trace、独立 deterministic evaluator、benign utility、false-trigger control、至少一个 strict defense boundary、adaptive attacker/defense 条件、两个实现或框架、完整文本邻近工作检查，以及 synthetic-only containment。模型 ASR 或 LLM judge 不能替代协议状态和实际 canary effect。

本报告没有新增 `CLAIMS.md` 行，也没有生成 threat JSON 或修改任何共享黑板文件；这是有意的，因为当前任务是 threat-model 预审而非授权实验或 thesis 选择。
