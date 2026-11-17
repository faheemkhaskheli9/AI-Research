"""CLI for deterministic toy continual-memory experiments."""
import argparse
import json

from .core import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--episodes", type=int, default=240,
                        help="Number of evaluation episodes")
    parser.add_argument("--train-episodes", type=int, default=120)
    parser.add_argument("--poison-every", type=int, default=5,
                        help="Attack every N evaluation episodes, or 0 to disable")
    args = parser.parse_args()
    result = run_experiment(seed=args.seed, train_episodes=args.train_episodes,
                            eval_episodes=args.episodes, poison_every=args.poison_every)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
