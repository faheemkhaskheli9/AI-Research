# Brain-Inspired Language Modeling under a Hard 100-Token Context Window

**Research status:** Research proposal and implementation plan; **no trained model or experimental results are claimed**.  
**Prepared:** 2026-11-18.  
**Related work:** [100-token bounded-context LM review](TINY_100_TOKEN_STATEFUL_LM_LITERATURE_REVIEW.md).  
**Proposed project name:** *Neuro100* — Bounded-Attention Language Modeling with Adaptive Episodic and Semantic Memory.

## 0. Problem definition and non-negotiable constraints

**Objective:** Investigate whether a genuinely small language model (5M–50M parameters initially, optionally scaling to 100M) with a **hard maximum of 100 directly attended text-token positions at every decoding step** can continue generating 1K–100K+ tokens, track long-range facts, learn from experience, maintain goals, and avoid degeneracy using mechanisms *inspired by* cognitive memory systems.

A 100-token window is not equivalent to human working-memory capacity. Humans maintain a small number of **chunks**, with limits influenced by task and representation; LLM subword tokens and cognitive chunks are fundamentally different units [Cowan 2001]. Nor does the analogy establish a biologically accurate brain simulation.

**Two contracts:**

- **C0 / strict 100-token LM:** the probability of the next token depends only on the most recent <=100 prompt/output tokens, with no hidden state persisting after their eviction, no summary/retrieval store, no recurrent state, and no extra memory tokens. This model can emit arbitrarily many tokens but cannot in general recover an arbitrary evicted fact.
- **C1 / brain-inspired bounded-attention LM:** causal text attention sees <=100 recent token positions. Separate continuous recurrent, episodic and semantic memory may survive beyond the window and influence decoding via bounded latent cross-attention, gating or explicitly budgeted textual substitution. Total memory is **more than 100 tokens of information** and **must be disclosed in bytes**. It is dishonest to call C1 a 100-token *total-memory* model.
- **C2 / expanding external memory upper bound (optional):** the same 100-token direct attention constraint, but a persistent disk store may grow. This track tests a storage/quality upper bound and is *not* constant-memory.

“Unlimited output” means the decoder may continue **without a context-size-imposed stopping point** if external stop, time and storage permit. It does not guarantee literally infinite execution, correctness or coherence.

## 1. Neuroscience grounding (function-level analogies, not anatomical claims)

| Biological observation/framework | Engineering analogy | Known limitation |
|---|---|---|
| Limited active working memory and chunking [1] | A 100-token active ring buffer | 100 tokens do not equal four chunks |
| Complementary learning systems: rapid episodic acquisition / slower semantic integration [2,3] | Immediate episode store + slower replay-based semantic updates | This is an abstract analogy |
| Episodic recall from cues and pattern completion [4] | Keyed similarity/associative recall | Vector lookup is not a literal hippocampus |
| Consolidation / replay [2,4,5] | Offline rehearsal of validated experiences into adapter/model | Training can create interference and invented details |
| Attention and executive control | Gated retrieval, write priority, plan maintenance | Such a controller is not a biological executive circuit |

**2026 closest prior art:** Spens et al. [4] explicitly model hippocampal–neocortical interaction as compressed retrieval-augmented generation, with gist/detail memory and consolidation. Their paper uses pretrained Mistral-7B in key memory simulations and does **not** demonstrate our proposed tiny-model hard-100-token training protocol. Also see the 2026 complementary-learning-system preprint [5], which uses sparse episode-specific adapters plus consolidation. These works make simplistic “we invented brain-like memory for an LLM” claims untenable.

## 2. Technical architecture

\`\`\`text
stream input / previous generated token
                |
       [Causal local token buffer]
          100 token IDs MAX
                |
         Tiny decoder backbone
          5M -> 20M -> 50M
                |
    +-----------+------------+----------------+
    |           |            |                |
    v           v            v                v
 short-lived   episodic     semantic         goal /
 recurrent     event bank   knowledge        executive
 trace         (fast)       (slow)           control
    |           |            |                |
    +-----------+------[active retrieval]-----+
                       |
             bounded latent interface
                       |
               next-token logits
                       |
             stream output, update
\`\`\`

### 2.1 Working-memory and decoder

- Backbone: token embeddings; 4–8 lightweight causal attention blocks or a hybrid recurrent/attention decoder; tied embedding/output weights; vocabulary 8K–16K to keep small models practical.
- Strict causal local window of **100 text positions** (including all special/sink token positions that are truly in self-attention). Hard-reject benchmarks that exceed the input contract; never secretly retain a full-history KV cache.
- Rolling RoPE/relative-position handling must be tested after >100K steps; do not silently rely on a position table trained only up to 100 positions.
- Text tokens in the buffer are *prompt and generated tokens*, not just the user's original prompt.
- Output is written to a streaming sink, rather than accumulated as a growing tensor or Python list.

### 2.2 Fast recurrent trace (optional, C1 only)

Let \`h_t = GRU(h_{t-1}, pool(hidden(window_t)))\`. Alternatively compare a compact selective SSM or RWKV recurrence. The state can compress older context, but cannot losslessly encode arbitrary unbounded history at finite precision. Sweep 0, 512 B, 4 KiB, 32 KiB, and 256 KiB equivalent budgets. The strict C0 model has **no recurrent trace**.

### 2.3 Episodic memory: fast, explicitly versioned events

Each event record:

\`\`\`text
event_id, entity_ids, event_type, compact_summary,
embedding_or_key, timestamp, source_id, source_kind,
confidence, valid_from, valid_to, supersedes_event_id,
importance, last_accessed, protected
\`\`\`

Important: do **not** treat model-generated guesses as verified external facts. Memory writes must distinguish observed inputs, external ground truth, generated narrative commitments, inferences and later corrections. For fiction, a generated event can become valid **story canon** even though it is not a real-world fact.

Prototype storage: SQLite (structured entries) plus vector/lexical search. Hard-cap at 64/256/1024 events for bounded-memory experiments. Include an unbounded disk upper-bound track only when clearly labeled as such. Report total key/value bytes, metadata, indexing and external retrieval cost.

### 2.4 Semantic memory: slower integration

Begin with stable language-model weights and a structured semantic graph containing validated reusable rules. Only after that baseline succeeds test replay into small adapters or tiny model weights (with rollback and held-out tests).

A repeated episode can teach a reusable rule; merely looking up that episode is *retrieval*, not learning a transferable skill. Measure novel-task transfer after experience.

### 2.5 Executive controller and memory selection

A small controller sees local hidden state, goal state, uncertainty and memory search statistics. It chooses among:

- \`READ(memory_query)\`: retrieve top-k evidence;
- \`WRITE(episode)\`: store a novel, likely-useful fact/event;
- \`REVISE(event)\`: correct or supersede stale information;
- \`CONSOLIDATE\`: schedule replay and abstraction (usually offline);
- \`CONTINUE\`: emit token without memory operations;
- \`CHECK\`: verify planned constraints or story canon.

Initial controller may be deterministic/heuristic. A later learned controller is trained using counterfactual or supervised memory-utility labels, followed by RL only if reliable evaluation is available. **Do not** require expensive proprietary LLMs inside the memory loop when claiming a tiny independent model.

A candidate priority score:

\[
u(e,t) = \alpha\,\mathrm{novelty}(e) + \beta\,\mathrm{future\ relevance}(e,t) +
\gamma\,\mathrm{goal\ alignment}(e,t)+\delta\,\mathrm{evidence}(e)-
\eta\,\mathrm{storage\ cost}(e)-\zeta\,\mathrm{conflict\ risk}(e).
\]

The challenge is that importance is only partly observable when writing an event. Evaluate how often the controller discards an event needed later.

### 2.6 Critical retrieval interface: tokenless vs textual

At most 100 *text* positions may enter self-attention; memory delivery follows one of two explicit mechanisms:

1. **Text-budgeted recall:** make the retrieved memory occupy part of those 100 text positions (for instance, 60 recent text + 40 retrieved text). This respects the *total token-attention* bound but reduces recency.
2. **Latent recall:** cross-attend to k separate learned compressed vectors, with the same 100 text positions in self-attention. This preserves a **100-text-token attention bound**, but **does not** constrain total attention inputs to 100 positions; the extra k latent vectors, parameters and FLOPs must be separately reported.

Do not compare methods with unequal memory-information budgets as if they used identical context. Include byte-matched and FLOP-matched baselines.

## 3. Formal model and objective

Let \`z_{<=t}\` be the concatenated input and generated tokens. Define \`w_t = suffix_100(z_{<=t})\`.

**C0:** \`p(y_{t+1}|z_{<=t}) = f_theta(w_t)\`.

**C1:**
\[
q_t = Q_\phi(w_t,h_t,g_t), \quad m_t = \mathrm{Retrieve}(q_t,E_t,k)
\]
\[
h_{t+1} = F_\theta(h_t,w_t,m_t), \quad
p(y_{t+1}) = G_\theta(w_t,h_{t+1},m_t,g_t)
\]
\[
E_{t+1} = \mathrm{Update}(E_t,\mathrm{observed\ event}_t, a_t).
\]

Only current information is in the 100-token window. Long-term history enters C1 through \`h_t\` and \`m_t\`, with disclosed storage.

Start with LM loss, then controlled auxiliary tasks:

\[
L = L_{NTP}+\lambda_1 L_{delayed-recall}+\lambda_2 L_{overwrite}
+\lambda_3 L_{goal-consistency}+\lambda_4 L_{memory-utility}
+\lambda_5 L_{interference}.
\]

- Delayed recall: reproduce a controlled key, name, relationship, rule or event after 200, 1K, 10K, 100K intervening tokens.
- Overwrite: old value must not be retrieved after a timestamped correction.
- Goal consistency: story/plan predicates remain true at the end of a long generated sequence.
- Memory utility: memory writes are rewarded based on **future task improvement**, not merely retrieval similarity.
- Interference: after new experiences, preserve established skills without preventing valid updates.
- Add calibrated uncertainty for unsupported details; never optimize “memory of hallucinations” as if it were truth.

## 4. A credible experimental novelty claim

The literature already includes:

- recurrent memory tokens (RMT; 2022) [6];
- recurrent/state-space long-history inference (RWKV and Mamba family) [7,8];
- learned memory at test time (Titans; NeurIPS 2025) [9];
- explicit brain-inspired compressed episodic + semantic learning (Spens et al.; 2026) [4];
- sparse hippocampus-like episode adapters + consolidation (2026 preprint) [5];
- **Four Kilobytes of Memory**, a 9.97M-parameter fixed-state recurrent BabyLM model with ~4.2 KiB bf16 state [10];
- Unified Memory Agent, training a memory-operation policy and evaluating long-horizon state tracking [11].

**Therefore the unvalidated novelty candidate is not “a language model with brain-like memory”.** Investigate **adaptive memory survival under a rigid, audited 100-token active context** and tiny-model parameter budget. Specifically, compare three mechanisms in a common harness: (i) compressed recurrent state, (ii) event-level episodic storage and controlled recall, and (iii) replay-based semantic consolidation, using closed-loop **self-generated long outputs** and later information updates.

### Hypotheses (must be falsifiable)

- **H1:** With the same base model and memory byte budget, selective utility-trained episodic retention gives higher 10K-token delayed recall than recency-only or similarity-only policies.
- **H2:** Combining structured episode updates with goal state reduces contradictions during 10K+ generated tokens compared to fixed-state recurrence alone.
- **H3:** Replay-based semantic consolidation improves transfer to held-out *novel rules/tasks* versus retrieval-only memory, without large forgetting on a frozen general-language validation suite.
- **H4:** A learned cross-attention retrieval interface is useful after controlling for extra latent memory bytes and compute, compared with a 100-token *text-budgeted* retrieval interface.

Negative results are publishable as a bounded-context evaluation benchmark or capacity analysis.

## 5. Reproducible evaluation

### Data and licenses

- Small natural-language training corpus from licensed/open sources, with tokenization and deduplication documented.
- Deterministic synthetic streams: key-value assignments, changing attributes, nested goals, character continuity, graph relations, arithmetic rules and distractor text.
- Controlled event injection in extended generation. Keep task-generation seeds and *entity IDs*, templates, value distributions and test tasks separate from training.
- For naturalistic long generation, create a short prompt, allow the model to establish story facts, and validate **self-committed canon** using pre-registered structured event extraction audited by humans.

### Primary protocol

| Axis | Settings |
| --- | --- |
| Active text context | Exactly capped at 100 tokens throughout |
| Prompt | 25, 50, 100 tokens |
| Output length | 1K, 10K, 100K tokens; optional 1M streaming stress test |
| Base model sizes | ~5M debug, ~10M main pilot, ~30M controlled study, optional ~50M |
| Memory state | 0 B; 512 B; 4 KiB; 32 KiB; 256 KiB; plus capped event stores |
| Memory bank entries | 0, 16, 64, 256, 1024 |
| Retrieval operations | none, fixed periodic, event-triggered, learned policy |
| Seeds | at least 3 initially; 5 for final comparisons |
| Benchmarks | controlled long-generation dataset + adapted LongMemEval, LoCoMo, Ledger-QA, AMA-Bench |

**Crucial:** LongMemEval, LoCoMo, Ledger-QA and AMA-Bench do not by themselves validate **very long self-generated output**. The new benchmark must test coherent long output, because most memory benchmarks use long *inputs*, histories, or interaction streams.

### Mandatory metrics

1. Retention score as a function of lag: \`accuracy(lag, number_of_stored_facts)\`; confidence intervals and right-censoring if a threshold is not reached.
2. Rewrite/update accuracy; evidence provenance and cross-session leakage rate.
3. Memory selection regret: fraction of later-useful episodes wrongly discarded; erroneous writes per 1K tokens.
4. Story/goal constraint violations per 1K generated tokens, measured by structured programs and a calibrated blinded human audit.
5. Repetition/degeneration: repeated 20/50-token spans, distinct-n, semantic loops and topic drift.
6. Transfer to new tasks after consolidation, forgetting on earlier tasks, and general-language perplexity.
7. Parameter count, memory-state bytes, peak VRAM, CPU/disk bytes, latency percentiles, tokens/sec and total training FLOPs.
8. Accuracy–state-byte–FLOP Pareto frontier, not raw accuracy alone.

**Required ablations:** strict local-100; no gating; random write; FIFO vs LRU vs surprise; fixed read schedule vs learned; remove goal state; remove episodic store; remove consolidation; no provenance; oracle retrieval upper bound; masked past facts; identical total information budget.

### Leakage and resource audit

- Assert \`effective_local_text_positions <= 100\` at each attention call.
- Verify all model layers use causal masking, no full-history cache, no hidden summary in C0.
- Log extra *latent tokens*, recurrent state bytes, disk memory growth, and external tool/model calls separately.
- Compare parameter-, training-data-, compute- and state-budget-matched baselines where possible.
- Report when memory writes occur at inference. Do not permit an oracle to access future test events.
- Stream output to file; confirm memory is stable with generation length when claiming constant inference memory.
- Use holdout generators and blinded judges; report confidence intervals and failures as well as successes.

## 6. Compute and training plan

On a laptop with 16 GB RAM and **6 GB GPU VRAM**, prefer **a 1M–5M debug baseline** to establish cache invariants and synthetic tasks, then approximately 10M parameters for first serious training. For a 10M model trained on 200M tokens, a rough dense LM FLOPs heuristic is \`~6*N*D = 1.2e16\` FLOPs, **not** a reliable wall-clock or price estimate. Full architecture sweeps may need larger GPU access. No speed or final quality is asserted until measured.

Parameter budget example (not an exact calculated config):

- Token embedding/head 8–16K vocab x 256–384 width, tied.
- 4–8 attention or hybrid blocks, small MLPs.
- Small gated recurrent state and event encoder/controller; report its parameters as part of total.
- Train with mixed precision, short unroll, gradient accumulation, checkpoints, deterministic synthetic datasets.
- If the model cannot reliably acquire English next-token prediction at 10M scale, use a restricted language/task prototype or a slightly larger controlled backbone before claiming practical narrative quality.

Training stages:

1. **A: strict-100 harness** — implement an audited causal 100-token sliding-window Transformer with generation to 10K/100K tokens and tests for memory invariants.
2. **B: local LM competence** — fit minimal natural-language and synthetic data; report perplexity, repetition, throughput.
3. **C: fast memory** — event encoder, fixed-capacity store, event updates, search and token-budgeted retrieval.
4. **D: closed-loop generation** — prompt->generate->extract canon->write->retrieve->continue; validate automatic event extraction accuracy.
5. **E: small recurrent state** — add GRU/RMT/Mamba-like state and evaluate memory advantage vs simpler methods.
6. **F: consolidate** — offline replay, rule abstraction, transfer tests, forgetting guards and rollback.
7. **G: learned controller** — supervised memory-survival targets before any RL; measure end-task gain at fixed storage budget.
8. **H: open benchmark/paper** — publish exact task generator, seeds, controls, plots, failure cases and code/checkpoints if rights permit.

**Stop/go criteria:** do not add a complex mechanism if it fails to outperform a simpler, resource-matched baseline in repeated experiments. A memory read that merely prints the correct answer once is not evidence of knowledge consolidation.

## 7. Adversarial review

- **“100-token context is a gimmick.”** Justify as a controlled severe-memory bottleneck and map the memory/quality Pareto frontier. Show performance at 32, 64, 100, 128 and 256 tokens as a sensitivity analysis.
- **“You hid a much larger context in external memory.”** Disclose C0 versus C1 versus C2; exact bytes, reads, latent positions, retrieval bandwidth, disk use.
- **“This already exists in 2026 brain-memory RAG papers.”** Yes, much of the architecture does. Novelty must be specifically demonstrated in fixed-100 tiny-LM policies and controlled closed-loop generation.
- **“It is not like a brain.”** Describe functional inspiration only, not biological validity or claims of cognition.
- **“Remembering model hallucinations worsens accuracy.”** Track truth status and provenance; use a separate notion of in-story canon.
- **“Consolidation forgets old skills.”** Replay stratified samples, frozen eval suite, rollback, limited adapter updates.
- **“Memory scores measure lookup, not learning.”** Measure unseen task transfer, actual policy gains and generalization.
- **“Text generation to 100K becomes repetitive.”** Track progression curves, controlled decoder settings, blinded audits and error accumulation.
- **“A second model performs the actual intelligence.”** Do not silently delegate retrieval, summary or scoring to an enormous external LLM; if used for analysis, label it and account for its computational cost.
- **“The memory policy has seen future answers.”** Train/test stream isolation and non-oracle memory access.
- **“The controller adds compute.”** Equal-total-FLOPs and wall-clock efficiency comparisons.
- **“A 10M LM may be too weak for fluent stories.”** Separate the concept proof on synthetic tasks from open-domain natural-language generation.

## 8. Deliverables and publication strategy

The intended contribution is **not** a claim of a new human-like intelligence architecture. Deliverables:

- Strict100-TinyLM baseline with invariant tests and streaming inference.
- Neuro100 with optional memory mechanisms under explicitly recorded budgets.
- **BWM-100** (Brain-inspired Working Memory, 100-token) controlled benchmark for active memory selection, changing facts, later retrieval and long-output continuity.
- Reproducible plots: memory retention versus distance; accuracy versus memory byte budget; coherence versus generation length; transfer/forgetting after consolidation.
- A peer-review-oriented manuscript: *“Learning What to Remember: Tiny Language Models Under a Hard 100-Token Working-Memory Constraint”* (tentative, claim dependent on results).

## 9. Prioritized reading list and source status

The following papers motivate or challenge the design. They are **not** proof of performance for Neuro100.

1. **Cowan (2001), The magical number 4 in short-term memory** — capacity/chunking foundation. https://pubmed.ncbi.nlm.nih.gov/11515286/
2. **McClelland, McNaughton & O'Reilly (1995), Why There Are Complementary Learning Systems in the Hippocampus and Neocortex** — fast/slow memory. https://pubmed.ncbi.nlm.nih.gov/7624455/
3. **Complementary Learning Systems (2012 review)** — updated account of episodic/semantic integration. https://pubmed.ncbi.nlm.nih.gov/22141588/
4. **Spens et al. (2026), Hippocampo-neocortical interaction as compressive retrieval-augmented generation**, Nature Communications — *particularly close prior art*. https://www.nature.com/articles/s41467-026-74357-6
5. **A complementary learning system for continual episodic memory in large language models (2026)** — sparse episode adapters and consolidation, preprint and reviewed-preprint discussion. https://www.biorxiv.org/content/10.64898/2026.08.24.746712v1 ; https://elifesciences.org/reviewed-preprints/112891
6. **Bulatov et al. (2022), Recurrent Memory Transformer**, NeurIPS — memory tokens. https://arxiv.org/abs/2207.06881 ; https://github.com/booydar/recurrent-memory-transformer
7. **RWKV language model (2023)** — efficient recurrent representation. https://arxiv.org/abs/2305.13048 ; https://github.com/RWKV/RWKV-LM
8. **Gu & Dao (2023), Mamba; Dao & Gu (2024), Mamba-2** — state space and structured duality. https://arxiv.org/abs/2312.00752 ; https://proceedings.mlr.press/v235/dao24a.html ; https://github.com/state-spaces/mamba
9. **Titans: Learning to Memorize at Test Time (NeurIPS 2025)** — learned neural memory and surprise-based write. https://proceedings.neurips.cc/paper_files/paper/2025/hash/a4ca07aa108036f80cbb5b82285fd4b1-Abstract-Conference.html
10. **Four Kilobytes of Memory: A 10M-Parameter Fixed-State Recurrent LM (BabyLM 2026)** — small fixed-state direct baseline. https://aclanthology.org/2026.babylm-main.40/
11. **Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning (EMNLP 2026)** — learned memory actions and Ledger-QA. https://aclanthology.org/2026.emnlp-main.1299/
12. **AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications (ICML 2026)**. https://proceedings.mlr.press/v306/zhao26bs.html
13. **Memory-Centric Continual Learning for AI Agents (2026)** — future-task improvement criterion. https://arxiv.org/abs/2610.29357
14. **Nested Learning (NeurIPS 2025)** — multi-timescale updates; investigate as an alternative, not a free novelty claim. https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/
15. **Learning to remember: advances in memory mechanisms for large language models (November 2026)** — survey/taxonomy. https://link.springer.com/article/10.1007/s44336-026-00044-1

**Provenance:** This is a synthesis and original *proposal*. Statements about other papers reflect their published abstracts/text; no local model weights, accuracy gains or latency data have yet been generated or independently reproduced.
