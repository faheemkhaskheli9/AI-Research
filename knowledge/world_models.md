# World models and grounded intelligence

A **world model** is a learned representation of environment dynamics that supports prediction, imagination, or action selection. Strong reconstruction quality alone does not establish causal understanding or control competence.

## Three distinct research tracks

1. **Predictive representation learning:** representation consistency and future-state prediction (e.g. [V-JEPA 2](https://arxiv.org/abs/2506.09985)).
2. **Model-based reinforcement learning:** optimize behavior using imagined trajectories (e.g. [DreamerV3](https://arxiv.org/abs/2301.04104)).
3. **Vision-language-action control:** transfer multimodal pretraining into actions (e.g. [RT-2](https://arxiv.org/abs/2307.15818)).

## Questions and evaluation

- Can an action-conditioned model predict effects of **interventions**, not just video frames?
- How does rollout uncertainty compound over longer horizons?
- What transfers from simulated environments to novel dynamics?
- What is the effect of learning an inaccurate model on downstream control?

Evaluate one-step and multi-step prediction, control reward, state coverage, counterfactual interventions, robustness under shifted physics, and compute. Avoid inferring a physical understanding claim from good-looking video outputs alone.

For an affordable starting point: use a small gridworld or deterministic dynamical system with controllable changes; then migrate to an established simulation environment.
