# Step 07 - Minimal Agent Workflow

## What was built

- A minimum Obid-compatible agent-enhanced n8n workflow was added under `cognitive_logic/workflows/`.
- The workflow receives one temperature event, prepares the current event as agent input, runs one LLM decision step, parses the structured action output, and routes supported fan actions to the same Step 4 middleware endpoints used by the deterministic baseline.
- One prompt set was defined in `cognitive_logic/prompts/system-prompt-v1.md`.
- One memory choice was defined in `cognitive_logic/memory/memory-choice-v1.md`.
- The documented memory strategy is stateless execution / no memory.
- The workflow output is expected to match the Step 5 agent-action contract fields: `action_id`, `target`, `reason`, and `requires_approval`.
- A minimal unrouted branch exists for non-contract actions, but this is not the Step 8 safety layer.

## Why it matters for the thesis

This step adds the smallest agent-enhanced path needed for the narrowed new-yacoub thesis. It keeps the Obid-compatible layer minimal while giving the project a second workflow mode to compare against the Step 6 deterministic baseline.

The workflow matters because the thesis evaluation plan requires two modes:

- deterministic baseline
- minimal agent-enhanced workflow with validation/approval later

Step 7 provides the agent-enhanced workflow artifact and runtime evidence, while keeping safety enforcement and measurement work deferred to later steps.

## Evidence produced

- `cognitive_logic/workflows/agent-minimal.json`
- `cognitive_logic/workflows/agent-minimal.md`
- `cognitive_logic/prompts/system-prompt-v1.md`
- `cognitive_logic/memory/memory-choice-v1.md`
- `cognitive_logic/workflows/evidence/step-07/step-07-runtime-verification.md`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-canvas.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-agent-output.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-parsed-action.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-fan-on-output.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-canvas.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-agent-output.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-parsed-action.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-fan-off-output.png`
- `shared_interfaces/json-schema/agent-action.schema.json`

The Step 7 runtime evidence records:

- n8n running locally through Docker at `http://localhost:5678`
- middleware running locally with `python -m middleware.api.app`
- middleware reachable from Dockerized n8n through `http://host.docker.internal:8000`
- model used: Google Gemini Chat Model
- memory strategy: stateless / no memory
- screenshot evidence of the minimal LLM decision node with Google Gemini Chat Model connected
- screenshot evidence of the prompt/system-message setup used by the decision node
- screenshot evidence of structured JSON output from the agent path
- screenshot evidence of stateless/no-memory canvas setup, with no memory node connected
- high-temperature input `31.4 C` producing `fan_on`, routing to `POST /fan/on`, and receiving a simulated middleware response with `status = ok`, `action = fan_on`, and `fan = on`
- low-temperature input `24.5 C` producing `fan_off`, routing to `POST /fan/off`, and receiving a simulated middleware response with `status = ok`, `action = fan_off`, and `fan = off`

The Step 7 screenshots therefore cover:

- model setup
- prompt/system-message setup
- structured JSON output
- no-memory/stateless canvas setup
- `fan_on` and `fan_off` middleware routing

## Report chapters it feeds

- Chapter 4 - Choice of approach: why the agent-enhanced path is minimal, why model benchmarking is out of scope, and why no-memory execution was chosen.
- Chapter 5 - Implementation: n8n agent workflow, prompt file, stateless memory decision, structured action parsing, and middleware routing.
- Chapter 6 - Results: initial runtime evidence for the agent-enhanced high-temperature and low-temperature branches.
- Chapter 7 - Discussion: limitations of the minimized Obid-compatible path, prompt limitations, stateless/no-memory tradeoffs, and deferred safety validation.

## Limitations or assumptions

- This is the minimum Obid-compatible agent-enhanced path, not a broad multi-agent architecture.
- The workflow uses one prompt set only.
- The workflow uses one memory choice only: stateless execution / no memory.
- The evidence names one model setup, Google Gemini Chat Model, but this step does not compare models.
- Step 8 safety validation and human approval enforcement do not exist yet.
- Step 9 latency, RAM, CPU, thermal/resource, and repeated-run evaluation measurements do not exist yet.
- The middleware fan actions remain simulated; no real GPIO or physical fan is controlled.
- The workflow expects structured action output matching `agent-action.schema.json`, but final runtime safety enforcement is deferred to Step 8.
- The agent-enhanced workflow has not yet been formally compared against the Step 6 deterministic baseline with the final evaluation harness.
- `agent-minimal.json` is documented as a draft/export-candidate that must stay aligned with the verified n8n UI workflow and configured model credential.

## Screenshots/logs still needed

- Final exported n8n workflow after any UI import/re-export changes.
- Repeated-run logs for the same test cases once the Step 9 measurement harness exists.
- Latency, RAM, CPU, and thermal/resource measurements from Step 9.
- Baseline-vs-agent comparison tables after Step 9.
- Step 8 safety evidence showing validation, blocked output handling, and human approval behavior.
