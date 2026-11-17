# 4. World models and physical intelligence

**Research brief · 2026-11-18 · scoping synthesis; no independent reproduction.**

## Scientific motivation

A world model may generate persuasive motion but fail to predict what would happen after an action or intervention. Grounded planning requires calibrated transitions, causal counterfactuals and correction when simulated dynamics diverge from observations.

## State of research through November 2026

DreamerV3 demonstrated a general model-based RL paradigm; V-JEPA 2 investigates visual predictive representations and planning. October 2026 Genie 4 is an industrial research demonstration of interactive audiovisual simulations. Reported realism does not imply calibrated physical dynamics, and some system details or training resources are not available for independent replication.

### Source-audited literature

| Work (original source) | Evidence status | Contribution (author report) | Critical limitation |
|---|---|---|---|
| [Mastering Diverse Domains through World Models (DreamerV3)](https://arxiv.org/abs/2301.04104) | 2023 research; model-based RL | Learns latent dynamics and chooses behavior using imagined trajectories. | RL benchmark performance need not guarantee open-world causal understanding. |
| [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) | 2025 preprint; predictive representation | Studies video-based latent representations with action-conditioned robot planning. | Strong visual pretraining can still suffer under shifted dynamics. |
| [Genie 4: A New Generation of World Simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) | Oct 2026 organization research report | Describes interactive environments with native audio and improved physical coherence. | Public demonstration is not a peer-reviewed, reproducible control benchmark. |

**Evidence discipline:** a conference listing verifies publication status, not reproducibility. A preprint is not peer reviewed; an organization demonstration is not a controlled independent evaluation. Source links are citations, not an invitation to redistribute PDFs without permission.

## Open gaps worth testing

1. Predict controllable action outcomes under shifted gravity, friction and object interactions.
2. Measure *planning regret* of learned vs. true simulators, not just visual quality.
3. Use model uncertainty to decide when to simulate, seek observations or abstain.

## Falsifiable research hypothesis

**H1:** Planning with calibrated model-uncertainty penalties reduces catastrophic rollout errors under held-out dynamics relative to optimistic model-based planning.

**H0:** The proposed mechanism offers no meaningful improvement versus the strongest resource-matched baseline. Define the effect threshold and paired confidence interval *before* looking at test results.

## Experimental design

Train a lightweight dynamics predictor on synthetic 2-D collisions or grid navigation; randomize physics at test time. Compare random actions, model-free control, deterministic learned-model planning, uncertainty-aware planning and an oracle-simulator upper bound. At horizons 1, 5, 20, and 50 steps, log predicted state distribution, state error and realized reward.

- **Baselines:** Oracle simulator; model-free policy; deterministic latent model; ensemble or probabilistic model with uncertainty; no-planning policy.
- **Metrics:** Multi-step rollout calibration, planning regret, return, collision rate, out-of-distribution sensitivity, sample/compute cost.
- **Budget/feasibility:** Small world-model experiments are achievable on laptop/CPU; general-purpose video world models require major compute.
- **Do not mistake:** high answer accuracy for grounded learning, model-produced rationale for verified action, or a single demo for a reproducible finding.

## Adversarial review / likely failure

An accurate next-frame predictor can exploit background shortcuts. Test intervention-based transitions and unseen dynamics. Do not equate interactive video generation with causal identification.

## Further repository context

[World models notes](../../knowledge/world_models.md), [multimodal track](../MULTIMODAL_GROUNDED_INTELLIGENCE.md).

**Status:** literature review and experimental proposal only; the above experiment has not been run. Keep positive, null and negative results in version control.
