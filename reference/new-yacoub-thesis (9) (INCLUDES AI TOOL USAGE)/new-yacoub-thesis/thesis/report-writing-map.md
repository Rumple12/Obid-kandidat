# Thesis Report Writing Map

Status: first-task skeleton map for the narrowed new-yacoub DT099G thesis.

This map follows the existing MIUN LaTeX template at:

- `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/thesis.tex`

The repository already contained a LaTeX template, so no separate `thesis/main.tex`
tree was created. The template uses `literature.bib` rather than
`references.bib`.

## Global Scope Rules

- Write an argument, not a step-by-step project diary.
- Treat `docs/plans/implementation-plan.md`, `docs/ongoing/yacoub-scope.md`,
  `infrastructure/`, `middleware/`, `evaluation/`, and `docs/decisions.md` as
  the primary implementation scope sources.
- Use `docs/report-notes/*.md` and `docs/report-notes/final-evidence-inventory.md`
  as evidence summaries, not final prose.
- Do not claim full n8n-on-Raspberry-Pi deployment.
- Do not claim real GPIO hardware or physical fan control.
- Do not claim production-grade safety enforcement.
- Do not expand into broad multi-agent architecture, broad model benchmarking,
  or multiple-device evaluation.
- Use `[CHECK VALUE: path/file]` when a measurement or claim needs verification.
- Use `[REFERENCE NEEDED: topic]` until a verified source is added to the
  bibliography.

## Template and Course Sources

| Item | Source | Use |
|---|---|---|
| Course expectations | `docs/course/DT099G information 2026-1 (1) (1).pdf` | Scientific method, systematic problem solving, evaluation, discussion/conclusion, ethical and societal reflection, presentation/submission context. |
| Report template | `docs/templates/Miun ThesisTemplate 2026-01-21 (1).docx` | Required sections, abstract/sammanfattning, AI tools section, division of work, terminology, appendix/source-code guidance. |
| LaTeX output template | `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/` | Build format and front matter layout. |

## Front Matter Map

| File/section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| `00-abstract.tex` | Final Chapters 3-7; `evaluation/results/processed/*.csv`; `evaluation/results/pi-validation/pi-workflow-run-final.csv` | `final-evidence-inventory.md` | No figures; summarize only final verified values | None in abstract | `[CHECK VALUE: final 200-250 word abstract after Results/Discussion]` |
| `00-sammanfattning.tex` | Final English abstract | None | No figures | None | `[CHECK VALUE: Swedish translation after English abstract is stable]` |
| `00-terminology.tex` | `README.md`; `docs/architecture/README.md`; `shared_interfaces/json-schema/*.json`; `evaluation/metrics/metrics-schema.md` | Steps 5, 8, 9, 10, 11 | Terminology table scaffold | None | Define Tier 1.5, JSON contract, HITL, GPIO limitation carefully |
| `00-acknowledgements.tex` | Author decision | None | None | None | `[CHECK VALUE: keep or remove optional section]` |

## Chapter 1 - Introduction

| Section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| 1.1 Background and Motivation | `README.md`; `docs/architecture/README.md` | Step 1 | Optional reference to final architecture figure | `[REFERENCE NEEDED: IoT/edge computing source]`; `[REFERENCE NEEDED: workflow automation/orchestration source]`; `[REFERENCE NEEDED: n8n documentation]` | Frame fan as proxy, not final real-world deployment |
| 1.2 Problem Statement | `docs/plans/implementation-plan.md`; `docs/decisions.md`; `README.md` | Step 11 | None | None | `[CHECK VALUE: final problem statement]`; keep it measurable |
| 1.3 Aim | `docs/plans/implementation-plan.md`; `docs/ongoing/yacoub-scope.md` | Step 1 | None | None | `[CHECK VALUE: aim aligned to RQ1-RQ3]` |
| 1.4 Research Questions | User-approved RQ wording; check `docs/ongoing/research-questions.md` only for history | Step 1 | None | None | Use only the 3 approved RQs; no separate safety RQ |
| 1.5 Scope and Limitations | `docs/ongoing/yacoub-scope.md`; `docs/decisions.md` | `final-evidence-inventory.md`; Step 11 | Optional scope table | None | State simulated fan, no GPIO, no full n8n-on-Pi, no production safety |
| 1.6 Contributions | `docs/report-notes/step-11-implementation-freeze.md`; `final-evidence-inventory.md` | Step 11 | None | None | `[CHECK VALUE: supervisor name and final CRediT-style roles]` |
| 1.7 Usage of AI Tools | `AGENTS.md`; final author workflow notes | Step notes if relevant | None | `[REFERENCE NEEDED: university/course AI-use policy if required]` | Must state author responsibility; do not overstate AI role |
| 1.8 Division of Work / Author Contribution | Final author/supervisor notes | All steps | None | None | `[CHECK VALUE: confirm single-author wording and external help]` |
| 1.9 Report Outline | Current LaTeX skeleton | None | None | None | Update after final chapter titles are stable |

## Chapter 2 - Theory and Related Work

| Section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Workflow Automation and Orchestration | `docs/architecture/README.md`; `infrastructure/docker/README.md` | Steps 1, 3 | None | `[REFERENCE NEEDED: workflow automation/orchestration source]` | Keep focused on event-action orchestration |
| n8n as a Workflow Automation Platform | `docs/n8n-version.md`; `infrastructure/docker/docker-compose.yml`; `cognitive_logic/workflows/*.md` | Steps 3, 6, 7 | Workflow figures later in Chapter 5 | `[REFERENCE NEEDED: n8n official documentation]` | Discuss only used n8n features |
| Middleware and API Boundary Design | `middleware/api/app.py`; `middleware/api/routes.py`; `middleware/webhooks/n8n_sender.py` | Step 4 | Optional endpoint table | `[REFERENCE NEEDED: middleware/API design source]` | List only real endpoints from repository |
| IoT-Style Event-Action Systems | `evaluation/datasets/test-cases.json`; `shared_interfaces/json-schema/sensor-event.schema.json` | Steps 4, 5 | None | `[REFERENCE NEEDED: IoT event/action or edge computing source]` | Fan is controlled proxy only |
| JSON Contracts and Structured Action Formats | `shared_interfaces/json-schema/*.json`; `shared_interfaces/examples/*.json` | Step 5 | Optional schema field table | `[REFERENCE NEEDED: JSON Schema documentation]` | Do not imply runtime enforcement beyond evidence |
| Deterministic and Minimal Agent-Enhanced Workflows | `cognitive_logic/workflows/deterministic-baseline.md`; `cognitive_logic/workflows/agent-minimal.md`; `cognitive_logic/prompts/system-prompt-v1.md`; `cognitive_logic/memory/memory-choice-v1.md` | Steps 6, 7 | Figures in Chapter 5 | `[REFERENCE NEEDED: LLM agent workflow or structured-output source]` | Do not broaden to multi-agent architecture |
| Safety Validation and HITL Concepts | `safety_layer/policies/action-policy-v1.md`; `safety_layer/parsers/output-validation-v1.md`; `safety_layer/approvals/hitl-v1.md`; `safety_layer/examples/*.md` | Step 8 | Optional safety-case table | `[REFERENCE NEEDED: safety validation or human-in-the-loop source]` | Minimum design/case evidence only |
| Edge Computing and Raspberry Pi Context | `infrastructure/os/raspberry-pi-notes.md`; `infrastructure/docker/pi-deployment-notes.md`; `evaluation/results/pi-validation/README.md` | Step 10 | None | `[REFERENCE NEEDED: Raspberry Pi documentation]`; `[REFERENCE NEEDED: edge computing source]` | State n8n stayed on PC |
| Related Work | None yet | None | Optional related-work comparison table | `[REFERENCE NEEDED: 2-4 related scientific works]` | Do not invent citations |

## Chapter 3 - Methodology

| Section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Scientific Method Description | `docs/plans/implementation-plan.md`; `docs/ongoing/yacoub-scope.md`; `docs/decisions.md` | Step 1 | Optional method flow figure | `[REFERENCE NEEDED: design science or proof-of-concept methodology source if used]` | `[CHECK VALUE: final methodology label]` |
| Controlled Temperature-to-Fan Scenario | `evaluation/datasets/test-cases.json`; `shared_interfaces/examples/sensor-event.example.json` | Steps 5, 9 | Test-case table | None | Confirm threshold and expected actions from workflow artifacts |
| Deterministic Baseline Evaluation | `cognitive_logic/workflows/deterministic-baseline.md`; `scripts/collect_metrics.py` | Steps 6, 9 | Action-correctness table later | None | `[CHECK VALUE: final valid run count]` |
| Minimal Agent-Enhanced Evaluation | `cognitive_logic/workflows/agent-minimal.md`; `cognitive_logic/prompts/system-prompt-v1.md`; `shared_interfaces/json-schema/agent-action.schema.json` | Steps 7, 9 | Baseline-vs-agent table later | `[REFERENCE NEEDED: structured LLM output source if cited]` | Include contract-validity in RQ2 |
| Contract-Validity and Safety Case Evaluation | `shared_interfaces/json-schema/agent-action.schema.json`; `safety_layer/examples/*.md`; `evaluation/results/processed/safety_outcomes.csv` | Steps 5, 8, 9 | Safety-case table | `[REFERENCE NEEDED: JSON Schema documentation]` | `safety_outcomes.csv` currently has headers only |
| CSV-Based Evaluation Harness | `scripts/collect_metrics.py`; `scripts/aggregate_results.py`; `evaluation/metrics/metrics-schema.md`; `evaluation/results/raw/*.csv`; `evaluation/results/processed/*.csv` | Step 9 | None | None | Verify processed files do not mix setup failures into final reported counts |
| Local Execution Measurement | `evaluation/results/processed/summary_latency.csv`; `evaluation/results/processed/summary_resources.csv`; `evaluation/results/step-09-small-measurement-notes.md` | Step 9 | Local latency/resource table | `[REFERENCE NEEDED: Docker stats documentation if discussed]` | Local thermal is `not_available` |
| Raspberry Pi Tier 1.5 Validation | `evaluation/results/pi-validation/pi-workflow-run-final.csv`; `evaluation/results/pi-validation/pi-validation-notes.md`; `infrastructure/os/raspberry-pi-notes.md` | Step 10 | Pi validation table/screenshot | `[REFERENCE NEEDED: Raspberry Pi documentation]` | n8n stayed on PC; no real GPIO |
| Methodological Limitations | `final-evidence-inventory.md`; Step 9 and Step 10 notes | Steps 9, 10, 11 | Optional limitations table | None | Reuse in Chapter 7 |

## Chapter 4 - Choice of Approach / System Design

| Section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Narrowed Tier 1.5 Scope | `docs/plans/implementation-plan.md`; `docs/ongoing/yacoub-scope.md`; `docs/decisions.md` | Steps 1, 11 | Optional scope comparison table | None | Avoid old Yacoub/Obid broader scope |
| PC-Hosted n8n Runtime | `infrastructure/docker/docker-compose.yml`; `docs/n8n-version.md`; `docs/decisions.md` D-011 | Step 3 | None | `[REFERENCE NEEDED: Docker documentation]`; `[REFERENCE NEEDED: n8n documentation]` | No full n8n-on-Pi claim |
| Python Middleware Boundary | `middleware/api/app.py`; `middleware/api/routes.py`; `middleware/gpio/mock_sensor.py`; `middleware/webhooks/n8n_sender.py` | Step 4 | Optional endpoint table | `[REFERENCE NEEDED: middleware/API design source if needed]` | Only list endpoints present in code |
| Shared JSON Contracts | `shared_interfaces/json-schema/*.json`; `shared_interfaces/examples/*.json`; `docs/ongoing/integration-contract.md` | Step 5 | Optional contract table | `[REFERENCE NEEDED: JSON Schema documentation]` | Do not overclaim runtime enforcement |
| Simulated Fan Action Path | `middleware/api/routes.py`; `middleware/gpio/mock_sensor.py` | Step 4 | None | None | No physical fan/GPIO |
| Deterministic and Agent-Enhanced Comparison | `cognitive_logic/workflows/deterministic-baseline.md`; `cognitive_logic/workflows/agent-minimal.md` | Steps 6, 7 | Workflow figures in Chapter 5 | `[REFERENCE NEEDED: LLM workflow or structured-output source if used]` | Model/provider is not comparison axis |
| Final Architecture | `docs/architecture/final-architecture-report.md`; `docs/architecture/final-architecture-report.mmd`; copied `Figures/final-architecture-report.png` | Step 11 | `Figure: final architecture` | None | Check PDF readability |

## Chapter 5 - Implementation

| Section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Infrastructure Setup | `infrastructure/docker/docker-compose.yml`; `infrastructure/docker/README.md`; `infrastructure/docker/evidence/*`; `docs/n8n-version.md` | Step 3 | Optional n8n runtime screenshot | `[REFERENCE NEEDED: Docker documentation]`; `[REFERENCE NEEDED: n8n documentation]` | Keep runtime simple; no heavy observability stack |
| Middleware API Bridge | `middleware/api/app.py`; `middleware/api/routes.py`; `middleware/gpio/mock_sensor.py`; `middleware/webhooks/n8n_sender.py`; `middleware/tests/manual-test-notes.md` | Step 4 | Optional endpoint table | None | Fan state simulated in memory |
| Shared Interfaces and Contracts | `shared_interfaces/json-schema/*.json`; `shared_interfaces/examples/*.json` | Step 5 | Contract table | `[REFERENCE NEEDED: JSON Schema documentation]` | Contract boundary explicit |
| Deterministic Baseline Workflow | `cognitive_logic/workflows/deterministic-baseline.md`; `cognitive_logic/workflows/deterministic-baseline.json`; `cognitive_logic/workflows/evidence/step-06-runtime-verification.md`; copied `Figures/deterministic-baseline-canvas.png` | Step 6 | `Figure: deterministic workflow canvas` | n8n docs if needed | `[CHECK VALUE: exact threshold rule]` |
| Minimal Agent-Enhanced Workflow | `cognitive_logic/workflows/agent-minimal.md`; `cognitive_logic/workflows/agent-minimal.json`; `cognitive_logic/prompts/system-prompt-v1.md`; `cognitive_logic/memory/memory-choice-v1.md`; copied `Figures/agent-workflow-canvas.png` | Step 7 | `Figure: agent workflow canvas` | `[REFERENCE NEEDED: structured LLM output source if used]` | Stateless/no-memory; not multi-agent |
| Minimum Safety and Validation Design | `safety_layer/policies/action-policy-v1.md`; `safety_layer/parsers/output-validation-v1.md`; `safety_layer/approvals/hitl-v1.md`; `safety_layer/examples/*.md` | Step 8 | Optional safety-case table | `[REFERENCE NEEDED: HITL/validation source if cited]` | Design/case evidence, not production enforcement |
| Evaluation Harness | `evaluation/datasets/test-cases.json`; `evaluation/metrics/metrics-schema.md`; `scripts/collect_metrics.py`; `scripts/aggregate_results.py`; `evaluation/README.md` | Step 9 | Optional data-flow table | None | Exclude non-final setup files in reporting |
| Raspberry Pi Middleware/Action Endpoint Validation | `infrastructure/os/raspberry-pi-notes.md`; `infrastructure/docker/pi-deployment-notes.md`; `evaluation/results/pi-validation/*` | Step 10 | Pi screenshot in Chapter 6 | `[REFERENCE NEEDED: Raspberry Pi documentation]` | n8n on PC, Pi runs middleware/action endpoint only |

## Chapter 6 - Results

| Section | Result files | Report notes | Figures/tables | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Deterministic Workflow Action Correctness | `evaluation/results/processed/baseline_vs_agent.csv`; `evaluation/results/raw/run_20260429T165733Z_deterministic.csv` | Steps 6, 9 | Final action-correctness table | None | `[CHECK VALUE: verify processed deterministic rows because setup failure may be included]` |
| Agent-Enhanced Workflow Output Correctness | `evaluation/results/processed/baseline_vs_agent.csv`; `evaluation/results/raw/run_20260429T165859Z_agent.csv` | Steps 7, 9 | Baseline-vs-agent comparison table | None | `[CHECK VALUE: contract-validity count]` |
| Contract Validity and Safety Outcomes | `evaluation/results/processed/safety_outcomes.csv`; `shared_interfaces/json-schema/agent-action.schema.json`; `safety_layer/examples/*.md` | Steps 5, 8, 9 | Safety-case table | None | `safety_outcomes.csv` currently has headers only |
| Latency Results | `evaluation/results/processed/summary_latency.csv`; `evaluation/results/pi-validation/pi-workflow-run-final.csv` | Steps 9, 10 | Final latency table/chart | None | `[CHECK VALUE: local latency values after cleanup]`; Pi CSV has final observed rows |
| Resource and Thermal Behavior | `evaluation/results/processed/summary_resources.csv`; `evaluation/results/pi-validation/pi-validation-notes.md`; `evaluation/results/pi-validation/3. Measure CPU_RAM of the middleware process.png`; `evaluation/results/pi-validation/pi-temp-measurement.png` | Steps 9, 10 | Resource/thermal table | None | Local thermal not available; Pi values are limited endpoint/middleware validation evidence |
| Raspberry Pi Tier 1.5 Validation Observations | `evaluation/results/pi-validation/pi-workflow-run-final.csv`; `evaluation/results/pi-validation/pi-validation-notes.md`; copied `Figures/pi-validation-fan-on-output.png` | Step 10 | `Figure: Pi validation output`; Pi validation table | None | Do not imply full Pi deployment |
| Missing or Limited Measurements | `final-evidence-inventory.md`; Step 9 note; Step 10 note | Steps 9, 10, 11 | Optional missing-data table | None | Be explicit before interpretation |

## Chapter 7 - Discussion

| Section | Source/result files | Report notes | Figures/tables | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Limitations of the Evidence | `final-evidence-inventory.md`; `evaluation/results/step-09-small-measurement-notes.md` | Steps 9, 10, 11 | Optional limitations table | None | Put limitations early |
| Answer to RQ1 | Chapter 6 deterministic results | Steps 6, 9 | Refer to Chapter 6 table | None | `[CHECK VALUE: deterministic success counts]` |
| Answer to RQ2 | Chapter 6 agent/contract results; `agent-action.schema.json` | Steps 7, 9 | Refer to Chapter 6 table | `[REFERENCE NEEDED: structured output source if used]` | Safety/contract evaluated under RQ2 |
| Answer to RQ3 | `summary_latency.csv`; `summary_resources.csv`; `pi-workflow-run-final.csv`; Pi notes | Steps 9, 10 | Refer to Chapter 6 tables | `[REFERENCE NEEDED: edge computing source if used]` | Separate local and Pi observations |
| Deterministic vs Agent-Enhanced Comparison | Workflow docs and result CSVs | Steps 6, 7, 9 | Comparison table | `[REFERENCE NEEDED: LLM workflow source if cited]` | Agent adds structured decision path only |
| Contract and Safety Limitations | `shared_interfaces/`; `safety_layer/`; `docs/decisions.md` | Steps 5, 8, 11 | Safety-case table if used | `[REFERENCE NEEDED: safety/HITL source]` | No production-grade enforcement |
| Tier 1.5, Not Full Edge Deployment | `evaluation/results/pi-validation/`; `docs/decisions.md` D-003, D-012 | Step 10 | Pi validation figure/table | `[REFERENCE NEEDED: Raspberry Pi documentation]`; `[REFERENCE NEEDED: edge computing source]` | n8n stayed on PC |
| Broader Use-Case Relevance | `docs/architecture/README.md`; final architecture figure | None | None | `[REFERENCE NEEDED: smart building or industrial IoT source if making contextual claims]` | Smart building, industrial, environmental, and health/environment contexts are possible extensions only |
| Threats to Validity | `evaluation/README.md`; `final-evidence-inventory.md` | Steps 9, 11 | Optional validity table | `[REFERENCE NEEDED: validity/methodology source if used]` | Small controlled evidence base |
| Ethical and Societal Discussion | `safety_layer/`; `docs/decisions.md`; Chapter 1 AI tools section | Step 8 | None | `[REFERENCE NEEDED: AI/automation safety or human oversight source if used]` | Follow DT099G ethical/societal requirement |

## Chapter 8 - Conclusions

| Section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Conclusion | Chapters 6-7; `docs/decisions.md` D-013 | Step 11 | None | None | `[CHECK VALUE: final conclusion wording]` |
| Answers to the Research Questions | Final Chapter 6 values and Chapter 7 answers | Steps 6-10 | Optional summary table | None | Directly answer RQ1-RQ3 |
| What Was Achieved | `final-evidence-inventory.md`; Step 11 | Step 11 | None | None | Keep achievement list evidence-bound |
| What Was Not Achieved | `docs/decisions.md`; `final-evidence-inventory.md` | Step 11 | None | None | Repeat key limits: no full Pi deployment, no GPIO, no production safety |
| Future Work | Chapter 7 limitations and broader-use-case section | None | None | `[REFERENCE NEEDED: future-work references only if making technical recommendations]` | Future work must be framed as extension, not result |

## Appendix A - Source Code and Artifacts

| Section | Source files | Report notes | Figures/tables/results | References needed | Missing and scope notes |
|---|---|---|---|---|---|
| Repository Reference | GitHub repository `Rumple12/new-yacoub-thesis`; local repo | Step 2, Step 11 | None | None | `[CHECK VALUE: final URL and commit/tag]` |
| Workflow and Screenshot Evidence | `cognitive_logic/workflows/`; `cognitive_logic/workflows/evidence/` | Steps 6, 7 | Extra screenshots not used in main report | None | Do not overload main report with screenshots |
| Evaluation Artifacts | `evaluation/results/raw/`; `evaluation/results/processed/`; `evaluation/results/pi-validation/` | Steps 9, 10 | CSV inventory | None | Mark non-final setup files clearly |

## Copied Main-Report Figure Assets

| Clean figure | Original source | Intended location |
|---|---|---|
| `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/Figures/final-architecture-report.png` | `docs/architecture/final-architecture-report.mmd.png` | Chapter 4 |
| `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/Figures/deterministic-baseline-canvas.png` | `cognitive_logic/workflows/evidence/full tree.png` | Chapter 5 |
| `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/Figures/agent-workflow-canvas.png` | `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-canvas.png` | Chapter 5 |
| `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/Figures/pi-validation-fan-on-output.png` | `evaluation/results/pi-validation/pi-high-temp-fan-on-output.png` | Chapter 6 |

## Missing or To-Check Items

- `[CHECK VALUE: final thesis title]`
- `[CHECK VALUE: author name]`
- `[CHECK VALUE: supervisor name]`
- `[CHECK VALUE: examiner name]`
- `[CHECK VALUE: registration number]`
- `[CHECK VALUE: study programme or course]`
- `[CHECK VALUE: final repository URL and commit/tag]`
- `[CHECK VALUE: processed local result tables after deciding whether setup failures are excluded]`
- `[CHECK VALUE: contract-validity count for agent outputs]`
- `[CHECK VALUE: final safety outcome wording because safety_outcomes.csv currently has headers only]`
- `[FIGURE NEEDED: result chart/table if a chart is required rather than CSV-derived tables]`
- `[FIGURE NEEDED: optional Gantt chart only if quick and useful]`

## Reference Placeholders

- `[REFERENCE NEEDED: n8n official documentation]`
- `[REFERENCE NEEDED: Docker documentation]`
- `[REFERENCE NEEDED: Raspberry Pi documentation]`
- `[REFERENCE NEEDED: IoT / edge computing scientific source]`
- `[REFERENCE NEEDED: agentic AI or LLM agent workflow scientific source]`
- `[REFERENCE NEEDED: workflow automation / orchestration source]`
- `[REFERENCE NEEDED: safety / human-in-the-loop or validation source]`
- `[REFERENCE NEEDED: JSON Schema documentation]`
- `[REFERENCE NEEDED: middleware/API design source if used]`
- `[REFERENCE NEEDED: design science or proof-of-concept methodology source if used]`
- `[REFERENCE NEEDED: smart building or industrial IoT source if making broader contextual claims]`

## Recommended Writing Order

1. Chapter 5 Implementation
2. Chapter 4 Choice of Approach / System Design
3. Chapter 6 Results
4. Chapter 3 Methodology
5. Chapter 7 Discussion
6. Chapter 1 Introduction
7. Chapter 2 Theory and Related Work
8. Abstract and Sammanfattning last
