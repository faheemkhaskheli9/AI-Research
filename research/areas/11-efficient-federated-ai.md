# 11. Efficient, private, and federated AI

**Research brief · 2026-11-18 · source-linked scoping review, not an independent reproduction.**

## Research motivation and definitions

Privacy-sensitive learning and local deployment are constrained by non-IID client data, memory, bandwidth, energy and leakage risk. Federated optimization does not automatically provide formal privacy: gradients and adapters can leak information unless accompanied by appropriate threat models and mechanisms.

## State of research through November 2026

ICML 2026 research explores personalized federated LoRA subspaces, robust federated adaptation, heterogeneous adapter sketching and resource-adaptive variants. ICLR 2026 work revisits privacy-preserving LoRA under differential privacy budgets. Efficiency claims must specify architecture, hardware, client churn, privacy guarantee and wall-clock communication.

### Primary-source literature

| Paper / research report | Evidence level | Main contribution (as described by authors) | Limitation to investigate |
|---|---|---|---|
| [FedPissa: Towards Federated Personalized Adaptation of Foundation Models via LoRA Subspace Mapping](https://proceedings.mlr.press/v306/he26p.html) | ICML 2026; federated adaptation | Investigates selective LoRA aggregation and subspace decoupling under heterogeneous clients. | Quality and communication gains are measured under study-specific client partitions. |
| [Federated Sketching LoRA: A Flexible Framework for Heterogeneous Collaborative Fine-Tuning of LLMs](https://proceedings.mlr.press/v306/fang26e.html) | ICML 2026; method | Uses sketching to address heterogeneity in collaborative adapter tuning. | Sketch-size, client dropout and data heterogeneity can reverse gains. |
| [Rethinking LoRA for Privacy-Preserving Federated Learning in Large Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/34b13425b5ba8ad05d97b0043df52ed3-Abstract-Conference.html) | ICLR 2026; privacy study | Studies low-rank adaptation under explicit differential privacy constraints. | A specific epsilon and data setup do not imply universal privacy or utility guarantees. |

Distinguish source verification from *replication*: conference status verifies publication, not robustness. Preprints and organization demonstrations require explicit status labels and independent testing.

## Open research problems

1. Prevent catastrophic forgetting during continual federation, not just single-round adapter aggregation.
2. Quantify member/privacy leakage independently of 'raw data never leaves device'.
3. Optimize usable utility per joule/byte while preserving minority-client performance.

## Candidate hypothesis

**H1:** Client-aware adapter aggregation with bounded replay will improve worst-client retention under sequential non-IID shifts over FedAvg-LoRA at equal communication and privacy budgets.

**H0:** The method does not outperform the strongest budget-matched baseline on predeclared held-out tasks. Publish null and negative results as well as successes.

## Proposed experiment

Partition a small public text/classification corpus by label/language/domain. Simulate 5–20 clients with temporal task shifts and intermittent availability. Compare independent local adapters, FedAvg-LoRA, personalization, and a proposed replay/aggregation variant. Measure both worst-client and weighted-average utility; when privacy is claimed, use a credible DP implementation and report accountant settings and threats.

- **Baselines:** Centralized training upper bound; local-only; FedAvg-LoRA; personalized federated adapters; resource-matched client-aware method.
- **Metrics:** Worst-decile client accuracy, forgetting, communication MB, wall-clock, peak client RAM, privacy epsilon/delta when applicable, measured leakage and energy.
- **Feasibility:** 5–20 CPU simulated clients with small adapters/classifiers are practical; formal DP or realistic LLM-scale studies require specialist tooling and larger compute.

Report exact data splits, per-task outcomes, preprocessing, model/build versions, compute and inference budgets, and paired uncertainty intervals. Reproduction must be distinguished from a new empirical result.

## Adversarial review

Synthetic Dirichlet partitions can be unrealistic; cross-device availability and privacy claims require real assumptions. Compression and fewer transmitted bytes are not proof of confidentiality.

## Connected research and code

[Architecture overview](06-new-architectures.md), [experimental protocol](../../knowledge/evaluation.md).

**Status:** no experiment in this proposed review has yet been run; results are not being claimed.
