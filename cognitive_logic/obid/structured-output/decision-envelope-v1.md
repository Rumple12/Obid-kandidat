# Internal decision envelope v1

The following `OBID_CREATED` envelope exists only inside CONFIG-OBID before the
shared action boundary.

State change:

```json
{
  "decision": "emit_action",
  "action": {
    "action_id": "fan_on",
    "target": "fan_1",
    "reason": "temperature_at_or_above_threshold",
    "requires_approval": false
  },
  "state_before": "off",
  "state_after": "on",
  "reason_code": "state_change_required"
}
```

State-aware suppression:

```json
{
  "decision": "no_action",
  "action": null,
  "state_before": "on",
  "state_after": "on",
  "reason_code": "desired_state_already_satisfied"
}
```

The envelope is not a shared protocol. When `action` is non-null, the nested
candidate retains exactly the `SHARED_INTERFACE` fields `action_id`, `target`,
`reason`, and `requires_approval`. `no_action` is never added to the shared
action schema; absence of a shared action is represented by `action: null`.

Step 7 performs only tolerant JSON-object extraction and `JSON.parse` before
minimal routing. It does not validate this envelope or the nested action against
JSON Schema, enforce an action policy, or implement approval/HITL.
