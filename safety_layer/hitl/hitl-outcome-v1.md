# HITL Outcome v1

These fields are `OBID_CREATED` internal runtime metadata. They are not part of
the frozen shared action schema.

| Outcome | Decision | Released action | Terminal stage | Endpoint permission |
| --- | --- | --- | --- | --- |
| Pending | `null` | `null` | `OBID_HITL_PENDING` | none |
| Approved | `approve` | exact stored held action | `OBID_HITL_APPROVED`, followed by inherited endpoint terminal | only after integrity check |
| Denied | `deny` | `null` | `OBID_HITL_DENIED` | none |
| Invalid decision / submission / integrity | `approve`, `deny`, or `null` as observed | `null` | `OBID_HITL_INVALID_DECISION` | none |
| Invalid precondition | `null` | `null` | `OBID_HITL_PRECONDITION` | none |

Stable metadata includes:

```json
{
  "hitl_request_id": "hitl-<execution-id>",
  "hitl_status": "pending | approved | denied | invalid_decision | blocked_precondition",
  "human_decision": "approve | deny | null",
  "held_action": {},
  "held_action_unchanged": true,
  "released_action": {},
  "approval_requested_at": "<ISO-8601>",
  "approval_decided_at": "<ISO-8601>",
  "hitl_completed_at": "<ISO-8601>"
}
```

For denial and every fail-closed outcome, `released_action` is `null`. For
approval it equals the held action field-for-field and still carries
`requires_approval: true`.

The endpoint-release invariant is:

```text
direct path:
schema_valid AND policy_decision == allow

HITL path:
schema_valid
AND policy_decision == approval_required
AND human_decision == approve
AND held_action_unchanged

all other states:
NO endpoint
```
