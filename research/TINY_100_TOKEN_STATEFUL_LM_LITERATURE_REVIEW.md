# Bounded-Memory Language Modeling with a 100-Token Window

**Research date:** 2026-11-18  
**Status:** Literature synthesis and proposed experiments; not an implemented or verified model  
**Working title:** Strict-100: Unbounded Streaming Generation Under a Hard 100-Token Context Window (and explicitly labeled bounded-memory extensions)  
**Research question:** Can a 10M–100M-parameter language model with a **hard 100-token context window at every decoding step** generate arbitrarily long output? How much long-range retention is possible without extra memory, and what measurable improvements arise when optional bounded recurrent state is explicitly introduced?

## Authoritative scope clarification — 100-token **context window** (2026-11-18)

The researcher means **at most 100 token positions in the model's active context at *every* generation step**, not merely a 100-token starting prompt. Once the model generates the 101st continuation token, it must evict the oldest directly attended token. This restriction remains active at output positions 1K, 10K, 100K, and beyond.

The core strict-window baseline implements

\[
p_\theta(y_t \mid y_{\max(1,t-100):t-1}, x_{\text{recent}})
\]

where the conditioning sequence is the **most recent 100 tokens of the concatenated prompt and generated output**. More precisely, if \(z = [x_1,\ldots,x_m,y_1,\ldots]\), the next-token distribution depends only on the suffix \(z_{\max(1,n-99):n}\), where \(n\) is the number of already-seen tokens. Its causal self-attention KV cache contains no more than 100 positions, including any retained special/sink tokens.

**Two research tracks must remain distinct:**

1. **Strict-100 / no out-of-window state.** Context consists solely of the most recent 100 token IDs. There are no recurrent state vectors, long-lived memory tokens, external databases, summary buffers, or persistent KV sinks outside that budget. This can stream indefinitely in principle, but once an old fact leaves the window it cannot be recovered *unless* the model keeps re-expressing it within the latest 100 tokens. No arbitrary long-range recall can be guaranteed.
2. **100-token attention + bounded state.** Direct attention sees at most 100 ordinary token positions, but recurrent vectors or a bounded memory bank encode information from older positions. This also permits unbounded-duration streaming with fixed inference-state bytes, but it is **not** a strict 100-token *total-information* model. State bytes and extra vectors are disclosed and compared against Track 1.

A sliding-window Transformer alone answers the **possibility** question: output length is not bounded by the attention window. The **research** question is whether a very small model can maintain meaningful long-form structure, goal consistency and delayed factual recall under that constraint. Any apparent gain from external memory should not be presented as coming from 100 tokens alone.

**Hard implementation invariants:** attention to no more than 100 actual token positions at each step; discard evicted KV entries or recompute from a 100-token ring buffer; avoid positional-embedding length exhaustion via a correctly specified rolling/relative position scheme; verify causal masking and that no full-history tensor or latent state is retained in the strict baseline; write generated tokens directly to an output sink rather than accumulating them. "Infinite" refers to arbitrarily long time/sequence under external stopping, not infinite computation or guaranteed high-quality text.

## Executive summary

An autoregressive LM can receive an initial prompt of at most 100 tokens and generate a potentially unbounded sequence of tokens. Output duration is not mathematically tied to prompt length. The scientific challenge is **preservation of reliable information over arbitrarily many decoding steps**.

The phrase "100 input tokens" has three possible interpretations that must never be conflated:

| Constraint | What is limited | Does it prevent long outputs? |
| --- | --- | --- |
| Initial user prompt <=100 tokens | Number of initially supplied prompt tokens | No. Even a standard Transformer can generate longer, subject to position, cache, runtime, and stop limits. |
| Active attention window =100 tokens | Number of recent token positions directly visible to attention per step | No. Old information must survive in recurrent or external memory. |
| Maximum 100 token-equivalents in KV cache | Direct stored token K/V entries | No. Other state may be used, but its size must be reported independently. |

**Proposed contribution:** First establish the quality limits of a **strict 100-token rolling window with zero hidden/external memory**, then characterize the separately labeled trade-off between **long-range retention** and **persistent memory bytes** under a 100-token direct-attention window. Do not claim “infinite context”: infinite output horizon and infinite information capacity are different.

## 1. Theoretical formulation and limitations

Let a prompt be \(x_{1:m}\), \(m\le100\), and generated tokens be \(y_1,y_2,\dots\). A full-history autoregressive LM models

\[
p(y_t\mid x_{1:m},y_{<t}).
\]

A bounded-state LM can instead update

\[
s_t=F_\theta(s_{t-1},e(y_t)), \qquad
p(y_{t+1})=G_\theta(s_t,e(y_t)).
\]

State \(s_t\) can remain fixed-size while the number of output tokens grows. However, a finite-precision state with \(d\) values and \(b\) effective bits per value can encode at most roughly \(db\) raw bits. It cannot losslessly remember an arbitrary unbounded transcript. Theoretical Turing-completeness arguments for RNNs can depend on unbounded precision or idealized assumptions [Weiss et al.](https://arxiv.org/abs/1805.04908).

**Distinctions:**

1. **Unbounded streaming:** the decoding algorithm has no sequence-length-dependent memory allocation requirement; feasible.
2. **No EOS:** generation continues until externally stopped; feasible if termination handling is configured.
3. **Global consistency forever:** cannot be guaranteed for arbitrary histories with fixed finite memory.
4. **Growing external memory:** may preserve a larger history, but total system memory is no longer constant.

Bounded-memory models also suffer **exposure bias**: during decoding they condition on their own prior samples, not always the teacher-forced contexts seen during training. Repetition, fabricated facts, and semantic drift are risks to measure, not facts to hide.

## 2. Literature map

### 2.1 Sliding and recurrent attention

- **Transformer-XL** — segment recurrence extends dependency beyond one segment, establishing a classic recurrent-attention baseline. Paper: [Dai et al., 2019](https://arxiv.org/abs/1901.02860).
- **Compressive Transformer** — compresses past activations rather than discarding them; includes long-document evaluation. Paper: [Rae et al., 2019](https://arxiv.org/abs/1911.05507).
- **Recurrent Memory Transformer (RMT)** — learned memory token vectors are transferred between segments, making a practical first implementation. [Paper](https://arxiv.org/abs/2207.06881); [implementation](https://github.com/booydar/recurrent-memory-transformer).
- **StreamingLLM** — retains local K/V plus initial attention sinks for stable streaming, but does **not** prove indefinite reliable semantic recall. [Paper](https://arxiv.org/abs/2309.17453).
- **Infini-attention** — bounded local attention combined with compressed long-term representation. [Paper](https://arxiv.org/abs/2404.07143).

### 2.2 Recurrent and state-space backbones

- **RWKV** — recurrent weighted mixing combines parallel training with fixed-state autoregressive inference. [Paper](https://arxiv.org/abs/2305.13048); [code](https://github.com/RWKV/RWKV-LM).
- **RetNet** — parallel, recurrent, and chunkwise-recurrent formulations. [Paper](https://arxiv.org/abs/2307.08621); [code](https://github.com/microsoft/torchscale).
- **Mamba** — selective state-space recurrence with linear sequence scaling. [Paper](https://arxiv.org/abs/2312.00752); [code](https://github.com/state-spaces/mamba).
- **Mamba-2** — structured state-space duality and improved core layer efficiency. [Paper](https://arxiv.org/abs/2405.21060).
- **RWKV-7** — more expressive state evolution. [Paper](https://arxiv.org/abs/2503.14456).

**Interpretation:** these architectures allow streaming at bounded neural-state memory, but they implicitly compress earlier facts into finite continuous state. Real long-term recall needs direct evaluation.

### 2.3 Episodic and learned memory

- **Memorizing Transformers** — non-differentiable approximate-nearest-neighbor key/value memory with retrieval. [Paper](https://arxiv.org/abs/2203.08913).
- **Titans** — learnable long-term memory applied at test time. [Paper](https://arxiv.org/abs/2501.00663).

### 2.4 Long-output planning

- **PLANET** — dynamic content planning for long-form generation. [ACL 2022](https://aclanthology.org/2022.acl-long.163/).
- **DOC** — hierarchical outline control to support longer story coherence. [ACL 2023](https://aclanthology.org/2023.acl-long.190/).
- **DOME** — dynamic hierarchical outlining with memory enhancement. [NAACL 2025](https://aclanthology.org/2025.naacl-long.63/).
- **IS-CoT** — interleaved structural planning and reflection rather than relying exclusively on a static outline. [ACL 2026](https://aclanthology.org/2026.acl-long.911/).

### 2.5 Benchmarks and theory

- **RULER** — configurable recall, aggregation and reasoning tests over long contexts. [Paper](https://arxiv.org/abs/2404.06654).
- **BABILong** — distributed facts and reasoning in long distractor contexts. [Paper](https://arxiv.org/abs/2406.10149).
- **∞Bench** — evaluation involving sequences beyond 100K tokens. [Paper](https://arxiv.org/abs/2402.13718).
- **Finite-precision RNN limits** — [Weiss et al.](https://arxiv.org/abs/1805.04908).
- **Chinchilla scaling** — [Hoffmann et al.](https://arxiv.org/abs/2203.15556). Treat its tokens-per-parameter heuristic as an approximate starting point, not a theorem for hybrid recurrent objectives.

**Research gap (hypothesis, not verified novelty):** Carefully matched, small-scale comparisons under exactly 100 directly visible tokens, varying retained state capacity and memory organization, may identify a useful memory-efficiency frontier. A literature search before paper submission must establish whether another group has already run this specific benchmark.

## 3. Model specification: TinyState

A proposed architecture for comparison—not a claim of achieved scientific novelty.

### Backbone

- 10M-parameter debug model; 25M–40M main experiments; 60M–100M only after validated gains.
- Vocabulary: 16K–32K subwords.
- Hidden width ~384, 8–10 layers, 6 attention heads.
- Local token attention: **100 most recent tokens**, enforced during both training and inference.
- Recurrent semantic state: 4–16 learned memory slots (initially 8).
- Optional continuous recurrence: compact RWKV/Mamba-style state.
- Optional episodic memory: 32 or 64 bounded vector entries, top-4 retrieval.
- Optional planner: ~4 state slots, revised every 100–500 tokens.
- Tied input/output embeddings when practical.

**Important capacity-accounting convention:** Memory slots and retrieved vectors are **separate from the 100-token K/V positions**. If a task truly caps *all* tokens including memory tokens to 100, use 92 local token positions + 8 memory positions or the equivalent budget. Always state which interpretation is tested.

### Decomposed memory state

\[
S_j=\{R_j,Z_j,P_j,E_j\},
\]

where:

- \(R_j\): recurrent semantic slots;
- \(Z_j\): recurrent/state-space hidden state;
- \(P_j\): high-level plan and global goals;
- \(E_j\): capped episodic event bank.

For segment \(C_j\) of up to 100 tokens:

\[
H_j=\operatorname{LocalLM}(C_j,R_j,P_j;Z_j),
\]
\[
R_{j+1}=\operatorname{MemoryUpdater}(R_j,H_j),
\]
\[
P_{j+1}=\operatorname{Planner}(P_j,R_{j+1}).
\]

A gated episodic write considers content importance, novelty, replacement of outdated facts, and memory budget. Only explicit fact/event representations should enter long-term episodic storage; a naïve token transcript cache would defeat the bounded-memory premise.

For 64 FP16 vectors of width 384, the value bank alone occupies about **49,152 bytes**. Count query/key projections, vector keys, index metadata, plan state, and all SSM/KV state separately.

### Stateful decoding pseudocode

~~~python
state = model.initial_state()
window = deque(maxlen=100)
memory = BoundedEpisodicMemory(capacity=64)
assert len(prompt_tokens) <= 100  # reject, do not truncate, an oversized prompt
model.consume_prompt(prompt_tokens, state, window)

while not external_stop_condition():
    memories = memory.retrieve(state.query, k=4)
    logits, state = model.step(
        state=state,
        local_window=window,
        episodic=memories,
        plan=state.plan,
    )
    token = sample(logits)
    stream_token(token)
    window.append(token)

    if state.memory_write_trigger:
        memory.upsert_or_evict(state.candidate_event)

    if state.plan_update_trigger:
        state.plan = model.update_plan(state)
~~~

The strict baseline does not call `memory.retrieve`, does not carry `state`, and does not use `plan`: it recomputes from or incrementally caches *only* the last 100 tokens. The illustrated hybrid algorithm is for the separately labeled 100-token-attention-plus-memory experiment. Reject oversized benchmark prompts; never silently truncate them. Also ensure that the token consumed by state and the token appended to the attention cache are synchronized exactly once: careless double consumption causes invalid comparisons.

With all banks capped, inference **model state and KV memory can be O(1)** with output length \(T\). Accumulating the output in RAM is still \(O(T)\); real streaming should write tokens to disk, a socket, or a consumer without retaining the whole transcript in process memory.

## 4. Training objectives

Start with standard next-token language modeling and evaluate whether the recurrent state is actually used:

\[
\mathcal L =
\mathcal L_{\mathrm{LM}}+
\lambda_r\mathcal L_{\mathrm{delayed\ recall}}+
\lambda_s\mathcal L_{\mathrm{state}}+
\lambda_c\mathcal L_{\mathrm{consistency}}+
\lambda_p\mathcal L_{\mathrm{plan}}+
\lambda_d\mathcal L_{\mathrm{repetition}}.
\]

- **Delayed recall:** insert an entity, key/value pair, or fact; reconstruct it after varying numbers of segments. Sample distances approximately log-uniformly to avoid over-weighting short delays.
- **State prediction:** reconstruct past-segment semantic features or contrast against shuffled segments.
- **Contradiction discrimination:** contrast a correct entity attribute with a swapped or outdated attribute.
- **State-change supervision:** ensure newer facts override obsolete facts (e.g. code 7192 changed to 8841).
- **Plan prediction:** plan the next section or event before token-level continuation.
- **Degeneration penalty:** prefer non-repeating long continuations without punishing intentional references.
- **Memory-bottleneck training:** penalize unnecessary writes and enforce fixed state capacity.

Use truncated backpropagation through time (TBPTT), detaching persistent state periodically. Detachment saves memory but weakens gradient credit assignment to very old facts; compare unroll length, auxiliary recall supervision, and state carryover.

Suggested progression of cumulative sequence distances: 400–800 -> 2K–4K -> 8K–16K -> 32K–128K. **The local attention window must never grow above 100.**

## 5. Data plan

- 50–60% permitted natural-language material, including long-form text.
- 20–30% reproducible synthetic memory and update tasks.
- 10–20% structured stories, event graphs, outlines and causal chronologies.

Synthetic tasks: copy/reverse; key-value lookup; entity-to-attribute binding; updated values; distractor paragraphs; ordered events; multiple simultaneous facts; temporal counters; multi-hop retrieval; and long-horizon consistency checks.

Use dataset licenses and record provenance, filtering, duplicates, contamination risk, and public split definitions. Do not evaluate on generated examples copied into the training set.

**Important protocol caveat:** RULER, BABILong, and ∞Bench mostly benchmark **long input** or long-context use. This project additionally studies **long generated output**, which requires purpose-built checkpoints, probes, and reference constraints; do not imply existing benchmarks alone measure long-output coherence.

## 6. Experimental baselines

Parameter-, tokenizer-, corpus-, optimization- and training-token-matched comparisons:

1. **Primary strict baseline:** sliding Transformer with exactly 100 total active token positions and **no hidden/external history**.
2. StreamingLLM-style sink + local cache (same **total** token-KV budget).
3. Recurrent Memory Transformer-style persistent memory tokens.
4. RWKV recurrent LM.
5. Mamba-family SSM LM.
6. TinyState core: local Transformer + semantic slots.
7. Core + continuous recurrence.
8. Core + bounded episodic memory.
9. Core + planner.
10. Full architecture and removal ablations.

Report exact memory byte budget, not merely model parameter count. Baselines that retain a larger global cache cannot be described as equivalent-memory comparisons.

## 7. Evaluation protocol

**Active context length at every decode step:** always <=100 token positions, counting prior prompt and generated tokens that remain in the window.  
**Initial prompt length:** <=100 tokens for the controlled benchmark; this is not the main research constraint.  
**Generated length:** 1K, 10K, 100K; optional 1M output tokens as an engineering stress test.  
**Seeds:** multiple fixed seeds and documented decoding settings (temperature, top-p, repetition handling).  
**Lengths:** evaluate both raw length reached and validity/quality conditioned on length.

### Retention and interference

Define

\[
A(d)=P(\text{correct answer to an inserted fact after }d\text{ tokens}).
\]

Estimate a retention curve, confidence intervals, and a predeclared half-life threshold \(d_{50}\) when the curve crosses 0.5. Avoid reporting a half-life when a model never crosses the threshold in the tested range; report right-censoring instead.

Sweep simultaneously stored facts \(N\in\{1,4,16,64,256\}\), lag \(d\), and overwrite rate. Distinguish retrieval of **initial prompt** facts from later **self-generated facts** and injected controlled events. The latter tests whether the model tracks its own history; simple prompt recall alone does not.

### Degeneration and consistency

- Distinct-2/3/4 n-gram ratios at each length.
- Exact repeated spans (length 20/50/100).
- Semantic repetition and repeated event loops, preferably with sampled human audits.
- Entropy and topic drift by output position.
- Contradictory attributes, aliases, plot/goal drift, impossible event ordering, forgotten updates.
- Local perplexity and blinded pairwise readability/coherence assessment.

Automated LLM judges should be calibrated against human annotations and blinded to model identity. Raw exact-match is useful for keys and attributes but insufficient for semantic consistency.

### Runtime and state

- Tokens/sec, latency distribution, peak VRAM, total CPU/GPU RAM, bytes of recurrent state, KV-cache bytes and external-storage bytes.
- Benchmark at 1K/10K/100K/1M positions and with output streamed rather than buffered.
- Report all eviction/retrieval costs and identify whether state is **truly bounded**.

**Primary result graphs:**

1. Accuracy \(A(d)\) versus distance.
2. Accuracy \(A(N,d)\) versus fact count and distance.
3. Long-range recall versus persistent state bytes.
4. Coherence versus output length.
5. Throughput and peak VRAM versus output length.

Memory-efficiency ratio may be reported as a descriptive statistic:

\[
\mathrm{ME}=\frac{\text{long-range recall score}}{\text{persistent memory bytes}},
\]

but compare on Pareto fronts as a ratio can be unstable at small denominators and ignores computational cost.

## 8. Compute and implementation sizing

Approximate training FLOPs for dense-transformer-like models can be estimated with \(C\approx6ND\), where \(N\) is parameter count and \(D\) is training tokens. This approximation is not exact for sliding attention, SSMs, memory modules, embeddings, and inefficient kernels.

| Model | Training tokens (starting proposal) | Rough FLOPs |
| --- | ---: | ---: |
| 10M | 200M | 1.2e16 |
| 30M | 600M | 1.08e17 |
| 60M | 1.2B | 4.32e17 |
| 100M | 2B | 1.2e18 |

Run synthetic prototype tests before expensive pretraining. On 6GB VRAM, prioritize 1M–10M debug models with short TBPTT unrolls, low batch sizes, mixed precision where supported, and gradient accumulation. Full 30M+ architecture sweeps and 100K-length evaluations may require rented 24GB+ accelerators. These are planning estimates, **not measured runtime**.

Required software stack: PyTorch, deterministic synthetic generators, tokenizer training, JSONL metric logging, pytest, and optional optimized official Mamba/RWKV kernels. The benchmark must run even if optional optimized kernels are not available.

## 9. Phased implementation and falsifiable gates

### Phase A — transparent reference implementation

- Write a strict 100-token causal baseline and streaming inference loop.
- Implement an RMT-style 4/8/16-slot recurrent memory baseline.
- Add tests enforcing prompt and KV-window limits; test no double state updates.
- Demonstrate state memory remains constant when streaming 100K tokens.
- Train on delayed-copy, key/value, and overwrite tasks.

**Gate:** recurrent memory improves delayed recall at the same overall resource budget. If not, diagnose optimization and memory-update supervision before adding complexity.

### Phase B — controlled architecture comparison

- Compare Local-100, StreamingLLM-style, RMT, RWKV, and Mamba at matched parameters and training tokens.
- Evaluate memory-retention half-life and write a reproducible comparison report.

### Phase C — learned, factorised memory

- Split local linguistic state from semantic slots.
- Add persistent-goal state and controlled memory allocation.
- Ablate individual tiers at equal byte budget.

### Phase D — episodic store

- Implement 8, 32, 64, 128-entry capacities and a no-limit upper bound.
- Measure **marginal recall gain per additional stored vector** and overwrite behavior.

### Phase E — hierarchical long-form planner

- Introduce goal -> chapter -> section -> block plans.
- Evaluate genuine 10K/100K long-form coherence and failure rates.

### Phase F — scaling and publication

- Scale only after Phase B/C effects reproduce over seeds.
- Freeze benchmark and run held-out evaluations.
- Publish source code, prompts, checkpoints if redistribution is permitted, dataset creation seeds, exact hardware use, result tables, and negative results.

## 10. Adversarial review

| Failure / reviewer objection | Mitigation |
| --- | --- |
| “Infinite output is trivial for an RNN.” | Make retention-per-byte and coherence at long horizons the central claim, not output length alone. |
| “Memory is secretly unbounded.” | Hard-cap all state tiers and report external storage + output buffering. |
| “Extra memory slots mean more than 100 active tokens.” | Report both total token-equivalent cache and 100 *text-token* visibility constraints; add strict 100-total-token ablation. |
| “Worse baselines got less training/data.” | Match optimizer, data, token budget, vocab and parameter count; tune each baseline fairly. |
| “Synthetic key recall is not text generation.” | Include long-form narrative continuity, event-graph audits, and blinded human quality evaluation. |
| “LLM judge prefers one style.” | Blind outputs, calibrate with human raters, report judge agreement and systematic disagreement. |
| “The model memorized evaluation patterns.” | Hold out keys, entity names, generators, and distance distributions. |
| “Capacity gain comes from extra compute.” | Report throughput, FLOPs/tokens, state bytes and quality Pareto fronts. |
| “Novelty is overclaimed.” | Compare RMT, Compressive Transformer, Memorizing Transformer, Mamba, Infini-attention, Titans and newer related work before submission. |
| “Training only with short unrolls cannot teach very long memory.” | Use delayed supervision, random long-state warmup, synthetic interference, and explicit ablations of TBPTT length. |
| “Endless generation ignores EOS and finite hardware.” | Define externally stopped open-ended streaming and avoid guaranteed literal infinity claims. |

## 11. What would constitute a publishable result?

A strong positive result: the same-size TinyState variant achieves statistically reliable gains in **retention at 10K+ generated tokens**, while maintaining no more than the declared persistent bytes and comparable token throughput. Qualitative examples alone are insufficient.

A strong negative result: identify where each state mechanism fails, e.g., failure to track overwrites or rapidly decaying long-lag fact retention; publish the measurement method and reproducible baselines.

**Potential paper title:** “100 Tokens Are Enough to Keep Going: Measuring Persistent Memory in Tiny Streaming Language Models.”

**Do not claim:** “infinite understanding,” “infinite context,” “lossless infinite memory,” “human-level reasoning,” or “guaranteed coherent infinite prose.”

## 12. Reproducibility checklist

- [ ] Record Git commit, config hash, exact packages and CUDA/runtime versions.
- [ ] Fix training/evaluation seeds; publish deterministic synthetic data generators.
- [ ] Declare what counts toward 100-token limit, state-byte budget and total model parameters.
- [ ] Verify train/validation/test separation and data permissions.
- [ ] Test memory-cap enforcement and streaming output not retained in RAM.
- [ ] Include all ablations and negative results.
- [ ] Separate authors' reported results from local experiments and hypotheses.
- [ ] Report confidence intervals and multiple seeds.
- [ ] Keep paper claims narrower than measured results.

## References and code

The primary publications and reference implementations linked throughout this review form the reading list. Core code sources:

- [RMT](https://github.com/booydar/recurrent-memory-transformer)
- [Mamba](https://github.com/state-spaces/mamba)
- [RWKV-LM](https://github.com/RWKV/RWKV-LM)
- [RetNet in TorchScale](https://github.com/microsoft/torchscale)

**Evidence note:** This document is a research planning synthesis derived from a Deep Research literature review on 2026-11-18. No training runs, parameter counts, recall improvements, memory-half-life measurements or GPU benchmarks described here have been independently executed in this repository.
