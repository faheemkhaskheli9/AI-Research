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

## Multimodal temporal reasoning track
See [MULTIMODAL_TEMPORAL_STRATEGY.md](research/MULTIMODAL_TEMPORAL_STRATEGY.md).
- [x] Literature review of 2025–2026 temporal grounding, audio-visual and memory work.
- [ ] Baseline: open omni model on SONIC-O1 localization, with vs without audio.
- [ ] Training-free attention-based timestamp decoding (H4).
- [ ] Action + audio event log pipeline; ablations for H1 and H3.
- [ ] Event graph + memory on long-video and causal benchmarks (H2).
- [ ] Demographic fairness analysis of localization errors.
- [ ] Pilot Urdu / code-switched audio-video grounding set.

## Multimodal grounded intelligence track (source review: 2026-11-18)

See [literature and adversarial review](research/MULTIMODAL_GROUNDED_INTELLIGENCE.md), [memory model](knowledge/multimodal_event_memory.md), and [experiment protocol](experiments/multimodal_memory/README.md).

- [x] Audit primary papers and update publication status for SONIC-O1.
- [x] Map prior art in hierarchical/event memory, audiovisual grounding and causal evidence.
- [x] Specify falsifiable hypotheses, equal-budget controls, evaluation protocol and resource constraints.
- [ ] Confirm reproducible SONIC-O1 dataset subset/licensing; create pinned manifest and parser.
- [ ] Reproduce oracle-evidence, question-only, recent-only and flat-retrieval baselines.
- [ ] Implement immutable observation and versioned claim schemas with invariants/tests.
- [ ] Add evidence replay and contradiction-based revision, then run preregistered ablations.
- [ ] Extend evaluation to MemInStream, CaST-Bench or EgoMemReason without mixing differing task metrics.
- [ ] Incorporate and verify any additional sources/findings from the full Deep Research report before making performance claims.


## Twelve frontier literature reviews (2026-11-18)

- [x] Source-linked scoping reviews and falsifiable proposals for each of the 12 frontier directions; see [index](research/areas/README.md).
- [x] Cross-reference the reviews against a machine-readable research/paper inventory and enforce it in CI.
- [ ] Preregister and execute **one** selected proposal with a resource-matched baseline and held-out task-family split.
- [ ] Record repeated-seed results with confidence intervals, real budget accounting and negative findings.
- [ ] Refresh each review when a major new primary-source result contradicts or strengthens its thesis.

**Priority:** focus first on provenance-aware continual learning + agent execution verification (areas 01, 02, 05). Reviews are *not* 12 completed experimental implementations.
