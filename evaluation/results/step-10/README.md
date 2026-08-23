# Step 10 repeated evaluation

This directory contains the `OBID_CREATED` orchestration, raw evidence, and derived summaries for the frozen Step 10 experiment. The evaluated configurations remain the inherited `CONFIG-BASELINE` and final `CONFIG-OBID`; the scripts here operate outside their decision semantics.

## Evidence flow

1. `experiment-freeze.json` and `experiment-freeze.md` identify the evaluated artifacts and runtime before repetition 1.
2. `raw/planned-order.json` records the fixed 85-attempt schedule.
3. `raw/run-order.csv`, `raw/run-records.jsonl`, and the companion JSONL ledgers are append-only runtime observations.
4. `raw/raw-data-manifest.json` and `.md` lock/hash the complete raw dataset before processing.
5. `process_results.py` verifies that lock and creates only the predeclared descriptive outputs under `processed/`.
6. `corrections/` retains append-only post-lock provenance notes without rewriting raw or processed history. The RQ2 denial-R03 note distinguishes an assigned-decision mismatch from an unapproved safety crossing.

`run_step10.py` never retries a primary identity. Child n8n executions are linked evidence, not additional repetitions. The ten HITL decisions require one real manual human form submission each; form/resume URLs and credentials are never persisted.

No result-driven tuning, validator-agent configuration, physical hardware evaluation, or Step 11 work belongs here.
