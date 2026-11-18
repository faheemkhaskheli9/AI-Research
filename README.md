# AI Research

A reproducible, source-linked research workspace for studying **lifelong learning, reliable autonomous agents, reasoning, world models, and grounded intelligence**, with tracks on **reliable multilingual voice agents for Urdu and Sindhi** and **multimodal temporal reasoning in video**.

> **Status:** research knowledge base and educational baselines. No new scientific results are claimed.

## Start here

- [Research map](research/FRONTIERS.md) — twelve active research directions and open problems.
- [Small reasoning LM + external knowledge adversarial review](research/SMALL_REASONING_LM_EXTERNAL_KNOWLEDGE_ADVERSARIAL_REVIEW.md) — corrected paper claims, falsification risks, and preregistered baselines.
- **[All 12 frontier research reviews](research/areas/README.md)** — verified literature, hypotheses, methods, baselines, evaluation, risks, and compute feasibility.
- [AI research areas overview](research/AI_RESEARCH_AREAS.md) — beginner-friendly map of the field.
- [Multimodal grounded intelligence review](research/MULTIMODAL_GROUNDED_INTELLIGENCE.md) — verified 2026 sources, novelty gaps, hypotheses and evaluation controls.
- [Research strategy](research/STRATEGY.md) — focused research program, hypotheses, milestones, and adversarial review.
- [Interpretability, AI control and trustworthy autonomy](research/INTERPRETABILITY_AI_CONTROL_LITERATURE_REVIEW.md) — source-linked literature synthesis, monitoring taxonomy, adversarial review and 90-day research design.
- [Voice-agent strategy](research/VOICE_AGENTS_STRATEGY.md) — Urdu/Sindhi voice-agent research track.
- [Multimodal temporal strategy](research/MULTIMODAL_TEMPORAL_STRATEGY.md) — audio-video temporal grounding, causal event chains and memory.
- [Multimodal literature review](knowledge/multimodal_temporal_literature_review.md) — 2025–2026 papers, gaps and reading order.
- [Paper catalog](papers/catalog.json) — curated references with original source links and evidence status.
- [Reading guide](papers/READING_GUIDE.md) — reading order, reproductions, and literature note conventions.
- [Knowledge base](knowledge/README.md) — definitions and methodological guidance.
- [Grounded multimodal memory protocol](experiments/multimodal_memory/README.md) — controlled comparisons and implementation gates.
- [Experiments](experiments/README.md) — offline baseline code and reproducibility details.
- [Roadmap](ROADMAP.md) — measurable objectives and priorities.
- [Contributing](CONTRIBUTING.md) — paper and experiment quality standards.

## Quick start

Requires Python 3.10+; all code uses the standard library only.

```bash
python -m unittest discover -s tests -v
python -m experiments.continual_memory.run --seed 42 --episodes 240
python -m experiments.voice_eval.run_demo
python scripts/validate_catalog.py
```

**Research principle:** distinguish a paper's authors' claims, independently verified observations, reproducible experimental results, and our own hypotheses. Summaries are original; links point to source materials rather than redistributing copyrighted PDFs.

Last literature review: **2026-11-18**.
