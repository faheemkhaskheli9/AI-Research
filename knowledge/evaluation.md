# Experimental and research evaluation protocol

## Validity

**Construct validity:** prove that the experiment actually tests learning, not recall, target leakage, or access to answer keys.

**Internal validity:** use the same task stream, reward visibility, training budget, memory budget, and feedback schedule across systems.

**External validity:** move from toy examples to established agent environments and finally prospectively collected tasks. Label every environment with its threat model and limitations.

**Statistical validity:** predefine seeds and metrics, use repeated trials and paired confidence intervals, report failures and variance.

## Core metrics

- **Success rate:** correct completed tasks / attempted tasks.
- **Retention:** performance on earlier tasks after learning new ones versus before; report both values and difference.
- **Adaptation lag:** number of observations after a verified change before performance recovers above a prespecified threshold.
- **Forward transfer:** improvement on previously unseen tasks sharing a learnable mechanism.
- **Contamination sensitivity:** drop in success when forged feedback or irrelevant memory is present.
- **Long-horizon reliability:** full-task success, checkpoint correctness, error-recovery success, and step count.
- **Efficiency:** token usage, inference calls, retrieval time, memory bytes, training cost, and energy if measurable.
- **Calibration:** correctness as a function of confidence; selective prediction or abstention where appropriate.

## Protocol checklist

- [ ] Freeze test data and protocols before selecting hyperparameters.
- [ ] Prevent train/eval contamination; split by hidden rule or environment, not just random prompts.
- [ ] Implement a non-learning baseline and at least one well-matched strong baseline.
- [ ] Run an equal-context/no-memory ablation.
- [ ] Log seeds, exact versions, environment fixtures, budgets and failures.
- [ ] Include poisoned-input and benign distribution-shift tests.
- [ ] Publish both aggregate and per-environment results.
- [ ] Mark untested claims as hypotheses.

## Threat modeling memory integrity

An agent should never accept a retrieved document's claim that it was 'verified' as proof of verification. Verification must be attached by the *trusted execution harness* after observing a tool/environment outcome. Test both incorrect benign feedback and an adversary that writes a forged positive outcome into a low-trust store.

The offline demonstration [here](../experiments/README.md) models an explicit trusted/untrusted flag, not cryptographic provenance or actual LLM agent execution.

## Reference benchmarks

- [MemoryBench](https://proceedings.mlr.press/v306/ai26e.html).
- [CL-Bench](https://arxiv.org/abs/2606.05661).
- [OSWorld 2.0](https://arxiv.org/abs/2606.29537).
- [AgentBench](https://arxiv.org/abs/2308.03688).
- [SWE-bench](https://arxiv.org/abs/2310.06770).

Each has a different construct; don't collapse its score into a universal 'intelligence' metric.
