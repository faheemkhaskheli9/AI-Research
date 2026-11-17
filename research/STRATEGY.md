# Research strategy: verified lifelong learning for autonomous agents

**Focus:** continual learning and memory (40%), reliable planning/verification (30%), reinforcement and causal learning (20%), grounded world models (10%). These percentages are a planning heuristic, not experimentally established priorities.

## Research thesis

A memory subsystem should be judged by **whether future actions improve**, not by answer-retrieval accuracy alone. We will test whether evidence-gated consolidation of episodic experience into reusable policies yields higher robust transfer at a fixed memory and compute budget.

**H0 (null):** verified consolidation does not improve task success or retention relative to matched memory and context baselines.

**H1 (alternative):** verified consolidation improves action success, retention, and contamination robustness on held-out task streams under matched budgets.

These are untested hypotheses; this repository currently contains only an educational simulation, not evidence for H1.

## Research program

### RQ1 — Behavior learning or merely retrieval?
Define task families with a hidden shared rule. Split **by rule family or environment seed**, not by nearly identical prompts. Measure transfer to unseen tasks, not just recall of previously seen answers.

### RQ2 — Memory under interference
Interleave old and new tasks, change latent rules, inject irrelevant events, and attempt malicious/incorrect feedback. Track forgetting and adaptation speed separately.

### RQ3 — Verifiability
Compare trusted environment/tool results, human-verified feedback, self-reported outcomes, and deliberately forged tool feedback. Evaluate provenance controls and detector false positives.

### RQ4 — Cost-aware learning
Fix total token, API, storage, retrieval, and compute budgets across methods; publish accuracy-versus-cost curves.

## Baselines to beat

1. Stateless or frozen policy.
2. Same base model with longer context but no persistent memory.
3. Naive append-only episodic retrieval.
4. Recency-weighted, summarized, and evidence-gated memories.
5. A trained continual-learning approach where feasible.

The included offline demo tests only a subset of these (stateless, naive episodic, evidence-gated episodic). Do not report it as a comparison against LLMs or as original research.

## Evaluation contract (before implementing a novel model)

- **Primary:** held-out success rate at matched budget and fixed seeds.
- **Secondary:** backward transfer/forgetting, forward transfer, adaptation latency, attack success, storage use, token/compute cost, calibration.
- **Controls:** equal number of observations, same tasks, random seed schedule, identical feedback availability, blinded held-out data.
- **Ablations:** no memory; no verifier; no consolidation; no retrieval ranking; no drift handling.
- **Statistics:** repeated seeds, paired confidence intervals, effect size; report failures and negative results.
- **Data integrity:** keep evaluation streams separate, audit benchmark contamination, avoid training on held-out instances.
- **Safety:** sandbox tool execution; keep untrusted text away from trusted provenance metadata.

## Adversarial review

| Criticism | Failure mode | Mitigation |
| --- | --- | --- |
| 'Memory' is just a lookup cache | No generalization | Held-out latent structures, equal-context baseline |
| Verification uses an unrealistic oracle | Inflated gains | Explicit trust model; real signed tool results; noisy-feedback settings |
| Synthetic tasks are too easy | No external validity | Replicate on established environments before claiming transfer |
| Baselines have unequal budgets | Confounded results | Log per-agent retrieval and token cost |
| Training/evaluation leak | Memorization disguised as transfer | Separate seeds, rule splits, contamination audit |
| Prompt or seed cherry-picking | Unstable benefits | Pre-register seeds and report all runs |
| Agent ignores a genuine regime change | Slow adaptation | Controlled drift and time-to-recovery measurement |
| Storing more experience always looks better | Confounded with memory size | Capacity-matched memory ablations |

## 12-month progression

| Months | Deliverable | Exit criterion |
| --- | --- | --- |
| 1–2 | Literature map, hypothesis registry, benchmark design | 20+ primary papers read and annotated |
| 3–4 | Independent reproductions of 2+ methods | Reproducibility scripts and baseline comparisons |
| 5–6 | Task streams with interference/drift/provenance tests | Leakage checks and benchmark report |
| 7–8 | First candidate consolidation algorithm | Source code, ablations, fixed budgets |
| 9–10 | Independent replicated evaluation | Repeated-seed results and negative results |
| 11–12 | Paper/preprint and public reproducibility bundle | Complete methods/results/caveats and submission |

**Go/no-go:** don't claim a breakthrough if matched baselines erase the gain. Publish exact negative results and refine the scientific question.

See [experimental protocol](../knowledge/evaluation.md), [papers](../papers/READING_GUIDE.md), and [roadmap](../ROADMAP.md).
