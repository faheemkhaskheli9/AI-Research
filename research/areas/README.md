# The 12 frontier research programs

**Latest scoping review: 2026-11-18.** These reviews complement the existing [beginner-oriented AI research areas](../AI_RESEARCH_AREAS.md), which use a *different* twelve-category taxonomy. The original [frontier map](../FRONTIERS.md) is the basis for this index.

**Evidence level:** primary-source-linked review and explicit experimental proposal, **not** a systematic meta-analysis or proof of an original finding. The central research gap and experimental hypothesis in every review are proposals, not authors' established conclusions.

| Research frontier | Research review | First measurable outcome | Practical cost |
|---|---|---|---|
| Continual learning and persistent memory | [Read](./01-continual-learning.md) | held-out transfer and forgetting | low to medium |
| Reliable long-horizon autonomous agents | [Read](./02-long-horizon-agents.md) | full-task completion and recovery | medium |
| Reasoning and verifiable reinforcement learning | [Read](./03-reasoning-and-rl.md) | held-out verified steps and final correctness | medium |
| World models and physical intelligence | [Read](./04-world-models.md) | OOD planning regret and predictive calibration | low to high |
| Interpretability and trustworthy AI control | [Read](./05-interpretability-control.md) | policy-violation recall and false-block rate | medium |
| New AI model architectures | [Read](./06-new-architectures.md) | quality at matched compute and peak memory | medium to high |
| Causal and neuro-symbolic methods | [Read](./07-causal-neurosymbolic.md) | interventional error under shifted distributions | low to medium |
| Multimodal temporal grounding | [Read](./08-multimodal-grounding.md) | temporal evidence accuracy and attribution | medium to high |
| AI for scientific discovery | [Read](./09-ai-for-science.md) | blinded scientific-claim validity and replication | low to high |
| Embodied AI and robotics | [Read](./10-embodied-robotics.md) | safe task success under dynamics shift | medium to high |
| Efficient and federated AI | [Read](./11-efficient-federated-ai.md) | worst-client retention per MB and privacy budget | low to high |
| Multi-agent learning and collective intelligence | [Read](./12-multiagent-collective.md) | team return per communication/token budget | low to medium |

## Suggested execution order

Start with **01 → 02 → 05** for an experimentally connected project: provenance-sensitive memory → long-horizon error recovery → independent effect monitoring. Test distinct hypotheses, but share task-generation, trace schemas, metrics and human review procedures to avoid three incompatible evaluation rigs.

Then investigate **08** (existing in-depth audiovisual event-memory work) and **07** (causal verification) as research extensions. Treat **06**, **10**, and LLM-scale **11** as infrastructure- or compute-intensive until credible small-scale baselines exist.

## Common replication contract

Every claimed result must state: frozen research question; provenance of data, source code and weights; independent holdout design; equal or explicitly accounted budgets; at least one non-learning/no-extra-memory baseline; >=5 independent seeds where stochastic; uncertainty intervals; ablations; adverse conditions; and reproducibility commands. A measured benchmark result is not necessarily scientific generalization.

The [machine-readable frontier registry](index.json) cross-references each review to three paper IDs in [the paper catalog](../../papers/catalog.json). Run `python scripts/validate_frontiers.py` to audit structural completeness. Source URLs are references; third-party papers or weights are not bundled.
