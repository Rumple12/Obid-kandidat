# new-yacoub-thesis

## What this repository is

This repository contains the implementation, planning documents, and report-support material for the **new-yacoub** bachelor thesis plan.

**new-yacoub** means:

- the original broader Yacoub/Obid thesis scope has been narrowed
- **Yacoub's thesis is the primary delivery target**
- only the **minimum Obid-compatible workflow, safety, and contract layers** are included
- the project is intentionally kept small, measurable, and pass-oriented

This repository is **not** a full dual-thesis implementation target.

---

## Primary objective

Complete Yacoub's thesis in a narrowed but complete form.

This includes:

- self-hosted n8n baseline
- Docker-based local runtime
- middleware/API bridge
- one sensor/event path
- one actuator/action path
- latency, RAM, CPU, and thermal/resource measurement support
- a reportable evaluation flow

---

## Secondary objective

Implement only the minimum Obid-compatible layer required for:

- workflow integration
- safety/validation
- shared contract definition
- evaluation support
- future handoff

This minimum layer is limited to:

- one workflow
- one prompt set
- one memory choice
- one JSON contract boundary
- one validation rule
- one human approval checkpoint

---

## Narrowed scope

The thesis focuses on **one complete end-to-end IoT scenario**.

Current intended scenario:

- temperature event
- middleware pushes event to n8n
- workflow decides whether a fan action is needed
- validation/approval checks the action
- middleware executes `/fan/on` or `/fan/off`
- metrics are logged

### Explicit non-goals

The following are out of scope unless the primary thesis is already complete:

- broad multi-agent systems
- elaborate ReAct expansion
- multiple memory strategies
- multiple devices/models
- deep n8n internals modification
- broad guardrail research
- heavy observability stacks such as Prometheus/Grafana
- early MCP integration

---

## Current status

The repository is in the **Step 11 implementation-freeze phase**.

Frozen Tier 1.5 implementation state:

- local n8n Docker baseline
- Python middleware implementation
- deterministic baseline workflow
- minimal agent-enhanced workflow
- shared JSON contract files
- minimum safety/validation design
- lightweight evaluation harness and CSV outputs
- Raspberry Pi validation where n8n stayed on the PC and the middleware/action endpoint ran on Raspberry Pi

Further work should focus on report writing, analysis, figure/table cleanup, and narrow bug fixes only.

---

## Local n8n baseline

The Step 3 local self-hosted n8n baseline lives in `infrastructure/docker/`.

Quick start:

```powershell
cd infrastructure/docker
Copy-Item .env.example .env
docker compose up -d
```

Then open `http://localhost:5678`.

---

## Evaluation harness

The Step 9 lightweight evaluation harness lives in `evaluation/` and `scripts/`.

Useful entry points:

```powershell
python scripts/collect_metrics.py --help
python scripts/aggregate_results.py --help
```

Raw run CSVs belong in `evaluation/results/raw/`; processed summaries belong in
`evaluation/results/processed/`.

---

## Optional Raspberry Pi validation

Step 10 Raspberry Pi validation is optional Tier 1.5 evidence. The local PC
system remains the primary baseline.

Notes and result location:

- `infrastructure/os/raspberry-pi-notes.md`
- `infrastructure/docker/pi-deployment-notes.md`
- `evaluation/results/pi-validation/`

---

## Repo structure

### High-priority implementation areas

- `infrastructure/`  
  Runtime, Docker, local self-hosted n8n, deployment assumptions, monitoring hooks

- `middleware/`  
  Python API, mock/real sensor path, webhook bridge, actuator endpoints

- `evaluation/`  
  Datasets, result files, measurement outputs, evaluation protocol

- `docs/`  
  Thesis planning, decisions, report support, architecture notes

### Minimum integration only

- `cognitive_logic/`  
  One workflow, one prompt set, one memory choice

- `safety_layer/`  
  One validation path, one approval path, one blocked/unsafe case

- `shared_interfaces/`  
  JSON schemas, example payloads, contract boundary between middleware and workflow logic

---

## Source-of-truth hierarchy

Use this order when making decisions:

1. `docs/plans/implementation-plan.md`
2. `docs/ongoing/yacoub-scope.md`
3. `docs/ongoing/integration-contract.md`
4. `docs/decisions.md`
5. active planning and reference files under `docs/plans/`

## Working style

This project should be built in **small vertical slices**.

Preferred order:

1. planning/specification lock
2. local n8n baseline
3. middleware baseline
4. contract baseline
5. deterministic baseline path
6. minimal workflow path
7. minimal safety path
8. metrics/evaluation
9. report writing from evidence

Every meaningful step should be:

- testable
- commit-worthy
- small enough to review

---

## Git discipline

Use:

- one feature = one branch
- one clean checkpoint = one commit

Do not batch many unrelated changes into one commit.

---

## Report alignment

This repo is structured to support the official MIUN thesis template.

The report will later be built around:

- Introduction
- Theory
- Methodology
- Choice of approach
- Implementation
- Results
- Discussion
- Conclusions
- Appendix A: Source Code

The repo exists to produce **evidence** for those chapters.

---

## Notes

If there is a conflict between:
- a broad historical plan
- a cool technical idea
- and the narrowed thesis implementation plan

the **new-yacoub implementation plan wins**.
