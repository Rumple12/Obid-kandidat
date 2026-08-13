# Step 04 - Middleware Skeleton

## What was built

- A minimal Python HTTP middleware skeleton was added under `middleware/`.
- The middleware can be started with `python -m middleware.api.app`.
- Initial endpoints are present:
  - `GET /status`
  - `POST /sensor-event`
  - `POST /fan/on`
  - `POST /fan/off`
- Mock temperature-event handling is implemented for PC-first development.
- Fan state is simulated in memory through `fan_on`, `fan_off`, and `get_state`.
- A configurable n8n webhook sender placeholder exists, but forwarding is skipped when `N8N_WEBHOOK_URL` is not configured.

## Why it matters for the thesis

This step creates the controlled execution layer between sensor/event input, future n8n workflow logic, and actuator-style actions. It supports the narrowed Yacoub thesis path by proving that the system can begin with mock sensor data and simulated actuator state before adding shared schemas, workflows, safety validation, measurement scripts, or hardware.

It also preserves the safety boundary: workflow logic does not directly control hardware at this stage, and no real GPIO path is implemented.

## Evidence produced

- `middleware/api/app.py`
- `middleware/api/routes.py`
- `middleware/gpio/mock_sensor.py`
- `middleware/webhooks/n8n_sender.py`
- `middleware/tests/manual-test-notes.md`
- `middleware/tests/evidence/step-04-middleware-smoke-test-2026-04-25.txt`

The smoke-test evidence records:

- middleware startup at `http://127.0.0.1:8000`
- `GET /status` returning middleware status and simulated hardware state
- `POST /fan/on` changing simulated fan state to `on`
- `POST /fan/off` changing simulated fan state to `off`
- `POST /sensor-event` accepting a valid temperature event
- malformed sensor input returning HTTP `400`
- n8n forwarding intentionally skipped because no Step 6 workflow is connected yet

## Report chapters it feeds

- Chapter 3 - Methodology: PC-first development, manual smoke testing, mock sensor data before hardware.
- Chapter 5 - Implementation: middleware API structure, sensor-event input path, simulated actuator endpoints, n8n webhook placeholder.
- Chapter 7 - Discussion: limitations of mock execution and why hardware-facing behavior is deferred until validation layers exist.

## Limitations or assumptions

- This step uses mock sensor data only.
- Fan behavior is simulated in memory; no real GPIO or physical fan control exists.
- No shared JSON schemas are used yet; Step 4 uses a minimal inline check for required fields.
- No deterministic n8n workflow integration exists yet.
- No agent-enhanced workflow exists yet.
- No safety layer or human approval checkpoint exists yet.
- No latency, RAM, CPU, or thermal/resource measurements are produced by this step.
- Middleware state is process-local and is not persisted across restarts.

## Screenshots/logs still needed

- Terminal screenshot or saved log showing middleware startup.
- Request/response logs for `/status`, `/sensor-event`, `/fan/on`, and `/fan/off` in a consistent evidence format.
- Screenshot or exported evidence once the Step 6 n8n workflow actually receives middleware events.
- Later measurement logs for latency, CPU, RAM, and thermal/resource behavior.
