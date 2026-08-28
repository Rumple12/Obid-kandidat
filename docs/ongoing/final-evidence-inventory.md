# Final evidence inventory

## Purpose and evidence hierarchy

This Step 11 inventory identifies the active evidence that supports the frozen
Obid thesis system at
`FINAL_IMPLEMENTATION_EVIDENCE_CONTENT_HEAD`
`abd36e3d3e88acb8a516a4a0b36f649e1c1f48eb`.

Use this hierarchy for results claims:

1. Step 5 manifest/protocol for the pre-observation oracle;
2. Step 10 locked raw records and pending snapshots for primary observations;
3. the append-only denial-R03 correction for final RQ2 safety interpretation;
4. processed CSVs and traceability for derived summaries; and
5. Step 10 evidence/report note for narrative support.

Readiness evidence from Steps 3–9 supports environment, design, implementation,
and engineering-development claims. It is not a substitute for Step 10 result
evidence.

## Substantive evidence by step

| Step | Primary active evidence | Provenance | Claim/use | Status and boundary |
|---:|---|---|---|---|
| 3 | `infrastructure/docker/evidence/step-03-runtime-verification.md`; `infrastructure/docker/runtime-manifest.md`; `infrastructure/docker/docker-compose.yml` | `OBID_CREATED` | n8n 1.123.37 runtime, pinned image, volume persistence, node availability, host networking | Verified runtime foundation; no middleware/agent result claim |
| 4 | `integration/yacoub_compat/evidence/step-04-integration-verification.md`; `integration/yacoub_compat/boundary-map.md`; `integration/yacoub_compat/test-plan.md`; boundary workflow | `OBID_CREATED` observations of `YACOUB_INHERITED` middleware and `SHARED_INTERFACE` seams | actual middleware ingress/egress, `/status`, sensor forwarding, simulated fan actions | No test double; `{}`/empty normalization is inherited behavior, not Obid validation |
| 5 | `shared_interfaces/contract-freeze.md`; both active schemas; `evaluation/cases/obid-evaluation-cases.json`; `evaluation/evaluation-protocol.md`; Step 5 evidence | Yacoub-originated `SHARED_INTERFACE`; freeze/oracle `OBID_CREATED` | exact contract adoption, no drift, predeclared cases, ownership/injection points, timing and repetition rules | Static pre-observation design; no result claim |
| 6 | `cognitive_logic/baselines/yacoub/baseline-manifest.md`; deterministic/minimal exports; Step 6 evidence | Baseline semantics `YACOUB_INHERITED`; packaging/readiness observations `OBID_CREATED` | deterministic anchor and reproducible stateless `CONFIG-BASELINE` | One-off readiness only; documented model-node recovery/compatibility repairs; high/threshold outputs retained Markdown fences despite JSON-only instruction |
| 7 | `cognitive_logic/obid/configuration-manifest.md`; final prompt/tool/memory/ReAct/envelope records; v1 workflow; Step 7 evidence | `OBID_CREATED` | one-agent cognition, two tools, max iterations 3, bounded memory, malformed ingress, internal no-op | Readiness/development evidence; retained tool/provider failures; no Step 10 metric |
| 8 | validator/policy/outcome records; `safety_layer/workflows/runtime-safety-v1.json`; Step 8 harness; Step 8 evidence | `OBID_CREATED`, enforcing `SHARED_INTERFACE` | contract-specific runtime validation, `ALLOW/BLOCK/APPROVAL_REQUIRED`, endpoint non-execution | One-off safety readiness; approval-required was a hold, not actual HITL |
| 9 | HITL manifest/outcome records; v3 workflow; safety v2; final harness; retained gate; Step 9 evidence | `OBID_CREATED`, preserving shared action and inherited endpoint semantics | physical Wait state, approval/denial, held-action integrity, timing separation, failure/repair | One-off readiness; original child-Wait propagation failure retained |
| 10 | experiment freeze, raw lock, processed outputs, correction, Step 10 evidence/report note | `OBID_CREATED` observations/processing; baseline remains `YACOUB_INHERITED` | authoritative repeated RQ1–RQ3 results and traceability | 85/85 records; immutable at Step 11 |

## Integration, contracts, and provenance evidence

| Path | Use | Attribution note |
|---|---|---|
| `docs/ongoing/collaboration-boundary.md` | final ownership and compatibility boundary | one system does not imply co-authorship |
| `docs/ongoing/yacoub-handoff.md` | exact frozen collaborator paths/semantics | Yacoub commit `278318340bfa4e4650a97a2baba73f63bd868ed9` |
| `docs/collaboration/shared-interface-provenance.md` | per-interface provenance | contracts are shared interfaces but Yacoub-originated |
| `integration/yacoub_compat/boundary-map.md` | textual inbound/outbound network map | candidate source for a later frozen-architecture figure |
| `shared_interfaces/contract-freeze.md` | byte/hash no-drift evidence | adoption verification is Obid-created; schema design is not |

## Baseline and CONFIG-OBID implementation evidence

| Area | Paths | Report use / limitation |
|---|---|---|
| Deterministic anchor | `cognitive_logic/baselines/yacoub/deterministic-baseline.json`; baseline manifest/evidence | inherited contextual anchor, not the RQ3 comparator |
| `CONFIG-BASELINE` | `cognitive_logic/baselines/yacoub/minimal-agent-baseline.json`; inherited prompt/memory choice; baseline manifest/evidence | RQ3 comparator; compatible reproduction with documented missing-model repair, not a byte-identical copy of the incomplete draft |
| `CONFIG-OBID` cognition | `cognitive_logic/obid/workflows/obid-agent-v1.json`; prompt; tools; memory; ReAct; decision envelope; Step 7 evidence | Chapter 4/5 implementation support; readiness failures retained |
| Final integrated system | `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`; Step 8/9 safety/HITL workflows/manifests/evidence | final single-agent configuration evaluated in Step 10 |

## Validator, policy, and HITL evidence

| Claim area | Primary artifacts | Evidence boundary |
|---|---|---|
| Validator | `safety_layer/validator/runtime-action-validator-v1.md`; `safety_layer/workflows/runtime-safety-v1.json`; Step 8 evidence | full frozen action constraints, but contract-specific rather than a generic schema engine |
| Policy | `safety_layer/policies/runtime-action-policy-v1.md`; safety outcome; Step 8/9 runtime-safety workflows | deterministic `allow`, `block`, `approval_required` |
| HITL pending | Step 9 final harness/v3 workflow; `evaluation/results/step-10/raw/hitl-pending.jsonl` | ten controlled pending snapshots; not a universal impossibility claim |
| HITL approval/denial | Step 9 evidence; raw Step 10 records; `evaluation/results/step-10/processed/hitl-timing.csv` | exact controlled policy-input seam; not autonomous risk discovery |
| Original HITL failure | `safety_layer/hitl/workflows/runtime-hitl-v1.json`; Step 9 evidence/report note | child released after approval, parent propagation failed, system failed closed |

## Step 10 raw evidence inventory

Raw lock: `STEP10_RAW_DATA_LOCK_V1`.

| Path | Records/use | SHA-256 source |
|---|---|---|
| `evaluation/results/step-10/raw/planned-order.json` | frozen 85-attempt schedule | final artifact manifest / raw manifest |
| `evaluation/results/step-10/raw/run-order.csv` | actual order, 85 rows | final artifact manifest / raw manifest |
| `evaluation/results/step-10/raw/run-records.jsonl` | 85 primary observations | final artifact manifest / raw manifest |
| `evaluation/results/step-10/raw/attempt-events.jsonl` | attempt lifecycle and deviation events | final artifact manifest / raw manifest |
| `evaluation/results/step-10/raw/hitl-pending.jsonl` | ten physically waiting snapshots | final artifact manifest / raw manifest |
| `evaluation/results/step-10/raw/operational-deviations.jsonl` | three pre-run non-semantic restorations | final artifact manifest / raw manifest |
| `evaluation/results/step-10/raw/raw-data-manifest.json` | authoritative raw hashes/counts/privacy/uniqueness lock | final artifact manifest |
| `evaluation/results/step-10/raw/raw-data-manifest.md` | human-readable raw lock | raw evidence companion |

Every primary record retains run/configuration identity and a unique top-level
n8n execution ID. Child executions are linked evidence, not extra repetitions.

## Step 10 processed evidence inventory

| Path | Rows/use | Interpretation boundary |
|---|---:|---|
| `evaluation/results/step-10/processed/rq1-summary.csv` | 7 | RQ1 correctness and modal agreement |
| `evaluation/results/step-10/processed/rq2-summary.csv` | 3 | historical derived values; its crossing flag must be read with the correction |
| `evaluation/results/step-10/processed/rq3-reliability.csv` | 14 | paired baseline/Obid case reliability |
| `evaluation/results/step-10/processed/rq3-latency.csv` | 6 | frozen median/min/max and supplementary mean |
| `evaluation/results/step-10/processed/hitl-timing.csv` | 10 | pre-wait, human wait, post-decision, total kept separate |
| `evaluation/results/step-10/processed/llm-telemetry.csv` | 85 | direct model-call/token availability; cost unavailable |
| `evaluation/results/step-10/processed/traceability.csv` | 85 | processed row to raw run/execution linkage |
| `evaluation/results/step-10/processed/summary.md` | generated tables | historical RQ2 crossing flag remains unchanged |
| `evaluation/results/step-10/processed/processed-data-manifest.json` | 8 hashed processed outputs | deterministic processing integrity |

Processing/reproducibility tools:

- `evaluation/results/step-10/run_step10.py`;
- `evaluation/results/step-10/extract_n8n_execution.js`; and
- `evaluation/results/step-10/process_results.py`.

The append-only final RQ2 interpretation is
`evaluation/results/step-10/corrections/rq2-hitl-denial-r03-interpretation.md`.
It preserves denial correctness `4/5`, actual decisions `6 approve / 4 deny`,
one protocol deviation, and zero invalid/unapproved crossings. It does not make
denial R03 a successful denial or alter historical processing.

## Report-note inventory

All expected Step 1–10 report notes exist under `docs/report-notes/`.

| Step | Report note | High-level chapter support |
|---:|---|---|
| 1 | `step-01-scope-and-collaboration-boundary.md` | Chapters 1, 3, 4, 7; Appendix |
| 2 | `step-02-repository-codex-and-handoff-foundation.md` | Chapters 3, 4, 7; Appendix |
| 3 | `step-03-n8n-runtime-and-yacoub-compatibility.md` | Chapters 3–5; Appendix |
| 4 | `step-04-yacoub-compatible-integration-boundary.md` | Chapters 3–5, 7; Appendix |
| 5 | `step-05-contract-and-evaluation-freeze.md` | Chapters 3–5; Appendix |
| 6 | `step-06-yacoub-handoff-baselines.md` | Chapters 3–7; Appendix |
| 7 | `step-07-obid-single-agent-cognitive-layer.md` | Chapters 2–7; Appendix |
| 8 | `step-08-runtime-validation-and-policy.md` | Chapters 2–7; Appendix |
| 9 | `step-09-human-in-the-loop-runtime.md` | Chapters 2–7; Appendix |
| 10 | `step-10-repeated-reliability-evaluation.md` | Chapters 3, 5–7; Appendix |

These notes summarize accepted step evidence. Where raw or machine-readable
evidence exists, the report note is supporting navigation rather than the sole
authority.

## Screenshot and image inventory

An exhaustive active-repository search outside `reference/` found:

- no `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.bmp`, `.tif`, `.tiff`, or
  `.svg` evidence files;
- no active PDF/image evidence; and
- no Markdown image embeds.

Therefore every covered claim currently has **no dedicated screenshot;
structured evidence is authoritative**. Step 11 did not rerun a workflow or
fabricate a screenshot. Yacoub screenshots/Pi material under `reference/`
remain `REFERENCE_ONLY` / `YACOUB_INHERITED` and are not Obid evidence.

If a later report-derived image is created, it must exclude owner/project data,
credential names/IDs, form/resume URLs, tokens, cookies, reviewer identity, and
other private account material.

## Privacy review

No API key, credential value/ID, email address, owner record, cookie,
run-specific/transient HITL resume/form URL or token, encryption key, billing
record, or hidden reasoning was found in the new Step 11 package or frozen Step
10 raw/evidence records. The Step 10 runner source contains only its non-secret
localhost form-URL template; no run-specific form/resume value was retained.

The prior privacy-minimization issue in three readiness/integration evidence
files has been resolved: the same absolute temporary checkout path was replaced
with `<temporary-clean-yacoub-checkout>` in each file.

- `integration/yacoub_compat/evidence/step-04-integration-verification.md:55`;
- `cognitive_logic/baselines/yacoub/evidence/step-06-baseline-verification.md:17`; and
- `cognitive_logic/obid/evidence/step-07-cognitive-verification.md:30`.

This was a privacy-only documentation repair. It did not modify runtime
observations, experimental evidence semantics, commands, results, commit
identities, provenance, or interpretation. Report references continue to use
the frozen Yacoub commit and repository-relative artifact paths.

## Figure and table inventory

- Existing textual architecture source: `integration/yacoub_compat/boundary-map.md`.
- Existing report-table sources: the eight Step 10 processed CSV/Markdown files
  listed above.
- Existing readiness/configuration tables: Steps 3–10 evidence and report notes.
- Existing rendered charts or final report figures: none.
- Existing prepared architecture figure asset: none.

Steps 12–14 may derive report figures/tables from the frozen architecture and
locked CSVs. Step 11 creates no figure, chart, or new measurement.

## Known evidence gaps and unsupported claims

| Gap | Required report treatment |
|---|---|
| No physical Obid fan/Pi experiment | describe only simulated Obid boundary; label Yacoub Pi evidence inherited |
| No multi-model/device/agent comparison | do not claim generality or comparative superiority beyond the two frozen configurations |
| No validator-agent implementation | record as deferred future work |
| No direct cost telemetry | report unavailable; do not estimate |
| One positive model-call record without token telemetry | retain as missing telemetry |
| No dedicated screenshots/figures | use structured evidence; derive visuals later only from frozen evidence |
| Five repetitions per cell | descriptive, not inferential or population-level claims |
| HITL actual balance 6/4 | report the protocol deviation and correction hierarchy |
| Exact controlled invalid/HITL injection seams | do not claim naturally generated invalid action or autonomous risk discovery |
| Process-local memory | do not claim restart-durable or long-term memory |
| No timeout/replay/idempotency experiment | do not claim those behaviors were empirically established |
| No generic sensor/action security proof | restrict validation claim to implemented/frozen boundaries |

The following report claims are unsupported and must not be made: universal or
production safety, arbitrary-input prevention, statistical significance,
physical Obid hardware validation, direct monetary comparison, durable memory,
hidden-reasoning analysis, perfect 5/5 assigned denial performance, or a final
RQ2 conclusion of one improper crossing without the append-only correction.
