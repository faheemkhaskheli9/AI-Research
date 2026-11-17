# Research frontiers — November 2026

This map is a **prioritized research assessment**, not an objective ranking of research quality or conference popularity. A topic is an area of investigation, not a claim that AGI has been reached. Reassess quarterly using primary literature and independently reproducible evidence.

| Area | Central scientific problem | Candidate evaluation |
| --- | --- | --- |
| Lifelong and continual learning | Learn online without catastrophic forgetting or spurious transfer | Sequential task accuracy, backward/forward transfer, memory budget |
| Reliable long-horizon agents | Maintain goals, recover from mistakes, verify actions | Environment task success, intervention rate, cost, steps, recovery |
| Reasoning and reinforcement learning | Make reasoning reliable rather than merely plausible | Outcome accuracy, verification, causal necessity of traces |
| World models and physical intelligence | Predict intervention consequences under distribution shift | Multi-step rollout error, planning regret, out-of-distribution success |
| Interpretability and AI control | Identify dangerous behavior and mismatches between intent and action | Detection recall, false positives, robustness to adaptive tests |
| New model architectures | Improve reasoning/learning under bounded compute | Accuracy per FLOP/token, memory, latency, scaling behavior |
| Causal and neuro-symbolic methods | Separate correlation from intervention and abstraction | Out-of-distribution causal generalization, intervention accuracy |
| Multimodal intelligence | Ground temporal/spatial reasoning across modalities | Localization, synchronization, cross-modal transfer |
| AI for scientific discovery | Generate hypotheses that survive experimental falsification | Prospective reproducibility, independent expert review |
| Embodied AI and robotics | Transfer safe behaviors from simulation to reality | Zero-shot transfer, intervention rate, energy and failure metrics |
| Efficient/decentralized AI | Train, infer, and learn under constrained memory and privacy | Quality/latency/energy Pareto frontier, privacy leakage |
| Multi-agent learning | Coordinate accurately despite partial knowledge and incentives | Team return, communication cost, adversarial robustness |

## Distinguish types of learning

- **Long-context recall**: finding information in a prompt; *not automatically learning*.
- **External episodic memory**: writing and retrieving events; improvements may be instance-specific.
- **Procedural/skill memory**: learning reusable tactics and policies from experience.
- **In-weight continual learning**: updating weights over a task stream, measuring forgetting.
- **Test-time adaptation**: adapting behavior at inference time, sometimes without gradients.

For a strong result, hold out **new task instances with a shared latent structure**. Report improvement over a matched no-memory or equal-token-context baseline, and include the cost of constructing and querying memory.

## Evidence and scope

Start with the [curated catalog](../papers/catalog.json). The most direct 2026 sources are:
- [Modular Memory position paper, ICML 2026](https://proceedings.mlr.press/v306/dorovatas26a.html).
- [MemoryBench, ICML 2026](https://proceedings.mlr.press/v306/ai26e.html).
- [Continual Learning Bench, 2026 preprint](https://arxiv.org/abs/2606.05661).
- [Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning, ICML 2026](https://proceedings.mlr.press/v306/yu26av.html).
- [OSWorld 2.0, 2026 preprint](https://arxiv.org/abs/2606.29537).
- [Stanford HAI 2026 AI Index](https://hai.stanford.edu/ai-index/2026-ai-index-report).

## Research questions with high leverage

1. Under equal storage and inference budgets, which experience-consolidation policy actually increases transfer?
2. Can agents detect and repair procedural errors **without** depending on self-reported correctness?
3. How can online learners distinguish genuine environment changes from adversarial or corrupted feedback?
4. Can intervention-aware latent world models reliably improve decisions on unseen dynamical systems?
5. Can verifiers evaluate intermediate decisions without relying on potentially unfaithful reasoning traces?

Do not optimize for leaderboard scores alone; predefine failure criteria, seek counterexamples, and publish limitations.

## Detailed multimodal track

The initial idea (temporal localization + extended audiovisual memory) has mature 2026 prior art; a plausible differentiated focus is **evidence-provenance-preserving revision under delayed or conflicting observations**. See [survey and falsifiable hypotheses](MULTIMODAL_GROUNDED_INTELLIGENCE.md). Do not claim that an event graph or hierarchical memory alone is novel.


## Per-frontier research reviews

See the [12-field literature index](areas/README.md) for individual source audits, specific hypotheses, reference benchmarks, baseline comparisons and adversarial caveats. Reviews are research proposals; experiments are not yet completed.
