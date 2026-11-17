# Literature Review: Temporal Grounding, Audio-Visual Reasoning and Memory in Video LLMs

Track: [Multimodal reasoning and grounded video understanding](../research/MULTIMODAL_TEMPORAL_STRATEGY.md)
Date: 2026-11-18
Scope: about 25 papers, mostly from 2025–2026. Summaries come from abstracts and paper pages. Check the full papers before citing any numbers.

---

## 1. Summary in 5 points

1. **"When" is still the weak spot.** Video LLMs answer "what happened" well but fail at "when did it happen". This holds across many benchmarks (SONIC-O1, FAVE, LVOmniBench, TimeLens).
2. **RL with IoU rewards is now the standard recipe** for temporal grounding (Time-R1, TempSamp-R1, TempR1, TimeLens2). The newest work improves the reward itself instead of the model architecture.
3. **Models "know" when before they say it.** Two 2026 papers show internal attention finds the right moment more accurately than the timestamps the model writes out. This is a cheap research opening.
4. **Audio is underused.** Most grounding models are vision-only, including TimeLens2, one of the strongest. Audio-visual grounding (ChronusOmni, AV-Flamingo, OmniGround) is new and still small.
5. **Event graphs and memory for long video are active but early.** Many papers build graphs or memory, but few test on audio-video benchmarks, and few use real action recognition as the event detector.

---

## 2. Benchmarks

| Benchmark | Year / venue | What it tests | Key finding |
|---|---|---|---|
| **SONIC-O1** ([arXiv 2601.21666](https://arxiv.org/abs/2601.21666)) | 2026, NeurIPS workshop | Summarization, MCQ, temporal localization on ~60 h of real conversations | Closed models beat open models by 22.6% on temporal localization; up to 21.4% gap across demographic groups |
| **FAVE** ([CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_FAVE_A_Structured_Benchmark_for_Fine-Grained_Audio-Visual_Temporal_Evaluation_in_CVPR_2026_paper.html)) | CVPR 2026 | Cross-modal alignment, event order, timestamp localization | 12 models are weak at joint audio-visual timing |
| **LVOmniBench** ([arXiv 2603.19217](https://arxiv.org/abs/2603.19217)) | Mar 2026 | Long audio-video: memory, temporal localization, perception | Omni models struggle as audio-visual input gets longer |
| **OmniVideoBench** ([ICLR 2026](https://alphaxiv.org/abs/2510.10689)) | ICLR 2026 | 13 question types, including temporal, causal, counting | Tests whether models really combine audio and video |
| **VCRBench** ([arXiv 2505.08455](https://arxiv.org/abs/2505.08455)) | 2025 | Put shuffled procedural clips back in causal order | Models rely mostly on language knowledge, not on what they see |
| **CausalStep** ([arXiv 2507.16878](https://arxiv.org/abs/2507.16878)) | 2025 | Step-by-step causal QA, 100 videos | Blocks shortcuts from global context |
| **Causal2Needles** | 2025 | Cause and effect events far apart in a long video | Tests multi-hop retrieval |
| Classic sets | — | Charades-STA, ActivityNet Captions, QVHighlights, Ego4D-NLQ, NExT-QA | Still the standard grounding and causal QA tests |

**Takeaway:** use SONIC-O1 and FAVE (audio-visual timing), LVOmniBench (long video) and VCRBench (causal reasoning). Together they cover all four of your research questions.

---

## 3. Temporal grounding methods

### 3.1 Data and baselines
- **TimeLens** ([arXiv 2512.14698](https://arxiv.org/abs/2512.14698)): says MLLMs understand "what" but fail at "when". Builds a strong baseline mainly by cleaning the data. **Lesson: label quality matters more than clever architecture.**
- **TimeLens2** ([arXiv 2607.17423](https://arxiv.org/abs/2607.17423), Jul 2026): built on Qwen3-VL. Predicts one or more evidence intervals. Trains with SFT, then GRPO with IoU plus a "temporal Wasserstein" reward that gives partial credit for near misses. The 4B model beats much larger models by 7.5 mIoU. **Limitation: vision only, no audio or subtitles.**
- **UniTime** (NeurIPS): puts timestamp tokens between video tokens so the model can read time directly.

### 3.2 Architecture tweaks
- **E.M.Ground** ([arXiv 2602.05215](https://arxiv.org/abs/2602.05215)): treats events as whole, continuous units instead of separate frames.
- **GroundVTS** ([arXiv 2604.02093](https://arxiv.org/abs/2604.02093)): keeps only the visual tokens that match the query.
- **SlotVTG** ([arXiv 2603.25733](https://arxiv.org/abs/2603.25733)): object-centric adapter that helps the model generalize to new domains.

### 3.3 Reinforcement learning
- **Time-R1** ([arXiv 2503.13377](https://arxiv.org/abs/2503.13377)): RL with a verifiable IoU reward. Reaches state of the art with only 2.5K training samples.
- **TempSamp-R1** (NeurIPS 2025): finds that on-policy GRPO explores poorly in a large time space, so it mixes in ground-truth samples.
- **TempR1** ([arXiv 2512.03963](https://arxiv.org/abs/2512.03963)): multi-task RL across 5 temporal tasks, ~60K videos, on Qwen2.5-VL-7B.

### 3.4 Interpretability: the model knows more than it says
- **TG-Heads** ([arXiv 2605.21954](https://www.alphaxiv.org/abs/2605.21954), May 2026): a few attention heads focus on the correct time interval even when the output timestamp is wrong.
- **OmniGround / TACG** (Oct 2026): finds the same gap in omni (audio + video) models. Fixes it by training attention and output timestamps to agree. Releases a 580K-sample training set.

**Takeaway:** decoding timestamps directly from attention could be a cheap, training-free way to improve grounding. This connects to interpretability research.

---

## 4. Audio-visual temporal models

- **ChronusOmni** ([arXiv 2512.09841](https://arxiv.org/abs/2512.09841)): puts text timestamps between video and audio tokens, then uses RL to enforce correct order. Defines 6 sub-tasks, for example "what is said when X appears". Releases the ChronusAV dataset.
- **AV-Flamingo (Nemotron)** ([arXiv 2607.16107](https://arxiv.org/abs/2607.16107), Jul 2026): three-stage curriculum from short clips to long multi-event video, plus chain-of-thought where each step is tied to a timestamp.
- **OmniGround** (above): omni-model grounding with attention-consistency training.

**Gap:** these are new and few. None of them have been tested on Urdu or other low-resource speech that I could find.

---

## 5. Long-video memory

| Paper | Idea | Note |
|---|---|---|
| **FlexMem** ([CVPR 2026](https://arxiv.org/abs/2603.29252)) | Training-free; stores visual KV cache as memory and recalls relevant parts | Runs on a single 3090 GPU, good for low budgets |
| **MM-Mem** ([arXiv 2603.01455](https://arxiv.org/abs/2603.01455)) | Pyramid memory from exact details to summaries | Works offline and streaming |
| **Visual Agentic Memory** ([arXiv 2605.16481](https://arxiv.org/abs/2605.16481)) | Online index, hierarchy, and agent-based retrieval | Scales to 51-day streams |
| **LatentStream** (2026) | Short, mid and long-term latent memory with a fixed budget | Streaming state of the art |
| **POINTS-Long** (CVPR 2026) | Switches between cheap standby mode and detailed focus mode | 10–40× fewer tokens |

---

## 6. Structured event representations

- **Semantic Event Graphs** ([arXiv 2601.06097](https://arxiv.org/abs/2601.06097)): YOLO tracking turns object proximity into start/end events, then builds a temporal graph. Uses 91% fewer tokens with similar accuracy. **Weak points:** tested on only 5 videos, has no action recognition, and ignores audio.
- **LVGraph** (NeurIPS 2026): coarse-to-fine graph; the model walks the graph based on the query instead of scanning every frame.
- **EGAgent** ([arXiv 2601.18157](https://arxiv.org/abs/2601.18157)): agent searches entity scene graphs plus audio and visual data across days of egocentric video.
- **GraphThinker** ([arXiv 2602.17555](https://arxiv.org/abs/2602.17555)): MLLM builds an event scene graph as an intermediate thinking step, trained with RL to reduce hallucination.
- **VCRBench's RRD**: splits the task into "recognize the steps" then "reason about their order", which helps.

**Takeaway:** the general idea of "event graph + LLM" is already taken. Your contribution needs a specific angle (see section 7).

---

## 7. Gaps you can work on

| # | Gap | Why it fits you |
|---|---|---|
| G1 | **Audio + action events for grounding.** Event-graph papers use objects or captions, not trained action-recognition models, and mostly ignore audio. | Directly uses your action-recognition experience |
| G2 | **Multi-interval grounding with audio.** TimeLens2 is vision-only. Adding audio to its recipe is a clear next step. | Builds on your speech work |
| G3 | **Attention-based timestamp decoding for omni models.** TG-Heads and OmniGround show the signal exists; a training-free decoder is cheap to test. | Low compute, fast results |
| G4 | **Demographic fairness in temporal grounding.** SONIC-O1 reports gaps of up to 21.4%, but I found no method that targets them. | Open problem with clear evaluation |
| G5 | **Urdu / code-switched audio-video grounding.** All benchmarks above are mostly English. | Links your two research tracks into one unique niche |

**Recommended focus:** G1 + G5, evaluated on SONIC-O1 and FAVE, with G3 as a quick first paper.

---

## 8. Changes to the research plan

- **H2 (event log beats captions)** is partly answered already (SEG, LVGraph, GraphThinker). Narrow it: *action-recognition events + audio events* vs *caption-only events*, on audio-video benchmarks.
- **New H4:** reading timestamps from attention heads improves temporal localization on SONIC-O1 without any training.
- **Baselines to compare against:** TimeLens2 (vision), ChronusOmni (audio-visual), Qwen omni models (general).
- **Reward design:** if you train with RL, start from IoU + Wasserstein (TimeLens2), not plain IoU.

---

## 9. Reading order

1. TimeLens → TimeLens2 (what makes grounding work)
2. Time-R1 → TempSamp-R1 (RL recipe)
3. SONIC-O1 → FAVE → LVOmniBench (where models fail)
4. ChronusOmni → AV-Flamingo (audio-visual timing)
5. TG-Heads → OmniGround (attention knows "when")
6. Semantic Event Graphs → GraphThinker → LVGraph (structured events)
7. FlexMem → Visual Agentic Memory (memory)
8. VCRBench (causal reasoning)

## 10. Catalog ids

All papers with arXiv links are in [papers/catalog.json](../papers/catalog.json):
`radwan26sonico1`, `tao26lvomnibench`, `li26omnivideobench`, `sarkar25vcrbench`, `li25causalstep`,
`zhang25timelens`, `zhu26timelens2`, `groundvts26`, `han26slotvtg`, `nie26emground`,
`wang25timer1`, `li25tempsampr1`, `wu25tempr1`, `du26tgheads`,
`chen25chronusomni`, `ghosh26avflamingo`,
`chen26flexmem`, `mmmem26`, `li26vam`,
`dixit26seg`, `rege26egagent`, `graphthinker26`.

Not in the catalog (no allowed primary-source link recorded yet): FAVE (CVPR 2026), UniTime, OmniGround, LatentStream, POINTS-Long, LVGraph, Causal2Needles.

## 11. Caveats

- Summaries are from abstracts and paper pages, not full reads.
- Some 2026 papers are preprints and have not been peer reviewed.
- "No paper found" in section 7 means a quick search found nothing, not a full survey. Search again before claiming novelty.
- A survey worth reading next: *A Survey on Video Temporal Grounding with Multimodal LLMs* (Wu et al., Feb 2026).
