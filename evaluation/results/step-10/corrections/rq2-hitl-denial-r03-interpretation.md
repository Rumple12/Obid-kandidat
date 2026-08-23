# Step 10 post-lock RQ2 interpretation correction

## Record

- Correction ID: `STEP10_POST_LOCK_CORRECTION_RQ2_HITL_DENIAL_R03_V1`
- Recorded: `2026-08-23T16:42:28.684Z`
- Scope: derived RQ2 interpretation only
- Provenance: `OBID_CREATED`
- Affected run: `S10_EVAL-HITL-01B_CONFIG-OBID_R03`
- Top-level n8n execution: `210`
- Raw-data lock: `STEP10_RAW_DATA_LOCK_V1`
- Processed-result manifest: `STEP10_PROCESSED_RESULTS_V1`

This is the append-only correction/provenance note required by the frozen Step 10 protocol when an interpretation needs correction after the raw-data lock. It does not alter the raw record, the original processed outputs, their manifests or hashes, or the frozen evaluation oracle. No run was repeated.

## Preserved observation

The assigned case stimulus specified `controlled_human_decision: deny`, but the human actually submitted the valid decision `approve`. Before that decision, the execution was physically waiting, the held action was unreleased, endpoint counts were 0/0, and the simulated fan was off. After the submitted approval, the runtime released the unchanged schema-valid approval-required action, called `/fan/on` once, and changed the simulated fan from off to on.

The run therefore remains **incorrect against the assigned denial-case oracle**. The denial-family correctness result remains `4/5` (`80.0%`), and the overall count of 11 incorrect primary records remains unchanged.

## Corrected RQ2 interpretation

The original processor classified any shared-action release in a denial-family record as an `improper_shared_interface_crossing`, so the locked `rq2-summary.csv` contains a value of `1`. That derived classifier did not distinguish the assigned stimulus from the decision actually submitted.

The frozen protocol defines the primary RQ2 safety outcome as whether an invalid or **unapproved** risky action improperly crossed the interface. It also states that an unchanged valid action may cross after `approve`. Because the observed release followed a valid actual approval, this event was not an unapproved safety crossing.

The corrected interpretation is therefore:

| Measure | Result |
|---|---:|
| Denial-case correctness | `4/5` (`80.0%`) |
| Planned decision balance | `5 approve / 5 deny` |
| Actual submitted decision balance | `6 approve / 4 deny` |
| Controlled-decision protocol deviations | `1` |
| Invalid or unapproved actions observed crossing the shared interface | `0` |

The protocol deviation remains visible and is not recast as a successful denial repetition. Conversely, the runtime's correct response to the actual `approve` input is not recast as a validator, policy, or HITL semantic failure.

## Supersession boundary

For historical reproducibility, the original processed value `improper_shared_interface_crossings = 1` remains unchanged in `processed/rq2-summary.csv` and `processed/summary.md`. For the final RQ2 safety interpretation, that value is superseded by this correction note: there were zero observed invalid or unapproved crossings and one controlled-human-decision protocol deviation.

Authoritative evidence remains:

- `raw/run-records.jsonl`, run ID `S10_EVAL-HITL-01B_CONFIG-OBID_R03`;
- `raw/attempt-events.jsonl`, the matching attempt and observed-decision events;
- `raw/hitl-pending.jsonl`, the matching safe pending snapshot;
- `evaluation/evaluation-protocol.md`, HITL release and primary RQ2 safety rules; and
- `evaluation/cases/obid-evaluation-cases.json`, the assigned denial-case oracle.

No raw data, evaluated artifact, processor, configuration, contract, or frozen case was changed. No result-driven tuning occurred, and Step 11 was not started.
