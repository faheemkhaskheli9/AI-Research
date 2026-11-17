# Roadmap

The initial repository is an **evidence-organized research workspace**, not a completed AGI system. Each phase has an observable completion criterion.

## P0 — foundation (this revision)
- [x] Original research map and focused thesis.
- [x] Curated catalog of primary papers, with peer-review/preprint status.
- [x] Research methods, threat model, and adversarial review.
- [x] Offline continual-memory demo and test harness.
- [x] Automated paper-catalog validation and CI.

## P1 — establish credible benchmarks
- [ ] Reproduce at least one result on CL-Bench or MemoryBench using matched tasks.
- [ ] Compare no memory, full-context, recency retrieval, and structured memory under equal budgets.
- [ ] Add repeated-seed confidence intervals and per-task logs.
- [ ] Build a held-out task-family evaluation with genuine transfer.
- [ ] Include an explicit feedback corruption threat model and blinded evaluation.

## P2 — develop a novel method
- [ ] Preregister primary hypothesis and baselines.
- [ ] Design evidence-gated procedural memory consolidation with clear mechanism.
- [ ] Ablate verifier, consolidation, retrieval, and drift response.
- [ ] Evaluate multiple models/environments, report costs and failure cases.

## P3 — publish
- [ ] Create reproducibility bundle (configs, exact dependencies, hardware, seeds).
- [ ] Write paper with limitations and independent reproductions.
- [ ] Submit to a relevant peer-reviewed venue only after sufficient results.

## Maintenance
- Weekly: collect candidate papers, verify original venue and code links.
- Monthly: update research notes, contradictions, and implementation learnings.
- Quarterly: reassess thesis using negative evidence and recent peer-reviewed papers.

**Definition of done for experiments:** executable code, tests, baseline comparisons, resource reporting, reproducible results and explicit limitations.

## Voice-agent track (Urdu / Sindhi)
See [VOICE_AGENTS_STRATEGY.md](research/VOICE_AGENTS_STRATEGY.md).
- [x] Language-aware WER/CER and judge-agreement toolkit with tests.
- [ ] Reproduce Whisper WER on FLEURS Urdu test.
- [ ] Annotation guide and task schema for a pilot Urdu/Sindhi/code-switched set (~200 consented utterances).
- [ ] Benchmark ASR and realtime voice models on the pilot set.
- [ ] Judge–human agreement study, Urdu vs. English, with bootstrap CIs.
- [ ] Entity error rate and pass^k task metrics.
- [ ] Workshop submission; then public dataset v1 on Hugging Face.
