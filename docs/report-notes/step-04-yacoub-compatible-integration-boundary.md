# Step 4 report-support note

## Step

Step 4 — Establish the Yacoub-compatible integration test boundary

## Status

Step 4 passed audit with no blocking findings and no non-blocking findings. The actual frozen Yacoub middleware was used, both integration directions were verified, and no test double was needed. Step 5 schema and evaluation-boundary work has not started. The Codex audit is a completion review, not experimental evidence.

## What Step 4 established

Step 4 verified two real integration seams.

### Inbound

```text
compatible sensor event
→ actual Yacoub middleware
→ POST /sensor-event
→ inherited N8N_WEBHOOK_URL forwarding
→ Obid n8n webhook boundary
```

### Outbound

```text
Obid n8n test trigger
→ n8n HTTP Request
→ actual Yacoub /fan/on or /fan/off
→ inherited simulated fan state
```

This replaced the earlier idea of building a separate Obid middleware/API stub. No competing middleware architecture was introduced.

## Why actual Yacoub middleware was used

The collaboration boundary already existed in Yacoub's implementation. Rebuilding it in Obid would duplicate infrastructure and blur authorship; the thesis-relevant task was to verify that Obid could integrate with the inherited boundary. The primary path therefore used the actual frozen Yacoub middleware.

`TEST_DOUBLE`: absent. A test double remains only a future fallback if the collaborator middleware becomes unavailable and an explicitly requested step authorizes one.

## Authoritative Yacoub source

- Repository: `Rumple12/new-yacoub-thesis`
- Frozen commit: `278318340bfa4e4650a97a2baba73f63bd868ed9`

The Step 4 middleware ran from a clean detached temporary checkout outside the active Obid repository. A pre-existing sibling/nested Yacoub checkout was dirty/pruned and was not used as runtime authority. No inherited source file was modified.

Relevant frozen source inspected included:

- `middleware/api/app.py`
- `middleware/api/routes.py`
- `middleware/webhooks/n8n_sender.py`
- `middleware/gpio/mock_sensor.py`

## Middleware runtime configuration

| Context | Address |
| --- | --- |
| Frozen source default | `127.0.0.1:8000` |
| Actual Step 4 bind | `0.0.0.0:8000` |
| Host-side access | `127.0.0.1:8000` |
| n8n-container access | `host.docker.internal:8000` |

The host override was supplied only as a runtime environment value so Dockerized n8n could reach the host process. It did not modify route names, request/response semantics, payload semantics, or inherited middleware source. `0.0.0.0` is the bind address, not a client destination.

## Obid n8n runtime

| Item | Verified value |
| --- | --- |
| Container | `obid-n8n` |
| n8n version | `1.123.37` |
| Host port | `5678` |
| Workflow | `Step 4 - Yacoub compatibility boundary` |
| Workflow ID | `step4-yacoub-compat` |
| Webhook mode | active production `/webhook/` |

The verified Step 3 runtime was reused rather than redesigned.

## Step 4 workflow

The sanitized workflow definition is `integration/yacoub_compat/workflows/step-04-boundary-test.json`. It contains exactly three Webhook nodes, one Set node, and two HTTP Request nodes.

Webhook paths:

- inbound: `obid-yacoub-compat`;
- outbound fan-on trigger: `obid-yacoub-compat-fan-on`;
- outbound fan-off trigger: `obid-yacoub-compat-fan-off`.

The workflow contains no LLM, AI Agent, Gemini configuration, prompt, tool-selection logic, ReAct behavior, memory, threshold decision, parser, schema validation, policy, HITL, or evaluation logic. Its action branches were manually and explicitly triggered to test the boundary; they are not agent decisions.

## Exact inbound forwarding configuration

`N8N_WEBHOOK_URL=http://127.0.0.1:5678/webhook/obid-yacoub-compat`

The inherited Yacoub sender reads `N8N_WEBHOOK_URL`, JSON-serializes the normalized event, POSTs it with a five-second timeout, and returns nested forwarding status. Step 4 verified this actual end-to-end forwarding path rather than only confirming configuration.

## `S4-STATUS-01` — middleware status/reachability

- Host: `GET http://127.0.0.1:8000/status` returned HTTP `200`.
- Container side: `GET http://host.docker.internal:8000/status` returned HTTP `200`.

The inherited response exposed middleware status, message, fan state, last sensor event, and `hardware: simulated`. This is reachability/state evidence only—not schema validation, agent correctness, or safety evidence.

## `S4-IN-01` — compatible inbound event

The one-off compatible stimulus was:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-08-20T13:24:30Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

The actual Yacoub `POST /sensor-event` returned HTTP `202`, top-level status `accepted`, nested forwarding status `sent`, and nested n8n status code `200`. n8n execution 1 succeeded, and all five observed values matched at the Obid webhook boundary.

The middleware calls inherited normalization logic. For this already-valid numeric input, the observed values remained semantically equal after normalization; this is not a general claim of byte-for-byte pass-through for every input. It was one integration stimulus, not schema adoption, a Step 5 dataset item, a repeated trial, or an RQ1 result.

## Outbound boundary checks

| Check | Obid trigger | n8n action call | Observed inherited response | Execution/state evidence |
| --- | --- | --- | --- | --- |
| `S4-OUT-01` | `POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-on` | `POST http://host.docker.internal:8000/fan/on` | `status: ok`, `action: fan_on`, `fan: on`, `simulated: true`, `reason: manual_api_call` | execution 2 succeeded; follow-up `/status` showed `fan: on` |
| `S4-OUT-02` | `POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-off` | `POST http://host.docker.internal:8000/fan/off` | `status: ok`, `action: fan_off`, `fan: off`, `simulated: true`, `reason: manual_api_call` | execution 3 succeeded; follow-up `/status` showed final `fan: off` |

These checks prove that n8n can call the inherited fan-action seams. They do not show that an agent selected either action.

## `S4-IN-02` — inherited empty-input characterization

| Input | Observed inherited behavior |
| --- | --- |
| `{}` body | HTTP `202`; middleware generated `sensor_id: temp_sensor_1`, a runtime timestamp, `type: temperature`, `value: 31.4`, `unit: C`; forwarding status `sent`; execution 4 succeeded |
| Zero-length body | Inherited request handling treated it as `{}`; the same default-event path returned HTTP `202`, forwarding status `sent`, and execution 5 succeeded |

This is `YACOUB_INHERITED` behavior. It is not Obid validation, RQ1 malformed correctness, RQ2 safety protection, or JSON Schema enforcement. Invalid JSON and non-object input are distinct: the frozen source may return HTTP `400`. Step 4 does not generalize that every malformed request becomes `31.4 C`.

## Execution evidence

| Execution | Purpose |
| --- | --- |
| 1 | compatible inbound event |
| 2 | fan on |
| 3 | fan off |
| 4 | `{}` characterization |
| 5 | zero-length characterization |

All five were successful bounded Step 4 integration executions. They are not repetitions, reliability trials, statistical samples, Step 5 evaluation cases, or RQ results.

## Timestamp evidence handling

A PowerShell JSON-deserialization comparison initially produced a misleading timestamp mismatch through type coercion. The raw response and privacy-scoped n8n execution evidence retained the exact string `2026-08-20T13:24:30Z`; the issue was an evidence-processing artifact, not an integration mismatch.

## Workflow privacy and sanitization

A raw n8n CLI export contained local owner/project metadata. It was not committed, was deleted from temporary locations, and was replaced by a sanitized repository workflow definition.

The committed workflow contains no owner identity or email, credential, token, cookie, session, API key, encryption key, or private project-membership block. It was compared with the live workflow for structural fidelity across ID, name, version identity, nodes, connections, settings, webhook paths, and HTTP destinations. No secret exposure was retained in the repository.

## Network boundary map

The verified map is `integration/yacoub_compat/boundary-map.md`.

```text
Inbound:
host client
→ 127.0.0.1:8000/sensor-event
→ actual Yacoub middleware
→ 127.0.0.1:5678/webhook/obid-yacoub-compat
→ Obid n8n

Outbound:
host test trigger
→ Obid n8n
→ host.docker.internal:8000/fan/on or /fan/off
→ actual Yacoub middleware
→ simulated fan state
```

The additional n8n trigger webhook paths are Obid-owned test plumbing, not additions to Yacoub's middleware contract.

## Provenance

### `YACOUB_INHERITED`

Middleware implementation, route behavior, normalization/default behavior, forwarding implementation, simulated fan implementation, and inherited API responses.

### `SHARED_INTERFACE`

The sensor/action semantics exercised and the meanings of the middleware endpoints. `SHARED_INTERFACE` does not imply co-authorship.

### `OBID_CREATED`

The Step 4 n8n integration workflow, disposable test-trigger paths, boundary map, test plan, new integration observations, and verification evidence.

### `TEST_DOUBLE`

Absent.

## Failures / operational observations retained

- The dirty/pruned existing Yacoub checkout was not used; a clean detached temporary checkout was used instead.
- One attempted background launch was rejected before changing runtime or filesystem state.
- The PowerShell timestamp coercion issue was retained and resolved using raw evidence.
- Raw n8n export privacy metadata was detected and excluded.
- Docker Desktop host forwarding produced localhost-looking middleware log origins, so n8n execution data established the workflow origin.
- The middleware was stopped after testing.
- No contract, route, version, or payload deviation was required.

## Test plan result

The bounded plan is `integration/yacoub_compat/test-plan.md`.

| Check | Final status |
| --- | --- |
| `S4-STATUS-01` | `PASS` |
| `S4-IN-01` | `PASS` |
| `S4-IN-02` | `PASS` |
| `S4-OUT-01` | `PASS` |
| `S4-OUT-02` | `PASS` |

This is a bounded integration verification set, not the thesis evaluation dataset.

## Handoff checklist result

Step 4 completed `[CHECK-S4-01]` through `[CHECK-S4-08]`: webhook paths/mode, `N8N_WEBHOOK_URL`, middleware reachability, `/status`, `/sensor-event`, `/fan/on`, `/fan/off`, and confirmation that no competing middleware or test double was introduced.

Step 5 and Step 6 remain unticked. Provenance/adoption prerequisite checks remain future until their assigned step.

## Evidence / source artifacts

- `integration/yacoub_compat/README.md`
- `integration/yacoub_compat/boundary-map.md`
- `integration/yacoub_compat/test-plan.md`
- `integration/yacoub_compat/workflows/step-04-boundary-test.json`
- `integration/yacoub_compat/evidence/step-04-integration-verification.md`
- `docs/collaboration/handoff-verification-checklist.md`

Repository checkpoint: `81a51c5f3a8eb542350fc3fef4ff91517e605d7b`

Authoritative Yacoub commit: `278318340bfa4e4650a97a2baba73f63bd868ed9`

The audit exists as Codex/thread review; this note does not invent a separate committed audit artifact.

## Thesis chapters supported

- Chapter 3 — integration verification method and bounded test procedure;
- Chapter 4 — architecture choice, collaboration boundary, and reuse rationale;
- Chapter 5 — integration implementation/plumbing;
- later Discussion — limitations and ownership separation; and
- Appendix — workflow export, boundary map, test matrix, and reproducibility details.

Step 4 does not provide final RQ1–RQ3 evaluation results.

## What Step 4 did NOT establish

Step 4 did not:

- adopt the sensor or action JSON Schema;
- perform formal no-drift schema verification;
- freeze the evaluation dataset or repetition count;
- define the final malformed-case ownership/injection matrix;
- import the deterministic or minimal-agent baseline;
- configure Gemini;
- implement an agent, prompts, tools, ReAct behavior, or memory;
- implement structured agent-output validation or action policies;
- implement HITL;
- run reliability evaluation or compare latency;
- deploy real Raspberry Pi/GPIO hardware; or
- establish production safety.

## Step 5 dependency

Step 4 leaves the project with a proven real collaboration boundary. Step 5 can freeze the shared-interface artifacts and evaluation boundary against a seam already observed working at runtime.

`Step 5 — Adopt/freeze shared contracts and freeze Obid evaluation cases` remains responsible for exact schema adoption or immutable reference, no-drift verification, formal case IDs, injection points, expected outcomes, ownership and terminal stage, malformed attribution, the required state-dependent bounded-memory case, and repeated-run protocol preparation.

No Step 5 work was performed in this note.
