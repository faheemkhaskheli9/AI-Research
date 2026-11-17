"""Toy contextual-action learning with trusted and forged memory observations.

No LLMs, learned model weights, or hidden-rule generalization are involved.
All 'verified' flags originate from this trusted harness, not from user text.
"""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Dict, Tuple

Key = Tuple[int, int]
ACTIONS = 3
DOMAINS = 3
CUES = 4


@dataclass(frozen=True)
class Episode:
    key: Key
    answer: int
    phase: str
    poisoned: bool


class Policy:
    name = "policy"

    def choose(self, key: Key) -> int:
        raise NotImplementedError

    def observe(self, key: Key, action: int, reward: bool, *, verified: bool) -> None:
        raise NotImplementedError


class StatelessPolicy(Policy):
    name = "stateless"

    def choose(self, key: Key) -> int:
        return 0

    def observe(self, key: Key, action: int, reward: bool, *, verified: bool) -> None:
        return None


class MemoryPolicy(Policy):
    """Keep last verified/reported successful action; revise after trusted failures.

    A negative report invalidates the current preference and eliminates that
    action from the immediate exploration cycle. All failures or successes are
    key-local. This is a tiny policy, not a neural memory mechanism.
    """

    def __init__(self, *, require_verified: bool):
        self.require_verified = require_verified
        self.name = "verified" if require_verified else "episodic"
        self.preferred: Dict[Key, int] = {}
        self.excluded: Dict[Key, set[int]] = {}

    def choose(self, key: Key) -> int:
        if key in self.preferred:
            return self.preferred[key]
        excluded = self.excluded.setdefault(key, set())
        available = [i for i in range(ACTIONS) if i not in excluded]
        if not available:
            excluded.clear()
            available = list(range(ACTIONS))
        return available[0]

    def observe(self, key: Key, action: int, reward: bool, *, verified: bool) -> None:
        if action not in range(ACTIONS):
            raise ValueError("action must be a valid index")
        if self.require_verified and not verified:
            return
        if reward:
            self.preferred[key] = action
            self.excluded.pop(key, None)
        else:
            if self.preferred.get(key) == action:
                del self.preferred[key]
            self.excluded.setdefault(key, set()).add(action)


def make_episodes(seed: int, train_episodes: int, eval_episodes: int,
                  poison_every: int) -> tuple[list[Episode], list[Episode]]:
    if train_episodes < 0 or eval_episodes < 2:
        raise ValueError("train_episodes must be >= 0 and eval_episodes >= 2")
    if poison_every < 0:
        raise ValueError("poison_every must be >= 0")
    rng = random.Random(seed)
    keys = [(domain, cue) for domain in range(DOMAINS) for cue in range(CUES)]
    rules = {key: rng.randrange(ACTIONS) for key in keys}

    def schedule(n: int) -> list[Key]:
        ordered: list[Key] = []
        while len(ordered) < n:
            shuffled = keys.copy()
            rng.shuffle(shuffled)
            ordered.extend(shuffled)
        return ordered[:n]

    train = [Episode(key, rules[key], "train", False)
             for key in schedule(train_episodes)]
    evaluation: list[Episode] = []
    for i, key in enumerate(schedule(eval_episodes)):
        drift = i >= eval_episodes // 2
        answer = (rules[key] + int(drift)) % ACTIONS
        evaluation.append(Episode(key, answer,
                                  "post_drift" if drift else "pre_drift",
                                  poison_every > 0 and i % poison_every == 0))
    return train, evaluation


def evaluate_policy(policy: Policy, train: list[Episode],
                    evaluation: list[Episode]) -> dict:
    for task in train:
        action = policy.choose(task.key)
        policy.observe(task.key, action, action == task.answer, verified=True)

    by_group: dict[str, list[int]] = {
        "overall": [], "pre_drift": [], "post_drift": [],
        "poisoned_trials": [], "unpoisoned_trials": [],
    }
    for task in evaluation:
        if task.poisoned:
            forged_action = (task.answer + 1) % ACTIONS
            policy.observe(task.key, forged_action, True, verified=False)
        action = policy.choose(task.key)
        correct = int(action == task.answer)
        policy.observe(task.key, action, bool(correct), verified=True)
        by_group["overall"].append(correct)
        by_group[task.phase].append(correct)
        by_group["poisoned_trials" if task.poisoned else "unpoisoned_trials"].append(correct)

    return {name: {"n": len(samples),
                   "successes": sum(samples),
                   "success_rate": round(sum(samples) / len(samples), 6)
                   if samples else None}
            for name, samples in by_group.items()}


def run_experiment(*, seed: int = 42, train_episodes: int = 120,
                   eval_episodes: int = 240, poison_every: int = 5) -> dict:
    train, evaluation = make_episodes(seed, train_episodes, eval_episodes, poison_every)
    policies: list[Policy] = [
        StatelessPolicy(), MemoryPolicy(require_verified=False),
        MemoryPolicy(require_verified=True),
    ]
    return {
        "experiment": "toy_continual_memory_v1",
        "seed": seed, "train_episodes": len(train),
        "eval_episodes": len(evaluation), "poison_every": poison_every,
        "policies": {policy.name: evaluate_policy(policy, train, evaluation)
                     for policy in policies},
        "limitations": (
            "Deterministic toy with binary feedback; no LLM, public benchmark, "
            "capacity matching, uncertainty intervals, or novel method claims."
        ),
    }
