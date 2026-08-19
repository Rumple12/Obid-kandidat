# Evaluation Harness

This folder contains the Step 9 lightweight measurement and evaluation harness.

It is intentionally small:

- standard-library Python scripts only
- CSV input/output
- no Prometheus or Grafana
- no Raspberry Pi deployment
- no fake result data

## Structure

- `datasets/test-cases.json` - minimal deterministic, agent, and safety cases
- `results/raw/` - raw CSV files produced by `scripts/collect_metrics.py`
- `results/processed/` - summary CSV files produced by `scripts/aggregate_results.py`
- `metrics/metrics-schema.md` - raw and processed result field notes

## Collect Workflow Metrics

Start n8n and middleware first. Then run one of these from the repository root,
using the test webhook URL shown in n8n.

Deterministic baseline:

```powershell
python scripts/collect_metrics.py --mode deterministic --webhook-url "<deterministic-test-webhook-url>" --runs 3
```

Agent-enhanced workflow:

```powershell
python scripts/collect_metrics.py --mode agent --webhook-url "<agent-test-webhook-url>" --runs 3
```

Safety cases are documentation/specification-level in Step 8. They can be
recorded with:

```powershell
python scripts/collect_metrics.py --mode safety --runs 1
```

The safety command does not prove runtime enforcement. It records the expected
case outcomes defined by the Step 8 safety artifacts.

## Aggregate Results

```powershell
python scripts/aggregate_results.py
```

Processed summaries are written to:

```text
evaluation/results/processed/
```

## Evidence Rule

Do not place example or fake CSV files in `results/raw/`. Only real collection
runs should create raw result files.
