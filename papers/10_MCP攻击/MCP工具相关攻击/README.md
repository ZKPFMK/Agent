# MCP 工具相关攻击论文

本目录用于保存与 MCP 工具选择、工具描述投毒、跨工具外泄、工具调用劫持、信任转换、工具调用隐私和资源放大相关的优先阅读工作。

## 已下载

| 本地文件 | 工作 | 来源 | 备注 |
|---|---|---|---|
| `2504_arxiv_mcp_safety_audit.pdf` | MCP Safety Audit: LLMs with the Model Context Protocol Allow Major Security Exploits | [arXiv:2504.03767](https://arxiv.org/abs/2504.03767) | 早期 MCP 安全审计与攻击生成器 |
| `2507_arxiv_trivial_trojans.pdf` | Trivial Trojans: How Minimal MCP Servers Enable Cross-Tool Exfiltration of Sensitive Data | [arXiv:2507.19880](https://arxiv.org/abs/2507.19880) | 恶意 Server 借助合法工具跨 Server 外泄 |
| `2512_arxiv_intentminer.pdf` | IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol | [arXiv:2512.14166](https://arxiv.org/abs/2512.14166) | 从合法工具调用反推用户意图 |
| `2601_arxiv_mcp_itp.pdf` | MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP | [arXiv:2601.07395](https://arxiv.org/abs/2601.07395) | 自动化隐式工具投毒 |
| `2602_arxiv_overthinking_loops.pdf` | Overthinking Loops in Agents: A Structural Risk via MCP Tools | [arXiv:2602.14798](https://arxiv.org/abs/2602.14798) | 诱导循环调用和资源放大 |
| `2604_arxiv_function_hijacking.pdf` | Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models | [arXiv:2604.20994](https://arxiv.org/abs/2604.20994) | MCP 相关的通用函数/工具选择劫持 |
| `2606_arxiv_sharelock.pdf` | ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP | [arXiv:2606.27027](https://arxiv.org/abs/2606.27027) | 将投毒载荷分散到多个工具描述 |
| `2608_arxiv_trustshiftprobe.pdf` | TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers | [arXiv:2608.23763](https://arxiv.org/abs/2608.23763) | 先建立信任、后切换恶意行为 |
| `2610_arxiv_privacytrace.pdf` | How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces | [arXiv:2610.41885](https://arxiv.org/abs/2610.41885) | 从工具调用轨迹推断用户属性 |
| `2611_arxiv_overserve.pdf` | OverServe: Resource Amplification Attacks on SaaS Agents via Tool–Prompt Co-Design | [arXiv:2611.14808](https://arxiv.org/abs/2611.14808) | MCP 工具驱动的资源放大和经济型 DoS |
| `2026_emnlp_beyond_max_tokens.pdf` | Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents | [ACL Anthology](https://aclanthology.org/2026.emnlp-main.2090/) | 隐蔽的长工具调用链和成本放大 |

## 本地目录中补入的核心论文

以下文件原本已经存在于上级 `10_MCP攻击` 目录及其子目录，本次复制到这里，便于集中阅读。它们不是重复下载的外部副本。

### 四篇核心攻击工作

| 本地文件 | 工作 | 来源 | 主要方向 |
|---|---|---|---|
| `2026_mpma.pdf` | MPMA: Preference Manipulation Attack Against Model Context Protocol | [AAAI 2026 / 本地 PDF](../AAAI近三年_MCP攻击/26_aaai_mpma.pdf) | 工具选择偏好操纵 |
| `2026_mcptox.pdf` | MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers | [arXiv:2508.14925](https://arxiv.org/abs/2508.14925) | 工具描述/元数据投毒 |
| `2026_parasites_toolchain.pdf` | Parasites in the Toolchain: A Large-Scale Analysis of Attacks on the MCP Ecosystem | [本地 PDF](../26_sp_parasites_toolchain.pdf) | 跨工具链组合与隐私外泄 |
| `2026_sope.pdf` | SOPE: Situation-Aware and Statistically Indistinguishable Privacy Exfiltration for MCP-enabled Agents | [PMLR](https://proceedings.mlr.press/v306/lin26r.html) | 情境感知、零点击隐私外泄 |

### 其它本地攻击、评测和安全分析工作

| 本地文件 | 工作 | 主要方向 |
|---|---|---|
| `2025_beyond_protocol.pdf` | Beyond the Protocol: Unveiling Attack Vectors in the MCP Ecosystem | 工具投毒、Puppet、Rug Pull、恶意外部资源 |
| `2025_when_mcp_servers_attack.pdf` | When MCP Servers Attack: Taxonomy, Feasibility, and Mitigation | 恶意 MCP Server 攻击分类与 PoC |
| `2025_mcpxkit.pdf` | MCPXKIT: The Unified Toolkit for Analyzing Model Context Protocol Security | 31 类 MCP 攻击工具包 |
| `2025_attractive_metadata_attack.pdf` | Attractive Metadata Attack: Inducing LLM Agents to Invoke Malicious Tools | 吸引性元数据与工具选择操纵 |
| `2025_invisible_prompts.pdf` | Invisible Prompts, Visible Threats: Malicious Font Injection in External Resources for Large Language Models | 外部资源隐藏注入 |
| `2025_tool_invocation_red_team.pdf` | Red-Teaming Coding Agents from a Tool-Invocation Perspective | ToolLeak 与工具调用劫持 |
| `2026_a2m.pdf` | A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem | 元数据吸引与返回轨迹操纵 |
| `2026_remote_mcp_server_attack_surfaces.pdf` | Beyond Tool Poisoning: Attack Surfaces of Malicious Remote MCP Servers Across LLM Platforms | 远程恶意 Server 攻击面 |
| `2026_log_to_leak.pdf` | Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via MCP | 追加日志调用和数据外泄 |
| `2026_signed_sealed_leaked.pdf` | Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains | 签名工具供应链与隐蔽外泄 |
| `2026_destructive_tool_approval.pdf` | When Neither Side Confirms: Destructive Tool Approval Across MCP Servers and Hosts | 破坏性工具调用授权错配 |
| `2026_filesystem_capability_laundering.pdf` | My Credentials, Please: Detecting Filesystem Capability Laundering in MCP Servers at Scale | 文件系统能力滥用与凭据泄露 |
| `2026_cross_framework_tool_poisoning.pdf` | MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study | 跨框架工具投毒测量 |
| `2026_gatewaybench.pdf` | GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways | 网关、工具面和间接攻击评测 |
| `2026_mcp_safetybench.pdf` | MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers | 真实 Server、多轮、多侧攻击基准 |
| `2026_msb.pdf` | MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents | 12 类 MCP 攻击综合基准 |
| `2026_copex.pdf` | COPEX: Benchmarking LLM Robustness to Adversarial Context Across MCP Layers | 分层和观测边界评测 |

## 尚未下载的优先工作

以下两篇已确认是优先相关工作，但当前公开下载请求被 ACM 的 Cloudflare challenge 返回 HTTP 403，因此没有把错误页面保存为 PDF：

- **MSA: A Cross-MCP Privacy Attack via Memory Exfiltration of Large Language Models** — [ACM DOI](https://doi.org/10.1145/3733802.3764057)
- **Confused Deputy Attack against Model Context Protocol** — [ACM DOI](https://doi.org/10.1145/3830467)；公开实现：[Puppet](https://github.com/Redempt1onzzZZ/Puppet)

## 下载说明

所有已下载文件均来自论文的 arXiv 或 ACL Anthology 公开 PDF 地址，并在复制到本目录前用 `file` 和 `pdfinfo` 验证为 PDF。文件名使用提交年份/月份或会议年份前缀，便于与上级目录的命名保持一致。
