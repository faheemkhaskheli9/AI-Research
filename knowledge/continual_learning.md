# Continual learning, memory and lifelong agents

## Working vocabulary

- **Catastrophic forgetting:** loss of older-task performance after learning newer tasks.
- **Stability–plasticity dilemma:** balancing retention with adaptation.
- **Backward transfer (BWT):** how learning later tasks changes performance on earlier tasks; negative BWT may indicate forgetting, depending on definition.
- **Forward transfer (FWT):** how prior experience helps performance on tasks not previously learned.
- **Episodic memory:** records of particular observations and outcomes.
- **Semantic memory:** generalized facts or relations.
- **Procedural memory:** reusable skills or action policies.
- **Non-parametric adaptation:** behavior changes without weight updates, e.g. via memory or retrieval.
- **In-weight learning:** parameter changes that persist beyond an inference context.

## What to measure

Separate *recollection accuracy* from *behavioral improvement*. A memory may retrieve the correct past observation yet still choose a worse next action. Conversely, an agent may perform well through strong pretrained priors without learning from the current interaction stream. Evaluate on **sequential, causally related, held-out experiences** and control for growing context length.

A minimal task stream should include:
1. stable shared patterns and a no-memory baseline;
2. task switches and negative interference;
3. environment drift requiring timely revision;
4. noisy/forged feedback and an explicit provenance policy;
5. a fixed memory budget and independent seeds.

## Reading

- [Modular Memory is the Key to Continual Learning Agents](https://proceedings.mlr.press/v306/dorovatas26a.html) (ICML 2026 position paper): framework combining in-context and in-weight adaptation.
- [MemoryBench](https://proceedings.mlr.press/v306/ai26e.html) (ICML 2026): benchmark for memory and feedback-driven learning.
- [CL-Bench](https://arxiv.org/abs/2606.05661) (2026 preprint): distinguishes experience-dependent gains from starting model capability.
- [Memory-Centric Continual Learning](https://arxiv.org/abs/2610.29357) (2026 preprint): evaluates retention, adaptation, and transfer.
- [JitRL](https://proceedings.mlr.press/v306/li26cv.html) (ICML 2026): no-gradient adaptation using retrieval and action advantages.

## Open problems

- Does consolidation yield **compositional generalization** or just a better cache?
- Can memories be both evidence-grounded and resilient to genuine regime changes?
- How can retrieval and policy-update costs be measured on the same budget?
- How should multi-session, partially conflicting memories be audited?
