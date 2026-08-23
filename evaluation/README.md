# Evaluation Area

## Purpose and ownership

This active area is reserved for Obid's evaluation definitions and evidence. New protocols, raw runs, and processed results created in authorized later steps are `OBID_CREATED`; inherited Yacoub results remain read-only collaborator evidence.

## Frozen design and completed evaluation

- `cases/obid-evaluation-cases.json` freezes the future expected-outcome oracle.
- `evaluation-protocol.md` freezes applicability, repetitions, correctness, timing, state reset, and evidence rules.
- `evidence/step-05-contract-and-evaluation-freeze.md` records static freeze evidence.
- `results/step-10/` contains the locked 85-record raw evaluation and reproducible processed summaries.
- `evidence/step-10-repeated-evaluation.md` records the concise Step 10 evaluation evidence.

Step 10 produced the reportable repeated raw evidence and traceable processed summaries without changing the Step 5 oracle.

Raw failures, malformed outputs, blocks, rejects, timeouts, missing values, and unexpected results must remain preserved with their run/configuration identity.

## Current boundary

Step 5 files remain the pre-observation experiment design; Step 10 files are the observed results. No implementation tuning, optional validator-agent work, thesis chapter prose, or Step 11 work belongs in this area during Step 10.
