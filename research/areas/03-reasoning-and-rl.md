# 3. Reasoning, planning, and reinforcement learning

**Research brief · 2026-11-18 · scoping synthesis; no independent reproduction.**

## Scientific motivation

A high-scoring final answer can hide unfaithful intermediate claims, brittle search, incorrect tool use, or dependence on spurious rewards. Verifiable reward and process supervision can improve results, but do not by themselves establish causally faithful reasoning.

## State of research through November 2026

ICML 2026 separates correctness of outcomes from causal importance and sufficiency of reasoning. ICLR 2026 research uses formal Lean feedback for process-level supervision; ICML 2026 explores formal symbolic verification in natural-language reasoning. These results motivate precise verifier definitions rather than assuming verbose chains of thought are trustworthy.

### Source-audited literature

| Work (original source) | Evidence status | Contribution (author report) | Critical limitation |
|---|---|---|---|
| [Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning](https://proceedings.mlr.press/v306/yu26av.html) | ICML 2026; analysis | Introduces causal-importance and sufficiency diagnostics for reasoning traces. | Interventions are task- and model-specific; text may not reveal all computation. |
| [Process-Verified Reinforcement Learning for Theorem Proving via Lean](https://proceedings.iclr.cc/paper_files/paper/2026/hash/554a5982e26d0129f4038ad7a68fb3aa-Abstract-Conference.html) | ICLR 2026; method | Uses proof-assistant feedback as structured intermediate reward signals. | Formal theorem proving has stronger verification than open-world tasks. |
| [Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models](https://proceedings.mlr.press/v306/cao26y.html) | ICML 2026; method | Combines language reasoning with formal verification signals. | Solver coverage and formalization errors limit generality. |

**Evidence discipline:** a conference listing verifies publication status, not reproducibility. A preprint is not peer reviewed; an organization demonstration is not a controlled independent evaluation. Source links are citations, not an invitation to redistribute PDFs without permission.

## Open gaps worth testing

1. Train effective search with verifiers that are independent of model text.
2. Measure trace faithfulness using interventions, not merely text quality judgments.
3. Characterize generalization to problems with no readily available verifier.

## Falsifiable research hypothesis

**H1:** Using executable intermediate-step checks can improve robustness on held-out compositional tasks relative to binary outcome-only reward at matched interaction cost.

**H0:** The proposed mechanism offers no meaningful improvement versus the strongest resource-matched baseline. Define the effect threshold and paired confidence interval *before* looking at test results.

## Experimental design

Generate multi-step symbolic tasks with executable checkers (algebraic transforms, dependency planning, program synthesis). Compare terminal-only reward, dense but noisy process reward, and exact intermediate verification. Train a small policy or perform controlled search; evaluate on unseen depth, operation ordering and misleading feedback. Separately perturb intermediate steps to estimate whether the trace influences the answer.

- **Baselines:** Best-of-N samples with outcome checker; process reward ranking; exact step verification; identical search budget without supervision.
- **Metrics:** Final correctness, proof-check success, trace sufficiency, performance at unseen depth, model calls, total generated tokens.
- **Budget/feasibility:** Use procedural symbolic tasks and an off-the-shelf small model initially; full RL training is compute-intensive.
- **Do not mistake:** high answer accuracy for grounded learning, model-produced rationale for verified action, or a single demo for a reproducible finding.

## Adversarial review / likely failure

Solver checkers may accept the wrong abstraction; a proof may be valid for a wrongly formalized problem. Avoid cherry-picked demos and test latent-rule counterexamples.

## Further repository context

[Research evaluation protocol](../../knowledge/evaluation.md), [interpretability review](../INTERPRETABILITY_AI_CONTROL_LITERATURE_REVIEW.md).

**Status:** literature review and experimental proposal only; the above experiment has not been run. Keep positive, null and negative results in version control.
