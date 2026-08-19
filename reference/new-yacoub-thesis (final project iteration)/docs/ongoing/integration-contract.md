# Integration contract

This document defines the minimum contract boundary between the Yacoub runtime side and the minimum workflow/safety side in the **new-yacoub** thesis.

The purpose of this contract is to:

- keep middleware and workflow logic aligned
- prevent schema drift
- make the system reproducible
- support testing and evaluation
- ensure unsafe actions cannot bypass validation

## Contract boundary

The main contract boundary in this thesis is:

```text
Middleware <-> Shared Interfaces <-> Workflow / Safety logic
```

### Input side

Middleware creates or receives sensor events and represents them using a shared event schema.

### Output side

Workflow logic produces a proposed action using a shared action schema.

### Safety rule

No risky or malformed action may reach middleware execution without passing validation and, when needed, approval.

## Initial scenario

The first implementation is intentionally limited to one small end-to-end scenario:

```text
Temperature event
  -> Middleware receives or generates the event
  -> Middleware pushes the event to n8n
  -> Workflow decides whether fan action is needed
  -> Validation checks the action
  -> Approval is required if the action is risky or malformed
  -> Middleware executes /fan/on or /fan/off
```

## Input contract

Sensor events are represented in a shared JSON schema.

Concrete schema file:

- `shared_interfaces/json-schema/sensor-event.schema.json`

### Required fields

- `sensor_id`
- `timestamp`
- `type`
- `value`
- `unit`

### Sensor input example

Concrete example file:

- `shared_interfaces/examples/sensor-event.example.json`

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:00:00Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

### Input assumptions

- `sensor_id` uniquely identifies the event source
- `timestamp` uses ISO 8601 format
- `type` identifies the sensor/event kind
- `value` contains the measured reading
- `unit` identifies the measurement unit

## Output contract

Workflow decisions are represented in a shared JSON schema for actions.

Concrete schema file:

- `shared_interfaces/json-schema/agent-action.schema.json`

### Required fields

- `action_id`
- `target`
- `reason`
- `requires_approval`

### Allowed action example

Concrete example file:

- `shared_interfaces/examples/fan-on.example.json`

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_above_threshold",
  "requires_approval": false
}
```

### Output assumptions

- `action_id` identifies the requested action
- `target` identifies the intended device or actuator
- `reason` explains why the action was proposed
- `requires_approval` indicates whether execution may continue directly or must pause for approval

## Validation and approval rules

All workflow-produced actions must be checked before middleware execution.

Step 8 defines the minimum safety boundary in:

- `safety_layer/policies/action-policy-v1.md`
- `safety_layer/parsers/output-validation-v1.md`
- `safety_layer/approvals/hitl-v1.md`
- `safety_layer/examples/allowed-case.md`
- `safety_layer/examples/blocked-case.md`
- `safety_layer/examples/risky-approval-case.md`

These files document the intended validation and approval behavior. They do not
claim runtime enforcement unless later implementation and test evidence is
added.

### Approval is required when

- the action is not in the allowed action list
- the target device is unknown
- the output is malformed
- the action includes unexpected fields

### Blocked case example

Concrete example file:

- `shared_interfaces/examples/blocked-action.example.json`

The blocked example is intentionally **schema-invalid** and **policy-invalid**
for Step 5 because:

- `open_window` is outside the minimal allowed action set
- `unknown_device` is outside the minimal allowed target set

It is included as a future Step 8 safety-layer test case. Step 5 only defines
the contract artifact; it does not implement safety logic.

```json
{
  "action_id": "open_window",
  "target": "unknown_device",
  "reason": "hallucinated_action_outside_first_scenario",
  "requires_approval": true
}
```

### Expected handling of blocked/risky output

- malformed or unknown output must not execute directly
- risky output must be stopped or routed to approval
- middleware should only execute actions that passed validation

## First allowed action list

The first implementation supports only a very small action set.

### Initially allowed

- `fan_on`
- `fan_off`

### Initially allowed targets

- `fan_1`

### Not allowed in the first implementation

- unknown device actions
- actions outside the defined scenario
- multi-device actions
- free-form or hallucinated commands

## Error cases

The first implementation must be able to handle at least these error cases:

1. malformed sensor event
2. missing required input field
3. malformed action output
4. unknown target device
5. unsupported action id
6. unexpected fields in action payload

These error cases should be visible in evaluation and discussion later.

## Relationship to implementation

This contract must stay aligned with:

- `shared_interfaces/json-schema/`
- `shared_interfaces/examples/`
- `middleware/`
- `cognitive_logic/`
- `safety_layer/`
- `docs/architecture/`

If communication behavior changes, this file must be updated.

Step 5 defines these schema and example artifacts only. The Step 4 middleware
does not yet enforce JSON Schema validation at runtime; runtime validation and
safety behavior remain deferred to later steps.

## Scope note

This contract is intentionally minimal.

It is designed only to support:

- one scenario
- one sensor-event path
- one action path
- one validation layer
- one approval checkpoint

It is not intended to define a broad multi-device or multi-agent protocol at this stage.
