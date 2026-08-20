# Step 4 Yacoub-Compatible Integration Boundary

This directory contains the `OBID_CREATED` plumbing and evidence used to verify the two shared seams between Obid n8n and the actual frozen Yacoub middleware. It is not an agent workflow, baseline workflow, schema adoption, safety layer, or evaluation dataset.

## Provenance and ownership

- The middleware implementation and its existing runtime behavior are `YACOUB_INHERITED` from `Rumple12/new-yacoub-thesis` commit `278318340bfa4e4650a97a2baba73f63bd868ed9`.
- The sensor/action semantics being exercised are `SHARED_INTERFACE`; this does not imply co-authorship.
- The Step 4 workflow, test plan, boundary map, and new observations are `OBID_CREATED`.
- No `TEST_DOUBLE` exists. The actual frozen middleware ran successfully from a clean detached temporary checkout outside this repository.

## Verified boundary

Inbound production path:

```text
host client
  -> POST http://127.0.0.1:8000/sensor-event
  -> actual Yacoub middleware
  -> N8N_WEBHOOK_URL=http://127.0.0.1:5678/webhook/obid-yacoub-compat
  -> Obid n8n workflow boundary
```

Outbound production paths used only to trigger this integration check:

```text
POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-on
  -> n8n HTTP Request
  -> POST http://host.docker.internal:8000/fan/on

POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-off
  -> n8n HTTP Request
  -> POST http://host.docker.internal:8000/fan/off
```

The n8n workflow is named `Step 4 - Yacoub compatibility boundary`, has ID `step4-yacoub-compat`, and contains only Webhook, Set, and HTTP Request nodes. It does not decide which action should be taken; each action branch is invoked explicitly for boundary verification.

## Bounded reproduction

Prerequisites:

- the verified Step 3 n8n environment running on `http://localhost:5678`;
- Python 3.11 or later;
- a clean detached checkout of the frozen Yacoub commit outside Obid;
- host port 8000 available.

The workflow export is `workflows/step-04-boundary-test.json`. The verified credential-free lifecycle was CLI import while n8n was stopped, CLI activation, and n8n restart. n8n CLI imports are assigned internally to the local owner project; no owner identity or credential is needed for the command. The repository export deliberately omits local owner/project metadata.

From the Obid repository root, import and activate only this workflow:

```powershell
$step4WorkflowPath = (Resolve-Path "integration/yacoub_compat/workflows/step-04-boundary-test.json").Path
docker compose --project-directory infrastructure/docker stop n8n
docker compose --project-directory infrastructure/docker run --rm --no-deps -v "${step4WorkflowPath}:/tmp/step-04-boundary-test.json:ro" n8n import:workflow --input=/tmp/step-04-boundary-test.json
docker compose --project-directory infrastructure/docker run --rm --no-deps n8n update:workflow --id=step4-yacoub-compat --active=true
docker compose --project-directory infrastructure/docker up -d n8n
```

Confirm `http://localhost:5678` returns before starting the middleware. The CLI activation takes effect after the shown restart.

From the clean Yacoub checkout root, start the inherited middleware with runtime-only settings:

```powershell
$env:MIDDLEWARE_HOST = "0.0.0.0"
$env:MIDDLEWARE_PORT = "8000"
$env:N8N_WEBHOOK_URL = "http://127.0.0.1:5678/webhook/obid-yacoub-compat"
python -u -m middleware.api.app
```

With the inherited middleware running, the bounded PowerShell invocations are:

```powershell
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/status"

$step4Event = [ordered]@{
  sensor_id = "temp_sensor_1"
  timestamp = "2026-08-20T13:24:30Z"
  type = "temperature"
  value = 31.4
  unit = "C"
} | ConvertTo-Json -Compress

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/sensor-event" -ContentType "application/json" -Body $step4Event
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-on" -ContentType "application/json" -Body "{}"
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/status"
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-off" -ContentType "application/json" -Body "{}"
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/status"
```

Use the one-off stimuli and pass criteria in `test-plan.md`. Do not treat them as Step 5 cases or repeat them as an evaluation protocol. The `{}` and zero-length characterization commands are intentionally not part of this concise normal-path reproduction; their exact one-off observations are retained in the evidence note.

## Boundary rules

- Do not copy or modify Yacoub middleware here.
- Do not silently rename paths or change shared semantics.
- Do not import either inherited baseline into this workflow.
- Do not add LLM, agent, prompt, memory, parser, policy, HITL, schema-validation, or evaluation nodes.
- If the actual middleware becomes unavailable in a future reproduction, stop and request authorization before creating any `TEST_DOUBLE`.
