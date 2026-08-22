# Step 9 HITL Configuration Manifest

**Configuration:** `CONFIG-OBID` v3 HITL  
**Runtime:** n8n `1.123.37`, container `obid-n8n`  
**Provenance:** runtime mechanism `OBID_CREATED`; action contract
`SHARED_INTERFACE`; Yacoub design and middleware semantics
`YACOUB_INHERITED` / `REFERENCE_ONLY`

## Portable workflow identities

| Role | Name / ID | Path | SHA-256 | Final state |
| --- | --- | --- | --- | --- |
| Integrated configuration | `CONFIG-OBID - Single Agent v3 HITL` / `obid-agent-v3-hitl` | `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json` | `1a09ee5a3199289c39845f9b97a3a3f516f277924d6a8fcb52da52780b0eaf78` | inactive, sanitized |
| Safety component | `Step 9 - Runtime safety v2 HITL` / `runtime-safety-v2-hitl` | `safety_layer/workflows/runtime-safety-v2-hitl.json` | `8dbf1826f43cdea34d510ff53e90fed52e45c93d5ed29956cf3a6dbfd6de652d` | inactive, sanitized |
| Final readiness harness | `Step 9 - HITL readiness harness` / `step-09-hitl-harness` | `safety_layer/hitl/workflows/step-09-hitl-harness.json` | `090715a02ed15ce0a385788fad8f25abceec7cd473422f63c9114909d850eaac` | inactive, sanitized |
| Retained first-attempt gate | `Step 9 - Runtime HITL gate v1` / `runtime-hitl-v1` | `safety_layer/hitl/workflows/runtime-hitl-v1.json` | `fd9ce59e033c6074d6688d9eb0037dff7afc3d882a74fea0743901dfa041d902` | inactive, sanitized; retained compatibility-failure artifact |

The live harness was deactivated after readiness verification. CONFIG-OBID v3
is stored inactive and credential-sanitized; the Step 7 Gemini node settings,
prompt, tools, memory, and iteration limit are unchanged.

## Actual human mechanism

- Node: `n8n-nodes-base.wait`, type version `1.1`.
- Mode: `resume: form`, indefinite wait, local controlled interaction.
- Final placement: directly embedded in the harness and CONFIG-OBID v3 because
  the pinned runtime did not propagate a completed child-Wait result to its
  synchronous parent.
- Request ID: `hitl-<current caller execution ID>`.
- Decision values: `approve`, `deny`.
- Human input: decision only; the action is read-only display data.
- Stored action: persisted pre-Wait output plus four-field snapshot.
- Transient form URL: presented to the reviewer but not stored in artifacts.
- Single use: native n8n waiting-form completion behavior.

## Controlled policy context

Only this exact internal object is recognized:

```json
{
  "policy_case_id": "POLICY-HITL-REQUIRED",
  "approval_required": true,
  "shared_contract_field": false
}
```

It is evaluated only after the original candidate passes the unchanged Step 8
validator. It copies the action and changes only `requires_approval` from
`false` to `true`; `action_id`, `target`, and `reason` remain unchanged. An
absent context preserves Step 8 behavior. Any other supplied context fails
closed. The context never enters the shared action object or schema.

## Safety v1 to v2 delta

The Step 9 safety workflow derives from the frozen
`safety_layer/workflows/runtime-safety-v1.json` snapshot. Its action parser and
schema-validation Code parameters are identical. Step 9 inserts the exact
policy-context handler only after successful validation and before policy,
then makes the existing deterministic policy read the resulting
`policy_action`. With no context, the allow/block/approval decision and held
or released action semantics remain those of v1. Invalid input still blocks
before context handling; its terminal now also records that context was not
evaluated. The approval terminal drops the obsolete `PENDING_STEP9` wording
because the caller now implements the real wait.

## Pending, approval, and denial behavior

- Pending: status `waiting`, held action present, released action `null`, no
  endpoint.
- Approval: exact stored action released unchanged and routed by the caller;
  `requires_approval` remains `true`.
- Denial: held action retained as evidence, released action `null`, terminal
  `OBID_HITL_DENIED`, no endpoint.
- Invalid action: validator block before policy context and before HITL.
- Normal valid action without context: direct ALLOW path, no human gate.

## Timing and readiness identities

The four timestamps are `hitl_flow_started_at`, `approval_requested_at`,
`approval_decided_at`, and `hitl_completed_at`. Derived timing keeps human wait
separate from automated processing.

Actual bounded execution identities:

- original fail-closed approval attempt: harness `64`, safety `65`, HITL child
  `66`;
- repaired approval verification: harness `71`, safety `72`;
- denial: harness `73`, safety `74`;
- invalid-action regression: harness `67`, safety `68`;
- normal-allow regression: harness `69`, safety `70`.

No validator agent, second agent, second model, risk engine, Step 10 repetition,
or repeated evaluation was implemented.
