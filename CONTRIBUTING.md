# Contributing research

Every paper addition must have a canonical source URL, year, status (`peer_reviewed` or `preprint`), at least one topic, a short **original** summary, a falsifiable open question, and a review date. Do not claim unverified preprints have been accepted. Use `python scripts/validate_catalog.py`.

Research code must include documentation of assumptions, seeded evaluation, tests, and a baseline. Write tests for malicious or invalid inputs and compare algorithms using equal feedback and budget. Keep synthetic demos clearly separate from experimental results.

Never copy whole paper bodies, closed datasets, restricted model weights or other third-party files without verifying rights. Cite external claims in the nearest note. Capture failed experiments and contradictory evidence in Git history rather than deleting them.

For a major research result, add a dated experiment report containing the exact command, commit SHA, data provenance, model version, seeds, all runs, hardware, costs, and what **did not work**.
