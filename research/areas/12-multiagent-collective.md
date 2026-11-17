# 12. Multi-agent learning and collective intelligence

**Research brief · 2026-11-18 · source-linked scoping review, not an independent reproduction.**

## Research motivation and definitions

Multiple agents do not guarantee better decisions. Teams can amplify correlated hallucinations, duplicate work, generate costly communications, or fail to cooperate despite individually capable models.

## State of research through November 2026

ICML 2026 studies distilled coordination policies and reports cooperation failures even in tasks with little cost to helping. AgentWorld (Sept 2026 preprint) introduces longer collaborative workflows. Findings suggest measuring team behavior under partial observability and budgets rather than assuming that adding agents improves reliability.

### Primary-source literature

| Paper / research report | Evidence level | Main contribution (as described by authors) | Limitation to investigate |
|---|---|---|---|
| [Distilling Task-Level Coordination Policies for Generalizable Multi-Agent Cooperation](https://proceedings.mlr.press/v306/zhai26c.html) | ICML 2026; method | Distills LLM coordination into lighter team policies; evaluates cooperative environments. | Distillation may be layout- and communication-protocol-dependent. |
| [More Capable, Less Cooperative? When LLMs Fail at Zero-Cost Collaboration](https://proceedings.mlr.press/v306/yadav26a.html) | ICML 2026; behavioral analysis | Documents cooperation failures not fully predicted by individual model capability. | Behavior in curated games does not generalize to all incentives. |
| [AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-Agent LLMs](https://arxiv.org/abs/2609.31590) | Sep 2026 preprint; benchmark | Benchmarks persistent multi-agent collaboration under longer workflows. | Team success can hide inefficient communications and role leakage. |

Distinguish source verification from *replication*: conference status verifies publication, not robustness. Preprints and organization demonstrations require explicit status labels and independent testing.

## Open research problems

1. Establish when multi-agent architectures outperform a strong single agent with equal inference tokens.
2. Learn communication protocols robust to dropped messages, unequal knowledge and deceptive teammates.
3. Evaluate stable division of labor and credit assignment, not debate volume.

## Candidate hypothesis

**H1:** A task-adaptive sparse communication scheduler improves team utility per inference token under partial observability relative to fixed always-chat teams at equal coordination budgets.

**H0:** The method does not outperform the strongest budget-matched baseline on predeclared held-out tasks. Publish null and negative results as well as successes.

## Proposed experiment

Start with Overcooked-style coordination or distributed grid logistics. Give agents private partial maps or goals, allow messages with costs and delays, and vary team size. Compare centralized oracle, independent learners, always-chat agents, fixed-period messages and task-adaptive messaging. Insert correlated mistaken beliefs and a single unreliable teammate.

- **Baselines:** Best single agent where meaningful; independent agents; centralized coordinator; fixed-period communication; adaptive scheduler.
- **Metrics:** Joint task return, full-task success, messages per solved task, inference tokens, teammate failure sensitivity, welfare/fairness gap, generalization to new teams.
- **Feasibility:** Grid-world simulations feasible on CPU; real multi-agent LLM studies require matched multi-call budgets.

Report exact data splits, per-task outcomes, preprocessing, model/build versions, compute and inference budgets, and paired uncertainty intervals. Reproduction must be distinguished from a new empirical result.

## Adversarial review

If the single agent sees more observations than the group, comparisons are unfair; ensure matched total information and compute. Shared base models produce correlated failures, so nominal agent count is not independent evidence.

## Connected research and code

[Agent experiments](02-long-horizon-agents.md), [evaluation protocol](../../knowledge/evaluation.md).

**Status:** no experiment in this proposed review has yet been run; results are not being claimed.
