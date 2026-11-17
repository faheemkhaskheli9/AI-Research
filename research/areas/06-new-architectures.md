# 6. New architectures and efficient sequence modeling

**Research brief · 2026-11-18 · scoping synthesis; no independent reproduction.**

## Scientific motivation

Autoregressive attention is a powerful baseline but long histories, streaming inputs, and repeated token generation impose memory and latency costs. Novel architectures must demonstrate better quality-efficiency tradeoffs rather than a speedup in a narrow benchmark.

## State of research through November 2026

ICLR 2026 presents Mamba-3 and new ways to reason about hybrid Mamba–Transformer context length. ICML 2026 DiffuMamba combines diffusion generation with a state-space backbone, reporting throughput improvements in the authors' evaluated setting. These are emerging architectural alternatives, not evidence that Transformers have been superseded.

### Source-audited literature

| Work (original source) | Evidence status | Contribution (author report) | Critical limitation |
|---|---|---|---|
| [Mamba-3: Improved Sequence Modeling using State Space Principles](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8abd2043b71a074278d5f687947bff9c-Abstract-Conference.html) | ICLR 2026; architecture | Develops state-space sequence modeling to improve efficient inference. | Architecture wins can reverse with workload, hardware and implementation changes. |
| [DiffuMamba: High-Throughput Diffusion LMs with Mamba Backbone](https://proceedings.mlr.press/v306/singh26d.html) | ICML 2026; architecture | Studies bidirectional Mamba masked diffusion and hybrid attention variants. | Reported throughput is scale-, sequence-length- and batching-dependent. |
| [From Collapse to Control: Understanding and Extending Context Length in Emerging Hybrid Models via Universal Position Interpolation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c72fed3fc0f51d0a11f4e06ede3ef07b-Abstract-Conference.html) | ICLR 2026; context extension | Studies position interpolation across mixed attention/state-space models. | Long-context recall and actual effective reasoning context differ. |

**Evidence discipline:** a conference listing verifies publication status, not reproducibility. A preprint is not peer reviewed; an organization demonstration is not a controlled independent evaluation. Source links are citations, not an invitation to redistribute PDFs without permission.

## Open gaps worth testing

1. Compare attention vs. state-space recurrence at fixed parameter count and useful task accuracy.
2. Assess memory-state stability across hundreds of thousands of streaming tokens.
3. Explore whether short external context plus persistent state solves tasks without hidden state collapse.

## Falsifiable research hypothesis

**H1:** A compact state-space or hybrid recurrent model can outperform a matched Transformer on streaming associative tasks per unit peak memory *without* sacrificing out-of-distribution generalization.

**H0:** The proposed mechanism offers no meaningful improvement versus the strongest resource-matched baseline. Define the effect threshold and paired confidence interval *before* looking at test results.

## Experimental design

Implement a small Transformer, GRU/SSM, and hybrid recurrent learner with identical training tokens and comparable parameter counts. Use synthetic copy, delayed-match and rule-shift streams; benchmark increasing lengths under batch-size and precision controls. Add reset/contamination perturbations and independent OOD samples.

- **Baselines:** Small causal Transformer; GRU; selective state-space model; hybrid attention/state-space network; fixed-context memory retrieval.
- **Metrics:** Accuracy at length, throughput tokens/sec, latency, GPU/CPU peak memory, training FLOPs/steps, effective context retention, error after hidden-state corruption.
- **Budget/feasibility:** Toy recurrent/Transformer comparisons feasible with 6-GB VRAM or CPU; reproduction of 1B-scale diffusion LMs is not locally feasible.
- **Do not mistake:** high answer accuracy for grounded learning, model-produced rationale for verified action, or a single demo for a reproducible finding.

## Adversarial review / likely failure

Naive CPU implementations can unfairly favor one architecture; optimized kernels differ by platform. Avoid inferring 'infinite context' from a bounded-state recurrent model and benchmark model quality and compute jointly.

## Further repository context

[100-token stateful LM literature review](../TINY_100_TOKEN_STATEFUL_LM_LITERATURE_REVIEW.md), [architecture concept](../BRAIN_INSPIRED_100_TOKEN_CONTEXT_ARCHITECTURE.md).

**Status:** literature review and experimental proposal only; the above experiment has not been run. Keep positive, null and negative results in version control.
