# Research Track: Multimodal Reasoning and Grounded Video Understanding

Status: second specialization, alongside the [voice-agent track](VOICE_AGENTS_STRATEGY.md)
Last updated: 2026-11-18
Literature review: [knowledge/multimodal_temporal_literature_review.md](../knowledge/multimodal_temporal_literature_review.md)

> No new scientific results are claimed. Everything below is a plan and hypotheses.

## 1. The problem

Multimodal LLMs describe single frames well, but they still struggle to:
- say **when** something happened in a long video (temporal localization)
- link **what was heard** to **what was seen** at the same moment
- follow **cause and effect** across many events
- keep a **running memory** of what has happened so far

## 2. Key evidence: SONIC-O1 (`radwan26sonico1`)

| Item | Detail |
|---|---|
| First released | arXiv 2601.21666, 29 Jan 2026 |
| Venue | NeurIPS 2026 workshop poster ("Grounded and Faithful Vision-Language Models for Real-World Deployment"). Not an EMNLP paper. |
| Size | ~60 hours, 231 clips, 13 conversational domains, 4,958 human-verified annotations |
| Tasks | Summarization, evidence-grounded MCQ, temporal localization with rationale |

Reported findings (authors' claims):
- MCQ: smallest gap between closed and open models.
- Temporal localization: best closed model beats best open model by 22.6%.
- Temporal localization differs by up to 21.4% across demographic groups.

Open models answer "what" questions reasonably well but fall behind on "when" questions. That is the gap this track targets.

Links: [paper](https://arxiv.org/abs/2601.21666) · [code](https://github.com/vectorinstitute/sonic-o1) · [dataset](https://huggingface.co/datasets/vector-institute/sonic-o1) · [leaderboard](https://huggingface.co/spaces/vector-institute/sonic-o1-leaderboard)

## 3. Where this track fits (from the literature review)

- "Event graph + LLM" alone is already explored (`dixit26seg`, `graphthinker26`, `rege26egagent`).
- Strong grounding models are often vision-only (`zhu26timelens2`).
- Audio-visual grounding is new and small (`chen25chronusomni`, `ghosh26avflamingo`).
- Models' attention locates the right moment better than their written timestamps (`du26tgheads`).
- No method found that targets the demographic gaps reported in `radwan26sonico1`.
- The benchmarks reviewed are mostly English.

**Chosen angle:** events from **action recognition + audio**, linked in a time-ordered graph, evaluated on audio-video benchmarks, then extended to **Urdu / code-switched speech**. This uses past computer vision and action recognition experience and links to the voice-agent track.

## 4. Research questions

1. **RQ1 – Temporal grounding:** Can an open model close the gap to closed models on event timing by adding explicit audio and action events?
2. **RQ2 – Causal event chains:** Does a graph of action and audio events (before / causes / overlaps) improve "why" and "what led to" answers?
3. **RQ3 – Persistent memory:** Can a streaming event log keep early events usable in hour-long videos?
4. **RQ4 – Fairness:** Does better grounding shrink or widen the gaps between demographic groups?
5. **RQ5 – Language:** How much does grounding drop when speech is Urdu or code-switched?

## 5. Testable hypotheses

- **H1:** Timestamped audio events (ASR + speaker turns + sound events) next to frames improve temporal localization mIoU by at least 5 points over frames-only input on SONIC-O1.
- **H2 (narrowed):** Events from action recognition + audio beat caption-only events on long-video causal QA when the answer depends on events far apart in time.
- **H3:** Action-recognition anchors (e.g. VideoMAE) improve localization more than sampling more frames at the same token budget.
- **H4:** Reading timestamps from grounding attention heads improves localization on SONIC-O1 without training.

## 6. Proposed system

```
Video + Audio
   │
   ├─ Action recognition (short clips)  → action events with timestamps
   ├─ ASR + speaker turns + sound tags  → audio events with timestamps
   └─ Sparse frame captions             → scene events
             │
             ▼
     Event log (time-ordered, streaming)
             │
             ▼
     Event graph (before / causes / overlaps)
             │
             ▼
     LLM reasoner → answer + timestamp + evidence events
```

## 7. Baselines

- Vision grounding: `zhu26timelens2`, `wang25timer1`
- Audio-visual: `chen25chronusomni`
- Structured events: `dixit26seg`
- Memory: `chen26flexmem` (runs on a single consumer GPU)
- General open omni model (e.g. a recent Qwen omni model)

If training with RL, start from IoU + temporal Wasserstein reward (`zhu26timelens2`), not plain IoU.

## 8. 12-month plan

| Months | Goal | Output |
|---|---|---|
| 1 | Read the core papers in the reading order below | Reading notes in `knowledge/reading_notes/` |
| 2 | Run 2 open models on SONIC-O1 localization, with and without audio | First baseline table |
| 3 | Test H4 (attention-based timestamps), training-free | Short workshop paper candidate |
| 4–5 | Build the event log pipeline; test H1 and H3 | Ablation table |
| 6–7 | Add event graph + memory; test H2 on long videos (LVOmniBench, VCRBench) | Long-video results |
| 8–9 | Fairness analysis (RQ4) | Error analysis by group |
| 10–11 | Small Urdu / code-switched audio-video grounding set (RQ5) | Pilot dataset |
| 12 | Write paper | Paper + open code |

## 9. Reading order

1. `zhang25timelens` → `zhu26timelens2`
2. `wang25timer1` → `li25tempsampr1` → `wu25tempr1`
3. `radwan26sonico1` → `tao26lvomnibench` → `li26omnivideobench`
4. `chen25chronusomni` → `ghosh26avflamingo`
5. `du26tgheads`
6. `dixit26seg` → `graphthinker26` → `rege26egagent`
7. `chen26flexmem` → `mmmem26` → `li26vam`
8. `sarkar25vcrbench` → `li25causalstep`

## 10. Risks

- **Compute:** long video is expensive. Start with short clips, frozen backbones and training-free methods.
- **Benchmark size:** SONIC-O1 has only 231 clips. Always report a second benchmark.
- **Closed-model comparisons:** API models change. Record model version and date for every run.
- **Novelty:** many 2026 preprints in this area. Search again before claiming anything is new.

## 11. First concrete step

Run one open omni model on the SONIC-O1 temporal localization split, with and without audio. This tests whether audio helps timing and gives the first baseline.
