# AI Research

A reproducible, source-linked research workspace for studying **lifelong learning, reliable autonomous agents, reasoning, world models, and grounded intelligence**.

> **Status:** research knowledge base and educational baselines. No new scientific results are claimed.

## Start here

- [Research map](research/FRONTIERS.md) — twelve active research directions and open problems.
- [Research strategy](research/STRATEGY.md) — focused research program, hypotheses, milestones, and adversarial review.
- [Paper catalog](papers/catalog.json) — curated references with original source links and evidence status.
- [Reading guide](papers/READING_GUIDE.md) — reading order, reproductions, and literature note conventions.
- [Knowledge base](knowledge/README.md) — definitions and methodological guidance.
- [Experiments](experiments/README.md) — offline baseline code and reproducibility details.
- [Roadmap](ROADMAP.md) — measurable objectives and priorities.
- [Contributing](CONTRIBUTING.md) — paper and experiment quality standards.

## Quick start

Requires Python 3.10+; the baseline uses the standard library only.

```bash
python -m unittest discover -s tests -v
python -m experiments.continual_memory.run --seed 42 --episodes 240
python scripts/validate_catalog.py
```

**Research principle:** distinguish a paper's authors' claims, independently verified observations, reproducible experimental results, and our own hypotheses. Summaries are original; links point to source materials rather than redistributing copyrighted PDFs.

Last literature review: **2026-11-18**.
