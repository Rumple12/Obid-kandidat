# Active Yacoub Engineering Handoff

**Handoff status:** Frozen source inspected during Step 1

**Inspection date:** 2026-08-19

**Upstream repository:** `https://github.com/Rumple12/new-yacoub-thesis`

**Frozen commit:** `278318340bfa4e4650a97a2baba73f63bd868ed9`

`git ls-remote` confirmed on 2026-08-19 that upstream `HEAD` and `refs/heads/main` both point to the frozen commit. Exact file contents were inspected from that commit with `git show`, rather than relying on historical prose or the local nested working-tree state.

This file is the active Obid engineering handoff. The source note at `reference/yacoub-handoff.md` remains read-only.

## Handoff role

Yacoub provides the completed workflow/action-side system and the minimum compatible cognitive baseline. Obid consumes the interfaces, verifies the baselines, and upgrades the decision/reliability layer. No artifact listed here becomes Obid-authored through reuse.

## Exact inherited artifact paths

All paths in this section are relative to the frozen Yacoub repository.

| Purpose | Frozen source path | Handoff status |
| --- | --- | --- |
| Sensor contract | `shared_interfaces/json-schema/sensor-event.schema.json` | Inherited interface; preserve |
| Action contract | `shared_interfaces/json-schema/agent-action.schema.json` | Inherited interface; preserve |
| Sensor example | `shared_interfaces/examples/sensor-event.example.json` | Reference input |
| Allowed action example | `shared_interfaces/examples/fan-on.example.json` | Reference output |
| Invalid action example | `shared_interfaces/examples/blocked-action.example.json` | Negative/reference case |
| Middleware entry point | `middleware/api/app.py` | Yacoub-owned runtime |
| Middleware routes | `middleware/api/routes.py` | Yacoub-owned API boundary |
| Mock sensor/fan state | `middleware/gpio/mock_sensor.py` | Yacoub-owned simulated action behavior |
| n8n sender | `middleware/webhooks/n8n_sender.py` | Yacoub-owned event forwarding |
| Deterministic baseline | `cognitive_logic/workflows/deterministic-baseline.json` | Inherited comparison baseline |
| Deterministic baseline description | `cognitive_logic/workflows/deterministic-baseline.md` | Baseline semantics |
| Deterministic evidence | `cognitive_logic/workflows/evidence/step-06-runtime-verification.md` | Inherited evidence |
| Minimal agent baseline | `cognitive_logic/workflows/agent-minimal.json` | Inherited comparison baseline/export candidate |
| Minimal agent description | `cognitive_logic/workflows/agent-minimal.md` | Baseline semantics and limitations |
| Minimal agent evidence | `cognitive_logic/workflows/evidence/step-07/step-07-runtime-verification.md` | Inherited runtime note |
| Baseline system prompt | `cognitive_logic/prompts/system-prompt-v1.md` | Inherited prompt |
| Baseline memory choice | `cognitive_logic/memory/memory-choice-v1.md` | Inherited stateless choice |
| Integration contract narrative | `docs/ongoing/integration-contract.md` | Reference explanation; schemas control exact shape |
| Safety parser design | `safety_layer/parsers/output-validation-v1.md` | Specification only |
| Action policy design | `safety_layer/policies/action-policy-v1.md` | Specification only |
| HITL design | `safety_layer/approvals/hitl-v1.md` | Specification only |
| Safety examples | `safety_layer/examples/allowed-case.md`, `blocked-case.md`, `risky-approval-case.md` | Expected behavior only |
| Frozen architecture | `docs/architecture/final-architecture.md` | Yacoub architecture/provenance context |
| Yacoub evaluation material | `evaluation/`, `scripts/collect_metrics.py`, `scripts/aggregate_results.py` | Inherited methodology/evidence; not Obid results |
| Raspberry Pi material | `infrastructure/os/raspberry-pi-notes.md`, `infrastructure/docker/pi-deployment-notes.md`, `evaluation/results/pi-validation/` | Inherited Yacoub evidence |

## Sensor-event contract

Source: `shared_interfaces/json-schema/sensor-event.schema.json`

The payload must be one JSON object with no additional properties.

| Field | Requirement |
| --- | --- |
| `sensor_id` | required non-empty string |
| `timestamp` | required string with JSON Schema `date-time` format |
| `type` | required string, exactly `temperature` |
| `value` | required number |
| `unit` | required string, exactly `C` |

Frozen example:

```json
{
  "sensor_id": "temp_sensor_1",
  "timestamp": "2026-04-25T20:00:00Z",
  "type": "temperature",
  "value": 31.4,
  "unit": "C"
}
```

The middleware's `normalize_sensor_event()` checks required fields, `type`, and numeric coercion, but it does not enforce the JSON Schema's timestamp format, unit constant, additional-properties rule, or all field types. Obid must not mistake this inline check for full runtime schema validation.

Frozen-source inspection also verified that a zero-length request body is parsed as `{}` and that either this result or an explicit empty object causes `normalize_sensor_event()` to substitute the generated default mock temperature event (`temp_sensor_1`, `temperature`, `31.4 C`, with a generated timestamp). Empty-body/empty-object transformation is inherited middleware behavior and integration/context evidence; it is not Obid agent decision correctness.

## Action contract

Source: `shared_interfaces/json-schema/agent-action.schema.json`

The payload must be one JSON object with no additional properties.

| Field | Requirement |
| --- | --- |
| `action_id` | required string; exactly `fan_on` or `fan_off` |
| `target` | required string; exactly `fan_1` |
| `reason` | required non-empty string |
| `requires_approval` | required Boolean |

Frozen allowed example:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_above_threshold",
  "requires_approval": false
}
```

Supported action IDs are exactly `fan_on` and `fan_off`. The supported target is exactly `fan_1`.

## Middleware and workflow endpoints

The middleware defaults to host `127.0.0.1`, port `8000`. Dockerized n8n reaches it at `http://host.docker.internal:8000`.

| Method and path | Frozen behavior |
| --- | --- |
| `GET /status` | Returns middleware status and simulated state |
| `POST /sensor-event` | Parses/normalizes an event and sends it to the externally configured `N8N_WEBHOOK_URL`; returns HTTP 202 when accepted |
| `POST /fan/on` | Sets simulated fan state to `on` and returns an action response |
| `POST /fan/off` | Sets simulated fan state to `off` and returns an action response |

The frozen workflows call:

- `fan_on` -> `POST http://host.docker.internal:8000/fan/on`
- `fan_off` -> `POST http://host.docker.internal:8000/fan/off`

The action endpoints do not consume the shared action object. They are route-selected calls and return `reason: "manual_api_call"`. Obid must preserve this route mapping unless a later explicit compatibility decision changes it.

Configured n8n webhook paths in the inherited exports are:

- deterministic baseline: `POST` path `deterministic-baseline`
- minimal agent baseline: `POST` path `agent-minimal`

The deterministic runtime note records the test URL `http://localhost:5678/webhook-test/deterministic-baseline`. The sender itself stores no fixed n8n URL; it uses `N8N_WEBHOOK_URL`.

## Deterministic baseline

Artifacts:

- `cognitive_logic/workflows/deterministic-baseline.json`
- `cognitive_logic/workflows/deterministic-baseline.md`
- `cognitive_logic/workflows/evidence/step-06-runtime-verification.md`

Exact rule:

```text
if value >= 30.0 C: fan_on
else: fan_off
```

The workflow receives the event through the `deterministic-baseline` webhook, evaluates `$json.body.value`, constructs the shared action fields, and calls the corresponding fan endpoint. The inherited runtime note records `31.4 C -> fan_on` and `24.5 C -> fan_off`.

This is an inherited comparison anchor, not Obid-authored work.

## Minimal Obid-compatible agent baseline

Artifacts:

- `cognitive_logic/workflows/agent-minimal.json`
- `cognitive_logic/workflows/agent-minimal.md`
- `cognitive_logic/prompts/system-prompt-v1.md`
- `cognitive_logic/memory/memory-choice-v1.md`
- `cognitive_logic/workflows/evidence/step-07/step-07-runtime-verification.md`

Frozen behavior:

```text
Webhook agent-minimal
  -> prepare JSON-stringified event
  -> one LLM decision step
  -> regex extract first JSON-looking object and JSON.parse
  -> route action_id == fan_on or fan_off
  -> otherwise mark unrouted_non_contract_action
```

The prompt applies the same `30.0 C` rule, requires JSON-only output, allows only `fan_on`/`fan_off` and `fan_1`, and forbids invented hardware instructions.

### Baseline model

The runtime note and workflow screenshot evidence identify the provider node as **Google Gemini Chat Model**. The frozen JSON export does not contain the configured model node, credential, exact Gemini model name/version, temperature, or other generation settings.

### Baseline memory

The evidenced choice is **stateless execution / no memory**. No memory node is connected. Window buffer memory and other memory strategies were explicitly deferred in Yacoub's narrowed scope.

### Reproducibility qualification

`agent-minimal.json` labels itself a draft/export candidate and contains the LLM chain but no connected language-model node in the committed export. The screenshot shows a connected Google Gemini Chat Model during runtime. Step 6 must therefore verify or re-export the baseline before it is used as the RQ3 comparison configuration.

## Existing safety and HITL state

What exists:

- a parser/validation specification
- an action-policy specification
- a HITL approve/reject specification
- allowed, blocked, and risky example documents
- an `Unrouted non-contract action` fallback after action-ID routing
- a regex plus `JSON.parse` extraction step in the minimal agent workflow

What does **not** exist in the frozen runtime:

- JSON Schema validation of agent output
- validation of all required fields, field types, target, or extra fields before route execution
- a deterministic runtime policy decision component
- a runtime `requires_approval` gate
- an actual approval UI/message/wait/resume path
- an auditable reviewer approve/reject record
- middleware-side enforcement preventing direct calls to `/fan/on` or `/fan/off`

The Yacoub safety documents repeatedly state that they are documentation/specification-level only. They must not be cited as proof of runtime enforcement. Converting this design into runtime validation, policy, and actual HITL behavior is Obid-owned core work.

## Semantics Obid must preserve

- exact sensor-event field names and constants
- exact action field names, allowed actions, and target
- `30.0 C` threshold semantics for inherited baseline comparison
- action-to-endpoint mapping
- middleware ownership and route behavior
- simulated `fan_on`/`fan_off` observability as the minimum integration result
- no direct agent-to-GPIO, shell, or invented hardware execution path
- failure visibility and provenance of inherited evidence
- baseline identity: stateless/no-memory minimal agent unless Step 6 records a narrowly necessary reproducibility repair

## Reference-only material

Everything under the active repository's `reference/` directory, every file in upstream Yacoub commit `2783183...`, all Yacoub screenshots/results, and all Yacoub Raspberry Pi material are reference/inherited artifacts. They must not be copied into active Obid implementation folders during Step 1 or described as Obid results.

Historical directories such as `reference/new-yacoub-thesis (9) (INCLUDES AI TOOL USAGE)/`, `reference/Master prompts/`, and the Yacoub 14-step PDF are process/history sources only, not active implementation instructions.

## `[CHECK]` items for later bounded steps

1. **Step 2:** Confirm whether the locally nested final-project reference was intentionally pruned/changed; its nested Git working tree is not clean even though `HEAD` is the frozen commit. Continue using the upstream commit object as the exact source.
2. **Step 3:** Record the actual n8n runtime version used by Obid and verify compatibility with Yacoub's pinned `n8nio/n8n:1.123.37` without upgrading silently.
3. **Step 4:** Verify the exact Obid webhook URL/path and the `N8N_WEBHOOK_URL` forwarding path end to end.
4. **Step 6:** Recover or recreate a reproducible minimal-agent baseline export with the connected Google model node.
5. **Step 6:** Record the exact Gemini model name/version, credential-independent node settings, and generation parameters. The frozen handoff only evidences "Google Gemini Chat Model."
6. **Step 6:** Reconfirm both inherited baseline outputs under the Obid runtime before beginning the extended workflow comparison.
7. **Step 5:** Decide how a valid schema-conforming `requires_approval: true` fan action will be generated as the risky/HITL test case without expanding the allowed action or target set.
