# Minimal Agent-Enhanced Workflow

This document describes the Step 7 minimum agent-enhanced workflow for the
new-yacoub thesis repository.

Runtime verification status: **completed for Step 7 runtime evidence**.

The Step 7 evidence includes both high-temperature `fan_on` and
low-temperature `fan_off` runs. In both cases, the parsed action matches the
shared contract and the middleware returns `status=ok` with simulated fan
execution.

The companion JSON file, `cognitive_logic/workflows/agent-minimal.json`, is a
valid JSON draft/export-candidate. The exact n8n AI/LangChain node structure
depends on the installed n8n version and configured model credential, so the AI
node must be verified inside the n8n UI before this is treated as a final
workflow export.

## Purpose

This workflow adds the smallest useful Obid-compatible decision layer to the
Yacoub runtime side.

It is not a broad cognitive architecture. It does not implement:

- multiple agents
- ReAct loops
- multiple prompts
- memory comparison
- model benchmarking
- MCP
- safety approval enforcement
- real GPIO

The purpose is to compare one deterministic baseline against one minimal
agent-enhanced path on the same temperature-to-fan scenario.

## Difference From Deterministic Baseline

The deterministic baseline applies this fixed rule directly in n8n:

```text
if temperature >= 30.0 C:
    fan_on
else:
    fan_off
```

The minimal agent workflow instead passes the current event into one LLM
decision step. The LLM is instructed to return only a structured action object
matching `shared_interfaces/json-schema/agent-action.schema.json`.

Both workflows call the same middleware endpoints:

- `POST http://host.docker.internal:8000/fan/on`
- `POST http://host.docker.internal:8000/fan/off`

## Expected Input Shape

Input follows `shared_interfaces/json-schema/sensor-event.schema.json`.

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

Inside n8n's Webhook node, this is expected to be available as:

```text
$json.body
```

The draft workflow passes this to the agent as:

```text
JSON.stringify($json.body)
```

## Expected Structured Output Shape

The agent must return only one JSON object:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_at_or_above_threshold",
  "requires_approval": false
}
```

Allowed `action_id` values:

- `fan_on`
- `fan_off`

Allowed `target`:

- `fan_1`

The workflow parses this structured action and routes only `fan_on` and
`fan_off` to middleware endpoints. If the output is outside the contract, the
draft workflow records an unrouted result. Formal validation and approval
belong to Step 8 and are not implemented here.

## Prompt Choice

Prompt file:

```text
cognitive_logic/prompts/system-prompt-v1.md
```

The prompt is intentionally strict:

- output JSON only
- use only `fan_on` or `fan_off`
- use only `fan_1`
- do not invent hardware instructions
- do not implement approval logic
- mention that Step 8 handles safety and approval enforcement later

## Memory Choice

Memory file:

```text
cognitive_logic/memory/memory-choice-v1.md
```

Chosen strategy:

```text
stateless execution / no memory
```

This keeps the workflow reproducible, resource-light, and directly comparable
with the deterministic baseline.

## Middleware Endpoints

Because n8n runs in Docker and middleware runs on the Windows host, the workflow
uses Docker Desktop's host alias:

- `http://host.docker.internal:8000/fan/on`
- `http://host.docker.internal:8000/fan/off`

The middleware remains simulated. No real GPIO is used.

## Expected Workflow Shape

```text
Webhook
  -> Prepare agent input
  -> Minimal LLM decision
  -> Parse structured action
  -> IF action_id == fan_on
       -> POST /fan/on
     ELSE IF action_id == fan_off
       -> POST /fan/off
     ELSE
       -> Unrouted non-contract action
```

The unrouted branch is not the Step 8 safety layer. It is a minimal routing
fallback in the draft workflow so an unexpected action is not accidentally
mapped to a fan endpoint during manual testing.

## Manual Import

1. Start the Step 3 local n8n baseline.
2. Start the Step 4 middleware:

```powershell
python -m middleware.api.app
```

3. Open n8n:

```text
http://localhost:5678
```

4. Import:

```text
cognitive_logic/workflows/agent-minimal.json
```

5. Inspect and repair the imported workflow before testing:

- Webhook path is `agent-minimal`
- the agent receives `JSON.stringify($json.body)` or equivalent event data
- the AI node uses exactly one configured model/provider credential
- the AI node uses `cognitive_logic/prompts/system-prompt-v1.md`
- no memory node is connected
- parse node reads the actual AI output field used by the n8n node
- action routing checks `action_id`
- fan-on URL is `http://host.docker.internal:8000/fan/on`
- fan-off URL is `http://host.docker.internal:8000/fan/off`
- no safety approval node exists yet

If n8n changes or rejects the AI node during import, recreate the same logic
manually in the UI and export the verified workflow back to
`agent-minimal.json`.

## Manual Test

Use the n8n test webhook URL shown by the Webhook node.

High-temperature payload:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:00:00Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

Expected structured action:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_at_or_above_threshold",
  "requires_approval": false
}
```

Expected middleware result:

- `POST /fan/on`
- response includes `fan: on`

Low-temperature payload:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:05:00Z",
  "type": "temperature",
  "value": 24.5,
  "unit": "C"
}
```

Expected structured action:

```json
{
  "action_id": "fan_off",
  "target": "fan_1",
  "reason": "temperature_below_threshold",
  "requires_approval": false
}
```

Expected middleware result:

- `POST /fan/off`
- response includes `fan: off`

PowerShell example, replacing `<test-webhook-url>` with the n8n test webhook:

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
- screenshot of the AI node prompt/model configuration
- screenshot showing no memory node is connected
- screenshot or log of the structured `fan_on` output
- screenshot or log of the structured `fan_off` output
- middleware terminal log showing `/fan/on` and `/fan/off`
- final verified n8n export JSON after UI import/re-export

Do not claim runtime verification until the workflow has actually been imported
and run in n8n.

## Report Usage

Chapter 4:

- supports the chosen approach of comparing deterministic and agent-enhanced
  behavior without model benchmarking
- explains why the Obid-compatible layer is minimized
- documents the decision to use no memory

Chapter 5:

- documents the minimal agent workflow implementation
- records the strict prompt and structured output boundary
- shows how the workflow still uses the same middleware endpoints as the
  deterministic baseline

Chapter 7:

- supports discussion of limitations and safety boundaries
- explains that Step 7 only asks for structured output
- explains that actual validation and human approval enforcement are deferred to
  Step 8
