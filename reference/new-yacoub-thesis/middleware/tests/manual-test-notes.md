# Middleware Manual Test Notes

These notes cover the Step 4 middleware skeleton only.

Scope limits:

- mock sensor data only
- simulated fan action only
- no real GPIO
- shared JSON schemas are defined in Step 5 but are not enforced by this Step 4 middleware yet
- no deterministic n8n workflow yet
- no agent workflow yet
- no safety layer yet

## Local run

From the repository root:

```powershell
python -m middleware.api.app
```

Default URL:

```text
http://127.0.0.1:8000
```

Optional environment variables:

```powershell
$env:MIDDLEWARE_HOST = "127.0.0.1"
$env:MIDDLEWARE_PORT = "8000"
$env:N8N_WEBHOOK_URL = ""
python -m middleware.api.app
```

`N8N_WEBHOOK_URL` is intentionally optional. It should stay empty until the
Step 6 n8n workflow exists.

Step 5 defines the shared JSON schema files under `shared_interfaces/`, but
these manual tests still exercise the Step 4 middleware behavior. The
middleware does not perform JSON Schema validation at runtime yet.

## Endpoint summary

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/status` | `GET` | Confirm middleware is running and inspect simulated state |
| `/sensor-event` | `POST` | Receive a mock temperature event and optionally forward to n8n |
| `/fan/on` | `POST` | Simulate turning the fan on |
| `/fan/off` | `POST` | Simulate turning the fan off |

## PowerShell tests

### GET /status

```powershell
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/status"
```

Expected shape:

```json
{
  "status": "ok",
  "message": "middleware running",
  "state": {
    "fan": "off",
    "last_sensor_event": null,
    "hardware": "simulated"
  }
}
```

### POST /sensor-event

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
  -Uri "http://127.0.0.1:8000/sensor-event" `
  -ContentType "application/json" `
  -Body $body
```

Expected shape while `N8N_WEBHOOK_URL` is empty:

```json
{
  "status": "accepted",
  "message": "sensor event received by middleware",
  "event": {
    "sensor_id": "temp_sensor_1",
    "timestamp": "2026-04-25T20:00:00Z",
    "type": "temperature",
    "value": 31.4,
    "unit": "C"
  },
  "n8n": {
    "status": "skipped",
    "reason": "N8N_WEBHOOK_URL is not configured; n8n workflow wiring is pending Step 6."
  }
}
```

### POST /fan/on

```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/fan/on"
```

Expected shape:

```json
{
  "status": "ok",
  "action": "fan_on",
  "fan": "on",
  "simulated": true,
  "reason": "manual_api_call"
}
```

### POST /fan/off

```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/fan/off"
```

Expected shape:

```json
{
  "status": "ok",
  "action": "fan_off",
  "fan": "off",
  "simulated": true,
  "reason": "manual_api_call"
}
```

### Malformed sensor event check

```powershell
$badBody = @{ sensor_id = "temp_sensor_1" } | ConvertTo-Json

Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8000/sensor-event" `
  -ContentType "application/json" `
  -Body $badBody
```

Expected result:

```json
{
  "error": "missing_required_field",
  "missing": ["timestamp", "type", "value", "unit"],
  "message": "Step 4 uses a minimal inline check; JSON schemas come in Step 5."
}
```

## curl tests

```bash
curl http://127.0.0.1:8000/status
curl -X POST http://127.0.0.1:8000/fan/on
curl -X POST http://127.0.0.1:8000/fan/off
curl -X POST http://127.0.0.1:8000/sensor-event \
  -H "Content-Type: application/json" \
  -d '{"sensor_id":"temp_sensor_1","timestamp":"2026-04-25T20:00:00Z","type":"temperature","value":31.4,"unit":"C"}'
```

## Evidence to save

For Chapter 3 methodology:

- terminal command used to start the middleware
- manual test commands used
- short note that PC-first mock sensor data was used before hardware

For Chapter 5 implementation:

- successful `/status` response
- successful `/sensor-event` response showing n8n forwarding skipped until Step 6
- successful `/fan/on` and `/fan/off` simulated action responses
- one malformed sensor-event response showing minimal Step 4 validation behavior
