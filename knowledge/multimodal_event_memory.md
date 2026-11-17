# Persistent multimodal event memory — knowledge note

**Status:** Proposed design and definitions; not implemented or evaluated. [Evidence review](../research/MULTIMODAL_GROUNDED_INTELLIGENCE.md).

## Observation, inference, event, claim and belief

- **Observation:** timestamped sampled evidence of pixels, sound, ASR text or a detector output. Detector output is fallible; preserve provenance and uncertainty.
- **Event:** a bounded change in environment state inferred from one or more observations; event time can be uncertain or interval-censored.
- **Claim:** an assertion attributed to evidence IDs with confidence and time validity; classify as observed, inferred, or hypothesized causal relation.
- **Belief revision:** adding a new version of a claim based on contradictory or clarifying evidence, while preserving prior versions.
- **Grounded answer:** every consequential claim points to evidence time ranges and a resolvable source pointer; unsupported or unobserved details are abstained from.

## Suggested minimal record fields

| Record | Required fields |
| --- | --- |
| Observation | observation_id, media_hash, modality, start_ms, end_ms, source_ref, extraction_model, extraction_version, recorded_at |
| Event | event_id, start_ms, end_ms, entities, observation_ids, type, uncertainty, detected_at |
| Claim | claim_id, subject, predicate, object_or_value, valid_from_ms, valid_to_ms, support_ids, refute_ids, epistemic_type, confidence, revision_parent_id, status |
| Query trace | query_id, query_time_ms, retrieved_evidence_ids, excluded_future_evidence_count, model_version, prompt_hash, latency_ms, answer_claim_ids |

## Non-negotiable invariants

1. Observations are immutable, except authorized removal of source data for privacy/licensing compliance; derived records retain referential integrity.
2. Query at time T may not use observations with observation time greater than T.
3. A revised claim cannot delete evidence contradicting the superseded version.
4. A detected event occurring before another is not automatically a cause.
5. Timestamp support must reference the original media clock after transformations and sampling.
6. State assertions include time validity and are evaluated at query time, not at end of recording.
7. An answer that lacks required causal evidence must explicitly label uncertainty or abstain.
8. Memory consolidation cannot replace raw evidence provenance with untraceable summary text.

## Failure examples to retain

- **Occlusion:** glass falls while hand is hidden. Nearby person is not established as cause.
- **Delayed correction:** early frames suggest an object is missing; later view reveals it behind another object.
- **Audio source mismatch:** audible crash aligns with a visible moving object but originates off-screen.
- **Entity switch:** two similar-looking actors cross and a tracker swaps identities.
- **ASR hallucination:** speech transcript contains an invented action while video contradicts it.
- **Memory contamination:** a summary asserts an unverified interpretation and later retrieval treats it as raw fact.

## Evidence-gated revision workflow

1. Write source-linked observation (never an unconstrained factual summary).
2. Create candidate event and claim with epistemic type and provisional uncertainty.
3. On contradiction, independently retrieve supporting and refuting original intervals; compare with budget-matched baseline.
4. Ask a verifier to choose retained, revised, unresolved, or rejected status; log revision and threshold.
5. For a new query, reason over time-valid claims but cross-check original evidence at key inference steps.
6. Measure incorrect confident claims, accepted correct abstentions, calibration and computational cost.

**Scientific warning:** An event graph or human-readable rationale does not guarantee causal or mechanistic faithfulness. Use intervention-controlled recordings and counterfactual variants for stronger causal claims.

## Open questions

- What constitutes a reliable enough contradiction signal across independently noisy audio and video?
- Can calibration be learned from labeled validity intervals rather than self-reported model confidence?
- When does evidence replay become less effective than simply retrieving a longer contiguous clip?
- What memory retention policy best preserves low-frequency events that later become important?
- Can event boundaries be learned without overfitting to speech transitions or camera cuts?

Sources: [PyraVid](https://aclanthology.org/2026.emnlp-main.777/), [WorldMM](https://openaccess.thecvf.com/content/CVPR2026/html/Yeo_WorldMM_Dynamic_Multimodal_Memory_Agent_for_Long_Video_Reasoning_CVPR_2026_paper.html), [EMMA](https://aclanthology.org/2026.findings-emnlp.1256/), [CaST-Bench](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_CaST-Bench_Benchmarking_Causal_Chain-Grounded_Spatio-Temporal_Reasoning_for_Video_Question_Answering_CVPR_2026_paper.html), [MemInStream](https://arxiv.org/abs/2611.15640).
