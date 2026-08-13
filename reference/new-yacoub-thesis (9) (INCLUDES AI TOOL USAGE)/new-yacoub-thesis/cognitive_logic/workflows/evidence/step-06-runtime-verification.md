# Step 06 Runtime Verification - Deterministic Baseline

This note records the local runtime verification for the Step 6 deterministic
baseline workflow.

## Test environment

- n8n ran locally through Docker at `http://localhost:5678`.
- Middleware ran locally with `python -m middleware.api.app`.
- Dockerized n8n reached the middleware through `http://host.docker.internal:8000`.
- The workflow was tested through the n8n test webhook:
  `http://localhost:5678/webhook-test/deterministic-baseline`.

## High-temperature test

Input:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:00:00Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

Expected deterministic result:

- The `value >= 30.0` condition is true.
- The workflow follows the `fan_on` branch.
- The HTTP Request node calls `POST http://host.docker.internal:8000/fan/on`.

Observed middleware response:

```json
{
  "status": "ok",
  "action": "fan_on",
  "fan": "on",
  "simulated": true,
  "reason": "manual_api_call"
}
```

Evidence files:

- `step-06-high-temp-webhook-input.png`
- `step-06-high-temp-if-condition.png`
- `step-06-high-temp-fan-on-output.png`
- `high-temp_terminal.txt`

## Low-temperature test

Input:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:05:00Z",
  "type": "temperature",
  "value": 24.5,
  "unit": "C"
}
```

Expected deterministic result:

- The `value >= 30.0` condition is false.
- The workflow follows the `fan_off` branch.
- The HTTP Request node calls `POST http://host.docker.internal:8000/fan/off`.

Observed middleware response:

```json
{
  "status": "ok",
  "action": "fan_off",
  "fan": "off",
  "simulated": true,
  "reason": "manual_api_call"
}
```

Evidence files:

- `step-06-low-temp-webhook.png`
- `step-06-low-temp-fan-off-canva.png`
- `step-06-low-temp-fan-off-output.png`
- `low-temo_terminal.txt`

## Verification conclusion

The deterministic baseline workflow was verified locally for both required
branches:

- `31.4 C -> fan_on`
- `24.5 C -> fan_off`

This completes the Step 6 runtime evidence needed before the Step 7
agent-enhanced workflow begins.
