# 10. Embodied AI, robot learning, and real-world control

**Research brief · 2026-11-18 · source-linked scoping review, not an independent reproduction.**

## Research motivation and definitions

Robotic competence involves closed-loop sensing, dynamics, safety and action latency. Vision-language model fluency does not guarantee robust grasping, human-safe movement or transfer to new bodies, objects and environments.

## State of research through November 2026

ICLR 2026 Cosmos Policy explores converting video-model spatiotemporal priors into visuomotor control. RT-2 and V-JEPA 2 provide influential language-conditioned and video-predictive approaches. Reported simulation performance is informative but depends on robot embodiment, trajectories, task mix and test conditions.

### Primary-source literature

| Paper / research report | Evidence level | Main contribution (as described by authors) | Limitation to investigate |
|---|---|---|---|
| [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/748becc400a57c0e31cfe6a2e7951467-Abstract-Conference.html) | ICLR 2026; policy learning | Uses pretrained video-model priors for action policy adaptation. | Simulation wins may not transfer to contact-rich or unseen physical settings. |
| [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | 2023 research; VLA | Maps multimodal instructions and visual observations to robot actions. | Web knowledge is not a substitute for contact-rich dynamics learning. |
| [V-JEPA 2](https://arxiv.org/abs/2506.09985) | 2025 preprint; video prediction/planning | Studies predictive visual representations and their use in action planning. | A representation that anticipates video is not necessarily calibrated to action interventions. |

Distinguish source verification from *replication*: conference status verifies publication, not robustness. Preprints and organization demonstrations require explicit status labels and independent testing.

## Open research problems

1. Safe policy recovery after distribution shift, occlusion or contact error.
2. Uncertainty-aware shared-control systems that defer to a human when reliability collapses.
3. Cross-embodiment transfer without secretly relying on matched trajectories or favorable calibration.

## Candidate hypothesis

**H1:** An uncertainty-triggered recovery controller can reduce safety-critical failures in unseen manipulations more than simply increasing action replanning frequency.

**H0:** The method does not outperform the strongest budget-matched baseline on predeclared held-out tasks. Publish null and negative results as well as successes.

## Proposed experiment

Use a robot simulator and fixed policies for simple push, pick, place or navigation tasks. Randomize friction, illumination, unseen objects and actuator delay. Compare model-free policy, vision-language-action policy, periodic replanning, and uncertainty-triggered safe recovery. Track separate simulated successes and real-robot results if physical hardware becomes available.

- **Baselines:** Open-loop imitation; standard closed-loop control; reactive replanning; uncertainty-aware stop/recovery; oracle-state control.
- **Metrics:** Task success, collision/hazard events, human interventions, expected calibration error, recovery latency, cross-domain transfer and energy.
- **Feasibility:** Begin with small 2D simulators on CPU; pretrained VLA fine-tuning and physical manipulation normally need greater compute and/or hardware.

Report exact data splits, per-task outcomes, preprocessing, model/build versions, compute and inference budgets, and paired uncertainty intervals. Reproduction must be distinguished from a new empirical result.

## Adversarial review

Simulator labels may leak hidden states; perfect physics and deterministic actuators overstate deployment readiness. Report simulation-only evidence as simulation-only. Do not execute unsafe real-world tests.

## Connected research and code

[World model notes](../../knowledge/world_models.md), [resource links](../../resources/TOOLS.md).

**Status:** no experiment in this proposed review has yet been run; results are not being claimed.
