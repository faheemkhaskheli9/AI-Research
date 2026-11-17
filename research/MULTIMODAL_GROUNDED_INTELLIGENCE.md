# Multimodal reasoning and grounded intelligence — targeted literature review

**Reviewed:** 2026-11-18. **Scope:** long-horizon video/audio understanding, temporal localization, persistent event memory, evidence-grounded reasoning, and state/belief revision. **Status:** source-audited research synthesis and experimental proposal; **not** an independent reproduction or a claim of novel results. The separate Deep Research review is still running and is not yet incorporated.

## Research question

Can an agent build a bounded, persistent, **evidence-addressable history** from long audiovisual streams, answer questions about past events, and **revise uncertain interpretations** when subsequent evidence conflicts with stored beliefs—without confusing temporal sequence with causal certainty?

**Precise distinction:** perceptual detection establishes *observations*; an event graph represents *relationships*; retrieval provides *candidate evidence*; a causal assertion requires an appropriate causal basis. An observed sequence "person walked near table → glass fell" does not establish that the person caused the fall.

## Taxonomy: what systems actually do

| Subproblem | Typical methods | Main failure / confound |
| --- | --- | --- |
| Temporal grounding | sampled frames, dense retrieval, segment reranking, timestamp heads | coarse sampling loses decisive events; answer might use language prior |
| Streaming perception | online frame encoders, KV-cache reuse, incremental event extraction | future information may leak into supposed online evaluation |
| Long-video memory | summaries, hierarchical event banks, dynamic visual-text memories, graphs | unsupported summaries become durable false observations |
| Cross-modal grounding | speech/ASR, acoustic events, visual entities, time synchronization | model notices sound but attributes it to wrong visible actor |
| Multi-step event reasoning | retrieved timestamps, event chains, narrative graphs, temporal logic | correct answer with wrong or insufficient cited evidence |
| Causal interpretation | candidate cause/effect localization, counterfactual tests | temporal order and semantic plausibility are not causality |
| Persistent state and revision | entity history, versioned beliefs, raw evidence pointers | state overwrite hides contradictions and destroys provenance |

## Key prior art (chronological synthesis)

**2024–2025:** Long-video sparse-memory approaches such as MovieChat and memory-augmented multimodal models made compression and query answering central. Temporal grounding and online-streaming work showed that packing many frames into context does not guarantee accurate event timing. Treat these as necessary efficiency foundations, not sufficient evidence of episodic learning.

**2026 — retrieval and memory architectures:** [WorldMM (CVPR)](https://openaccess.thecvf.com/content/CVPR2026/html/Yeo_WorldMM_Dynamic_Multimodal_Memory_Agent_for_Long_Video_Reasoning_CVPR_2026_paper.html) uses a dynamic multimodal memory agent; [PyraVid (EMNLP)](https://aclanthology.org/2026.emnlp-main.777/) uses event-inspired hierarchical multimodal memory; [EMMA (EMNLP Findings)](https://aclanthology.org/2026.findings-emnlp.1256/) segments around visual semantic and speech transitions; [NEST (EMNLP)](https://aclanthology.org/2026.emnlp-main.2512/) studies narrative event structures; and [TRACE (EMNLP)](https://aclanthology.org/2026.emnlp-main.2626/) emphasizes anchored evidence. Consequently, "hierarchical event memory", "event graphs", "semantic segmentation", and "evidence-based video retrieval" are **not standalone novelty claims**.

**2026 — finding events:** [VideoTrace-R1 (ICML)](https://proceedings.mlr.press/v306/cao26m.html) combines retrieval and reinforcement learning; [hour-long temporal grounding (EMNLP)](https://aclanthology.org/2026.emnlp-main.2112/) analyzes grounding as search; [EviScan (EMNLP)](https://aclanthology.org/2026.emnlp-main.2144/) performs task-oriented near-second localization. A proposed method must compare against strong targeted-retrieval baselines, not only uniform sampling.

**2026 — judging whether models actually reason and remember:** [SONIC-O1 (EMNLP)](https://aclanthology.org/2026.emnlp-main.767/) evaluates audio-video summarization, MCQ and temporal localization with supporting rationales. Its corpus spans ~60 hours, 231 clips, 13 domains and 4,958 human-verified annotations; reported group differences and open/closed model gaps are **authors' findings**, not reproduced here. [CaST-Bench (CVPR)](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_CaST-Bench_Benchmarking_Causal_Chain-Grounded_Spatio-Temporal_Reasoning_for_Video_Question_Answering_CVPR_2026_paper.html) evaluates localized cause/effect evidence chains. [Video-MME-Logical (Findings EMNLP)](https://aclanthology.org/2026.findings-emnlp.423/) offers 25 controllable tasks and intermediate-state diagnostics. [EgoMemReason (COLM)](https://proceedings.colm.cc/paper_files/paper/2026/hash/a4e720ce31ccd8ba747d8863e1580fa8-Abstract-Conference.html) evaluates multi-segment egocentric memory. [ANCHOR (arXiv preprint)](https://arxiv.org/abs/2610.22964) tests alignment of audiovisual reasoning traces with temporal/spatial/acoustic evidence. [MemInStream (arXiv preprint, submitted Nov 11)](https://arxiv.org/abs/2611.15640) tests **evidence solvability** and **memory necessity** to screen out recognition/language shortcuts. Its paper reports 3,799 questions in 17 tasks; do not describe it as peer-reviewed.

## Comparison: which contribution is already occupied?

| Source | Core contribution | Audio? | Persistent / long-video memory? | Remaining gap to test |
| --- | --- | --- | --- | --- |
| SONIC-O1 (EMNLP 2026) | human-verified AV benchmark, localization/rationale | Yes | Evaluation, not a persistent-memory method | synchronized audio/visual event evidence across sessions |
| WorldMM (CVPR 2026) | dynamic multimodal memory agent | Multimodal | Yes | provenance-preserving belief corrections |
| PyraVid (EMNLP 2026) | hierarchical event memory | Multimodal | Yes | conflicting beliefs, calibrated revision |
| EMMA (Findings EMNLP 2026) | audiovisual event boundary detection and retrieval | Speech transitions | Yes | whether revision gives gains above segmentation |
| VideoTrace-R1 (ICML 2026) | retrieval and RL for long temporal reasoning | Video-focused | Retrieval | rationale sufficiency/faithfulness |
| CaST-Bench (CVPR 2026) | cause/effect spatial-temporal evidence chains | Video | Benchmark | causal alternatives and cross-modal uncertainty |
| EgoMemReason (COLM 2026) | long-horizon egocentric memory reasoning | Video | Benchmark | memory necessity and visual-confound disambiguation |
| MemInStream (2026 preprint) | evidence-controlled streaming-memory evaluation | Video | Benchmark | evaluate revision and long-term correction |
| ANCHOR (2026 preprint) | grounded audiovisual rationale QA | Yes | Benchmark | persistent, revisable claim provenance |

*Source definitions of “multimodal” vary: verify model-level audio inputs and modality-specific scores from the original methods before claiming a direct audio ablation. These are conceptual comparisons, not a standardized leaderboard.*

## Critical synthesis

1. **Perception vs memory failure:** test an *oracle evidence* condition. If the backbone cannot answer with the correct clip supplied, failure in a streaming run cannot be attributed to forgetting alone.
2. **Memory necessity:** evaluate question-only, audio-only, recent-only, post-evidence-only, and time-shuffled inputs. Correct answers from these controls do not demonstrate memory retrieval.
3. **Evidence-grounding vs answer accuracy:** score timestamp IoU, relevant-evidence precision/recall, chain completeness and unsupported statements separately from final answer accuracy.
4. **Causal chains:** "because" may be warranted by observed interactions in a constrained environment, but video evidence usually supports *hypotheses*, not interventionally identified causal effects. Report plausible alternatives and abstention.
5. **Online integrity:** strictly prohibit future observations before query timestamp; log both observation and query times, downsampled frames, retrieved clips and cumulative inference cost.
6. **Subgroup claims:** SONIC-O1 demographic annotations concern perceived attributes and may be imperfect; report uncertainty and sample sizes before subgroup conclusions.
7. **Comparison hygiene:** match backbone checkpoint, prompts, available audio, frame budget, wall-clock/GPU compute, memory bytes, retrieval calls and available lookahead. Model-family cross-comparisons are descriptive, not mechanistic evidence.

## Novelty proposal: evidence-aware episodic belief revision

**Working hypothesis, not claimed invention:** Versioned observation-claim memory with explicit uncertainty and evidence replay may improve **later corrected-state accuracy** and **claim faithfulness** beyond retrieval-only, graph-only and hierarchical-memory baselines at equal cost.

Represent each raw observation independently of a revisable belief:

- **Observation:** media hash; source URI; [start,end] timestamps; modality; detector/version; raw span or feature pointer; entity candidates; uncertainty; ingestion time.
- **Claim:** subject-predicate-object/value; valid-time interval; confidence/calibration; supporting and contradicting observation IDs; inferred/observed distinction; model+prompt version; revision parent.
- **Event relation:** before/after/overlaps; directly observed interaction; claimed cause (explicitly marked as hypothesis unless supported by experimental control).
- **Revision:** never overwrite a raw observation; append new claim versions, preserving evidence provenance and contradiction history.

**Decision procedure:** ingest synchronized observation → tentative entities/events → detect changed state or contradictory evidence → retrieve both supporting and opposing original intervals → re-inspect with a bounded retrieval budget → update claim status/uncertainty → answer with timestamped evidence and abstain when insufficient. Avoid relying on an LLM's self-reported confidence without calibration.

## Falsifiable hypotheses

- **H1 (retrieval):** For matched sampling/inference costs, an evidence-indexed timeline has higher temporal-localization Recall@IoU 0.5 than recency-only and flat embedding retrieval. *Reject if 95% confidence interval of paired gain overlaps 0 or retrieval budget differs.*
- **H2 (revision):** On delayed-clarification sequences, append-only claim revision improves latest-state accuracy while reducing unsupported assertions versus append-only summaries and overwrite-only state stores. *Reject if no improvement at equal bytes and evidence budget.*
- **H3 (audio):** Synchronized acoustic observations improve event localization for genuinely audio-dependent queries vs video-only, while not worsening audiovisual contradiction cases. *Reject if gains disappear after audio-only/question-only controls.*
- **H4 (causal restraint):** Evidence sufficiency checks plus selective abstention lower unsupported-cause rate at a prespecified answer coverage. *Reject if gains come only from answering fewer questions or from a stronger backbone.*

## Evaluation and experiment design

**Benchmark roles:** SONIC-O1 (AV and timing), Video-MME-Logical (controlled state/order), CaST-Bench (grounded chains), EgoMemReason (multi-event memory), MemInStream (necessity and solvability). Do not assume all benchmarks share permissible model or data licenses.

**Baselines:** (B0) question-only / modality-free, (B1) recent N frames, (B2) uniform sampled fixed context, (B3) dense retrieval with flat store, (B4) text event summary, (B5) hierarchical memory or best reproducible prior method, (B6) proposed evidence-linked memory without revision, (B7) proposed full revision method.

**Ablations:** audio removed; evidence replay removed; contradiction tracking removed; calibration removed; raw evidence pointers removed; fixed vs adaptive sampling; equal-memory-budget scaling; distractor events; shuffled event order; independent data sources; delayed contradictory evidence; different camera/speaker conditions.

**Primary metrics:** temporal IoU / Recall@0.5; evidence precision/recall; event/entity state accuracy; unsupported-causal-claim rate per answered query; risk-coverage/AURC and calibration ECE; average and p95 latency; total visual tokens; memory bytes and GPU-seconds. Report paired bootstrap 95% intervals by **video**, not only per question, and multiple seeds for stochastic systems.

**Minimal prospective dataset:** 30–50 consenting or synthetic short clips with controlled delayed state corrections (e.g., occluded object placement, sound-source ambiguity, misleading verbal descriptions). Annotate raw observations, changing states, query time, necessary evidence windows, plausible causal alternatives and permitted abstention. Hold out video locations, objects and speakers; explicitly avoid using personally identifying surveillance footage without consent.

## Low-resource plan (16 GB host RAM; 6 GB VRAM)

1. Start with the **official released annotations**, not full video ingestion. Implement deterministic timestamp retrieval and evidence bookkeeping first.
2. Precompute visual embeddings and ASR/acoustic observations offline; use a frozen encoder and an optional small/quantized VLM for targeted clips. Budget GPU memory including video tokens, KV cache and decoding overhead.
3. Run corpus subsets at 16–64 indexed events per clip before increasing duration; store cached features, source hashes, config and timestamp mapping.
4. Freeze the same answer backbone and compare B0–B7. First produce *no-memory* and *flat-retrieval* controls before testing revision.
5. Use larger hosted inference only if necessary, with identical inputs and per-query monetary/latency reporting; do **not** interpret differing backbones as architectural gains.

## Go/no-go criteria and adverse findings

- **Go:** baseline reproducible, held-out performance measurable, oracle-evidence upper bound above chance, controlled revision gives a useful paired improvement after matching budgets, and evidence claims are auditable.
- **Stop/revise:** score changes vanish against question-only or recent-frame baselines; observations are too noisy for correct answers even with oracle evidence; improvement disappears at equal token cost; no original distinction from PyraVid/EMMA/TRACE; data cannot be redistributed ethically/licensably.
- Publish negative results and retain configurations, disagreements and failed tests.

## Reading order and directly linked primary sources

1. [SONIC-O1 — EMNLP 2026](https://aclanthology.org/2026.emnlp-main.767/) and [official benchmark code](https://github.com/VectorInstitute/sonic-o1).
2. [MemInStream — Nov 2026 preprint](https://arxiv.org/abs/2611.15640) for evidence necessity/solvability.
3. [PyraVid — EMNLP 2026](https://aclanthology.org/2026.emnlp-main.777/), [WorldMM — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Yeo_WorldMM_Dynamic_Multimodal_Memory_Agent_for_Long_Video_Reasoning_CVPR_2026_paper.html), [EMMA — Findings EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.1256/).
4. [VideoTrace-R1 — ICML 2026](https://proceedings.mlr.press/v306/cao26m.html), [hour-long temporal grounding — EMNLP 2026](https://aclanthology.org/2026.emnlp-main.2112/), [EviScan — EMNLP 2026](https://aclanthology.org/2026.emnlp-main.2144/).
5. [CaST-Bench — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_CaST-Bench_Benchmarking_Causal_Chain-Grounded_Spatio-Temporal_Reasoning_for_Video_Question_Answering_CVPR_2026_paper.html), [Video-MME-Logical — EMNLP Findings 2026](https://aclanthology.org/2026.findings-emnlp.423/), [EgoMemReason — COLM 2026](https://proceedings.colm.cc/paper_files/paper/2026/hash/a4e720ce31ccd8ba747d8863e1580fa8-Abstract-Conference.html).
6. [ANCHOR — Oct 2026 preprint](https://arxiv.org/abs/2610.22964), [TRACE — EMNLP 2026](https://aclanthology.org/2026.emnlp-main.2626/), [NEST — EMNLP 2026](https://aclanthology.org/2026.emnlp-main.2512/), [TempCore — EMNLP 2026](https://aclanthology.org/2026.emnlp-main.125/).

For machine-readable reference metadata, status and open questions, see [paper catalog](../papers/catalog.json). No benchmark results have been independently reproduced in this repository.
