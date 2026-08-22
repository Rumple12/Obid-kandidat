# Runtime Action Policy v1

**Step:** 8; **status:** implemented and one-off verified; **provenance:** `OBID_CREATED`

## Purpose and provenance

Yacoub's frozen `safety_layer/policies/action-policy-v1.md` is a `YACOUB_INHERITED` specification that explicitly did not prove runtime enforcement. Obid Step 8 implements the executable `Apply deterministic action policy` Code node (`n8n-nodes-base.code`, type version 2) in [`runtime-safety-v1.json`](../workflows/runtime-safety-v1.json).

The inherited action/target meanings and endpoint mappings remain the `SHARED_INTERFACE`; the runtime policy and its internal metadata are Obid-created.

## Stage separation

The policy node is downstream of an explicit `schema_valid == true` branch. Invalid candidates terminate before this node, with `policy_executed: false`. The policy receives the unchanged schema-valid action and applies a deliberately redundant deterministic allowlist.

| Condition | Decision | Reason code | Released action | Held action | Endpoint eligibility |
| --- | --- | --- | --- | --- | --- |
| Schema invalid | `block` before policy execution | `BLOCK_INVALID_ACTION` | `null` | `null` | None |
| Action or target fails the policy allowlist | `block` | `BLOCK_POLICY_ALLOWLIST_MISMATCH` | `null` | `null` | None |
| Valid action with `requires_approval: true` | `approval_required` | `VALID_ACTION_REQUIRES_APPROVAL` | `null` | Unchanged valid action | None in Step 8 |
| Valid allowed action with `requires_approval: false` | `allow` | `ALLOW_VALID_DIRECT_ACTION` | Unchanged valid action | `null` | Deterministic mapped endpoint |

The schema normally makes the second row unreachable, but the separate allowlist is retained as defense in depth and as an independently observable policy decision.

## Runtime outcome fields

```json
{
  "policy_executed": true,
  "policy_decision": "allow",
  "policy_reason_code": "ALLOW_VALID_DIRECT_ACTION",
  "released_action": {
    "action_id": "fan_on",
    "target": "fan_1",
    "reason": "temperature_at_or_above_threshold",
    "requires_approval": false
  },
  "held_action": null,
  "terminal_stage": "OBID_RUNTIME_POLICY_ALLOW"
}
```

These fields are internal Obid metadata. They do not extend or replace the shared action schema.

## Endpoint-release invariant

An action is released only when both conditions are true:

```text
schema_valid == true
AND
policy_decision == allow
```

Routing remains frozen and deterministic:

- `fan_on` -> `POST /fan/on`
- `fan_off` -> `POST /fan/off`

Parse errors, schema failures, policy blocks, approval-required outcomes, and internal no-ops execute zero action endpoints.

## Step 8 approval boundary

Step 8 recognizes a schema-valid action already carrying `requires_approval: true`, preserves it as `held_action`, and terminates at `OBID_APPROVAL_REQUIRED_PENDING_STEP9`. It does not transform a false flag, classify risk, ask a human, persist a decision, approve, deny, wait, or release after approval. Actual HITL remains Step 9.

Unknown actions and targets are invalid and blocked. Human approval can never rescue an action outside the frozen contract.
