# 9. AI for scientific discovery and automated research

**Research brief · 2026-11-18 · source-linked scoping review, not an independent reproduction.**

## Research motivation and definitions

An agent that drafts plausible hypotheses or papers is not a scientific discovery engine. Scientific contributions require valid controls, prospective predictions, tool and data provenance, statistical uncertainty and independent replication.

## State of research through November 2026

2026 SciAgentArena and PaperArena expose multi-tool scientific workflows; ICML 2026 SEDRAS proposes symbolically evaluated research problems with controllable inductive structure. AI-Scientist-style pipelines illustrate workflow automation, but automatic peer-review scores, nice-looking plots or internally graded 'novelty' do not establish discovery.

### Primary-source literature

| Paper / research report | Evidence level | Main contribution (as described by authors) | Limitation to investigate |
|---|---|---|---|
| [SciAgentArena: Benchmarking AI Agents for Addressing Scientific Challenges Across Scales](https://arxiv.org/abs/2606.12736) | 2026 preprint; benchmark | Evaluates agents on scientific tasks across domains and levels of complexity. | Benchmark success is not independent experimental validation of a discovery. |
| [SEDRAS: Symbolically Evaluated Deep Research And Science](https://proceedings.mlr.press/v306/carlsson26a.html) | ICML 2026; benchmark | Constructs synthetic symbolically checkable research investigations with controlled difficulty. | Synthetic controlled environments may lack real scientific uncertainty and tooling. |
| [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) | 2024 preprint; research system | Automates ideation, code execution, experiment reporting and manuscript generation. | Automated review and produced paper count are weak proxies for research validity. |

Distinguish source verification from *replication*: conference status verifies publication, not robustness. Preprints and organization demonstrations require explicit status labels and independent testing.

## Open research problems

1. Calibrate whether agent-generated hypotheses outperform preregistered trivial and human baselines prospectively.
2. Distinguish retrieval of previously known findings from truly held-out testable predictions.
3. Automate experimental bookkeeping and validity checks without replacing domain experts.

## Candidate hypothesis

**H1:** An evidence-auditing research assistant with preregistered hypotheses and independent code-based checking will reduce invalid scientific claims versus a similarly resourced general-purpose research agent.

**H0:** The method does not outperform the strongest budget-matched baseline on predeclared held-out tasks. Publish null and negative results as well as successes.

## Proposed experiment

Choose reproducible public datasets with blinded analysis tasks. Register expected controls and valid statistical tests; supply agents the same tools and budget. Evaluate generated analysis plans, code execution, correct statistical claims and prospective holdout performance. Include intentionally misleading related work, data leakage traps and faulty scripts. Have qualified reviewers score claims blind to system identity.

- **Baselines:** Template statistical workflow; single-agent research assistant; multi-agent researcher/reviewer; audited agent with executable checks.
- **Metrics:** Reproduced task success, invalid-claim rate, blinded expert agreement, calibration of predictive claims, false novelty claims, compute/dollar cost.
- **Feasibility:** Low-cost statistical research workflows on tabular data are practical; wet-lab or high-end simulations require collaborations and oversight.

Report exact data splits, per-task outcomes, preprocessing, model/build versions, compute and inference budgets, and paired uncertainty intervals. Reproduction must be distinguished from a new empirical result.

## Adversarial review

The evaluator may share the agent's training-set knowledge or latent bias; choose post-hoc withheld/independent tasks. No synthetic benchmark score alone justifies announcing scientific breakthroughs.

## Connected research and code

[Research methodology](../../knowledge/how_ai_research_works.md), [research evaluation protocol](../../knowledge/evaluation.md), [paper catalog](../../papers/catalog.json).

**Status:** no experiment in this proposed review has yet been run; results are not being claimed.
