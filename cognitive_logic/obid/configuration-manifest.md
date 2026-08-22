# CONFIG-OBID configuration manifest

**Configuration ID:** `CONFIG-OBID`

**Provenance:** `OBID_CREATED`

**Implementation status:** implemented and partly runtime-verified on
2026-08-22; one reset-probe tool-call observation remains pending because the
private Gemini credential reached its free-tier quota

**Comparison anchor:** `CONFIG-BASELINE` remains unchanged and
`YACOUB_INHERITED`

## Runtime and workflow identity

| Item | Frozen Step 7 value |
|---|---|
| n8n | `1.123.37` |
| Image | `n8nio/n8n:1.123.37` |
| Image digest | `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Main workflow | `CONFIG-OBID - Single Agent v1` |
| Runtime/portable ID | `obid-agent-v1` |
| Portable path | `cognitive_logic/obid/workflows/obid-agent-v1.json` |
| Portable SHA-256 | `7e26e8c36786d75cf5e3d8a6f3bc496aea389495eac6d2c1df374476b4de4a17` |
| Webhook | production `POST /webhook/obid-agent-v1` |
| Portable activation | `active: false` |
| Live readiness state | active locally; private credential attached by human |

## Agent and model

| Item | Frozen value |
|---|---|
| Agent node | `@n8n/n8n-nodes-langchain.agent`, type version `3` |
| Iteration property | `options.maxIterations` |
| Iteration value | `3` |
| Intermediate steps | `false` |
| Streaming | `false` |
| Model node | `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`, type version `1` |
| Model | `models/gemini-2.5-flash` |
| Stored generation options | `{}`; no explicit temperature/top-P/top-K/token/safety overrides |
| Fallback model | none |
| Prompt | `cognitive_logic/obid/prompts/system-prompt-v1.md` |
| Prompt SHA-256 | `f8b4171e5d70df6be5aa136a63336dc8c32edca61036272a047b6fa3746cfec2` |

The prompt locks one temperature event, target `fan_1`, actions `fan_on` and
`fan_off`, the inclusive `30.0 C` threshold, controlled tool selection,
state-aware suppression, exact JSON-only envelope output, and no hidden
chain-of-thought disclosure.

## Exactly two tools

| Identity | Node | Type version | Boundary |
|---|---|---:|---|
| `temperature_threshold_tool` | `@n8n/n8n-nodes-langchain.toolCode` | `1.3` | deterministic `>= 30.0 C` fact; read-only |
| `fan_status_tool` | `@n8n/n8n-nodes-langchain.toolWorkflow` | `2.2` | inline Execute Workflow Trigger -> `GET /status` -> normalized simulated state; read-only |

The status Workflow Tool is the smallest pinned-runtime-compatible fallback.
The initially inspected legacy `toolHttpRequest` v1.1 was installed but failed
at runtime with `Invalid URL` through n8n's replacement routing engine. The
inline subworkflow has no agent, recursion, credential, fan action call, or
generic tool platform.

## Memory

| Item | Frozen value |
|---|---|
| Node | `@n8n/n8n-nodes-langchain.memoryBufferWindow` |
| Display/type version | Simple Memory / `1.3` |
| Window | `contextWindowLength: 2` completed input/output pairs |
| Session type | `customKey` |
| Session expression | `={{ $json.session_id }}` |
| Metadata source | synthetic `X-Obid-Session-Id` header outside the sensor body |
| Persistence | same n8n process only; lost on restart; stale cleanup after one hour |
| Eviction meaning | older pairs excluded from model-visible load, not physically deleted from backing history |

## Internal behavior

The deterministic input gate requires an object body, non-empty `sensor_id` and
`timestamp`, `type: temperature`, finite numeric `value`, `unit: C`, and a
non-empty synthetic session header. A failure terminates at
`OBID_INPUT_HANDLING` before model, memory, tools, or endpoints.

The internal envelope contains `decision`, `action`, `state_before`,
`state_after`, and `reason_code`. `decision: no_action` requires `action: null`.
For `emit_action`, the nested candidate uses only the inherited shared fields.
Step 7 performs tolerant JSON extraction and minimal `fan_on`/`fan_off` routing;
it does not perform full schema validation.

Candidate actions may route to the actual inherited middleware:

- `fan_on` -> `POST http://host.docker.internal:8000/fan/on`
- `fan_off` -> `POST http://host.docker.internal:8000/fan/off`
- internal no-op or unrouted output -> no endpoint

Runtime action-schema validation/policy is not implemented (Step 8). HITL is
not implemented (Step 9). Five-run evaluation is not executed (Step 10).
