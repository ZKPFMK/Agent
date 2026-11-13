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

## 尚未下载的优先工作

以下两篇已确认是优先相关工作，但当前公开下载请求被 ACM 的 Cloudflare challenge 返回 HTTP 403，因此没有把错误页面保存为 PDF：

- **MSA: A Cross-MCP Privacy Attack via Memory Exfiltration of Large Language Models** — [ACM DOI](https://doi.org/10.1145/3733802.3764057)
- **Confused Deputy Attack against Model Context Protocol** — [ACM DOI](https://doi.org/10.1145/3830467)；公开实现：[Puppet](https://github.com/Redempt1onzzZZ/Puppet)

## 下载说明

所有已下载文件均来自论文的 arXiv 或 ACL Anthology 公开 PDF 地址，并在复制到本目录前用 `file` 和 `pdfinfo` 验证为 PDF。文件名使用提交年份/月份或会议年份前缀，便于与上级目录的命名保持一致。
