# 5. Mechanistic interpretability, AI control, and trustworthy autonomy

**Research brief · 2026-11-18 · scoping synthesis; no independent reproduction.**

## Scientific motivation

Safety claims require knowing whether a monitor can detect consequential unauthorized behavior, and whether interventions actually reduce harm without destroying legitimate task completion. Reported chain-of-thought may differ from underlying decision-making.

## State of research through November 2026

ICML 2026 falsification experiments find that some SAE features labelled as reasoning respond strongly to superficial cue injection. OpenAI's Nov 10, 2026 monitorability report studies how training and architecture affect chain-of-thought monitoring. These studies argue against interpreting attractive visualizations or narrated steps as direct access to model intent.

### Source-audited literature

| Work (original source) | Evidence status | Contribution (author report) | Critical limitation |
|---|---|---|---|
| [Do Sparse Autoencoders Identify Reasoning Features in Language Models?](https://proceedings.mlr.press/v306/ma26v.html) | ICML 2026; falsification | Uses targeted counterexamples and interventions to challenge SAE reasoning feature labels. | Feature activation alone is not a unique causal explanation. |
| [What affects chain-of-thought monitorability across the model lifecycle?](https://alignment.openai.com/cot-monitorability-model-lifecycle/) | Nov 10, 2026 research report | Compares pretraining, architectures, reinforcement learning and training-data effects on monitoring. | Organization report; monitoring channels and tests must transfer independently. |
| [Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning](https://proceedings.mlr.press/v306/yu26av.html) | ICML 2026; analysis | Separates output correctness from trace sufficiency and causal importance. | A trace that fails an intervention test need not imply deliberate deception. |

**Evidence discipline:** a conference listing verifies publication status, not reproducibility. A preprint is not peer reviewed; an organization demonstration is not a controlled independent evaluation. Source links are citations, not an invitation to redistribute PDFs without permission.

## Open gaps worth testing

1. Detect policy violations using audited tool effects, not only model self-reports.
2. Build adaptive attack tests and control for model-family/verbosity confounds.
3. Measure causal effect of monitoring/blocking on task completion and unauthorized side effects.

## Falsifiable research hypothesis

**H1:** An independent tool-side monitor that sees structured action/state provenance will detect more prohibited side effects under adaptive prompt injection than a chain-of-thought-only monitor at the same false-alarm budget.

**H0:** The proposed mechanism offers no meaningful improvement versus the strongest resource-matched baseline. Define the effect threshold and paired confidence interval *before* looking at test results.

## Experimental design

Use sandbox agent tools with synthetic policies (disallowed file writes, unapproved recipients, budget limits). Construct benign and adversarial traces, including forged tool outputs and misleading explanations. Compare monitor with input-only, CoT-only (if available), tool-arguments-only, and tool-effects+trusted-policy signals. Evaluate before executing candidate actions, and separately measure controller-block success.

- **Baselines:** Rule-based action allowlist; text classifier; CoT monitor; tool-argument monitor; structured side-effect monitor.
- **Metrics:** Detection precision/recall at fixed base rate, false-blocked legitimate tasks, prevented side effects, latency, adaptive attack success.
- **Budget/feasibility:** A strong black-box study can be done with sandboxed synthetic tools and small models; white-box SAE analysis requires model activations and GPU.
- **Do not mistake:** high answer accuracy for grounded learning, model-produced rationale for verified action, or a single demo for a reproducible finding.

## Adversarial review / likely failure

Monitoring CoT may reward hiding indicators rather than safer behavior; test adversaries aware of the monitor. Explainable features can be spurious. Never test destructive actions on real systems.

## Further repository context

Detailed [interpretability and control literature review](../INTERPRETABILITY_AI_CONTROL_LITERATURE_REVIEW.md).

**Status:** literature review and experimental proposal only; the above experiment has not been run. Keep positive, null and negative results in version control.
