# Multimodal grounded-memory experiment protocol

**Status:** Preregistration draft; no runs completed. See [literature review](../../research/MULTIMODAL_GROUNDED_INTELLIGENCE.md) and [data model](../../knowledge/multimodal_event_memory.md).

## Question

Under the same model, observations, time budget, and stored-memory bytes, does revision-capable evidence-linked memory improve temporal localization and corrected state tracking without increasing unsupported causal assertions?

## Design

1. Pick a legally accessible SONIC-O1 subset with temporal annotations. Record each selected file's hash, licensing terms, clip duration, and annotation IDs. Start with public metadata if media access is unavailable.
2. Fix backbone, tokenizer, decoding parameters, prompt, frame size and observed frames. Precompute visual features and audio embeddings/transcripts once to avoid differences in preprocessing cost.
3. Split by **original video**, with disjoint recordings (not individual questions from the same recording). Use three seeds if sampling and inference are nondeterministic.
4. Compare B0 question-only, B1 last-N-frame, B2 uniform frame context, B3 flat retrieval, B4 text event summary, B5 hierarchical memory (where reproducible), B6 evidence-linked memory without revision, B7 with revision.
5. Replay observation streams in strict chronological order. At query time T, block access to frames/audio from >T, including human-created final-video summaries.
6. Evaluate oracle-evidence answerability. Retain failure logs even when the oracle cannot solve the question; report separate conditional and unconditional scores.
7. For delayed-correction scenes, annotate old-state, update-event and current-state targets; rate unsupported causal claims independently from final-answer correctness.
8. Compute paired video-cluster bootstrap intervals, per-video errors, memory writes/bytes, retrieval counts, GPU-seconds and p95 latency.

## Pre-registered outcomes

| Outcome | Measurement | Failure mode |
| --- | --- | --- |
| Event localization | Recall@IoU 0.5 and median boundary error | coarse frames hide event |
| Memory necessity | oracle-evidence vs recent-only/text-only gap | answer doesn't require history |
| Correct state after revision | time-conditional state accuracy | later evidence incorrectly overwrites facts |
| Evidence attribution | precision/recall on annotated intervals | plausible wrong rationale |
| Causal discipline | unsupported cause statements / answered queries | correlation portrayed as causality |
| Abstention | selective risk at matched coverage; calibration ECE | apparent gains from refusing everything |
| Efficiency | total tokens, retrieval calls, memory bytes, GPU-sec, p95 latency | extra compute explains score gain |

## Required ablations

- same backbone / frame and audio availability / identical memory budget;
- disable claim revision; disable contradiction retrieval; disable raw-evidence replay;
- audio-only, video-only, text-only and shuffled evidence;
- controlled negative videos where visible proximity is not the cause;
- evaluation with time-shifted audio and altered object identities;
- performance versus video length and frequency of memory write/read.

## Resource guidance

For 6 GB VRAM and 16 GB RAM, start with offline Python event indexing, metadata-only benchmark scripts and precomputed features. Do **not** promise full long-video VLM inference locally. Measure peak VRAM; use sequential clip processing, compact batches, disk-backed features, and an optional external model for short re-inspection windows only.

## Reproducibility checklist

- [ ] record exact dataset version, URL, terms, clip IDs and hashes
- [ ] define full annotations and evidence solvability test
- [ ] freeze backbone checkpoints and prompts
- [ ] prevent train/test video overlap and query-time lookahead
- [ ] record all sampling seeds, frame clocks and modality alignments
- [ ] run matched-cost baselines and modality-free shortcut controls
- [ ] calculate paired confidence intervals grouped by recording
- [ ] log successes, failures, unsupported causal claims and abstentions
- [ ] archive code commit hash and dependency lockfile
- [ ] report ethical constraints and limitations

**Decision gate:** A stronger score without controlled evidence grounding and equal budget is insufficient to claim memory improvement.
