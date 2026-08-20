# Step 4 Integration Test Plan

This is a bounded, single-run integration verification set. It is not the Step 5 evaluation dataset, does not define repeated trials, and does not test agent accuracy, runtime schema validation, policy, or safety.

Evidence for every row is recorded in `evidence/step-04-integration-verification.md`.

| ID | Purpose | Stimulus | Expected inherited/boundary behavior | Provenance | Pass criterion | Final status |
| --- | --- | --- | --- | --- | --- | --- |
| `S4-STATUS-01` | Verify actual middleware availability and simulated state shape | Host and container-side `GET /status` | HTTP 200 with `status`, `message`, and `state` containing `fan`, `last_sensor_event`, and `hardware: simulated` | Runtime behavior `YACOUB_INHERITED`; endpoint `SHARED_INTERFACE` | Both addressing directions reach the actual process and response matches source behavior | `PASS` |
| `S4-IN-01` | Verify middleware-to-n8n delivery of one compatible event | One five-field `31.4 C` temperature event sent to host `POST /sensor-event` | Middleware normalizes numeric value, returns 202, reports n8n `sent`/200, and n8n records the same five values | Middleware `YACOUB_INHERITED`; event semantics `SHARED_INTERFACE`; n8n receipt `OBID_CREATED` | Middleware and n8n execution evidence both contain matching values; no decision node runs | `PASS` |
| `S4-IN-02` | Characterize inherited empty-input behavior without treating it as Obid validation | One `{}` body and one zero-length body to `POST /sensor-event` | Each becomes Yacoub's generated `temp_sensor_1`, `31.4 C` event and is forwarded to n8n | Normalization `YACOUB_INHERITED`; observation `OBID_CREATED` | Each response is 202, forwarding is sent/200, and n8n records the generated event | `PASS` |
| `S4-OUT-01` | Verify n8n-to-middleware fan-on seam | POST the Obid n8n `obid-yacoub-compat-fan-on` production webhook | n8n HTTP Request calls actual `POST /fan/on`; response and `/status` show simulated fan `on` | Middleware/action `YACOUB_INHERITED` / `SHARED_INTERFACE`; trigger/evidence `OBID_CREATED` | Successful n8n execution, response action `fan_on`, simulated true, state `on` | `PASS` |
| `S4-OUT-02` | Verify n8n-to-middleware fan-off seam | POST the Obid n8n `obid-yacoub-compat-fan-off` production webhook | n8n HTTP Request calls actual `POST /fan/off`; response and `/status` show simulated fan `off` | Middleware/action `YACOUB_INHERITED` / `SHARED_INTERFACE`; trigger/evidence `OBID_CREATED` | Successful n8n execution, response action `fan_off`, simulated true, final state `off` | `PASS` |

## Representative compatible stimulus

The `S4-IN-01` body was a one-off integration stimulus:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-08-20T13:24:30Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

Its presence here does not adopt the Yacoub JSON Schema or freeze a future evaluation case.

