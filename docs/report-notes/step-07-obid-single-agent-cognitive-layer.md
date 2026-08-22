# Step 7 report-support note

## Step

Step 7 — Upgrade the handoff into the real Obid single-agent system

## Status

Step 7 implemented `CONFIG-OBID`, completed the bounded cognitive-readiness observations, and passed formal audit with no blocking or non-blocking findings. Step 7 readiness is complete, and this report-support note completes the repository closure for the step. Step 8 has not started.

The observations documented here are one-off implementation/readiness evidence. They are not repeated reliability evidence, RQ1–RQ3 results, or production-safety evidence. The Codex audit is a completion review rather than experimental evidence.

## Why Step 7 was necessary

Step 6 reproduced and froze the inherited comparison control, `CONFIG-BASELINE`:

```text
one Gemini decision
+ inherited prompt
+ minimal JSON parsing
+ fan_on/fan_off routing
+ stateless/no memory
```

Step 7 introduced the first substantive `OBID_CREATED` cognitive workflow:

```text
valid event
→ controlled single AI Agent
→ explicit tools
→ bounded tool-use cycle
→ bounded recent-state memory
→ structured internal decision
→ candidate shared action OR internal no-op
```

This adds cognitive behavior without changing the shared sensor schema, shared action schema, inherited inclusive threshold, allowed actions, target, or Yacoub middleware endpoints.

## Contribution boundary

| Configuration | Provenance | Characteristics |
| --- | --- | --- |
| `CONFIG-BASELINE` | `YACOUB_INHERITED` | One LLM decision, inherited Yacoub prompt, minimal parser, stateless, no explicit tools, no bounded ReAct-style loop, no Obid memory, and no runtime validator, policy, or HITL |
| `CONFIG-OBID` | `OBID_CREATED` | One tool-capable AI Agent, Obid-authored prompt, exactly two tools, bounded tool interaction and iterations, one bounded-memory configuration, state-aware duplicate suppression, an internal structured decision envelope, and a malformed-input gate |

Step 7 does not transfer authorship of the inherited threshold, action, shared-interface, or middleware semantics to Obid.

## Main `CONFIG-OBID` artifact

- Artifact: `cognitive_logic/obid/workflows/obid-agent-v1.json`
- Workflow: `CONFIG-OBID - Single Agent v1`
- Workflow ID: `obid-agent-v1`
- Production webhook: `POST /webhook/obid-agent-v1`
- n8n version: `1.123.37`
- Portable export state: inactive
- SHA-256: `7e26e8c36786d75cf5e3d8a6f3bc496aea389495eac6d2c1df374476b4de4a17`

The committed portable export is credential-sanitized.

## Model-control preservation

| Property | Value |
| --- | --- |
| Node | `@n8n/n8n-nodes-langchain.lmChatGoogleGemini` |
| Type version | `1` |
| Model | `models/gemini-2.5-flash` |
| Stored generation options | `{}` |

The configuration intentionally preserves the Step 6 baseline model control so that the later RQ3 comparison does not silently become a different-model study. Step 7 introduced no alternate model, fallback model, model router, or explicit generation tuning. Google may change remote behavior behind the model identifier; that remains a reproducibility limitation.

## AI Agent and bounded ReAct-style behavior

| Property | Value |
| --- | --- |
| Agent node | `@n8n/n8n-nodes-langchain.agent` |
| Type version | `3` |
| Iteration property | `options.maxIterations` |
| Maximum iterations | `3` |
| Intermediate steps retained | `false` |

“Controlled ReAct-style” denotes the bounded observable cycle:

```text
event
→ agent selects a permitted tool
→ tool returns an observable result
→ agent may select the second permitted tool
→ agent emits one final structured decision
```

Evidence is limited to observable tool identity, input, output, call order/count, final model output, and workflow execution metadata. No hidden chain-of-thought, scratchpad, or private reasoning was requested or retained.

## Obid system prompt

- Artifact: `cognitive_logic/obid/prompts/system-prompt-v1.md`
- Provenance: `OBID_CREATED`
- SHA-256: `f8b4171e5d70df6be5aa136a63336dc8c32edca61036272a047b6fa3746cfec2`

The prompt materially extends the inherited prompt while preserving one temperature event, target `fan_1`, actions `fan_on`/`fan_off`, and the inclusive `>= 30.0 C` threshold. It restricts the agent to the permitted tools, requires threshold-tool use, allows the status tool only when recent state is unavailable, allows recent memory to replace a status lookup, suppresses duplicate actions, and requires one final JSON decision envelope without Markdown, prose, or chain-of-thought disclosure. The prompt alone is not evidence of reliability.

## Tool 1 — temperature threshold tool

`temperature_threshold_tool` is documented in `cognitive_logic/obid/tools/tool-definitions-v1.md`. It uses `@n8n/n8n-nodes-langchain.toolCode` type version `1.3` and is deterministic, read-only, and `OBID_CREATED`. It maps `value >= 30.0 C` to desired `fan_on`/`on`, and lower values to desired `fan_off`/`off`.

Representative threshold-tool output:

```json
{
  "threshold_c": 30,
  "relation": "at_or_above",
  "desired_action": "fan_on",
  "desired_fan_state": "on"
}
```

The threshold tool does not call `/fan/on` or `/fan/off`, modify memory, or perform Step 8 action-schema validation.

## Tool 1 implementation repairs

Execution 13 exposed a singleton-enum/const tool-schema incompatibility, and execution 14 exposed a conflict between `additionalProperties: false` and n8n wrapper fields. The internal tool schema was repaired without changing the threshold, shared schemas, decision semantics, deterministic code behavior, or Step 5 oracle.

## Tool 2 — fan-status tool

`fan_status_tool` uses `@n8n/n8n-nodes-langchain.toolWorkflow` type version `2.2`. It is a read-only tool based on the actual inherited Yacoub middleware.

The status tool uses the narrow path:

```text
Execute Workflow Trigger
→ GET Yacoub /status
→ normalize current simulated fan state
```

Representative result:

```json
{
  "target": "fan_1",
  "fan_state": "off",
  "simulated": true,
  "source": "yacoub_status"
}
```

It cannot call `/fan/on` or `/fan/off`, contains no agent recursion or credential, and is not a generic tool platform.

## Tool 2 compatibility repair

Execution 15 showed that an installed legacy HTTP Tool failed with `Invalid URL`; it was replaced with the installed Workflow Tool v2.2 and a minimal read-only status subworkflow. The semantic capability remained identical, with no extra service, API, or action capability introduced. Execution 15 remains retained as development evidence.

## Exactly two tools

| Tool | Final capability |
| --- | --- |
| `temperature_threshold_tool` | deterministic desired-state calculation |
| `fan_status_tool` | read-only inherited current-state lookup |

No action-execution tool, extra reasoning tool, dynamic tool creation, recursive agent tool, MCP, or third-party service tool is exposed. Fan action endpoint calls occur after cognition through narrow workflow routing, not as agent tools.

## Bounded-memory configuration

- Artifact: `cognitive_logic/obid/memory/window-buffer-v1.md`
- Node: `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- Display/type version: Simple Memory / `1.3`
- Window: `contextWindowLength: 2`
- Meaning: two completed input/output interaction pairs remain model-visible
- Session type: `customKey`
- Session expression: `={{ $json.session_id }}`
- External metadata source: `X-Obid-Session-Id`

The synthetic session identifier is provided outside the frozen sensor-event body; no shared schema field was added, and the identifiers contain no personal identity. Step 7 uses one memory strategy only, with no vector database, long-term memory, or memory-strategy comparison.

## Memory persistence limitation

Memory is process-local and is not durable across an n8n restart. Older backing history may remain internally: the bounded property is exclusion from the model-visible active window, not physical deletion.

## Memory inclusion evidence

| Stage | Execution | Memory/tool evidence | Observable decision/state |
| --- | ---: | --- | --- |
| A | 23 | Cold session; memory empty; threshold ×1; status ×1 | Fan initially off; `fan_on`; off → on |
| B | 25 | Same session; A loaded; threshold ×1; status ×0 | Remembered on and desired on; internal `no_action`; `action: null`; no action endpoint; state remains on |
| C | 27 | Same session; A+B loaded; threshold ×1; status ×0 | Desired off; `fan_off`; on → off |

Execution 25 is the readiness proof for state-aware duplicate suppression. Earlier provider-quota failures at executions 22 and 26 remain retained rather than being erased.

## Active-window eviction evidence

Execution 28 loaded the recent context before a later provider-quota failure. Its active window contained B+C and omitted A, showing that the model-visible window is bounded to two completed interactions. It does not show physical deletion from backing history.

## Session isolation evidence

Executions 29–32 used new reset-session contexts and loaded empty memory before provider rejection. They are valid session-isolation observations, but initially could not prove cold status lookup because the provider stopped the model before tool execution.

## Final reset/cold-session proof

One final authorized readiness probe was performed. Main execution 33 and inline status subexecution 34 recorded:

- a new synthetic session and `25.0 C` input;
- simulated fan explicitly preconditioned off;
- empty memory;
- `temperature_threshold_tool` ×1 followed by `fan_status_tool` ×1;
- status off and desired state off;
- no `/fan/on` or `/fan/off` call;
- final simulated fan state off; and
- successful termination within `maxIterations: 3`.

The retained final decision was:

```json
{
  "decision": "no_action",
  "action": null,
  "state_before": "off",
  "state_after": "off",
  "reason_code": "desired_state_already_satisfied"
}
```

This completes the cold/reset-session behavior proof:

```text
empty memory
→ threshold tool
→ status tool
→ current state already desired
→ internal no-op
```

## Cold versus warm behavior

| Context | Observable behavior |
| --- | --- |
| Cold | memory unavailable → threshold tool → status tool → decision |
| Warm | recent state available → threshold tool → no status lookup → decision |
| Reset/new session | new session → empty memory → status lookup returns |

The comparison shows that connected bounded memory changes observable tool-selection behavior. It is not repeated evidence that memory improves reliability or accuracy.

## Internal structured decision envelope

The `OBID_CREATED` internal envelope is documented in `cognitive_logic/obid/structured-output/decision-envelope-v1.md`. Its fields are `decision`, `action`, `state_before`, `state_after`, and `reason_code`.

An emitted-action form retains the exact inherited shared fields inside the nested action:

```json
{
  "decision": "emit_action",
  "action": {
    "action_id": "fan_on",
    "target": "fan_1",
    "reason": "temperature_at_or_above_threshold",
    "requires_approval": false
  },
  "state_before": "off",
  "state_after": "on",
  "reason_code": "state_change_required"
}
```

No Obid metadata is inserted into the nested shared action.

## Internal no-op semantics

The internal no-op form is:

```json
{
  "decision": "no_action",
  "action": null
}
```

`no_action` is not a new shared `action_id` or a contract change. It represents the absence of a shared action, so no fan endpoint is called. This preserves the frozen Step 5 `EVAL-MEMORY-01B` expectation.

## Malformed-input handling

Readiness case `S7-INPUT-MALFORMED`, execution 12, supplied a sensor event missing `value`. It terminated at `OBID_INPUT_HANDLING`: the model, memory, and tools were not called, and no shared action or action endpoint was reached.

The deterministic pre-agent input gate checks the minimum sensor-event requirements needed before entering the agent: an object body, non-empty `sensor_id` and `timestamp`, `type: temperature`, a finite numeric `value`, `unit: C`, and a non-empty synthetic session header. This is input handling for RQ1 readiness. It is not the Step 8 candidate-action output validator.

## Minimal final-output parsing

The Step 7 parser may extract a JSON-looking object, parse it, recover the internal envelope, branch on `decision`, and expose a nested candidate action. It does not yet perform full action JSON Schema validation, complete candidate field/type/enum enforcement, deterministic action-policy enforcement, a retry/repair loop, or a self-correction loop. The parser is not safety evidence.

## Controlled action routing

For cognitive/integration readiness, routing is limited to:

```text
fan_on candidate  → POST /fan/on
fan_off candidate → POST /fan/off
internal no-op    → no endpoint
```

This uses the actual inherited Yacoub middleware. The branch logic is not Step 8 policy.

## Normal readiness observations

| Observation | Execution | Main behavior |
| --- | ---: | --- |
| Malformed | 12 | Rejected before agent |
| High | 16 | Threshold → status → `fan_on` |
| Low | 18 | Threshold → status → `fan_off` |
| Exact threshold | 20 | `30.0 C` → `fan_on` |
| Memory A | 23 | Cold → status → `fan_on` |
| Memory B | 25 | Remembered on → `no_action` |
| Memory C | 27 | Remembered on → `fan_off` |
| Eviction probe | 28 | B+C visible; A excluded before later quota failure |
| Reset | 33 / 34 | Empty memory → threshold → status → `no_action` |

These are one-off readiness observations, not Step 10 repetitions.

## Retained failures and deviations

| Execution(s) | Retained observation |
| --- | --- |
| 13 | Internal singleton-enum/const tool-schema incompatibility |
| 14 | Tool wrapper-field incompatibility with `additionalProperties: false` |
| 15 | Legacy HTTP Tool `Invalid URL` incompatibility |
| 22 | Provider-quota interruption before successful memory A observation |
| 26 | Provider-quota interruption before successful memory C observation |
| 28 | Provider quota after a valid memory-load/eviction observation |
| 29–31 | New-session empty memory, but quota interruption before tools |
| 32 | Attached credential was exercised, but the provider still reported a free-tier daily quota |

Failures were not erased. Implementation repairs and provider-access reruns are distinct from the later five-repetition experimental protocol. No model, threshold, memory window, iteration limit, schema, or Step 5 oracle was tuned to manufacture passing cognitive decisions.

## Tier-1 continuation context

After the human reported that Gemini API Tier 1 had been enabled, one final authorized readiness probe was performed; execution 33 succeeded. Billing tier is operational access context only, not thesis experiment evidence. No payment, account, or credential details are retained.

## Bounded termination evidence

The successful relevant executions 16, 18, 20, 23, 25, 27, and 33 each completed one AI Agent node run, used no more than two tool calls, called each tool at most once, terminated within `maxIterations: 3`, and contained no recursive or unbounded loop. Model-call counts are not used to infer hidden reasoning steps.

## Actual Yacoub middleware boundary

- Frozen Yacoub commit: `278318340bfa4e4650a97a2baba73f63bd868ed9`
- Runtime address from n8n: `host.docker.internal:8000`
- Inherited endpoints used: `GET /status`, `POST /fan/on`, and `POST /fan/off`
- Hardware: simulated fan only

No middleware was copied, no test double was introduced, and no Raspberry Pi/GPIO work occurred.

## Privacy and sanitization

The committed `CONFIG-OBID` workflow is inactive and sanitized. No Gemini credential, credential ID/name, API secret, owner/account identity, billing information, cookie, session token, or encryption key is committed. Synthetic session IDs are non-private, and local credential attachment remains outside repository artifacts.

## Provenance

| Label | Step 7 attribution |
| --- | --- |
| `YACOUB_INHERITED` | threshold/action semantics, middleware, `/status`, fan endpoints, and simulated fan behavior |
| `SHARED_INTERFACE` | frozen sensor-event schema, frozen agent-action schema, and endpoint meanings |
| `OBID_CREATED` | `CONFIG-OBID` workflow, system prompt, tool definitions and implementation, bounded ReAct control, memory configuration, input handling, internal decision envelope, and cognitive/readiness evidence |

Reuse of inherited semantics does not transfer authorship.

## What Step 7 demonstrates

Step 7 runtime evidence narrowly demonstrates that:

- one single-agent `CONFIG-OBID` exists;
- the two permitted tools are observably and boundedly used;
- recent memory is included while an older interaction is excluded from the active window;
- different synthetic sessions are isolated;
- memory can suppress an unnecessary status lookup and a duplicate action;
- internal no-op produces no shared action;
- malformed input can terminate before the agent; and
- valid candidate actions can reach the inherited middleware.

It does not demonstrate repeated or superior reliability, lower latency, production safety, or completion of RQ1–RQ3.

## Step 7 methodological limitations

| Limitation | Meaning |
| --- | --- |
| Remote model behavior | `models/gemini-2.5-flash` identifies the configuration, but Google may change behavior behind it |
| Provider defaults | Generation settings remain runtime/provider defaults |
| Process-local memory | Simple Memory is not durable across restart |
| Active-window eviction | Exclusion from model-visible context does not prove physical deletion of backing history |
| One-off observations | Readiness evidence is not statistical or repeated evidence |
| Development compatibility failures | Tool-schema and legacy-tool failures occurred and remain retained |
| Provider interruptions | Quota failures occurred and remain retained |
| Tier 1 context | Billing tier is operational context only |
| Safety boundary | Step 8 action-schema validation and deterministic policy remain absent |
| HITL boundary | Step 9 HITL remains absent |

These are accepted readiness/reproducibility limitations, not Step 7 defects requiring repair.

## Step 5 oracle preservation

Step 7 did not modify the sensor schema, action schema, evaluation cases, repetition count, run order, expected high/low/threshold outcomes, malformed-input oracle, memory A→B→C oracle, internal no-op semantics, RQ mappings, latency subset, or HITL cases. `CONFIG-OBID` was built to conform to the frozen oracle rather than rewrite it.

## Step 6 baseline preservation

All artifacts under `cognitive_logic/baselines/yacoub/` remained unchanged. `CONFIG-BASELINE` remains inherited, stateless, minimal, and unmodified; no retroactive baseline improvement occurred.

## Step 8 boundary

Step 7 does not establish runtime safety. Full action JSON Schema validation, action required-field/type/enum enforcement, target enforcement as deterministic policy, invalid-action blocking proof, deterministic action policy, and approval policy remain missing by design. They belong to `Step 8 — Convert the documented safety design into runtime validation and policy enforcement`.

## Step 9 boundary

No actual HITL exists yet. Risk classification, approval transformation, a wait state, approve/deny gate, and human release logic remain Step 9 work.

## Step 10 boundary

No five repetitions, frozen five-round ordering, reliability percentage, RQ3 latency comparison, final baseline-versus-Obid experiment, invalid-action repetitions, or HITL repetitions occurred. All Step 7 runs are development/readiness evidence only.

## Thesis chapters supported

- Chapter 2 — applied tool-using agents, bounded ReAct-style behavior, and memory concepts;
- Chapter 3 — cognitive-readiness method and evidence discipline;
- Chapter 4 — `CONFIG-OBID` architecture and design choices;
- Chapter 5 — main agent implementation;
- Chapter 6 — qualitative implementation/readiness context only, not final RQ results;
- Chapter 7 — design tradeoffs and memory/provider/reproducibility limitations; and
- Appendix — workflow export, prompt, tool definitions, memory configuration, and execution evidence.

## Main Step 7 artifacts

- `cognitive_logic/obid/README.md`
- `cognitive_logic/obid/workflows/obid-agent-v1.json`
- `cognitive_logic/obid/prompts/system-prompt-v1.md`
- `cognitive_logic/obid/tools/tool-definitions-v1.md`
- `cognitive_logic/obid/react/react-control-v1.md`
- `cognitive_logic/obid/memory/window-buffer-v1.md`
- `cognitive_logic/obid/structured-output/decision-envelope-v1.md`
- `cognitive_logic/obid/configuration-manifest.md`
- `cognitive_logic/obid/evidence/step-07-cognitive-verification.md`

Repository checkpoints:

- Initial implementation: `e15198ff5aef657faf94424aaf1273e9b392cbbe`
- Quota-blocked continuation: `21f1db29d6ec9de53f91e02ff12c593b5638927a`
- Final readiness: `d01d80850adfaddd0dd10b49f28fddf2884525d5`
- Closed Step 6: `a4b4e878f166d26e2343c9aadca28018333e6331`

The formal audit exists as Codex/thread review; no separate committed audit artifact is asserted.

## Step 8 dependency

Step 7 leaves a cognitive candidate-action pipeline ready for the runtime reliability layer:

```text
valid sensor event
→ CONFIG-OBID agent
→ bounded tools + memory
→ internal decision
→ candidate shared action / no action
```

Step 8 may insert the actual runtime reliability boundary between candidate output and inherited action endpoint:

```text
candidate action
→ parse
→ full schema validation
→ deterministic policy
→ allow/block
→ inherited action interface
```

Step 8 must preserve `CONFIG-OBID` cognitive behavior, the shared schemas, model control, memory design, Step 5 oracle, and Step 6 baseline. No Step 8 implementation was begun in this note.
