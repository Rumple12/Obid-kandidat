# Final implementation and evidence freeze

## Freeze identity and purpose

- Step: `11 — Freeze implementation and final evidence`
- Status: `FINAL_IMPLEMENTATION_EVIDENCE_FREEZE: ACTIVE`
- Substantive frozen state: `abd36e3d3e88acb8a516a4a0b36f649e1c1f48eb`
- Frozen Yacoub source: `278318340bfa4e4650a97a2baba73f63bd868ed9`
- Machine-readable integrity record: `docs/ongoing/final-artifact-manifest.json`

`abd36e3d3e88acb8a516a4a0b36f649e1c1f48eb` is the
`FINAL_IMPLEMENTATION_EVIDENCE_CONTENT_HEAD`: the complete implementation,
experiment, audited results, correction, and Step 10 report-support state that
the thesis may describe. Step 11 adds inventory/freeze metadata on top of that
state and does not try to self-reference its later documentation commit.

Feature development and new reportable experimentation stop at this boundary.
The remaining normal work is report production from frozen evidence.

## Final architecture

```text
YACOUB_INHERITED / SHARED_INTERFACE
compatible sensor event and action/endpoint meanings
        |
        +---------------------> CONFIG-BASELINE
        |                         inherited minimal agent
        |                         stateless / no memory
        |                         minimal parse and route
        |
        `---------------------> CONFIG-OBID (OBID_CREATED)
                                  one Decision Agent
                                  -> two read-only tools
                                  -> one bounded-memory configuration
                                  -> structured candidate OR internal no_action
                                  -> runtime action-schema validator
                                  -> deterministic action policy
                                     |-> ALLOW: unchanged valid action
                                     |-> BLOCK: stop, no shared action
                                     `-> APPROVAL_REQUIRED
                                           -> native n8n Wait/form
                                           -> approve: unchanged held action
                                           `-> deny: no release
                                  -> YACOUB_INHERITED middleware endpoint
                                  -> simulated fan state
```

The final architecture contains no validator agent, second agent, second model,
dynamic risk engine, additional device, competing middleware, or physical Obid
hardware path.

## Final core configurations

| Item | `CONFIG-BASELINE` | `CONFIG-OBID` |
|---|---|---|
| Provenance | `YACOUB_INHERITED` | `OBID_CREATED` |
| Workflow | `cognitive_logic/baselines/yacoub/minimal-agent-baseline.json` | `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json` |
| Workflow SHA-256 | `ed8697e07eb83deaecac3879c82b860e2c4b8f597bde1bc355a3c5b863c15585` | `1a09ee5a3199289c39845f9b97a3a3f516f277924d6a8fcb52da52780b0eaf78` |
| Prompt | `cognitive_logic/baselines/yacoub/system-prompt-v1.md` | `cognitive_logic/obid/prompts/system-prompt-v1.md` |
| Prompt SHA-256 | `a5e24dc517d3bb91eb45ebebb6efd79bbc77bcf7197ecd9b3daf76fd1aab92cd` | `f8b4171e5d70df6be5aa136a63336dc8c32edca61036272a047b6fa3746cfec2` |
| Agent/model nodes | inherited minimal decision / one Gemini node | one Decision Agent / one Gemini node |
| Tools | inherited route plumbing, not Obid tools | exactly two read-only tools |
| Memory | stateless / no memory | one process-local, two-interaction window |
| Iteration bound | not a ReAct agent | `maxIterations: 3` |
| Runtime reliability | no Obid validator, policy, or HITL | schema validator, deterministic policy, actual HITL |
| Internal no-op | absent | `no_action` is internal and emits no shared action |

The final Obid tool record is
`cognitive_logic/obid/tools/tool-definitions-v1.md`; the bounded-memory record is
`cognitive_logic/obid/memory/window-buffer-v1.md`. Their executable nodes are
embedded in the final v3 workflow.

## Model and runtime freeze

| Item | Frozen value |
|---|---|
| Model | `models/gemini-2.5-flash` |
| Stored generation options | `{}` |
| Fallback model | none |
| n8n | `1.123.37` |
| Image/digest | `n8nio/n8n:1.123.37|sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Frozen Yacoub commit | `278318340bfa4e4650a97a2baba73f63bd868ed9` |
| Middleware boundary | actual frozen Yacoub middleware |
| Observable device boundary | inherited simulated fan, not physical Obid hardware |

Private model-credential attachment remains a runtime prerequisite. No
credential identity, value, account, owner identity, token, or key is frozen as
evidence.

## Shared contract freeze

| Contract | Path | SHA-256 | Provenance |
|---|---|---|---|
| Sensor event | `shared_interfaces/json-schema/sensor-event.schema.json` | `416cec7d396912672171e1fbfdce828820017c9218e2c418de3f784e329ee007` | Yacoub-originated `SHARED_INTERFACE` |
| Agent action | `shared_interfaces/json-schema/agent-action.schema.json` | `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b` | Yacoub-originated `SHARED_INTERFACE` |

Frozen semantics remain:

- `value >= 30.0 C -> fan_on`;
- `value < 30.0 C -> fan_off`;
- target `fan_1`;
- `GET /status`;
- `POST /sensor-event`;
- `POST /fan/on`; and
- `POST /fan/off`.

No field, action, target, threshold, or endpoint was changed.

## Safety and HITL freeze

| Identity | Path | SHA-256 | Final role |
|---|---|---|---|
| `runtime-safety-v1` | `safety_layer/workflows/runtime-safety-v1.json` | `d179f0f4b3ef3977ab65456cc172854176e9dc56336a43e87b9bf92fea3ee378` | Step 8 validator/policy snapshot |
| `runtime-safety-v2-hitl` | `safety_layer/workflows/runtime-safety-v2-hitl.json` | `8dbf1826f43cdea34d510ff53e90fed52e45c93d5ed29956cf3a6dbfd6de652d` | final policy-context/HITL safety component |
| `step-09-hitl-harness` | `safety_layer/hitl/workflows/step-09-hitl-harness.json` | `090715a02ed15ce0a385788fad8f25abceec7cd473422f63c9114909d850eaac` | controlled HITL/evaluation seam |
| `runtime-hitl-v1` | `safety_layer/hitl/workflows/runtime-hitl-v1.json` | `fd9ce59e033c6074d6688d9eb0037dff7afc3d882a74fea0743901dfa041d902` | retained original child-Wait attempt |

The final release invariant is:

```text
parse succeeds
+ frozen action schema valid
+ deterministic policy allows direct release
  -> unchanged action may reach the inherited endpoint

or

parse succeeds
+ frozen action schema valid
+ deterministic policy requires approval
+ actual human approve
+ held action unchanged
  -> unchanged approval-required action may reach the inherited endpoint
```

Every block, denial, pending state, invalid candidate, or internal no-op releases
no shared action. The original child-Wait/subworkflow propagation failure is
retained as development evidence: the child released correctly after approval,
the parent received the wrong pre-wait state, and the system failed closed. The
bounded compatibility repair embedded the same native Wait/form gate directly
in the caller.

## Evaluation design and evidence freeze

| Item | Frozen identity |
|---|---|
| Evaluation manifest | `evaluation/cases/obid-evaluation-cases.json`, SHA-256 `612a3c6cb6032ed4aa03eae87fa62e5632d61fcdb2cc0633c151bbf4d67aafb7` |
| Evaluation protocol | `evaluation/evaluation-protocol.md`, SHA-256 `27ecdd2d0b9bdd7110a2c25baee06803acefd4963a2cce00e931216a15f95117` |
| Experiment freeze | `STEP10_EXPERIMENT_FREEZE_V1` |
| Raw lock | `STEP10_RAW_DATA_LOCK_V1` |
| Core records | `70` |
| Invalid-action records | `5` |
| HITL records | `10` |
| Total primary records | `85` |
| Automated-latency eligible | `30` |
| Core configurations | `CONFIG-BASELINE`, `CONFIG-OBID` only |

The Step 5 manifest/protocol remain the original pre-observation oracle. Step 10
raw and processed files are immutable at this freeze. Raw hashes and every
processed artifact are indexed in `docs/ongoing/final-artifact-manifest.json`.

| Locked raw artifact | SHA-256 |
|---|---|
| `evaluation/results/step-10/raw/run-order.csv` | `096eef4b1d2ccdeba271206476087a2af4ab57ff373bbd5bbc6fd05f080e1604` |
| `evaluation/results/step-10/raw/run-records.jsonl` | `54bc2c4058e6324b478c1c527f2cf2d3b5ea24e4fc0d41c1419577db466a16e6` |
| `evaluation/results/step-10/raw/attempt-events.jsonl` | `a5ef39991790f8a29192a71ca7fd9d0fd64b98de7a13e21bb22e2d664f7c90bd` |
| `evaluation/results/step-10/raw/hitl-pending.jsonl` | `71007709c2eb352078bf37723bac3fa7877c23815ffb39e30eb8c513838a0f31` |
| `evaluation/results/step-10/raw/operational-deviations.jsonl` | `7f57913b9e1f16c22d57f00a6f5f3f928115e89faa16e46fe7d463f247dec764` |
| `evaluation/results/step-10/raw/planned-order.json` | `56f3602a1af82ed3a049393a741be48ae6d505693ecc181556bb7fdeffccd5d5` |

## Frozen result state

### RQ1

Within the seven frozen case families, `CONFIG-OBID` produced the expected
observable outcome in `35/35` attempts, with `100%` modal agreement in every
family:

| High | Low | Threshold | Malformed | Memory A | Memory B | Memory C |
|---:|---:|---:|---:|---:|---:|---:|
| 5/5 | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |

This is a bounded frozen-case result, not a universal reliability claim.

### RQ2

| Family | Assigned-oracle result |
|---|---:|
| Invalid action | 5/5 |
| HITL approval | 5/5 |
| HITL denial | 4/5 |

- Planned HITL decisions: `5 approve / 5 deny`.
- Actual HITL decisions: `6 approve / 4 deny`.
- Controlled-decision protocol deviations: `1`.
- Final observed invalid or unapproved crossings: `0`.

The locked historical processor classified denial R03 by its assigned denial
family and retained a crossing value of `1`. That value is not the final safety
interpretation. The append-only correction
`evaluation/results/step-10/corrections/rq2-hitl-denial-r03-interpretation.md`
controls the final interpretation while leaving raw and processed history
unchanged. Denial R03 remains incorrect as an assigned denial trial; the actual
valid `approve` input produced an approved release rather than an unapproved
crossing.

### RQ3 reliability

| Case | `CONFIG-BASELINE` | `CONFIG-OBID` |
|---|---:|---:|
| High | 5/5 | 5/5 |
| Low | 5/5 | 5/5 |
| Threshold | 5/5 | 5/5 |
| Malformed | 0/5 | 5/5 |
| Memory A | 5/5 | 5/5 |
| Memory B | 0/5 | 5/5 |
| Memory C | 5/5 | 5/5 |

Baseline absence of memory is not itself scored as failure. Its five observable
duplicate `fan_on` actions in memory-B are scored against the common oracle.

### RQ3 automated latency

| Case | Configuration | Median ms | Min ms | Max ms | Mean ms (supplementary) |
|---|---|---:|---:|---:|---:|
| High | `CONFIG-BASELINE` | 2130 | 2016 | 4631 | 2603.4 |
| High | `CONFIG-OBID` | 3792 | 3524 | 4803 | 4090.2 |
| Low | `CONFIG-BASELINE` | 2105 | 2009 | 2250 | 2118.6 |
| Low | `CONFIG-OBID` | 4472 | 4237 | 5565 | 4782.8 |
| Threshold | `CONFIG-BASELINE` | 2083 | 1998 | 2252 | 2108.8 |
| Threshold | `CONFIG-OBID` | 4487 | 4279 | 4689 | 4482.6 |

These are the existing Step 10 descriptive summaries. Human waiting is excluded.
No additional statistic or significance claim is introduced by Step 11.

## Frozen negative evidence

| Evidence | Classification | Frozen interpretation |
|---|---|---|
| Five baseline malformed failures, including two n8n non-success statuses | Experimental result | Remain in RQ1/RQ3 denominators; three other runs emitted unexpected `fan_off` |
| Five baseline memory-B duplicate `fan_on` actions | Experimental result | Consistent wrong observable outcome, not random instability |
| Step 9 original child-Wait propagation failure | Implementation-development evidence | Human approval and correct child release occurred; parent failed closed; repair retained separately |
| Step 10 denial R03 | Protocol deviation | Planned deny, actual approve; assigned denial remains incorrect; not a runtime safety semantic defect |
| Step 6 high/threshold Markdown-fenced model outputs | Inherited-baseline readiness limitation | JSON-only instruction was not followed exactly; inherited parser still extracted the contractual object; not a Step 10 result |
| Step 7 tool-schema/wrapper/legacy HTTP Tool failures | Implementation-development evidence | Motivated bounded compatibility repairs without shared-contract changes |
| Step 7 provider quota interruptions | Infrastructure/provider limitation | Retained readiness failures; not Step 10 result rows |
| One model-call record without token telemetry and no cost telemetry | Measurement/provider limitation | Values remain unavailable; none are guessed |

## Methodological limitations

1. One model identifier/family was evaluated; the remote provider backend is not an immutable local artifact.
2. Stored model options are `{}`; pinned runtime/provider defaults constrain reproducibility.
3. The domain is one controlled temperature-to-one-fan scenario.
4. Five repetitions per evaluated cell support descriptive consistency only.
5. Analysis is descriptive and does not establish inferential generalization.
6. The action boundary is a simulated fan; Obid produced no physical-hardware evidence.
7. Actual HITL distribution is six approvals and four denials because of one human protocol deviation.
8. Human waiting times are session-specific, not population estimates.
9. Automated latency compares complete configurations with different internal workloads; it does not isolate component-level causality.
10. Direct cost telemetry is unavailable; one positive model-call record lacks token telemetry.
11. Final RQ2 interpretation depends on the explicit append-only denial-R03 correction.
12. The repeated invalid-action result covers one injected unsupported action; broader validator constraints have one-off Step 8 readiness evidence.
13. HITL repetitions use the exact controlled policy-input seam; they do not prove autonomous risk discovery.
14. The action validator is contract-specific, not a general arbitrary-schema security engine.
15. Bounded memory is process-local, not restart-durable; active-window exclusion is not physical history deletion.
16. No memory-strategy, model, device, or multi-agent comparison was performed.
17. No production-safety, universal reliability, scalability, or model-superiority claim is supported.
18. Yacoub Raspberry Pi evidence is inherited context, not new Obid experimental evidence.

## Provenance freeze

### `YACOUB_INHERITED`

- workflow-to-action infrastructure and middleware/action API;
- deterministic and minimal-agent baselines;
- threshold/action semantics;
- original safety/HITL concept where cited; and
- Raspberry Pi/action-side evidence.

### `SHARED_INTERFACE`

- sensor-event contract;
- agent-action contract; and
- compatible endpoint/action meanings.

`SHARED_INTERFACE` is a compatibility role, not a co-authorship claim.

### `OBID_CREATED`

- stronger single-agent cognition, prompt, tools, bounded memory, and internal decision envelope;
- runtime action validation and deterministic policy;
- executable HITL and controlled evaluation seams;
- Step 10 orchestration, raw observations, processing, summaries, traceability, and correction; and
- Step 11 freeze documentation.

## Deferred work

`OPTIONAL_VALIDATOR_AGENT: DEFERRED_AFTER_FINAL_FREEZE`

The earlier `OPTIONAL_VALIDATOR_AGENT: SKIP_FOR_CORE` decision remains correct
for Steps 9–10. Because the substantive implementation/evidence state is now
frozen, a validator-agent/two-agent extension is deferred to future work rather
than added before report writing. No `CONFIG-OBID-VALIDATOR`, second agent,
second Gemini node, or supplementary experiment exists.

## Post-freeze change rule

Allowed without reopening the freeze:

- thesis prose, literature, references, citations, and formatting;
- figures, tables, and architecture diagrams derived only from frozen evidence;
- path/citation corrections, typo fixes, and non-semantic documentation fixes; and
- analysis that preserves the frozen measurements and stated limitations.

Not allowed without an explicit formal reopening decision:

- implementation or workflow semantic changes;
- new runs, repetitions, cases, models, agents, memory strategies, hardware tests, or result axes;
- optional validator-agent work;
- rewriting raw/processed evidence or replacing failures; or
- changing contracts, threshold, actions, target, policy, or HITL behavior.

No Step 12 chapter prose is part of this freeze record.
