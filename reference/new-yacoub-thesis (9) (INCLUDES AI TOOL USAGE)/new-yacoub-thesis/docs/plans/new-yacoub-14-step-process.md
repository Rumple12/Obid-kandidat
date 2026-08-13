# New Yacoub 14-Step Process

## Overview

### Core strategy inspired by the friend theses

The thesis should follow the same passing-oriented pattern visible in the friend examples:

1. narrow the scope hard
2. define the evaluation early
3. build one focused implementation
4. save evidence as development progresses
5. write the report from the artifacts, not from memory later

The thesis target remains:

- `Yacoub complete, narrowed`
- `Obid minimum integration only`

This means the thesis is not trying to fully implement the old Yacoub/Obid dual-thesis scope. The work focuses on a small but complete n8n-based IoT proof of concept, where Yacoub's infrastructure and measurement work is the main thesis target, and Obid's workflow/safety layer exists only as the minimum needed for integration.

The official MIUN report template also supports this structure because it expects clear scope, research questions, methodology, approach choice, implementation, measurement setup, results, discussion, conclusions, and an appendix linking to source code rather than pasting code into the report.

### Passing goalpost

The minimum passing system is one end-to-end scenario:

1. a temperature event is generated or received
2. Python middleware forwards the event to n8n
3. n8n evaluates whether the fan should turn on
4. output is validated against a contract or policy
5. risky or malformed output requires approval
6. middleware triggers `/fan/on` or `/fan/off`
7. latency and resource data are logged

If this system works, is measured properly, and the report is written around the evidence, then the thesis is inside a realistic passing zone.

---

## Phase 1: Planning and Setup

### Step 1 - Lock the thesis goal, scope, and research questions

#### Chapter focus

- Chapter 1 - Introduction
- Chapter 2 - Theory

#### Chapter 1 deliverables

- background and motivation
- problem statement
- aim
- research questions
- scope and limitations
- usage of AI tools section
- division of work section
- chapter outline

#### Chapter 1 feeds from

- `docs/ongoing/project-overview.md`
- `docs/ongoing/research-questions.md`
- `docs/ongoing/yacoub-scope.md`
- `docs/ongoing/obid-minimum-integration.md`
- `docs/plans/implementation-plan.md`
- `docs/decisions.md`

#### Chapter 2 deliverables

- initial theory boundaries
- what theory is relevant
- what theory is out of scope

#### Chapter 2 feeds from

- `docs/n8n-version.md`
- `docs/architecture/README.md`
- literature notes
- n8n notes
- edge/IoT notes
- API/validation notes

#### Goal

Freeze the thesis direction so it does not keep changing.

This step exists to stop the project from drifting back into the old broader Yacoub/Obid plan.

#### Work to complete

Finalize the core planning documents:

- `docs/plans/implementation-plan.md`
- `docs/ongoing/project-overview.md`
- `docs/ongoing/yacoub-scope.md`
- `docs/ongoing/obid-minimum-integration.md`
- `docs/ongoing/research-questions.md`
- `docs/ongoing/report-outline.md`
- `docs/n8n-version.md`
- `docs/decisions.md`

#### Research questions

The locked research questions should stay close to this:

1. Can a self-hosted n8n-based IoT system run in a resource-constrained environment with acceptable latency?
2. What RAM, CPU, and thermal/resource effects are observed during operation?
3. Can a minimal workflow/safety layer safely mediate one physical action?
4. How does a deterministic baseline compare to an agent-enhanced workflow on the same task?

#### Scope lock

The project is limited to:

- one scenario
- one sensor/event path
- one action path
- one middleware bridge
- one deterministic baseline
- one minimal agent-enhanced path
- one validation/approval path
- one evaluation loop

#### Evidence produced

- locked scope
- research questions
- decision log
- report outline
- n8n version pin
- scope documents
- narrowed implementation plan

---

### Step 2 - Create the repo foundation and reproducible environment

#### Chapter focus

- Chapter 3 - Methodology
- Chapter 4 - Choice of approach

#### Chapter 3 deliverables

- project/work method
- tool workflow
- use of Git/GitHub
- use of AI tools in development
- iterative development method

#### Chapter 3 feeds from

- `docs/plans/implementation-plan.md`
- `docs/decisions.md`
- `README.md`
- `AGENTS.md`
- Git commit history
- AI-tool workflow notes

#### Chapter 4 deliverables

- why this architecture was chosen
- why scope was narrowed
- why Antigravity/Codex are used as support tools
- why implementation is built as one vertical slice

#### Chapter 4 feeds from

- `docs/decisions.md`
- `docs/architecture/README.md`
- `docs/ongoing/integration-contract.md`

#### Goal

Make the project usable, version-controlled, and ready for implementation.

#### Work to complete

- GitHub repo is live
- branch/commit discipline is active
- `README.md` exists
- `AGENTS.md` exists
- Antigravity rules, workflows, and skill exist
- Codex threads are set up
- repo folders are created
- basic docs are populated

#### Set up

- `README.md`
- `AGENTS.md`
- `.agents/rules/thesis-boundaries.md`
- `.agents/workflows/audit-implementation.md`
- `.agents/skills/thesis-review/SKILL.md`
- `docs/architecture/README.md`
- `docs/ongoing/integration-contract.md`
- GitHub repo
- Codex `audit-review` thread
- Codex `repair-fix` thread
- Antigravity workspace

#### Keep minimal

Do not start with:

- MCP
- n8n core modification
- advanced multi-agent logic
- multiple devices
- full Raspberry Pi deployment
- broad benchmarking

#### Evidence produced

- GitHub repository
- clean commit history
- repo structure
- README
- AGENTS rules
- planning docs
- Antigravity rules
- Codex thread setup
- architecture overview
- initial contract document

---

## Phase 2: Building the Foundation

### Step 3 - Build the local n8n baseline

#### Chapter focus

- Chapter 4 - Choice of approach
- Chapter 5 - Implementation

#### Chapter 4 deliverables

- local self-hosted n8n vs broader/cloud-heavy alternatives
- why the local baseline comes before Raspberry Pi

#### Chapter 4 feeds from

- `docs/decisions.md`
- `docs/n8n-version.md`
- `infrastructure/docker/`

#### Chapter 5 deliverables

- infrastructure setup
- self-hosted n8n runtime
- reproducibility instructions

#### Chapter 5 feeds from

- `infrastructure/docker/docker-compose.yml`
- `infrastructure/docker/.env.example`
- `README.md`

#### Goal

Get the workflow engine running locally before involving hardware complexity.

Get the local workflow engine running before adding middleware, hardware, or agent logic.

#### Work to complete

Create the local infrastructure baseline:

- `infrastructure/docker/docker-compose.yml`
- `infrastructure/docker/.env.example`
- basic local n8n startup instructions
- note the n8n version/image used in `docs/n8n-version.md`

Create:

- `infrastructure/docker/docker-compose.yml`
- `infrastructure/docker/.env.example`
- `infrastructure/docker/README.md`

Update:

- `docs/n8n-version.md`
- `README.md`
- `docs/decisions.md`

#### What this proves

This proves that the thesis has a reproducible local runtime.

#### Evidence produced

- Docker files
- local n8n startup logs
- n8n version pin
- screenshots of running n8n
- basic run instructions

---

### Step 4 - Build the middleware skeleton

#### Chapter focus

- Chapter 3 - Methodology
- Chapter 5 - Implementation

#### Chapter 3 deliverables

- how manual testing was performed
- how mock sensor data was used before hardware

#### Chapter 3 feeds from

- `middleware/tests/manual-test-notes.md`
- `docs/decisions.md`

#### Chapter 5 deliverables

- middleware design
- API bridge
- sensor input path
- actuator endpoint path

#### Chapter 5 feeds from

- `middleware/`
- `middleware/tests/manual-test-notes.md`
- `docs/architecture/README.md`

#### Goal

Build the technical backbone of Yacoub's thesis: the bridge between sensor/action logic and n8n.

Build the main Yacoub bridge between sensor/action logic and n8n.

#### Work to complete

In `middleware/`, create the first minimal Python API structure:

- `middleware/api/app.py`
- `middleware/api/routes.py`
- `middleware/gpio/mock_sensor.py`
- `middleware/webhooks/n8n_sender.py`

Initial endpoints:

- `POST /sensor-event`
- `POST /fan/on`
- `POST /fan/off`
- `GET /status`

At this stage, mock sensor data is fine. Development starts on PC first; Raspberry Pi comes later as Tier 1.5 validation.

Create:

- `middleware/api/app.py`
- `middleware/api/routes.py`
- `middleware/gpio/mock_sensor.py`
- `middleware/webhooks/n8n_sender.py`
- `middleware/tests/manual-test-notes.md`

Initial endpoints:

- `POST /sensor-event`
- `POST /fan/on`
- `POST /fan/off`
- `GET /status`

#### What this proves

This proves that the system has a controlled execution layer and that workflow logic does not directly control hardware.

#### Evidence produced

- middleware source files
- example request/response logs
- terminal outputs
- manual test notes

---

### Step 5 - Define the shared contract layer

#### Chapter focus

- Chapter 4 - Choice of approach
- Chapter 5 - Implementation
- Chapter 7 - Discussion

#### Chapter 4 deliverables

- direct action vs validated contract boundary
- why schemas are used

#### Chapter 4 feeds from

- `docs/ongoing/integration-contract.md`
- `shared_interfaces/`
- `docs/decisions.md`

#### Chapter 5 deliverables

- shared interface implementation
- contract boundary

#### Chapter 5 feeds from

- `shared_interfaces/json-schema/`
- `shared_interfaces/examples/`
- `docs/ongoing/integration-contract.md`

#### Chapter 7 deliverables

- discussion of safety and system boundaries

#### Chapter 7 feeds from

- contract limitations
- schema drift prevention
- blocked/malformed cases

#### Goal

Lock the boundary between Yacoub's runtime side and the minimum Obid-compatible workflow/safety side.

#### Work to complete

Create:

- `shared_interfaces/json-schema/sensor-event.schema.json`
- `shared_interfaces/json-schema/agent-action.schema.json`
- `shared_interfaces/examples/sensor-event.example.json`
- `shared_interfaces/examples/fan-on.example.json`
- `docs/ongoing/integration-contract.md`

Create:

- `shared_interfaces/json-schema/sensor-event.schema.json`
- `shared_interfaces/json-schema/agent-action.schema.json`
- `shared_interfaces/examples/sensor-event.example.json`
- `shared_interfaces/examples/fan-on.example.json`
- `shared_interfaces/examples/blocked-action.example.json`

Update:

- `docs/ongoing/integration-contract.md`
- `docs/architecture/README.md`

#### What this proves

This proves that the system communicates through a defined interface instead of informal assumptions.

#### Evidence produced

- schemas
- example payloads
- integration contract
- architecture notes

---

## Phase 3: The Experiment

### Step 6 - Build the deterministic baseline workflow

#### Chapter focus

- Chapter 4 - Choice of approach
- Chapter 5 - Implementation
- Chapter 6 - Results

#### Chapter 4 deliverables

- why the deterministic baseline is needed
- baseline vs agent-enhanced comparison design

#### Chapter 4 feeds from

- `deterministic-baseline.md`
- `docs/decisions.md`

#### Chapter 5 deliverables

- deterministic workflow implementation

#### Chapter 5 feeds from

- `cognitive_logic/workflows/deterministic-baseline.json`
- workflow screenshots

#### Chapter 6 deliverables

- baseline result section

#### Chapter 6 feeds from

- baseline logs
- baseline latency measurements

#### Goal

Create the baseline that the agent-enhanced workflow will be compared against.

#### Work to complete

Create one n8n workflow with no agent reasoning:

- input: temperature event
- rule: if temperature is above threshold, request `fan_on`
- otherwise no action or `fan_off`
- call the middleware endpoint
- log the result

Store:

- exported workflow JSON
- short explanation of nodes
- workflow screenshot

Create:

- `cognitive_logic/workflows/deterministic-baseline.json`
- `cognitive_logic/workflows/deterministic-baseline.md`

The workflow should:

- receive temperature event
- apply threshold rule
- request `fan_on` or `fan_off`
- call middleware endpoint
- log result

#### What this proves

This gives the thesis a controlled comparison anchor.

#### Evidence produced

- deterministic workflow export
- workflow screenshot
- baseline test logs
- first latency measurements

---

### Step 7 - Build the minimum agent-enhanced workflow

#### Chapter focus

- Chapter 4 - Choice of approach
- Chapter 5 - Implementation
- Chapter 7 - Discussion

#### Chapter 4 deliverables

- full multi-agent vs minimal workflow reasoning
- why model benchmarking is out of scope

#### Chapter 4 feeds from

- `docs/decisions.md`
- `cognitive_logic/memory/memory-choice-v1.md`

#### Chapter 5 deliverables

- minimal agent workflow
- prompt and memory design

#### Chapter 5 feeds from

- `cognitive_logic/workflows/agent-minimal.json`
- `cognitive_logic/prompts/system-prompt-v1.md`
- `cognitive_logic/memory/memory-choice-v1.md`

#### Chapter 7 deliverables

- discussion of the minimized Obid layer
- limitations of the agent-enhanced path

#### Chapter 7 feeds from

- why Obid was minimized
- agent limitations
- prompt/memory limitations

#### Goal

Add only enough workflow intelligence to make the integrated system valid.

#### Work to complete

Create:

- `cognitive_logic/workflows/agent-minimal.json`
- `cognitive_logic/workflows/agent-minimal.md`
- `cognitive_logic/prompts/system-prompt-v1.md`
- `cognitive_logic/memory/memory-choice-v1.md`

Keep it limited to:

- one workflow
- one prompt set
- one memory choice
- one decision path
- structured output following schema

Create:

- `cognitive_logic/workflows/agent-minimal.json`
- `cognitive_logic/prompts/system-prompt-v1.md`
- `cognitive_logic/memory/memory-choice-v1.md`

Keep it limited to:

- one workflow
- one prompt set
- one memory choice
- one decision path
- structured output following the shared contract

#### What this proves

This proves the system can support a minimal agent-enhanced path without becoming a full Obid thesis implementation.

#### Evidence produced

- workflow export
- prompt file
- memory rationale
- structured output logs
- screenshots

---

### Step 8 - Add the minimum safety layer

#### Chapter focus

- Chapter 5 - Implementation
- Chapter 6 - Results
- Chapter 7 - Discussion

#### Chapter 5 deliverables

- safety layer implementation
- validation/approval design

#### Chapter 5 feeds from

- `safety_layer/`
- `shared_interfaces/examples/`

#### Chapter 6 deliverables

- safety test results

#### Chapter 6 feeds from

- `allowed-case.md`
- `blocked-case.md`
- approval logs

#### Chapter 7 deliverables

- reliability discussion
- ethical and societal discussion around physical actions

#### Chapter 7 feeds from

- safety limitations
- blocked case interpretation
- human approval tradeoffs

#### Goal

Make the system safe enough to be academically defendable.

#### Work to complete

Create:

- `safety_layer/policies/action-policy-v1.md`
- `safety_layer/parsers/output-validation-v1.md`
- `safety_layer/approvals/hitl-v1.md`
- `safety_layer/examples/allowed-case.md`
- `safety_layer/examples/blocked-case.md`

Required cases:

- one valid allowed action
- one malformed blocked action
- one risky or unknown action requiring approval or rejection

Create:

- `safety_layer/policies/action-policy-v1.md`
- `safety_layer/parsers/output-validation-v1.md`
- `safety_layer/approvals/hitl-v1.md`

Required safety cases:

- one valid action that is allowed
- one malformed action that is blocked
- one risky or unknown action that requires approval or is rejected

#### What this proves

This proves that the workflow output cannot directly trigger middleware action without validation.

#### Evidence produced

- policy file
- parser/validation notes
- allowed case
- blocked case
- approval screenshot/log

- good output example
- bad output example
- blocked case
- approval checkpoint screenshot/log

---

## Phase 4: Testing and Writing

### Step 9 - Build the measurement and evaluation harness

#### Chapter focus

- Chapter 3 - Methodology
- Chapter 5 - Implementation
- Chapter 6 - Results

#### Chapter 3 deliverables

- evaluation method
- measurement method
- repeatability

#### Chapter 3 feeds from

- `docs/evaluation/evaluation-protocol.md`
- `scripts/collect_metrics.py`
- `scripts/aggregate_results.py`

#### Chapter 5 deliverables

- measurement/evaluation setup subsection

#### Chapter 5 feeds from

- measurement setup
- metrics scripts

#### Chapter 6 deliverables

- latency results
- RAM/CPU results
- safety outcomes
- baseline-vs-agent comparison

#### Chapter 6 feeds from

- `evaluation/results/`
- charts
- tables

#### Goal

Produce repeatable evidence for the report.

#### Work to complete

Create:

- `docs/evaluation/evaluation-protocol.md`
- `evaluation/datasets/`
- `evaluation/results/raw/`
- `evaluation/results/processed/`
- `evaluation/metrics/`
- `scripts/collect_metrics.py`
- `scripts/aggregate_results.py`

Run both modes:

1. deterministic baseline
2. agent-enhanced workflow with validation/approval

Measure:

- success/failure
- latency
- RAM
- CPU
- thermal data or thermal collection path
- safe vs blocked action behavior

#### Evidence produced

- `evaluation/results/raw/run_01.csv`
- `evaluation/results/raw/run_02.csv`
- `evaluation/results/processed/summary_latency.csv`
- `evaluation/results/processed/summary_resources.csv`
- `evaluation/results/processed/safety_outcomes.csv`
- `evaluation/results/processed/baseline_vs_agent.csv`

#### Minimum run count

- at least 5 runs per test case per mode, if time allows
- if time is limited, at least 3 runs per test case per mode

The exact number of runs must be documented in the Results chapter.

#### What this proves

This creates the thesis results.

---

### Step 10 - Add Raspberry Pi validation if the core system is stable

#### Chapter focus

- Chapter 4 - Choice of approach
- Chapter 5 - Implementation
- Chapter 6 - Results
- Chapter 7 - Discussion

#### Chapter 4 deliverables

- justification for PC-first then Pi validation

#### Chapter 4 feeds from

- PC-first vs Pi-first decision
- `docs/decisions.md`

#### Chapter 5 deliverables

- edge deployment notes

#### Chapter 5 feeds from

- `infrastructure/os/`
- Pi deployment notes

#### Chapter 6 deliverables

- optional Pi validation results

#### Chapter 6 feeds from

- `evaluation/results/pi-validation/`

#### Chapter 7 deliverables

- limitations and practical edge discussion

#### Chapter 7 feeds from

- Pi limitations
- edge hardware constraints
- local vs Pi comparison

#### Goal

Strengthen Yacoub's edge-computing angle by adding a thin Tier 1.5 hardware validation.

#### Work to complete

Only after local system works:

- deploy the same system or relevant parts to Raspberry Pi
- run the same or simplified scenario
- collect at least limited real-hardware measurements
- document differences between PC and Raspberry Pi behavior

#### Important constraint

Raspberry Pi validation must not block the local thesis system from being complete.

If time collapses, the thesis can still survive with the local Tier 1 proof of concept.

#### Evidence produced

- Pi deployment notes
- Pi test logs
- hardware measurement notes
- limitations discussion

---

### Step 11 - Freeze implementation

#### Chapter focus

- Chapter 5 - Implementation
- Chapter 7 - Discussion

#### Chapter 5 deliverables

- final implementation narrative

#### Chapter 5 feeds from

- final repo state
- final architecture
- final screenshots

#### Chapter 7 deliverables

- limitations
- work method reflection
- why scope was frozen

#### Chapter 7 feeds from

- final limitations
- deferred work
- frozen scope decisions

#### Goal

Stop expanding and protect the report-writing phase.

#### Work to complete

- fix bugs only
- no new devices
- no new workflows
- no new architecture
- no MCP unless already stable and necessary
- tag or document final implementation state

#### Evidence produced

- final Git commit/tag
- final screenshots
- `docs/decisions.md` final-state note
- workflow exports
- final architecture image

---

### Step 12 - Write Chapters 1-5 from artifacts

#### Goal

Write the first half of the thesis using already-produced material.

#### Chapter focus

- Chapter 1 - Introduction
- Chapter 2 - Theory
- Chapter 3 - Methodology
- Chapter 4 - Choice of approach
- Chapter 5 - Implementation

#### Evidence used

- `docs/ongoing/`
- `docs/plans/`
- `docs/decisions.md`
- `docs/architecture/`
- `infrastructure/`
- `middleware/`
- `shared_interfaces/`
- `cognitive_logic/`
- `safety_layer/`
- workflow screenshots

#### Chapter 1 deliverables

- background
- aim
- research questions
- scope
- AI tools usage
- division of work

#### Chapter 2 deliverables

- relevant theory
- related work

#### Chapter 3 deliverables

- scientific method
- project method
- evaluation method

#### Chapter 4 deliverables

- alternatives
- comparison
- chosen approach

#### Chapter 5 deliverables

- architecture
- infrastructure
- middleware
- contracts
- workflows
- safety
- measurement setup

#### Evidence produced

- draft Chapters 1-5
- missing figure/table checklist

---

### Step 13 - Write results and discussion

#### Goal

Turn the evidence into findings and interpretation.

#### Chapter focus

- Chapter 6 - Results
- Chapter 7 - Discussion

#### Evidence used

- `evaluation/results/`
- `evaluation/metrics/`
- screenshots
- workflow outputs
- allowed/blocked cases
- baseline-vs-agent results
- Pi validation results if available

#### Chapter 6 feeds from

- summary CSVs
- result tables
- charts
- screenshots
- test logs

#### Chapter 7 feeds from

- Chapter 6 results
- limitations
- scope decisions
- method reflections
- future work notes

#### Chapter 6 deliverables

- resulting system
- measurement results
- baseline-vs-agent comparison
- safety results
- optional Pi validation results

#### Chapter 7 deliverables

- analysis of results
- project/work method discussion
- scientific discussion
- consequence analysis/recommendation
- ethical and societal discussion

#### Evidence produced

- results chapter
- discussion chapter
- figures/tables

---

### Step 14 - Conclusions, polish, and submission package

#### Goal

Make the thesis submission-ready.

#### Chapter focus

- Chapter 8 - Conclusions

#### Chapter 8 deliverables

- direct answers to the research questions
- final conclusion
- future work

#### Chapter 8 feeds from

- research questions
- Chapter 6 results
- Chapter 7 discussion
- future work notes

#### Front matter feeds from

- final abstract
- Swedish sammanfattning
- keywords
- terminology list

#### Appendix A feeds from

- GitHub repo link
- source-code structure
- workflow exports
- result files

#### Prepare

- thesis PDF
- GitHub repo
- workflow exports
- result CSVs
- figures
- appendix/source-code link

#### Chapter deliverables

##### Abstract / Sammanfattning

- final short summary of aim, method, results, conclusion

##### Chapter 8

- direct answers to research questions
- final conclusion
- future work

##### Appendix A

- source-code link
- repo reference
- implementation artifact location

#### Evidence produced

- final abstract / sammanfattning
- Chapter 8
- Appendix A

---

## Phase Summary

### Step order

1. Lock scope
2. Create repo foundation
3. Build local n8n baseline
4. Build middleware skeleton
5. Define shared contract
6. Build deterministic baseline
7. Build minimal agent workflow
8. Add minimum safety layer
9. Build measurement and evaluation harness
10. Add Raspberry Pi validation if stable
11. Freeze implementation
12. Write Chapters 1-5 from artifacts
13. Write results and discussion
14. Conclusions, polish, and submission package

### Final process summary

Lock scope -> build local runtime -> build middleware -> define contract -> build baseline -> add minimal agent path -> add safety -> measure -> optionally validate on Pi -> freeze -> write report from artifacts.
