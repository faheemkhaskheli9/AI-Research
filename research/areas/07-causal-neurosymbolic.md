# 7. Causal AI and neuro-symbolic reasoning

**Research brief · 2026-11-18 · source-linked scoping review, not an independent reproduction.**

## Research motivation and definitions

Generalization requires separating predictive correlations from causal mechanisms, while symbolic constraints can make some intermediate decisions verifiable. Causal discovery, theorem proving and natural-language logic are different tasks and must not be collapsed into a single 'reasoning' metric.

## State of research through November 2026

2026 ICML research explores symbolic validation and trace-to-program induction. ICLR 2026 work investigates how learned cross-modal representations preserve causal structure. Formal solvers can detect invalid derivations, but incorrect formalization and non-identifiability of causal structure remain central limitations.

### Primary-source literature

| Paper / research report | Evidence level | Main contribution (as described by authors) | Limitation to investigate |
|---|---|---|---|
| [LogicSAGE: Neuro-Symbolic Reasoning with Socratic-Guided Enhancement](https://proceedings.mlr.press/v306/tian26m.html) | ICML 2026; method | Combines language-based inference, solver verification and iterative correction. | Correct proof of a wrong formalization is still wrong. |
| [Lifting Traces to Logic](https://proceedings.mlr.press/v306/shao26i.html) | ICML 2026; agent skills | Induces condition-sensitive programs from agent trajectories. | Must test unseen conditions and conflicting state updates. |
| [CARL: Preserving Causal Structure in Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d63cf0622eed012a17fe88fced64dcb8-Abstract-Conference.html) | ICLR 2026; representation learning | Studies causal-structure preservation in learned cross-modal representations. | Representations may retain confounders under new interventions. |

Distinguish source verification from *replication*: conference status verifies publication, not robustness. Preprints and organization demonstrations require explicit status labels and independent testing.

## Open research problems

1. Recover stable mechanisms after interventions rather than memorizing observations.
2. Combine uncertain neural perception with exact symbolic constraints without cascading formalization errors.
3. Distinguish correlation, intervention, and counterfactual assumptions in generated explanations.

## Candidate hypothesis

**H1:** Explicit latent causal variables plus a symbolic constraint check will improve performance under intervention shift over purely predictive sequence models with matched training data.

**H0:** The method does not outperform the strongest budget-matched baseline on predeclared held-out tasks. Publish null and negative results as well as successes.

## Proposed experiment

Generate structural causal models (SCMs) with known DAGs, exogenous noise, and interventions. Train a small neural predictor and a causal-structure-aware variant on identical observational and intervention datasets. Add a deterministic logical constraint stage, then evaluate unseen interventions, flipped spurious correlations, and cases with ambiguous causal direction. Prevent label leakage through input variable names.

- **Baselines:** Ordinary MLP/regression predictor; supervised SCM; neural + symbolic checker; oracle SCM upper bound; randomized graph ablation.
- **Metrics:** Interventional prediction error, OOD accuracy, constraint violations, counterfactual consistency, sensitivity to non-identifiability, compute.
- **Feasibility:** CPU-feasible with generated SCMs and toy symbolic solvers; real data requires causal identifiability scrutiny.

Report exact data splits, per-task outcomes, preprocessing, model/build versions, compute and inference budgets, and paired uncertainty intervals. Reproduction must be distinguished from a new empirical result.

## Adversarial review

A synthetic SCM can reward assumptions engineered into the model. If intervention access is required, report that requirement. High formal accuracy does not imply correct translation of ambiguous natural-language premises.

## Connected research and code

[Experimental protocol](../../knowledge/evaluation.md), [world models notes](../../knowledge/world_models.md).

**Status:** no experiment in this proposed review has yet been run; results are not being claimed.
