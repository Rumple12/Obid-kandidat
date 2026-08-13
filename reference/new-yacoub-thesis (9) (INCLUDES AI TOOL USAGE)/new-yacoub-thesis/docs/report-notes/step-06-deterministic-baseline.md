# Step 06 - Deterministic Baseline

## What was built

- A deterministic non-AI n8n baseline workflow was created under `cognitive_logic/workflows/`.
- The workflow receives a temperature event through a Webhook node.
- It applies one fixed threshold rule:
  - if `body.value >= 30.0 C`, follow the `fan_on` branch
  - otherwise, follow the `fan_off` branch
- The workflow calls the Step 4 middleware through Docker host networking:
  - `POST http://host.docker.internal:8000/fan/on`
  - `POST http://host.docker.internal:8000/fan/off`
- The workflow output shape follows the Step 5 action contract fields: `action_id`, `target`, `reason`, and `requires_approval`.
- Local runtime evidence was saved for both high-temperature and low-temperature branches.

## Why it matters for the thesis

This step creates the deterministic comparison anchor required by the thesis plan and decision D-008. It gives the project a simple, explainable baseline before the Step 7 agent-enhanced workflow is introduced.

The baseline is important because later evaluation should compare the same task in two modes:

- deterministic baseline
- minimal agent-enhanced workflow with validation/approval

At this stage, the baseline proves the non-AI workflow path can route one temperature event to one simulated fan action through n8n and the middleware.

## Evidence produced

- `cognitive_logic/workflows/deterministic-baseline.json`
- `cognitive_logic/workflows/deterministic-baseline.md`
- `cognitive_logic/workflows/evidence/step-06-runtime-verification.md`
- `cognitive_logic/workflows/evidence/step-06-high-temp-webhook-input.png`
- `cognitive_logic/workflows/evidence/step-06-high-temp-if-condition.png`
- `cognitive_logic/workflows/evidence/step-06-high-temp-fan-on-output.png`
- `cognitive_logic/workflows/evidence/high-temp_terminal.txt`
- `cognitive_logic/workflows/evidence/step-06-low-temp-webhook.png`
- `cognitive_logic/workflows/evidence/step-06-low-temp-if-condition.png`
- `cognitive_logic/workflows/evidence/step-06-low-temp-fan-off-output.png`
- `cognitive_logic/workflows/evidence/step-06-low-temp-fan-off-canva.png`
- `cognitive_logic/workflows/evidence/low-temo_terminal.txt`
- `cognitive_logic/workflows/evidence/full tree.png`
- `cognitive_logic/workflows/evidence/fulltree_low.png`
- `cognitive_logic/workflows/evidence/no terminal log reason.txt`

The runtime verification evidence records:

- n8n running locally through Docker at `http://localhost:5678`
- middleware running locally with `python -m middleware.api.app`
- n8n reaching middleware through `http://host.docker.internal:8000`
- test webhook URL: `http://localhost:5678/webhook-test/deterministic-baseline`
- high temperature input `31.4 C` triggering the `fan_on` branch and receiving a simulated middleware response with `"action": "fan_on"` and `"fan": "on"`
- low temperature input `24.5 C` triggering the `fan_off` branch and receiving a simulated middleware response with `"action": "fan_off"` and `"fan": "off"`

## Report chapters it feeds

- Chapter 4 - Choice of approach: why a deterministic baseline is needed before the agent-enhanced path.
- Chapter 5 - Implementation: n8n Webhook, IF threshold rule, Set action nodes, HTTP Request calls to middleware, and simulated fan action path.
- Chapter 6 - Results: initial baseline runtime evidence for the high-temperature and low-temperature branches.
- Chapter 7 - Discussion: limitations of a fixed-rule baseline and why it must later be compared against the Step 7 agent-enhanced workflow.

## Limitations or assumptions

- This is the deterministic non-AI baseline only.
- No AI, agent behavior, prompt, or memory path exists in this Step 6 workflow.
- No safety validation exists yet.
- No human approval checkpoint exists yet.
- The workflow assumes the incoming event already follows the Step 5 sensor-event shape.
- The workflow uses the Step 4 simulated middleware fan endpoints; no real GPIO or physical fan is controlled.
- The action fields follow the shared contract shape, but this step does not prove runtime JSON Schema enforcement.
- The final measurement harness is not implemented yet.
- The saved evidence verifies branch behavior, but it does not provide final latency, RAM, CPU, thermal, or baseline-vs-agent measurements.
- `deterministic-baseline.json` contains a note that it is an export candidate and should remain aligned with the verified n8n UI workflow.

## Screenshots/logs still needed

- Final exported n8n workflow after any UI import/re-export changes.
- Consistent terminal or execution logs for repeated baseline runs.
- Latency measurements from the Step 9 measurement harness.
- RAM, CPU, and thermal/resource measurements from the Step 9 evaluation process.
- Baseline-vs-agent comparison results after the Step 7 agent-enhanced workflow and Step 9 measurement harness exist.
- Safety-layer evidence after Step 8, especially malformed or unsupported action handling.
