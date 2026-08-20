# Step 4 Integration Verification Evidence

**Execution date:** 2026-08-20

**Execution window:** approximately 15:22-15:28 CEST (`UTC+02:00`)

**Evidence provenance:** `OBID_CREATED`

**Collaborator runtime provenance:** `YACOUB_INHERITED`, executed unmodified from `Rumple12/new-yacoub-thesis` at frozen commit `278318340bfa4e4650a97a2baba73f63bd868ed9`

**Frozen-source inspection provenance:** `REFERENCE_ONLY`

## Scope and result

The actual frozen Yacoub middleware and one non-agent Obid n8n workflow were used to verify both shared integration directions. No schema was adopted, no baseline was imported, no agent decision was made, and no evaluation run was performed.

| Check | Status | Observation |
| --- | --- | --- |
| Actual Yacoub middleware | `VERIFIED` | Ran unmodified from a clean detached temporary checkout at the exact frozen commit. |
| Middleware `/status` | `PASS` | HTTP 200 from the host and from inside `obid-n8n`; response exposed inherited simulated state. |
| Compatible inbound event | `PASS` | Yacoub `/sensor-event` returned 202, forwarding status `sent`, and n8n status 200. |
| n8n inbound observation | `PASS` | Successful n8n execution 1 recorded the exact five event values at both inbound nodes. |
| n8n -> `/fan/on` | `PASS` | Successful n8n execution 2 returned inherited simulated `fan_on`; `/status` showed `on`. |
| n8n -> `/fan/off` | `PASS` | Successful n8n execution 3 returned inherited simulated `fan_off`; `/status` showed final state `off`. |
| `{}` characterization | `PASS` | Yacoub generated and forwarded its default `31.4 C` event; n8n execution 4 succeeded. |
| Zero-length characterization | `PASS` | Yacoub generated and forwarded its default `31.4 C` event; n8n execution 5 succeeded. |
| Test double | `NOT APPLICABLE` | No test double, stub, adapter, or competing middleware was created. |

## Runtime identities

### Obid n8n

| Item | Observed value |
| --- | --- |
| Container | `obid-n8n` |
| Runtime version | `1.123.37` from the running CLI before and after workflow installation |
| Host/container port | `5678 -> 5678/tcp` |
| Workflow name | `Step 4 - Yacoub compatibility boundary` |
| Workflow ID | `step4-yacoub-compat` |
| Mode | active production webhook mode |
| Inbound path | `obid-yacoub-compat` |
| Exact inbound URL | `http://127.0.0.1:5678/webhook/obid-yacoub-compat` |
| fan-on trigger path | `obid-yacoub-compat-fan-on` |
| fan-off trigger path | `obid-yacoub-compat-fan-off` |
| Nodes | three Webhook nodes, one Set node, two HTTP Request nodes |
| Credentials | none |

The Set node copies the five received fields into a boundary receipt. It performs no schema validation, safety classification, threshold decision, or agent action selection.

### Actual Yacoub middleware

| Item | Observed value |
| --- | --- |
| Frozen commit | `278318340bfa4e4650a97a2baba73f63bd868ed9` |
| Runtime checkout | `C:\Users\Jake_\AppData\Local\Temp\obid-step4-yacoub-78fabb31bf5f4ae6820746aa0093d8a3` |
| Checkout state | clean, detached, exact frozen commit |
| Python | `3.13.14`; middleware uses only the Python standard library |
| Source startup | `python -m middleware.api.app` from repository root |
| Actual startup | `python -u -m middleware.api.app` |
| Source bind default | `127.0.0.1:8000` |
| Actual runtime bind | `MIDDLEWARE_HOST=0.0.0.0`, `MIDDLEWARE_PORT=8000` |
| Host test URL | `http://127.0.0.1:8000` |
| Container action URL | `http://host.docker.internal:8000` |
| Exact `N8N_WEBHOOK_URL` | `http://127.0.0.1:5678/webhook/obid-yacoub-compat` |

The runtime host override was required so Dockerized n8n could reach the host process. It changes only bind reachability, not route or payload semantics. The process was stopped after testing; the temporary checkout remained clean and port 8000 was no longer listening.

## Frozen source inspected

Exact source contents were read at the commit, not inferred from the dirty sibling working tree:

- `middleware/api/app.py`
- `middleware/api/routes.py`
- `middleware/webhooks/n8n_sender.py`
- `middleware/gpio/mock_sensor.py`
- `middleware/tests/manual-test-notes.md`
- `middleware/tests/evidence/step-04-middleware-smoke-test-2026-04-25.txt`

Relevant inherited behavior confirmed from source:

- `N8N_WEBHOOK_URL` is stripped; if present, normalized event JSON is POSTed with a five-second timeout.
- `/sensor-event` returns 202 after normalization even when its nested forwarding result is `skipped` or `error`; the nested `n8n` object carries forwarding status.
- invalid JSON/non-object input is 400, but an absent/zero-length body becomes `{}`.
- `{}` becomes a generated five-field `temp_sensor_1`, `31.4 C` event.
- the inline checks are partial and are not JSON Schema enforcement.
- `/fan/on` and `/fan/off` mutate in-memory simulated state and return `reason: manual_api_call`.

## Workflow installation and mode verification

Before import, `n8n list:workflow` returned no workflow. The candidate definition was created outside the active repository and checked to contain only Webhook, Set, and HTTP Request nodes.

The verified lifecycle was:

1. stop `obid-n8n` without deleting its named volume;
2. run `n8n import:workflow` in a one-off Compose container using a read-only bind of the candidate;
3. run `n8n update:workflow --id=step4-yacoub-compat --active=true` in a second one-off container;
4. list the active workflow, which returned `step4-yacoub-compat|Step 4 - Yacoub compatibility boundary`;
5. restart `obid-n8n` and confirm HTTP 200 and runtime version `1.123.37`;
6. invoke the `/webhook/` production URLs successfully.

The `/webhook-test/` mode was not used. The repository JSON was created only after successful runtime execution and omits local ownership metadata. A read-only comparison with the live `workflow_entity` record then confirmed matching ID, name, active/version identity, nodes, connections, and settings.

## `S4-STATUS-01` - actual status and reachability

Host request:

```text
GET http://127.0.0.1:8000/status -> 200
```

Container-side request:

```text
GET http://host.docker.internal:8000/status -> 200
```

Both returned the inherited shape:

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

This proves runtime reachability and state observability only; it is not validation evidence.

## `S4-IN-01` - compatible middleware-to-n8n event

One representative event was sent to the actual middleware:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-08-20T13:24:30Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

Observed middleware result:

- `POST http://127.0.0.1:8000/sensor-event -> 202`
- top-level status: `accepted`
- nested n8n status: `sent`
- nested n8n status code: `200`
- nested n8n response:

```json
{
  "boundary_status": "received",
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-08-20T13:24:30Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

n8n execution 1 finished successfully in `webhook` mode. Privacy-scoped read-only inspection of that execution recorded:

```text
Receive Yacoub sensor event.body == sent five-field event
Record inbound boundary == boundary_status received plus the same five values
```

All five sent/received values match. No decision or action node is connected to this inbound branch.

## `S4-OUT-01` - n8n to inherited fan-on boundary

Trigger:

```text
POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-on
```

The request created successful n8n execution 2. Its `POST actual Yacoub fan_on` node returned:

```json
{
  "status": "ok",
  "action": "fan_on",
  "fan": "on",
  "simulated": true,
  "reason": "manual_api_call"
}
```

The immediately following host `/status` observation returned HTTP 200 with `state.fan: on` and `state.hardware: simulated`.

## `S4-OUT-02` - n8n to inherited fan-off boundary

Trigger:

```text
POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-off
```

The request created successful n8n execution 3. Its `POST actual Yacoub fan_off` node returned:

```json
{
  "status": "ok",
  "action": "fan_off",
  "fan": "off",
  "simulated": true,
  "reason": "manual_api_call"
}
```

The immediately following `/status` observation returned HTTP 200 with `state.fan: off` and `state.hardware: simulated`. This is the final observed simulated fan state. The later sensor-input characterization did not call either action route.

## `S4-IN-02` - inherited empty/default behavior

Two source-supported, bounded observations were made. These characterize Yacoub behavior and are not Obid validation successes, malformed-case results, or RQ2 evidence.

| Input to Yacoub `/sensor-event` | Middleware status | Generated event | Forwarding | n8n execution |
| --- | --- | --- | --- | --- |
| `{}` | 202 | `temp_sensor_1`, `2026-08-20T13:25:51Z`, `temperature`, `31.4`, `C` | `sent`, n8n 200 | 4, `success` |
| zero-length body | 202 | `temp_sensor_1`, `2026-08-20T13:25:52Z`, `temperature`, `31.4`, `C` | `sent`, n8n 200 | 5, `success` |

In both executions, `Receive Yacoub sensor event.body` and `Record inbound boundary` contained the generated five-field event.

## n8n execution summary

Execution metadata was read directly from the local n8n SQLite database using a read-only connection restricted to workflow `step4-yacoub-compat`; no owner or credential table was queried.

| Execution | Mode | Status | Purpose | Started UTC | Stopped UTC |
| --- | --- | --- | --- | --- | --- |
| 1 | `webhook` | `success` | compatible inbound event | `2026-08-20 13:24:24.728` | `2026-08-20 13:24:24.793` |
| 2 | `webhook` | `success` | fan on | `2026-08-20 13:25:31.789` | `2026-08-20 13:25:31.854` |
| 3 | `webhook` | `success` | fan off | `2026-08-20 13:25:32.030` | `2026-08-20 13:25:32.051` |
| 4 | `webhook` | `success` | `{}` characterization | `2026-08-20 13:25:51.096` | `2026-08-20 13:25:51.113` |
| 5 | `webhook` | `success` | zero-length characterization | `2026-08-20 13:25:52.286` | `2026-08-20 13:25:52.316` |

## Failures, deviations, and privacy handling

- The existing sibling and nested Yacoub checkouts were at the frozen commit but globally dirty/pruned. They were not executed. A clean detached temporary clone outside Obid was used instead.
- A first background-process launch attempt was rejected by local command policy before any middleware process started. The exact middleware was then run successfully in a managed foreground terminal session.
- A first PowerShell comparison marked the timestamp unequal because `ConvertFrom-Json` materialized one ISO timestamp as a date object. The raw n8n response and read-only execution record both contained the exact string `2026-08-20T13:24:30Z`; this was an evidence-processing type-coercion artifact, not an integration mismatch.
- The raw n8n CLI export included local owner-project metadata. It was not used as the repository artifact; exact temporary host and container copies were removed. The committed-candidate workflow export excludes the `shared` ownership block and contains no identity or credential data.
- Middleware access logs showed localhost source addresses under Docker Desktop host forwarding. Origin from n8n is established by successful workflow executions 2 and 3 and their HTTP Request node results, not by the translated log source address.
- The managed middleware session was stopped with Ctrl+C after testing. The application logged `Stopping middleware.`; the terminal reported exit code 1 from the interrupt, port 8000 closed, and the checkout remained clean.

No contract, route, version, or payload deviation was required.

## Test-double and future-step boundary

No `TEST_DOUBLE`, local API substitute, adapter, middleware copy, or competing service exists in Obid.

Step 5 remains responsible for schema adoption, no-drift comparison, formal case definitions, injection points, expected outcomes, and malformed attribution. This Step 4 result must not be cited as strict validation, agent correctness, repeated reliability evidence, or production-safety evidence.
