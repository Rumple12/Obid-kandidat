# Deterministic Baseline Workflow

This document describes the Step 6 deterministic non-AI baseline workflow for
the new-yacoub thesis repository.

Runtime verification completed locally in n8n. Evidence is stored in cognitive_logic/workflows/evidence/.


The companion JSON file,
`cognitive_logic/workflows/deterministic-baseline.json`, is a valid JSON
draft/export-candidate for n8n. It must be imported and checked in the n8n UI
before it is treated as the final workflow export.

## Purpose

The deterministic baseline gives the thesis a controlled comparison anchor for
the later agent-enhanced workflow.

This workflow does not use:

- AI agent nodes
- prompts
- memory
- safety approval logic
- real GPIO
- Raspberry Pi deployment

It is intentionally simple: receive one temperature event, apply one fixed
threshold rule, and call one simulated middleware fan endpoint.

## Threshold Rule

The baseline rule is:

```text
if temperature >= 30.0 C:
    request fan_on
else:
    request fan_off
```

The workflow reads the temperature from the Webhook node's parsed JSON body:

```text
$json.body.value
```

## Expected Input Shape

The input shape follows
`shared_interfaces/json-schema/sensor-event.schema.json`.

Example:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:00:00Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

Required fields:

- `sensor_id`
- `timestamp`
- `type`
- `value`
- `unit`

For Step 6, the workflow assumes the event has already arrived in this shape.
It does not implement safety-layer validation.

## Expected Action Outputs

The intended action output shape follows
`shared_interfaces/json-schema/agent-action.schema.json`.

High-temperature output:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_at_or_above_threshold",
  "requires_approval": false
}
```

Low-temperature output:

```json
{
  "action_id": "fan_off",
  "target": "fan_1",
  "reason": "temperature_below_threshold",
  "requires_approval": false
}
```

Allowed actions:

- `fan_on`
- `fan_off`

Allowed target:

- `fan_1`

## Middleware Endpoints Called

Middleware assumption from the Windows host:

```text
http://127.0.0.1:8000
```

Middleware URL from inside the Dockerized n8n container:

```text
http://host.docker.internal:8000
```

The workflow calls:

- `POST http://host.docker.internal:8000/fan/on` when `$json.body.value >= 30.0`
- `POST http://host.docker.internal:8000/fan/off` when `$json.body.value < 30.0`

These endpoints are simulated by the Step 4 middleware. No real hardware is
used. If n8n is later run directly on the host instead of Docker, the HTTP
Request URLs can be changed back to `http://127.0.0.1:8000/...`.

## Workflow Shape

Expected n8n node path:

```text
Webhook
  -> IF body.value >= 30.0
    -> Set fan_on action
    -> HTTP Request POST /fan/on
    -> middleware response is visible in execution data
  -> else
    -> Set fan_off action
    -> HTTP Request POST /fan/off
    -> middleware response is visible in execution data
```

The result path is documented through the n8n execution view:

- IF node branch selected
- action Set node output
- HTTP Request node response from middleware
- middleware terminal log showing `/fan/on` or `/fan/off`

## Manual Import

1. Start the Step 3 local n8n baseline.
2. Start the Step 4 middleware:

```powershell
python -m middleware.api.app
```

3. Open n8n at:

```text
http://localhost:5678
```

4. Import:

```text
cognitive_logic/workflows/deterministic-baseline.json
```

5. Inspect the imported nodes before treating the JSON as final:

- Webhook node path is `deterministic-baseline`
- IF node compares `={{ $json.body.value }}` with `30` using greater-than-or-equal
- true branch leads to `POST http://host.docker.internal:8000/fan/on`
- false branch leads to `POST http://host.docker.internal:8000/fan/off`
- no AI, prompt, memory, or safety approval node exists

If n8n changes or rejects any node parameter during import, recreate the same
logic manually in the UI and export the verified workflow back to this file.

## Manual Test

After importing the workflow, use the n8n test webhook URL shown by the Webhook
node.

High-temperature test payload:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:00:00Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

Expected result:

- IF true branch is selected
- action is `fan_on`
- middleware receives `POST /fan/on`
- middleware response says `fan: on`

Low-temperature test payload:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:05:00Z",
  "type": "temperature",
  "value": 24.5,
  "unit": "C"
}
```

Expected result:

- IF false branch is selected
- action is `fan_off`
- middleware receives `POST /fan/off`
- middleware response says `fan: off`

PowerShell example, replacing `<test-webhook-url>` with the n8n test URL:

```powershell
$body = @{
  sensor_id = "temp_sensor_1"
  timestamp = "2026-04-25T20:00:00Z"
  type = "temperature"
  value = 31.4
  unit = "C"
} | ConvertTo-Json

Invoke-RestMethod `
  -Method Post `
  -Uri "<test-webhook-url>" `
  -ContentType "application/json" `
  -Body $body
```

## Evidence To Save

Save these after n8n import and manual testing:

- screenshot of the full workflow canvas
- screenshot of the IF node threshold configuration
- screenshot or export showing the HTTP Request nodes
- n8n execution log for one high-temperature run
- n8n execution log for one low-temperature run
- middleware terminal log showing `/fan/on` and `/fan/off`
- final verified n8n export JSON after UI import/re-export

Do not claim runtime verification until those tests have actually run.

## Report Usage

Chapter 4:

- explains why a deterministic baseline is needed before the agent-enhanced path
- supports the baseline-vs-agent comparison design
- shows the non-AI alternative against which later workflow intelligence is compared

Chapter 5:

- documents the concrete n8n workflow implementation
- documents the threshold rule and middleware endpoints
- records that action execution is still simulated through middleware

Chapter 6:

- provides the baseline result path for later latency/resource comparison
- supplies the expected `fan_on` and `fan_off` outcomes for deterministic runs
- becomes the anchor for comparing Step 7 agent-enhanced behavior later
