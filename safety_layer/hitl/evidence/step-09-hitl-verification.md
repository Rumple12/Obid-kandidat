# Step 9 HITL Verification Evidence

**Execution date:** 2026-08-22  
**Runtime:** n8n `1.123.37`, container `obid-n8n`  
**Frozen action schema:** SHA-256
`55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b`  
**Frozen oracle/protocol:**
`612a3c6cb6032ed4aa03eae87fa62e5632d61fcdb2cc0633c151bbf4d67aafb7` /
`27ecdd2d0b9bdd7110a2c25baee06803acefd4963a2cce00e931216a15f95117`  
**New evidence provenance:** `OBID_CREATED`

These are bounded implementation-readiness observations, not Step 10
repetitions or RQ result aggregation. Raw execution data remains in the
persistent n8n execution database under the IDs below.

## Common HITL stimulus

The approval and denial runs used the exact frozen proposal:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature requires a policy-controlled fan activation",
  "requires_approval": false
}
```

with exact internal context:

```json
{
  "policy_case_id": "POLICY-HITL-REQUIRED",
  "approval_required": true,
  "shared_contract_field": false
}
```

In every HITL run the original proposal was schema-valid. Runtime safety
recorded the original action, changed only `requires_approval` to `true`,
proved the other three fields unchanged, returned `approval_required`, held
the transformed action, and released `null` before human interaction.

## Readiness matrix

| Observation | Main / child execution IDs | Human decision | Endpoint count (`on`, `off`) | State | Verdict |
| --- | --- | --- | --- | --- | --- |
| Original `S9-HITL-APPROVE` attempt | harness `64`, safety `65`, HITL child `66` | `approve` | `0`, `0` | off -> off | **FAIL-CLOSED**, retained compatibility failure |
| `S9-HITL-APPROVE-REPAIR-VERIFY` | harness `71`, safety `72` | `approve` | `1`, `0` | off -> on | PASS |
| `S9-HITL-DENY` | harness `73`, safety `74` | `deny` | `0`, `0` | off -> off | PASS |
| `S9-BLOCK-FAN-REVERSE` | harness `67`, safety `68` | none | `0`, `0` | off -> off | PASS |
| `S9-ALLOW-NORMAL` | harness `69`, safety `70` | none | `1`, `0` | off -> on | PASS |

No observation was discarded. The additional approval interaction was
explicitly human-authorized solely to verify the documented compatibility
repair; it is not a frozen Step 10 repetition.

## Original approval attempt — retained failure

Before the first manual decision, harness execution `64` and HITL child `66`
were both physically `waiting`, with `waitTill` set to n8n's indefinite value.
Request `hitl-66` held the valid `requires_approval: true` action, released
`null`, had zero endpoint nodes, and left the simulated fan `off`.

The controlled human reviewer manually selected `approve`. Child execution
`66` then recorded:

- `human_decision: approve`;
- `held_action_unchanged: true`;
- the correct unchanged released action with `requires_approval: true`;
- request `2026-08-22T18:24:56.471Z`;
- decision `2026-08-22T18:28:16.577Z`;
- child completion `2026-08-22T18:28:16.671Z`;
- 510 ms pre-wait automation;
- 200,106 ms human wait;
- 94 ms post-decision automation;
- 200,710 ms total HITL-flow elapsed time (its start timestamp originated in
  the harness before the child was invoked).

However, the synchronous parent Execute Sub-workflow node resumed with its
original pre-wait safety input rather than the child's completed output. The
parent's approval check therefore failed and terminated fail-closed at
`2026-08-22T18:28:16.834Z`. Neither action endpoint executed and the fan
remained `off`. This is retained as an implementation failure, not rewritten
as a successful approval case.

## Compatibility repair

Inspection of the installed n8n execution data showed the child result was
correct but unavailable at the resumed parent output in this Wait/subworkflow
combination. The repair embedded the same native gate nodes directly into the
caller workflows, avoiding only the failing propagation seam:

- `safety_layer/hitl/workflows/step-09-hitl-harness.json`;
- `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`.

The validator, policy, policy-context transformation, form, decision values,
held-action snapshot, timing rules, and endpoint authorization conditions did
not change.

## Approval repair verification

Execution `71`, request `hitl-71`, was directly observed in status `waiting`
before the human decision. Its trace ended at `Wait for human decision`; no
endpoint node existed in the trace, `released_action` was `null`, and `/status`
reported simulated fan `off`.

The controlled human reviewer manually selected `approve`. The resumed caller
recorded:

- `human_decision: approve` and `hitl_status: approved`;
- `held_action_unchanged: true`;
- no unexpected form fields;
- released action exactly equal to the held action;
- released `requires_approval: true`;
- exactly one `POST approved fan on` and no fan-off endpoint;
- inherited response `status: ok`, `action: fan_on`, `fan: on`,
  `simulated: true`;
- final terminal `YACOUB_ACTION_ENDPOINT_POST_FAN_ON`;
- successful execution and simulated fan off -> on.

Timing:

| Boundary | Timestamp / duration |
| --- | --- |
| Flow start | `2026-08-22T18:44:20.730Z` |
| Approval requested | `2026-08-22T18:44:21.228Z` |
| Human decision | `2026-08-22T18:46:05.529Z` |
| Completion | `2026-08-22T18:46:05.771Z` |
| Pre-wait automation | 498 ms |
| Human wait | 104,301 ms |
| Post-decision automation | 242 ms |
| Total | 105,041 ms |

## Denial readiness

After an explicit setup reset to `off`, execution `73`, request `hitl-73`, was
directly observed in status `waiting`. It held the valid approval-required
action, released `null`, contained no endpoint node, and the fan remained
`off`.

The controlled human reviewer manually selected `deny`. The completed
execution recorded:

- `human_decision: deny` and `hitl_status: denied`;
- `held_action_unchanged: true`;
- `released_action: null`;
- terminal `OBID_HITL_DENIED`;
- endpoint counts `0`, `0`;
- simulated fan off -> off.

Timing:

| Boundary | Timestamp / duration |
| --- | --- |
| Flow start | `2026-08-22T18:46:37.904Z` |
| Approval requested | `2026-08-22T18:46:38.229Z` |
| Human decision | `2026-08-22T18:47:21.261Z` |
| Completion | `2026-08-22T18:47:21.366Z` |
| Pre-wait automation | 325 ms |
| Human wait | 43,032 ms |
| Post-decision automation | 105 ms |
| Total | 43,462 ms |

## Regression observations

Execution `67` injected the frozen `fan_reverse` candidate with the exact HITL
context present. Safety execution `68` returned `UNKNOWN_ACTION`, did not run
policy or policy-context transformation, created no HITL request, ran no Wait,
called no endpoint, and left the fan `off`.

Execution `69` supplied one normal valid `fan_on` action with no policy context.
Safety execution `70` returned direct `allow`; no Wait or HITL node ran, exactly
one `/fan/on` call occurred, and the inherited simulated state became `on`.
This proves Step 9 did not require approval for all valid actions.

The optional no-action runtime regression was not run. Static comparison shows
CONFIG-OBID v3 retains the frozen Step 7 no-action branch and cognitive nodes;
avoiding an extra model run kept the readiness set bounded.

The controlled runtime observations used the dedicated harness at the frozen
`OBID_POLICY_INPUT` injection point. CONFIG-OBID v3 itself remained inactive
and was not sent through Gemini in Step 9. Its Step 7 cognitive nodes and
no-action branch were checked statically, and its embedded HITL gate is an
exact copy of the gate exercised by the repaired harness.

## Provenance and boundaries

Yacoub's frozen `safety_layer/approvals/hitl-v1.md` at commit
`278318340bfa4e4650a97a2baba73f63bd868ed9` is
`YACOUB_INHERITED` / `REFERENCE_ONLY` and specification-level only. The exact
frozen Git-blob SHA-256 is
`c264abd8e2507fe0bc17a34a22af0636fb7207158dd9e3bbc088990b6b21d829`.
The inherited middleware supplied only simulated `/fan/on`, `/fan/off`, and
`/status` behavior. Obid created the executable wait/form, context handling,
decision processing, integrity check, routing gate, timing, and evidence.

No transient form URL, resume identifier beyond non-secret execution/request
IDs, reviewer identity, credential, cookie, account information, or Gemini key
is stored. No validator agent, second model, broad risk engine, Step 10
repetition, reliability percentage, or latency comparison was produced. The
readiness harness was disabled after verification.
