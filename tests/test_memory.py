"""Tests for the educational continual-memory simulation."""
import unittest

from experiments.continual_memory.core import (
    MemoryPolicy, make_episodes, run_experiment,
)


class MemoryTests(unittest.TestCase):
    def test_verified_ignores_forged_reward(self):
        key = (0, 1)
        safe = MemoryPolicy(require_verified=True)
        unsafe = MemoryPolicy(require_verified=False)
        for policy in (safe, unsafe):
            policy.observe(key, 2, True, verified=True)
            policy.observe(key, 1, True, verified=False)
        self.assertEqual(safe.choose(key), 2)
        self.assertEqual(unsafe.choose(key), 1)

    def test_failure_invalidates_preference_and_explores(self):
        agent = MemoryPolicy(require_verified=True)
        key = (1, 2)
        agent.observe(key, 0, True, verified=True)
        agent.observe(key, 0, False, verified=True)
        self.assertNotEqual(agent.choose(key), 0)

    def test_invalid_action_is_rejected(self):
        agent = MemoryPolicy(require_verified=True)
        with self.assertRaises(ValueError):
            agent.observe((0, 0), 99, True, verified=False)

    def test_deterministic_results_and_same_task_schedule(self):
        a = run_experiment(seed=12, train_episodes=72, eval_episodes=120)
        b = run_experiment(seed=12, train_episodes=72, eval_episodes=120)
        self.assertEqual(a, b)
        for metrics in a["policies"].values():
            self.assertEqual(metrics["overall"]["n"], 120)
            self.assertEqual(metrics["pre_drift"]["n"], 60)
            self.assertEqual(metrics["post_drift"]["n"], 60)
            self.assertEqual(metrics["poisoned_trials"]["n"], 24)
            self.assertEqual(metrics["overall"]["successes"],
                             metrics["pre_drift"]["successes"] +
                             metrics["post_drift"]["successes"])

    def test_no_attack_yields_same_memory_behavior(self):
        result = run_experiment(train_episodes=120, eval_episodes=120, poison_every=0)
        self.assertEqual(result["policies"]["verified"],
                         result["policies"]["episodic"])

    def test_attack_does_not_help_poisoned_agent(self):
        result = run_experiment(seed=42, train_episodes=120, eval_episodes=240)
        safe = result["policies"]["verified"]["overall"]["success_rate"]
        unsafe = result["policies"]["episodic"]["overall"]["success_rate"]
        self.assertGreaterEqual(safe, unsafe)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            make_episodes(42, -1, 20, 5)
        with self.assertRaises(ValueError):
            make_episodes(42, 10, 1, 5)
        with self.assertRaises(ValueError):
            make_episodes(42, 10, 20, -1)


if __name__ == "__main__":
    unittest.main()
