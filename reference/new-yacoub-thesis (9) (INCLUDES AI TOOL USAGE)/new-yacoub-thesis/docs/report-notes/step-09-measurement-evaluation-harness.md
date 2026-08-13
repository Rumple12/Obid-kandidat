# Step 09 - Measurement Evaluation Harness

## What was built

- A lightweight Step 9 measurement and evaluation harness was added.
- The harness uses standard-library Python scripts and CSV files rather than a heavy observability stack.
- `scripts/collect_metrics.py` collects workflow run data for deterministic, agent, and safety modes.
- `scripts/aggregate_results.py` aggregates raw CSV rows into processed summary CSV files.
- `evaluation/datasets/test-cases.json` defines deterministic, agent, and safety test cases.
- `evaluation/metrics/metrics-schema.md` documents the raw and processed CSV fields.
- Real raw CSV files and processed summaries now exist under `evaluation/results/`.

## Why it matters for the thesis

This step turns the implementation from a technical demo into something that can produce report evidence. It supports the thesis research questions about latency, RAM, CPU, thermal/resource behavior, safety outcomes, and deterministic-vs-agent comparison.

It also follows decision D-004 by using lightweight local logging and Docker/runtime statistics instead of Prometheus, Grafana, or another broad monitoring stack.

## Evidence produced

- `docs/evaluation/evaluation-protocol.md`
- `evaluation/README.md`
- `evaluation/datasets/test-cases.json`
- `evaluation/metrics/metrics-schema.md`
- `evaluation/results/step-09-small-measurement-notes.md`
- `scripts/collect_metrics.py`
- `scripts/aggregate_results.py`

Raw CSV evidence:

- `evaluation/results/raw/run_20260429T165733Z_deterministic.csv`
- `evaluation/results/raw/run_20260429T165859Z_agent.csv`
- `evaluation/results/raw/dump/run_20260429T165702Z_deterministic.csv`

Processed CSV evidence:

- `evaluation/results/processed/summary_latency.csv`
- `evaluation/results/processed/summary_resources.csv`
- `evaluation/results/processed/safety_outcomes.csv`
- `evaluation/results/processed/baseline_vs_agent.csv`

The small measurement notes record these commands:

```powershell
python scripts/collect_metrics.py --mode deterministic --webhook-url "http://localhost:5678/webhook/deterministic-baseline" --runs 1
python scripts/collect_metrics.py --mode agent --webhook-url "http://localhost:5678/webhook/agent-minimal" --runs 1
python scripts/aggregate_results.py
```

The successful small measurement run included both workflow modes:

- deterministic mode: high-temperature `fan_on` and low-temperature `fan_off`
- agent mode: high-temperature `fan_on` and low-temperature `fan_off`

An earlier deterministic run returned HTTP `404` because the production webhook was not registered. That file is stored under `evaluation/results/raw/dump/` and should be treated as setup/misconfigured-webhook evidence, not final result evidence.

## Report chapters it feeds

- Chapter 3 - Methodology: evaluation method, repeatability, run commands, and data collection format.
- Chapter 5 - Implementation: measurement harness, dataset, metrics schema, collection script, and aggregation script.
- Chapter 6 - Results: raw and processed CSV evidence for later latency, resource, and baseline-vs-agent tables.
- Chapter 7 - Discussion: measurement limitations, setup errors, Windows/PC thermal limitation, and best-effort resource collection.

## Limitations or assumptions

- Final evaluation is not complete.
- The current successful run count is small: one run per workflow mode for initial harness verification.
- Larger repeated runs can be done later for final report tables, following the protocol target of at least 3 runs per test case per mode if time is limited, or 5 if time allows.
- The processed summaries are current small-run artifacts and should be reviewed before final report use because the earlier deterministic `404` setup attempt is reflected in the generated deterministic counts.
- Safety cases are defined in the dataset, but the current `safety_outcomes.csv` does not demonstrate runtime safety enforcement.
- Thermal data is currently `not_available` on the Windows/PC setup.
- CPU and RAM values are best-effort Docker/runtime values collected through `docker stats --no-stream` when available.
- No Raspberry Pi validation was started in this step.
- No charts or diagrams were created in this step.

## Screenshots/logs still needed

- Larger repeated raw CSV runs for deterministic and agent modes.
- Runtime safety-mode evidence after enforcement exists, if safety results are to be claimed.
- Final cleaned processed summaries for report tables.
- Terminal logs or screenshots showing the collection and aggregation commands running.
- Thermal collection evidence if Raspberry Pi validation is later performed.
- Charts or diagrams later, after final result CSVs are stable.
