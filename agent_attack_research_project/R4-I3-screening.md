# R4 screening — I3 tool-metadata preference to persistent routing

**Date:** 2026-11-07
**Status:** overlap / do not run
**Paper target:** ICML 2027 primary; next AAAI cycle secondary

## Candidate

I3 proposed that an attacker who controls only a tool name/description in an authorized sandbox could create a
persistent tool-selection preference that transfers across later tasks or downstream Agents.

## Local-corpus neighbours

- A10 MCPTox: benchmark for tool poisoning on real-world MCP servers;
- A11 MPMA: MCP preference manipulation;
- A19 ToolHijacker: tool-selection injection;
- B13 MemIncept: benign-query memory injection;
- B14 cross-tool control-flow theft and contamination;
- C17 long-horizon tool attacks.

## Public pre-emption screen

The quick public screen found work that directly overlaps the proposed delta:

- [MCPTox arXiv record](https://arxiv.org/abs/2508.14925) covers MCP tool poisoning and tool metadata attacks;
- [MCP-ITP](https://arxiv.org/abs/2601.07395) extends tool poisoning toward implicit selection of legitimate
  high-privilege tools;
- [MemMorph](https://arxiv.org/abs/2605.26154) directly studies tool hijacking through memory poisoning;
- [A2M](https://arxiv.org/abs/2609.26761) studies metadata attraction followed by tool-output/trace steering;
- [AAAI tool-poisoning publication record](https://ojs.aaai.org/index.php/AAAI/article/view/40895) is a venue-level
  source for the MCPTox line of work.

## Verdict

I3 is **pre-empted or too close to existing work as currently stated**. The proposed “persistent preference and
cross-agent transfer” wording is not enough to establish a paper contribution without full-text evidence showing a
specific unmeasured state, access constraint or defense boundary.

No I3 claim is registered and no I3 experiment is run.

## What would be needed to reopen it

A revised idea would need a new mechanism-level delta, for example a formally constrained provenance or routing
condition that the cited work does not measure, with full-text verification and a new control matrix. It must not
merely add more tasks, more Agents, more rounds or another tool benchmark.
