# 2. Reliable long-horizon autonomous agents

**Research brief · 2026-11-18 · scoping synthesis; no independent reproduction.**

## Scientific motivation

A single correct tool call does not guarantee completion of a workflow. Real tasks require maintaining authority boundaries, tracking partial state, noticing drift, retrying safely and verifying side effects across hundreds of actions.

## State of research through November 2026

OSWorld 2.0 introduces realistic long workflows and challenge labels for computer-use agents; the author site describes more than 250 average agent steps for tasks. Neuro-symbolic skill induction is a competing strategy for encoding state-dependent policies. Published benchmark scores depend heavily on agent harness, tools and budget; avoid comparing model names without normalization.

### Source-audited literature

| Work (original source) | Evidence status | Contribution (author report) | Critical limitation |
|---|---|---|---|
| [OSWorld 2.0: Benchmarking Computer-Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537) | 2026 preprint + benchmark site | Evaluates 108 long-horizon computer-use workflows; multi-app workflows expose failures missed by short tasks. | GUI/browser environment, infrastructure versions and step budgets complicate replication. |
| [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](https://proceedings.mlr.press/v306/shao26i.html) | ICML 2026; method | Induces reusable modular, condition-aware action programs from interaction traces. | Need to measure adaptation to unforeseen state changes rather than memorized workflows. |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | ICLR 2023; foundational | Interleaves action and environment feedback for tool-using language models. | Reasoning text is neither a verified state nor proof of successful external effects. |

**Evidence discipline:** a conference listing verifies publication status, not reproducibility. A preprint is not peer reviewed; an organization demonstration is not a controlled independent evaluation. Source links are citations, not an invitation to redistribute PDFs without permission.

## Open gaps worth testing

1. Model explicit workflow checkpoints and verify final external state, not agent-written completion messages.
2. Identify whether recovery improves with verified snapshots or simply greater retry budgets.
3. Distinguish planning failures from perception, authority, execution and environment-state failures.

## Falsifiable research hypothesis

**H1:** Structured checkpoint verification plus bounded rollback/replanning improves end-to-end success relative to the same agent with equal action budget and logging alone.

**H0:** The proposed mechanism offers no meaningful improvement versus the strongest resource-matched baseline. Define the effect threshold and paired confidence interval *before* looking at test results.

## Experimental design

Create 30–50 sandboxed workflows with intentionally flaky tool responses, delayed effects, stale screenshots and interrupted checkpoints. Randomize injection position; compare each configuration on paired seeded task streams. Then replicate on a subset of OSWorld 2.0 where benchmark harness access permits. Log planned actions, observed state, confirmed state, recovery actions, and genuine task completion.

- **Baselines:** Reactive ReAct loop; plan-and-execute; ReAct with retries; ReAct with checkpoint verifier; skill induction with verifier.
- **Metrics:** Full-workflow success, checkpoint correctness, recovery success, steps, retries, tool cost, time, unauthorized action count.
- **Budget/feasibility:** Start with a sandboxed Python/browser state machine; OSWorld 2.0 may require substantial setup and model inference budget.
- **Do not mistake:** high answer accuracy for grounded learning, model-produced rationale for verified action, or a single demo for a reproducible finding.

## Adversarial review / likely failure

A verifier using the agent's own answer is circular. Avoid tests with forgiving graders or leaked endpoint state; use independent environment oracles. Extra retry budget must be matched.

## Further repository context

[Agent strategy](../STRATEGY.md), [evaluation checklist](../../knowledge/evaluation.md), [control review](../INTERPRETABILITY_AI_CONTROL_LITERATURE_REVIEW.md).

**Status:** literature review and experimental proposal only; the above experiment has not been run. Keep positive, null and negative results in version control.
