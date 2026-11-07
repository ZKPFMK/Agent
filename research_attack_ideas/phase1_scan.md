# 第一阶段扫描报告：三类攻击论文目录

> 状态：扫描版。此文件只记录目录、文件类型、材料完整性和版本线索；正文语义字段将在正文核对后写入 `paper_inventory.md` 与 `paper_matrix.csv`。
>
> 扫描范围：`papers/01_攻击_外部交互`、`papers/02_攻击_内部认知`、`papers/03_攻击_多智能体协作`。未纳入 `papers/00_*` 及防御、框架、评测目录。

## 统计

| 类别 | 论文子目录 | PDF | Markdown 摘要 | 其他文件 | 备注 |
|---|---:|---:|---:|---:|---|
| A 外部交互 | 21 | 21 | 19 | 0 | A07、A21 缺少配套摘要 Markdown |
| B 内部认知 | 14 | 14 | 14 | 0 | 每个论文目录均有 PDF 和摘要 Markdown |
| C 多智能体协作 | 19 | 19 | 19 | 1 | 额外有 `.DS_Store` |
| **合计** | **54** | **54** | **52** | **1** | 目标目录内只有 PDF、摘要 Markdown 和 `.DS_Store` |

文件扩展名计数：`pdf=54`、`md=52`、`DS_Store=1`。

## 材料完整性和重复检查

- 54 个论文子目录均包含一个同名 PDF；因此当前可为每篇论文分配一个唯一扫描记录。
- A 类有两个 PDF 没有同目录的 `*_标题与摘要_中文.md`：`25_neurips_attractive_metadata`、`26_sp_parasites_toolchain`。
- 未发现 `.py`、`.ipynb`、`.sh`、`.yaml`、`.yml`、`.json`、`.toml`、`.csv`、`.tsv`、实验日志、单独附录、标签文件或人工批注文件。
- 文件名中出现 `code` 的条目（例如 C10、C14）属于论文/方法名称；这不构成存在代码仓库或实验代码的证据。
- 对 54 个 PDF 计算 SHA-256 后，未发现完全相同的文件哈希。仅凭文件名无法排除同一论文的不同 PDF 版本；版本关系需在正文元数据、页数、标题、作者和版本日期核对后判断。
- 摘要 Markdown 中可能包含外部代码链接；这属于论文材料中的链接线索，不能等同于本地代码已存在。

## 统一 ID 与文件清单

排序规则：各类别内按论文子目录名字典序分配 ID。目录前缀中的年份暂记为“目录线索”，不在正文核对前当作已确认发表年份。

### A：外部交互攻击

| ID | 目录 | PDF | 摘要 Markdown |
|---|---|---|---|
| A01 | `24_arxiv(preprint)_imprompter` | `papers/01_攻击_外部交互/24_arxiv(preprint)_imprompter/24_arxiv(preprint)_imprompter.pdf` | `..._标题与摘要_中文.md` |
| A02 | `24_arxiv(preprint)_wipi` | `papers/01_攻击_外部交互/24_arxiv(preprint)_wipi/24_arxiv(preprint)_wipi.pdf` | `..._标题与摘要_中文.md` |
| A03 | `25_acl_popup_attacks` | `papers/01_攻击_外部交互/25_acl_popup_attacks/25_acl_popup_attacks.pdf` | `..._标题与摘要_中文.md` |
| A04 | `25_emnlp(findings)_agentvigil` | `papers/01_攻击_外部交互/25_emnlp(findings)_agentvigil/25_emnlp(findings)_agentvigil.pdf` | `..._标题与摘要_中文.md` |
| A05 | `25_iclr_eia` | `papers/01_攻击_外部交互/25_iclr_eia/25_iclr_eia.pdf` | `..._标题与摘要_中文.md` |
| A06 | `25_icml_advagent` | `papers/01_攻击_外部交互/25_icml_advagent/25_icml_advagent.pdf` | `..._标题与摘要_中文.md` |
| A07 | `25_neurips_attractive_metadata` | `papers/01_攻击_外部交互/25_neurips_attractive_metadata/25_neurips_attractive_metadata.pdf` | **缺失** |
| A08 | `25_neurips_mip_against_agent` | `papers/01_攻击_外部交互/25_neurips_mip_against_agent/25_neurips_mip_against_agent.pdf` | `..._标题与摘要_中文.md` |
| A09 | `26_aaai_fact2fiction` | `papers/01_攻击_外部交互/26_aaai_fact2fiction/26_aaai_fact2fiction.pdf` | `..._标题与摘要_中文.md` |
| A10 | `26_aaai_mcptox` | `papers/01_攻击_外部交互/26_aaai_mcptox/26_aaai_mcptox.pdf` | `..._标题与摘要_中文.md` |
| A11 | `26_aaai_mpma` | `papers/01_攻击_外部交互/26_aaai_mpma/26_aaai_mpma.pdf` | `..._标题与摘要_中文.md` |
| A12 | `26_acl_ecommerce_deceptive_interfaces` | `papers/01_攻击_外部交互/26_acl_ecommerce_deceptive_interfaces/26_acl_ecommerce_deceptive_interfaces.pdf` | `..._标题与摘要_中文.md` |
| A13 | `26_acl_webagents_cost_attacks` | `papers/01_攻击_外部交互/26_acl_webagents_cost_attacks/26_acl_webagents_cost_attacks.pdf` | `..._标题与摘要_中文.md` |
| A14 | `26_iclr_chatinject` | `papers/01_攻击_外部交互/26_iclr_chatinject/26_iclr_chatinject.pdf` | `..._标题与摘要_中文.md` |
| A15 | `26_iclr_vpi_bench` | `papers/01_攻击_外部交互/26_iclr_vpi_bench/26_iclr_vpi_bench.pdf` | `..._标题与摘要_中文.md` |
| A16 | `26_icml_role_confusion` | `papers/01_攻击_外部交互/26_icml_role_confusion/26_icml_role_confusion.pdf` | `..._标题与摘要_中文.md` |
| A17 | `26_icml_safesearch` | `papers/01_攻击_外部交互/26_icml_safesearch/26_icml_safesearch.pdf` | `..._标题与摘要_中文.md` |
| A18 | `26_ndss_obliinjection` | `papers/01_攻击_外部交互/26_ndss_obliinjection/26_ndss_obliinjection.pdf` | `..._标题与摘要_中文.md` |
| A19 | `26_ndss_tool_selection_injection` | `papers/01_攻击_外部交互/26_ndss_tool_selection_injection/26_ndss_tool_selection_injection.pdf` | `..._标题与摘要_中文.md` |
| A20 | `26_sp_dark_patterns` | `papers/01_攻击_外部交互/26_sp_dark_patterns/26_sp_dark_patterns.pdf` | `..._标题与摘要_中文.md` |
| A21 | `26_sp_parasites_toolchain` | `papers/01_攻击_外部交互/26_sp_parasites_toolchain/26_sp_parasites_toolchain.pdf` | **缺失** |

### B：内部认知攻击

| ID | 目录 | PDF | 摘要 Markdown |
|---|---|---|---|
| B01 | `24_acl_badagent` | `papers/02_攻击_内部认知/24_acl_badagent/24_acl_badagent.pdf` | `..._标题与摘要_中文.md` |
| B02 | `24_icml_agent_smith` | `papers/02_攻击_内部认知/24_icml_agent_smith/24_icml_agent_smith.pdf` | `..._标题与摘要_中文.md` |
| B03 | `24_neurips_agentpoison` | `papers/02_攻击_内部认知/24_neurips_agentpoison/24_neurips_agentpoison.pdf` | `..._标题与摘要_中文.md` |
| B04 | `24_neurips_watch_out_agents` | `papers/02_攻击_内部认知/24_neurips_watch_out_agents/24_neurips_watch_out_agents.pdf` | `..._标题与摘要_中文.md` |
| B05 | `25_acl_agent_memory_privacy` | `papers/02_攻击_内部认知/25_acl_agent_memory_privacy/25_acl_agent_memory_privacy.pdf` | `..._标题与摘要_中文.md` |
| B06 | `25_acl_gpt_spills_tea` | `papers/02_攻击_内部认知/25_acl_gpt_spills_tea/25_acl_gpt_spills_tea.pdf` | `..._标题与摘要_中文.md` |
| B07 | `25_emnlp(findings)_demonagent` | `papers/02_攻击_内部认知/25_emnlp(findings)_demonagent/25_emnlp(findings)_demonagent.pdf` | `..._标题与摘要_中文.md` |
| B08 | `25_emnlp_breaking_agents` | `papers/02_攻击_内部认知/25_emnlp_breaking_agents/25_emnlp_breaking_agents.pdf` | `..._标题与摘要_中文.md` |
| B09 | `25_icml_udora` | `papers/02_攻击_内部认知/25_icml_udora/25_icml_udora.pdf` | `..._标题与摘要_中文.md` |
| B10 | `25_neurips_memory_injection` | `papers/02_攻击_内部认知/25_neurips_memory_injection/25_neurips_memory_injection.pdf` | `..._标题与摘要_中文.md` |
| B11 | `26_acl_stop_fixating_prompts` | `papers/02_攻击_内部认知/26_acl_stop_fixating_prompts/26_acl_stop_fixating_prompts.pdf` | `..._标题与摘要_中文.md` |
| B12 | `26_acl_visual_inception` | `papers/02_攻击_内部认知/26_acl_visual_inception/26_acl_visual_inception.pdf` | `..._标题与摘要_中文.md` |
| B13 | `26_icml_memincept` | `papers/02_攻击_内部认知/26_icml_memincept/26_icml_memincept.pdf` | `..._标题与摘要_中文.md` |
| B14 | `26_ndss_les_dissonances` | `papers/02_攻击_内部认知/26_ndss_les_dissonances/26_ndss_les_dissonances.pdf` | `..._标题与摘要_中文.md` |

### C：多智能体协作攻击

| ID | 目录 | PDF | 摘要 Markdown |
|---|---|---|---|
| C01 | `23_arxiv(preprint)_evil_geniuses` | `papers/03_攻击_多智能体协作/23_arxiv(preprint)_evil_geniuses/23_arxiv(preprint)_evil_geniuses.pdf` | `..._标题与摘要_中文.md` |
| C02 | `24_acl_psysafe` | `papers/03_攻击_多智能体协作/24_acl_psysafe/24_acl_psysafe.pdf` | `..._标题与摘要_中文.md` |
| C03 | `24_neurips_secret_collusion` | `papers/03_攻击_多智能体协作/24_neurips_secret_collusion/24_neurips_secret_collusion.pdf` | `..._标题与摘要_中文.md` |
| C04 | `25_aaai_multiagent_security_tax` | `papers/03_攻击_多智能体协作/25_aaai_multiagent_security_tax/25_aaai_multiagent_security_tax.pdf` | `..._标题与摘要_中文.md` |
| C05 | `25_acl(findings)_communication_attacks` | `papers/03_攻击_多智能体协作/25_acl(findings)_communication_attacks/25_acl(findings)_communication_attacks.pdf` | `..._标题与摘要_中文.md` |
| C06 | `25_acl_agents_under_siege` | `papers/03_攻击_多智能体协作/25_acl_agents_under_siege/25_acl_agents_under_siege.pdf` | `..._标题与摘要_中文.md` |
| C07 | `25_acl_contagious_jailbreak` | `papers/03_攻击_多智能体协作/25_acl_contagious_jailbreak/25_acl_contagious_jailbreak.pdf` | `..._标题与摘要_中文.md` |
| C08 | `25_arxiv(preprint)_ip_leakage` | `papers/03_攻击_多智能体协作/25_arxiv(preprint)_ip_leakage/25_arxiv(preprint)_ip_leakage.pdf` | `..._标题与摘要_中文.md` |
| C09 | `25_arxiv(preprint)_whos_the_mole` | `papers/03_攻击_多智能体协作/25_arxiv(preprint)_whos_the_mole/25_arxiv(preprint)_whos_the_mole.pdf` | `..._标题与摘要_中文.md` |
| C10 | `25_colm_mas_malicious_code` | `papers/03_攻击_多智能体协作/25_colm_mas_malicious_code/25_colm_mas_malicious_code.pdf` | `..._标题与摘要_中文.md` |
| C11 | `25_esorics(workshop)_prompt_infection` | `papers/03_攻击_多智能体协作/25_esorics(workshop)_prompt_infection/25_esorics(workshop)_prompt_infection.pdf` | `..._标题与摘要_中文.md` |
| C12 | `25_icml_faulty_agent_resilience` | `papers/03_攻击_多智能体协作/25_icml_faulty_agent_resilience/25_icml_faulty_agent_resilience.pdf` | `..._标题与摘要_中文.md` |
| C13 | `26_aaai_attack_messages` | `papers/03_攻击_多智能体协作/26_aaai_attack_messages/26_aaai_attack_messages.pdf` | `..._标题与摘要_中文.md` |
| C14 | `26_aaai_shadows_in_code` | `papers/03_攻击_多智能体协作/26_aaai_shadows_in_code/26_aaai_shadows_in_code.pdf` | `..._标题与摘要_中文.md` |
| C15 | `26_acl(findings)_corba` | `papers/03_攻击_多智能体协作/26_acl(findings)_corba/26_acl(findings)_corba.pdf` | `..._标题与摘要_中文.md` |
| C16 | `26_acl_conjunctive_prompt_attacks` | `papers/03_攻击_多智能体协作/26_acl_conjunctive_prompt_attacks/26_acl_conjunctive_prompt_attacks.pdf` | `..._标题与摘要_中文.md` |
| C17 | `26_acl_evo_attacker` | `papers/03_攻击_多智能体协作/26_acl_evo_attacker/26_acl_evo_attacker.pdf` | `..._标题与摘要_中文.md` |
| C18 | `26_acl_lying_with_truths` | `papers/03_攻击_多智能体协作/26_acl_lying_with_truths/26_acl_lying_with_truths.pdf` | `..._标题与摘要_中文.md` |
| C19 | `26_scis_flooding_manipulated_knowledge` | `papers/03_攻击_多智能体协作/26_scis_flooding_manipulated_knowledge/26_scis_flooding_manipulated_knowledge.pdf` | `..._标题与摘要_中文.md` |

## 下一步

1. 读取 52 个摘要 Markdown，并对 54 个 PDF 进行正文抽取与章节/页码核对。
2. 用核对结果回填 `paper_inventory.md` 和 `paper_matrix.csv`，使每个字段区分正文事实、摘要事实、推断和未验证信息。
3. 在清单冻结后再建立三个类别 taxonomy、交叉空白和候选想法；候选想法不会从文件名直接推断。
