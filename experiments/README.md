# Experiments

## 01 — Toy continual memory under rule drift and forged feedback

This is a **small, dependency-free, deterministic educational benchmark**. It is NOT a reproduction of MemoryBench, CL-Bench, JitRL, or any LLM benchmark. It does **not** show language learning, new algorithmic novelty, or general intelligence.

### Task

A hidden, deterministic mapping associates `(domain, cue)` with one of three actions. Each agent sees the same sequence of context keys, chooses an action, and receives a **binary** reward from the simulator. It never observes the correct answer directly. Halfway through evaluation, the action mapping changes. At specified intervals, a simulated attacker supplies a forged positive memory observation for a wrong action.

Policies:
- `stateless`: always chooses action 0; ignores feedback.
- `episodic`: remembers the last successful action, accepts forged and genuine feedback.
- `verified`: same learning rule, but accepts only genuine harness-attested feedback.

The latter two differ **only** in memory-write provenance policy. This is a deliberately simple design that isolates one threat model, not a real signed-verification system.

### Run

```bash
python -m unittest discover -s tests -v
python -m experiments.continual_memory.run --seed 42 --episodes 240 --train-episodes 120 --poison-every 5
```

All metrics are computed in-memory and emitted as JSON, including `pre_drift`, `post_drift`, `poisoned_trials`, and `overall` success rates, per policy, plus episode counts and explicit limitations.

### Threat-model and validity limitations

- The **execution harness** controls a trusted Boolean `verified` flag. That flag is not secure against a compromised harness and should never be copied from untrusted retrieved text.
- Attackers can inject fabricated successful memories before selected evaluation steps, not modify the trusted reward from the environment.
- The hidden mapping is sampled with a seed, but there are only a few discrete actions and context keys. No unseen-composition generalization is assessed.
- One shared environment sequence and identical feedback schedule are used across policies; the simpler stateless agent has no adaptive learning.
- There is no capacity-matched memory comparison, long-horizon tool use, LLM, realistic drift process, uncertainty estimator, confidence interval, or separate train/test latent-rule split.
- Metrics are **simulation outputs**, not scientific evidence of a new method or superiority on public benchmarks.

### Next experiment

Use actual CL-Bench or MemoryBench tasks, run paired multiple seeds, match retrieval and storage budgets, add an equal-context baseline, and test whether generalized skills outperform a naive cache.

See [research strategy](../research/STRATEGY.md).
