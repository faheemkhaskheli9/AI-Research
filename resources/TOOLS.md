# Research resources

Prefer primary sources; verify licenses before redistributing third-party code, datasets, figures or weights.

## Literature and metadata
- [PMLR proceedings](https://proceedings.mlr.press/) — peer-reviewed ICML and other conference proceedings.
- [OpenReview](https://openreview.net/) — review and conference submissions; verify acceptance separately.
- [arXiv](https://arxiv.org/) — preprints; not a peer-review guarantee.
- [Stanford AI Index](https://hai.stanford.edu/ai-index) — broad annual research reporting.
- [Papers with Code](https://paperswithcode.com/) — repository/benchmark discovery; verify against original paper.

## Evaluation and environments
- [OSWorld 2.0](https://osworld-v2.xlang.ai/) — long-horizon computer-use tasks.
- [AgentBench](https://github.com/THUDM/AgentBench) — multi-environment agent benchmark.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) — real repository tasks.
- [JitRL](https://github.com/liushiliushi/JitRL) — author-linked 2026 research implementation.

## Development practice
- Python standard library for tiny deterministically testable harnesses.
- PyTorch for learnable baselines and model ablations when needed.
- `pytest` and `ruff` may be introduced when dependencies justify their cost.
- Save experiments as config + seed + version + machine metadata + metrics.
- Do not commit credentials, restricted datasets, copyrighted PDFs, or large model checkpoints.
