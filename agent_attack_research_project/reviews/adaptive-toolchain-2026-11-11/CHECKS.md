# 本轮核查记录

日期：2026-11-11。此文件记录调研工件与来源完整性检查，不是攻击效果验证。

## 已执行

1. `python3 -I /Users/dj/Documents/paper/Agent/Agent-Attack-Research/skills/agent-attack-research/scripts/check_framework.py --corpus /Users/dj/Documents/paper/Agent/research_attack_ideas`
   - 退出状态 0。
   - `PASS corpus matrix parsed: 54 rows; counts A=21, B=14, C=19`。
   - 只验证已有语料结构，不表示 54 篇论文已全文核对。

2. 同一检查器的 `--project /Users/dj/Documents/paper/Agent/agent_attack_research_project`，本轮台账追加前执行。
   - 退出状态 0。
   - R0–R10 节点存在、论文矩阵 54 行、项目结构有效。
   - 结构检查不判定新颖性、可行性或科学 gate。

3. 主协调使用 `shasum -a 256` 核对原构想、四篇关键 PDF 及所检查的 `cra_mcp/agent.py`。
   - 命令均退出 0，原构想及四篇 PDF 与本地节点清单一致。
   - 原构想：`63ca1233a225b6ea87ed6ed07857c4c7568bcdd4de593089a830f4df233f413c`。
   - PDF 哈希与逐篇读取范围见 `LOCAL-PRIOR.md` 和 `local-sources/kb-curator-44809ef0/sha256.txt`。
   - `agent.py`：`83a493ac04d1d3cada5e98a52163e87fcc1e6f95c1c1f60e7ff97f96fe6c368d`；工具包 HEAD `463779b318f78a7c9e62e86639fec135c0423bc5`，工作区有既有修改，不能将该 HEAD 当整个工作区快照。

4. 主协调视觉复核 Parasites PDF p.4；官方 MCP 固定版 2025-11-25 Tools 与 Architecture 通过 WebFetch 读取。
   - 原文支持无需预知 MCP 配置、自然语言诊断载荷不写函数名但仍列出读/转发动作。
   - 官方语义及本地循环适用边界见 `MCP-SEMANTICS.md`。

5. 各独立节点以其各自报告记录读取范围、证据等级和缺源。完整文本提取不等于每页精读；公开抽象核查不升级为方法全文核查。

## 最终完整性审计

已在合成和台账追加后执行，全部通过。

- 命令：`python3 -I -`，stdin 为 stdlib 的 Path/hashlib/json/re 断言脚本。实际退出状态 **0**。
- 检查七份报告/节点文件存在且非空：REPORT、LOCAL-PRIOR、WEB-LITERATURE、DESIGN-REVIEW、MCP-SEMANTICS、SCOPE、CHECKS。
- 解析这些文件的 Markdown 链接，11 个本地链接目标全部存在；远程 URL 未作为文件路径处理，也未声称完成全站链接可用性检查。
- REPORT 中 `PENDING`、`待回收`、`尚未定稿` 标记为 0。
- 原构想 SHA-256 与输入一致；原稿未改动。
- 11 个最终公开来源目录均有非空阅读文本、下载 URL 和 HTML/PDF 原件。原件指纹见下表。
- 台账追加后重新执行 `check_framework.py --project /Users/dj/Documents/paper/Agent/agent_attack_research_project`：退出 **0**；R0–R10、54 行矩阵及项目结构 PASS。
- `git -C /Users/dj/Documents/paper/Agent diff --check -- agent_attack_research_project/STATE.md agent_attack_research_project/ATTACK-RESEARCH.md agent_attack_research_project/RESEARCH-GRAPH.md agent_attack_research_project/progress.md agent_attack_research_project/DECISIONS.md`：退出 **0**，无空白错误输出。

上述审计没有运行模型、工具服务器或攻击。科学结论保持：宽泛新攻击定位不支持，严格评测问题 UNCERTAIN；没有把结构 PASS 写成创新/可行性通过。

### 公开原件 SHA-256

路径相对本轮目录；下载内容只作来源证据。

| 原件 | SHA-256 |
|---|---|
| web-sources/injecagent-acl-1fe50e87/source.pdf | `690a5d14abf0d33002822b531b78fa375da51783ff831ba8ecbb6e22f3d4f382` |
| web-sources/agentdojo-1f993b9c/source.html | `7b6e97faaedcf0e1b5f3635b92a0da33afbe8529699d54a5c44ad58ce2fa8b02` |
| web-sources/agentdyn-v3-d6448ab0/source.html | `311dbdeec98d359a8f8c96cdf59ec8c5e2ba3be8635390f42aae7af4d118ddd8` |
| web-sources/asb-801adc32/source.html | `85bab447cf5c3c692c7d3dae2785f0bcc6a9e4f8d8e15da9aac5cb6ec976054b` |
| web-sources/mcptox-75437a85/source.html | `0842fbd6e9893e25da002be593d24d75cf89f7c80af9d989d925e9e39401780d` |
| web-sources/mcp-itp-87551812/source.html | `33408f3378c2b7945f37a12f265ce6449a960314328f6cbd58abae5b6e1fda6d` |
| web-sources/flowsteer-7ca31b42/source.html | `cc3d01ba3403c2361e63271d699d1a6bfb3dbd82e29d5f689f6709f272f29692` |
| web-sources/context-manipulation-528080a0/source.html | `0f0c588a4389a3f4137b582ca53047410da21b2acab25810a52a42b632c4c0fb` |
| web-sources/task-alignment-3afaa38f/source.html | `4777e9cf0393bb7bab469ef5bcf28dc31db3ff19624da575d290553c24ad6f11` |
| web-sources/firewalls-d7d6309f/source.html | `94a7199a1614cecccbb05e7dfd976f49fd94ad5848e6ab87e5fc8ec347ad5a12` |
| web-sources/task-tampering-049f480d/source.html | `ce88127b1830db9ad103ec57cd7c3d429959cb64b60b65a49aa2396ad44d55c4` |

## 2026-11-12 A11 / code-execution clarification audit

- User clarification: A11 refers to *When MCP Servers Attack* A11 Prompt Logic Attack. The local excerpt is linked in `REPORT.md` with the line number in link text, not as part of the path.
- Added and checked `CODE-EXECUTION-LITERATURE.md` and `CODE-EXECUTION-DESIGN.md`; both are nonempty and local links resolve.
- The final stdlib audit checked nine report/design files, 16 local Markdown links, no draft markers, and unchanged original idea SHA-256; actual exit status **0**.
- The project checker was rerun after the additions: actual exit status **0** (`R0-R10`, 54-row matrix, project structure PASS).
- `git diff --check` was rerun for the five shared ledger files: actual exit status **0**.
- No model, shell, MCP server, payload, live target or experiment ran. This is an evidence/design clarification only.

