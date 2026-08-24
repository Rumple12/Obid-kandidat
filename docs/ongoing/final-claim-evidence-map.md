# Final claim-to-evidence map

## Use rule

This map permits only claims supported at
`FINAL_IMPLEMENTATION_EVIDENCE_CONTENT_HEAD`
`abd36e3d3e88acb8a516a4a0b36f649e1c1f48eb`.

For result claims, read the evidence in this order: Step 5 oracle/protocol →
Step 10 locked raw records → denial-R03 correction where applicable → processed
tables/traceability → evidence/report notes. Readiness evidence from Steps 3–9
supports implementation and engineering context, not repeated-result claims.

## Supported claims

| Claim ID | Evidence-supported claim | RQ / likely chapter | Supporting artifacts | Provenance | Caveat |
|---|---|---|---|---|---|
| `RQ1-01` | Within all seven frozen RQ1 case families, `CONFIG-OBID` produced the expected observable outcome in `35/35` attempts and each family had 100% modal agreement. | RQ1; Chapters 3, 6, 7 | Step 5 cases/protocol; `raw/run-records.jsonl`; `processed/rq1-summary.csv`; `processed/traceability.csv`; Step 10 evidence/report note | Oracle/observations/processing `OBID_CREATED` | One domain, exact frozen cases, five repetitions; not universal reliability |
| `RQ1-02` | The exact missing-`value` case injected at `EVAL_DIRECT_PRE_DECISION_INGRESS` terminated at the Obid-controlled input path with no shared action in `5/5` CONFIG-OBID attempts. | RQ1; Chapters 3, 5, 6, 7 | Step 5 malformed case; final v3 workflow; Step 7 input/evidence; raw records; RQ1 summary | `OBID_CREATED` | One malformed form at a direct Obid seam; not inherited `{}` normalization or all malformed inputs |
| `RQ1-03` | The frozen A→B→C sequence produced off→on, duplicate suppression/no shared action, then on→off in CONFIG-OBID, `5/5` at each position. | RQ1; Chapters 4–7 | Step 5 sequence; bounded-memory record; final v3; Step 7 memory evidence; raw records; RQ1 summary | `OBID_CREATED` | One process-local two-interaction memory configuration; no durability or memory-strategy claim |
| `RQ2-01` | The injected unsupported `fan_reverse` candidate was blocked `5/5` with `UNKNOWN_ACTION`, no endpoint call, and fan off. | RQ2; Chapters 4–7 | Action schema; validator/policy artifacts; frozen invalid case; raw records; `processed/rq2-summary.csv`; traceability; Step 10 evidence/report | Validator/evaluation `OBID_CREATED`; contract `SHARED_INTERFACE` | Post-agent fault injection of one unsupported action, not naturally generated model output |
| `RQ2-02` | All ten controlled HITL executions were physically waiting with a held action, null release, endpoints 0/0, and simulated fan off before human input. | RQ2; Chapters 3–7 | Step 9 HITL implementation/evidence; `raw/hitl-pending.jsonl`; raw records; `processed/hitl-timing.csv`; Step 10 evidence/report | `OBID_CREATED` | Exact controlled policy-input seam; not a universal impossibility claim |
| `RQ2-03` | Assigned approvals succeeded `5/5`; after each actual approve, the unchanged valid `requires_approval:true` action was released and `/fan/on` executed once. | RQ2; Chapters 5–7 | Step 9 workflows/evidence; raw records; RQ2 summary; HITL timing; traceability; Step 10 evidence/report | `OBID_CREATED`, endpoint semantics `YACOUB_INHERITED` | Controlled action/context; no autonomous risk discovery claim |
| `RQ2-04` | Assigned denial correctness was `4/5`; planned decisions were 5 approve / 5 deny, actual decisions 6 approve / 4 deny, one protocol deviation occurred, and zero invalid or unapproved actions crossed. | RQ2; Chapters 3, 6, 7 | Raw records; attempt events; pending snapshots; historical RQ2 summary; `corrections/rq2-hitl-denial-r03-interpretation.md`; Step 10 evidence/report | `OBID_CREATED` | Historical processor flag `1` remains immutable but is not the final safety interpretation; R03 is not a successful denial |
| `RQ3-01` | Both configurations were `5/5` on high, low, threshold, memory A and memory C; baseline versus Obid was `0/5` versus `5/5` for malformed and memory B. | RQ3; Chapters 3, 6, 7 | Step 5 protocol; baseline manifest/workflow; final v3; raw records; `processed/rq3-reliability.csv`; traceability; Step 10 evidence/report | Baseline `YACOUB_INHERITED`; Obid/evaluation `OBID_CREATED` | Baseline no-memory status is not itself failure; its duplicate action is the scored outcome |
| `RQ3-02` | CONFIG-OBID had higher observed automated latency than CONFIG-BASELINE in every measured high/low/threshold family using the frozen median/min/max summaries. | RQ3; Chapters 3, 6, 7 | Step 5 timing rule; 30 eligible raw records; `processed/rq3-latency.csv`; traceability; Step 10 evidence/report | `OBID_CREATED` measurements; inherited comparator | Descriptive n=5/cell; complete configurations have different workloads; no significance or component-causality claim |
| `ARCH-01` | The final CONFIG-OBID is one agent with one Gemini node, exactly two tools, one bounded-memory configuration, max iterations 3, structured candidate/internal no-op, runtime validation, deterministic policy, and actual HITL. | Chapters 4, 5; Appendix | final v3 workflow; prompt/tool/memory/ReAct/envelope records; Step 7–9 manifests/evidence; final artifact manifest | `OBID_CREATED` | Describes frozen implementation only; no validator agent or broad autonomy |
| `COMPAT-01` | The active system preserves the Yacoub-compatible sensor/action contracts and calls the inherited middleware endpoint boundary with simulated fan observability. | Chapters 1, 4, 5; Appendix | collaboration boundary; active handoff; Step 4 boundary evidence; contract freeze; schemas; frozen Yacoub commit | Middleware/semantics `YACOUB_INHERITED`; contracts `SHARED_INTERFACE`; Obid verification `OBID_CREATED` | Shared use does not transfer authorship; no physical Obid hardware claim |
| `PROV-01` | Schemas, middleware, threshold/action meanings, deterministic baseline, minimal baseline, and Pi evidence originate with Yacoub; Obid created the stronger cognition/reliability layer and repeated evaluation. | Chapters 1, 3–5, 7; Appendix | collaboration boundary; handoff; shared-interface provenance; baseline manifest; Steps 4–10 evidence/report notes | Mixed, explicitly labelled | Active minimal baseline is a compatible provenance-labelled reproduction with documented repairs, not a byte-identical incomplete draft |

## Exact latency values permitted for `RQ3-02`

| Case | Baseline median/min/max ms | Obid median/min/max ms | Supplementary means ms |
|---|---|---|---|
| High | 2130 / 2016 / 4631 | 3792 / 3524 / 4803 | 2603.4 / 4090.2 |
| Low | 2105 / 2009 / 2250 | 4472 / 4237 / 5565 | 2118.6 / 4782.8 |
| Threshold | 2083 / 1998 / 2252 | 4487 / 4279 / 4689 | 2108.8 / 4482.6 |

Mean is supplementary. Human waiting is excluded from this table.

## Provenance claim map

| Provenance claim | Evidence |
|---|---|
| Yacoub owns workflow/action infrastructure, middleware API, baseline semantics, and existing Pi evidence. | `docs/ongoing/collaboration-boundary.md`; `docs/ongoing/yacoub-handoff.md`; frozen commit `278318340bfa4e4650a97a2baba73f63bd868ed9` |
| Sensor/action schemas are Yacoub-originated shared interfaces adopted without drift. | `docs/collaboration/shared-interface-provenance.md`; `shared_interfaces/contract-freeze.md`; Step 5 evidence |
| Baseline behavior is inherited, while active reconstruction/sanitization and new verification evidence are Obid-created. | baseline manifest; Step 6 evidence/report note |
| Stronger cognition, prompt/tools/memory, runtime validator/policy, executable HITL, Step 10 orchestration/raw/processing/correction, and Step 11 freeze are Obid-created. | Steps 7–10 manifests/workflows/evidence/report notes; final artifact manifest |

## Unsupported claims that must remain excluded

| Unsupported claim | Why unsupported |
|---|---|
| Assigned denial was 5/5 or actual HITL remained balanced 5/5 | Denial R03 received actual approve; assigned denial is 4/5 and actual balance is 6/4 |
| Final RQ2 conclusion is one improper crossing | Historical processor flag is superseded for safety interpretation by the append-only correction |
| Denial R03 was a successful denial | It remains incorrect against its assigned oracle |
| Every malformed input or every invalid/risky action is prevented | Repetition covers exact frozen forms/injection seams only |
| The agent naturally generated `fan_reverse` | The unsupported action was injected post-agent |
| The system autonomously discovers risk | The exact internal approval-required policy context was controlled |
| Full repeated Gemini→HITL end-to-end risk generation was evaluated | HITL repetitions entered at `OBID_POLICY_INPUT` through the controlled harness |
| HITL timeout, replay/idempotency, reviewer identity, or cryptographic action integrity was empirically proven | Those measurements were not part of the frozen experiment |
| The validator is a generic JSON Schema/security engine | It is a contract-specific implementation for the frozen action schema |
| Statistical significance, confidence, population estimates, or causal latency attribution | Protocol freezes descriptive measures only, with five repetitions/cell and unequal internal workloads |
| Direct monetary cost comparison | Direct cost telemetry is unavailable |
| Durable/long-term memory or physical deletion of history | Memory is process-local; eviction is active-window exclusion |
| Physical Obid fan/Raspberry Pi validation | Obid used the inherited simulated boundary; Pi evidence is Yacoub-owned context |
| RQ3 compared against the deterministic baseline | The comparator was the inherited minimal-agent `CONFIG-BASELINE` |
| Exact reason-text fidelity or hidden chain-of-thought analysis | Reason wording was not exact-scored and hidden reasoning was not collected |
| Universal reliability, production safety, scalability, or model superiority | The frozen single-domain/single-model experiment cannot support those generalizations |

Any future claim not represented above requires an evidence check. Missing
support must be reported as a limitation or future-work item, not invented.
