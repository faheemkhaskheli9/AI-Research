# 8. Multimodal intelligence and temporal grounding

**Research brief · 2026-11-18 · source-linked scoping review, not an independent reproduction.**

## Research motivation and definitions

Models often summarize a video convincingly but mislocate decisive events, confuse speakers, overlook audio-only evidence or turn temporal succession into an unsupported causal claim. Persistent memory can magnify early perceptual errors.

## State of research through November 2026

SONIC-O1 (EMNLP 2026) studies audio-video summarization, multiple-choice evidence and temporal localization; its authors report a notable closed/open gap on localization. CVPR 2026 work advances dynamic long-video memory and causal-chain-focused evaluation. Hierarchical event memory and evidence graphs are established prior art rather than novel ideas by themselves.

### Primary-source literature

| Paper / research report | Evidence level | Main contribution (as described by authors) | Limitation to investigate |
|---|---|---|---|
| [SONIC-O1: A Real-World Benchmark for Evaluating Multimodal Large Language Models on Audio-Video Understanding](https://aclanthology.org/2026.emnlp-main.767/) | EMNLP 2026; benchmark | Evaluates synchronized audio/video understanding, temporal localization, and human-verified rationales. | Short extracted answers may mask wrong time intervals or ungrounded rationales. |
| [WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning](https://openaccess.thecvf.com/content/CVPR2026/html/Yeo_WorldMM_Dynamic_Multimodal_Memory_Agent_for_Long_Video_Reasoning_CVPR_2026_paper.html) | CVPR 2026; method | Develops dynamic multimodal memories for long-video question answering. | Memory cost and unsupported event summaries complicate cross-video generalization. |
| [CaST-Bench: Benchmarking Causal Chain-Grounded Spatio-Temporal Reasoning for Video Question Answering](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_CaST-Bench_Benchmarking_Causal_Chain-Grounded_Spatio-Temporal_Reasoning_for_Video_Question_Answering_CVPR_2026_paper.html) | CVPR 2026; benchmark | Examines spatiotemporal grounding of candidate causal event chains. | Temporal ordering alone does not identify causation. |

Distinguish source verification from *replication*: conference status verifies publication, not robustness. Preprints and organization demonstrations require explicit status labels and independent testing.

## Open research problems

1. Preserve audiovisual provenance when long-video memory is summarized or revised.
2. Audit contradiction resolution when newer evidence changes an event label.
3. Measure whether successful answers actually depend on cited evidence timestamps.

## Candidate hypothesis

**H1:** A versioned event-memory system that stores source interval pointers and explicit contradictions reduces unsupported temporal answers after new observations compared with equal-budget summary retrieval.

**H0:** The method does not outperform the strongest budget-matched baseline on predeclared held-out tasks. Publish null and negative results as well as successes.

## Proposed experiment

Create a consented audiovisual corpus with expert-labeled events, speaker/sound-source links, time intervals and delayed contradictory evidence. Compare frame sampling, clip retrieval, summarization memory, event graph and provenance-versioned event memory at the same extraction/token budget. Insert synthetic misleading subtitles while preserving original videos. Use annotator disagreement and adjudication.

- **Baselines:** Uniform clip sampling; dense clip retrieval; hierarchical summary; dynamic video memory; proposed provenance-versioned memory.
- **Metrics:** Temporal intersection-over-union, timestamp precision/recall, evidence sufficiency, cross-modal attribution errors, update latency, memory bytes and cost.
- **Feasibility:** Begin with pre-extracted video/audio representations and a small consented corpus; long-video models themselves may exceed local VRAM.

Report exact data splits, per-task outcomes, preprocessing, model/build versions, compute and inference budgets, and paired uncertainty intervals. Reproduction must be distinguished from a new empirical result.

## Adversarial review

Data leakage can allow answers from subtitles or language priors without audiovisual understanding. 'Causal chain' labels require stronger evidence than simple temporal order. Record ambiguous annotations rather than forcing single labels.

## Connected research and code

[Full targeted literature review](../MULTIMODAL_GROUNDED_INTELLIGENCE.md), [multimodal memory experiment protocol](../../experiments/multimodal_memory/README.md), [multimodal temporal literature notes](../../knowledge/multimodal_temporal_literature_review.md).

**Status:** no experiment in this proposed review has yet been run; results are not being claimed.
