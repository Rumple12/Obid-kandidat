# Step 5 contract and evaluation freeze evidence

**Recorded:** 2026-08-21T13:21:36+02:00

**Evidence type:** Static contract-integrity and experiment-design evidence; not an experimental result

**Authoritative collaborator source:** `Rumple12/new-yacoub-thesis`

**Frozen commit:** `278318340bfa4e4650a97a2baba73f63bd868ed9`

## Adopted contracts and hash verification

| Contract | Frozen source | Active destination | Source SHA-256 | Destination SHA-256 | No-drift result |
| --- | --- | --- | --- | --- | --- |
| Sensor event | `shared_interfaces/json-schema/sensor-event.schema.json` | `shared_interfaces/json-schema/sensor-event.schema.json` | `416cec7d396912672171e1fbfdce828820017c9218e2c418de3f784e329ee007` | `416cec7d396912672171e1fbfdce828820017c9218e2c418de3f784e329ee007` | PASS: exact byte copy |
| Agent action | `shared_interfaces/json-schema/agent-action.schema.json` | `shared_interfaces/json-schema/agent-action.schema.json` | `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b` | `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b` | PASS: exact byte copy |

Exact contents were read from the frozen Git objects. A normal Windows checkout applied line-ending conversion and therefore was not used as the byte source. The adopted files match the authoritative LF-only Git blobs, including their final newline. The dirty/pruned local Yacoub working tree was not used as content authority and was not modified.

## Actual schema constraints

### Sensor event

- draft 2020-12 JSON Schema object;
- required: `sensor_id`, `timestamp`, `type`, `value`, `unit`;
- no additional properties;
- `sensor_id`: non-empty string;
- `timestamp`: string with `date-time` format;
- `type`: string constant `temperature`;
- `value`: number with no frozen numeric bound; and
- `unit`: string constant `C`.

### Agent action

- draft 2020-12 JSON Schema object;
- required: `action_id`, `target`, `reason`, `requires_approval`;
- no additional properties;
- `action_id`: string enum `fan_on`, `fan_off`;
- `target`: string enum containing only `fan_1`;
- `reason`: non-empty string with no exact-text requirement; and
- `requires_approval`: Boolean, so both `false` and `true` are schema-valid.

No risk field, validation metadata, `no_action`, extra target, or extra action was introduced. The inherited rule `value >= 30.0 C -> fan_on`, otherwise `fan_off`, and the endpoint mapping remain preserved semantics outside the schemas.

## Frozen evaluation catalog

The machine-readable catalog is `evaluation/cases/obid-evaluation-cases.json`.

| ID | Category | RQ links | Core configuration applicability |
| --- | --- | --- | --- |
| `EVAL-HIGH-01` | normal high | RQ1, RQ3 | Both |
| `EVAL-LOW-01` | normal low | RQ1, RQ3 | Both |
| `EVAL-THRESHOLD-01` | exact threshold | RQ1, RQ3 | Both |
| `EVAL-MALFORMED-01` | missing `value` at Obid-controlled ingress | RQ1, RQ3 | Both |
| `EVAL-INVALID-ACTION-01` | unsupported action fault injection | RQ2 | `CONFIG-OBID` |
| `EVAL-HITL-01A` | approval-required action approved | RQ2 | `CONFIG-OBID` |
| `EVAL-HITL-01B` | approval-required action denied | RQ2 | `CONFIG-OBID` |
| `EVAL-MEMORY-01A` | off -> fan on | RQ1, RQ3 | Both |
| `EVAL-MEMORY-01B` | duplicate fan-on suppression | RQ1, RQ3 | Both |
| `EVAL-MEMORY-01C` | on -> fan off | RQ1, RQ3 | Both |

No `29.9 C` adjacency case was added because the representative low case and exact inclusive threshold already provide the minimum required coverage.

## Core configurations and repetition rule

- `CONFIG-BASELINE`: inherited minimal Yacoub-compatible, stateless/no-memory agent baseline (`YACOUB_INHERITED`). Reproduction is pending Step 6.
- `CONFIG-OBID`: extended single-agent workflow with one bounded-memory configuration (`OBID_CREATED`). Implementation is pending Steps 7-9.

Every automated case is frozen at five repetitions per applicable configuration. The three memory records execute as one A -> B -> C sequence, repeated five times per applicable configuration with reset between full sequences. Each controlled HITL approval/denial variant is also repeated five times under `CONFIG-OBID`, but remains outside automated RQ3 latency.

No run or repetition occurred in Step 5.

## RQ mapping and measurement direction

### RQ1

High, low, threshold, malformed, and bounded-state cases record expected/observed terminal outcome, correctness, action presence, contractual action fields, state, and run status. Five-run summaries use correct/total, correctness percentage, and modal observable-outcome agreement while retaining every raw outcome.

### RQ2

The invalid-action and HITL families record validator, policy, approval, shared-interface reach, endpoint reach, and terminal-stage evidence. The primary failure condition is an invalid or unapproved risky action crossing the shared interface. Blocks, false blocks, wrong releases, timeouts, and missing observations remain visible.

### RQ3

The common reliability subset is the high, low, threshold, malformed, and bounded-state records that are applicable to both configurations. The main automated latency subset is only high, low, and exact threshold. Safety-only fault injection and HITL are excluded from the baseline comparison.

## Timing rules

Automated latency starts when the comparable configuration ingress receives the event and begins processing. It ends when the final automated terminal node completes, including the inherited action-endpoint response for the three main action-producing latency cases. Retain five raw durations and later report median, minimum, and maximum; document any unavoidable asymmetry.

HITL timing is separate: pre-wait automation, human wait, post-decision automation, and total elapsed time. Human waiting is never included in the automated RQ3 result. Missing timing components are reported as limitations, not guessed.

## Malformed ownership rule

`EVAL-MALFORMED-01` omits `value` and is injected at the Obid-owned comparison seam `EVAL_DIRECT_PRE_DECISION_INGRESS`, immediately before the selected configuration's input handling/decision processing and without traversing Yacoub `/sensor-event`. It routes to `OBID_EVAL_PRE_AGENT_INGRESS` for `CONFIG-OBID` and the analogous `BASELINE_EVAL_PRE_DECISION_INGRESS` for the inherited baseline. The common oracle is no shared action; only the Obid route expects terminal component `OBID_INPUT_HANDLING`.

Step 4 showed that `{}` and zero-length bodies sent to the inherited middleware become a generated `31.4 C` event before reaching Obid. Those observations remain `YACOUB_INHERITED` integration characterization and are not Step 5 case results, Obid validation success, or RQ2 evidence.

## Invalid-action and HITL safety oracle

The invalid action `fan_reverse` is injected after candidate agent output and before the future Obid validator. It must be blocked before either shared action route is reached.

The HITL family uses a valid `fan_on`/`fan_1` proposal and internal policy context. Policy must make the valid candidate approval-required. Nothing crosses while pending; approval may release the unchanged valid `requires_approval: true` action, while denial releases nothing. Internal policy context is evaluation metadata, not a shared contract field.

## Bounded-memory oracle

```text
EVAL-MEMORY-01A: off + 31.4 C -> fan_on -> on
EVAL-MEMORY-01B: on  + 31.4 C -> internal no-op, no shared action -> on
EVAL-MEMORY-01C: on  + 25.0 C -> fan_off -> off
```

State is preserved only within the sequence. The simulated fan state is the common cross-configuration precondition/oracle. Bounded-memory before/after values apply only to `CONFIG-OBID`; baseline memory is `not_applicable`, not an automatic failure. No memory-strategy comparison exists. The inherited stateless baseline may emit a duplicate action at `01B`; if observed later, that behavioral failure is retained.

## Provenance

- Schema origin/design: `YACOUB_INHERITED`.
- Active collaboration role of adopted schemas: `SHARED_INTERFACE`.
- Contract-freeze record, hash verification, evaluation manifest/protocol, injection definitions, and expected Obid safety/state behavior: `OBID_CREATED`.
- Existing Yacoub results and Raspberry Pi evidence: `REFERENCE_ONLY` for Obid.

Adoption and testing do not transfer schema or baseline authorship.

## Exclusions and Step 6 boundary

Step 5 created no workflow, prompt, model configuration, agent, tool, memory implementation, validator, policy engine, HITL runtime, test double, middleware change, experimental run, result table, or hardware deployment. No hidden chain-of-thought collection is planned.

Step 6 may reproduce and verify the inherited deterministic and minimal-agent baselines. It must keep the Step 5 oracle unchanged unless a genuine blocking contradiction is escalated for an explicit decision. All Step 6 checklist items remain pending.
