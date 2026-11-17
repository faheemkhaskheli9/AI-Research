# 1. Continual learning and persistent memory

**Research brief · 2026-11-18 · scoping synthesis; no independent reproduction.**

## Scientific motivation

A deployed agent must integrate experiences that change its future policy, while avoiding catastrophic forgetting and fabricated memories. Retrieval, in-context adaptation, and weight updates are distinct mechanisms: a longer prompt can improve scores without a learned reusable skill.

## State of research through November 2026

Research now treats memory as a modular system, not a single vector store. 2026 work includes a memory-centric architectural position, feedback-based evaluation, and test-time policy changes using retrieved trajectories. None by itself proves human-like lifelong learning. Established memory benchmarks may measure mixtures of personalization, recall and true transfer; analyze these separately.

### Source-audited literature

| Work (original source) | Evidence status | Contribution (author report) | Critical limitation |
|---|---|---|---|
| [Position: Modular Memory is the Key to Continual Learning Agents](https://proceedings.mlr.press/v306/dorovatas26a.html) | ICML 2026; position | A design argument for combining in-context and in-weight learning. | An architectural thesis, not evidence that a particular memory pipeline is optimal. |
| [MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://proceedings.mlr.press/v306/ai26e.html) | ICML 2026; benchmark | Feedback-driven tasks in multiple domains and languages. | Benchmark success can still conflate retrieval and learning. |
| [Just-In-Time Reinforcement Learning](https://proceedings.mlr.press/v306/li26cv.html) | ICML 2026; method | Retrieves trajectories and applies action-advantage logit adjustments without gradient updates. | Requires checking reward quality, retrieval budgets and robustness to contaminated feedback. |

**Evidence discipline:** a conference listing verifies publication status, not reproducibility. A preprint is not peer reviewed; an organization demonstration is not a controlled independent evaluation. Source links are citations, not an invitation to redistribute PDFs without permission.

## Open gaps worth testing

1. Demonstrate transfer to *unseen rule families*, not previously answered queries.
2. Decide when experience should become a procedural rule, remain episodic, or be discarded.
3. Detect genuine environment changes without accepting spoofed feedback or erasing valid knowledge.

## Falsifiable research hypothesis

**H1:** Under matched memory and model-call budgets, an evidence-gated consolidation policy will outperform recency retrieval on held-out sequential tasks, especially when feedback has nonzero corruption rates.

**H0:** The proposed mechanism offers no meaningful improvement versus the strongest resource-matched baseline. Define the effect threshold and paired confidence interval *before* looking at test results.

## Experimental design

Use a deterministic task-family generator with hidden rules and task switches, followed by a public benchmark slice. Collect a trusted execution trace; add 0%, 10%, and 30% untrusted forged-memory entries. For each policy, train on identical sequential experience then evaluate on unseen task variants. Repeat at least 10 paired seeds with fixed budgets and report both retention and new-task transfer.

- **Baselines:** No memory; full-context history; last-k retrieval; summary memory; fixed-budget verified memory; JitRL-style no-gradient adaptation when hardware permits.
- **Metrics:** Held-out success, backward/forward transfer, task-switch recovery time, false-memory adoption, storage and inference tokens, paired confidence intervals.
- **Budget/feasibility:** Feasible locally for simulation and modest API-based agent studies; reproducing published LLM baselines may require paid models or GPU time.
- **Do not mistake:** high answer accuracy for grounded learning, model-produced rationale for verified action, or a single demo for a reproducible finding.

## Adversarial review / likely failure

A gain that disappears under equal-context comparisons is likely improved recall, not continual learning. Trusted labels cannot be supplied by retrieved text. Test counterfactual rule changes and false-positive rejection.

## Further repository context

Existing [continual learning notes](../../knowledge/continual_learning.md), [toy experiment](../../experiments/continual_memory/README.md), [strategy](../STRATEGY.md).

**Status:** literature review and experimental proposal only; the above experiment has not been run. Keep positive, null and negative results in version control.
