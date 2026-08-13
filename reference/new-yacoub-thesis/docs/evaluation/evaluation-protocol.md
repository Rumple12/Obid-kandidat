# Evaluation protocol

This document defines the minimum evaluation protocol for the **new-yacoub** thesis.

The purpose is to make sure the implementation produces measurable evidence for the report, instead of becoming only a technical demo.

## Evaluation goal

Evaluate one small end-to-end n8n-based IoT scenario in two modes:

1. deterministic baseline
2. minimal agent-enhanced workflow with validation/approval

The evaluation focuses on:

- successful execution
- latency
- RAM usage
- CPU usage
- thermal/resource behavior
- safe vs blocked action handling

## Scenario

The evaluation scenario is:

```text
Temperature event
  -> middleware receives or generates the event
  -> middleware pushes the event to n8n
  -> workflow decides whether fan action is needed
  -> validation checks the proposed action
  -> approval is required if the action is risky or malformed
  -> middleware executes /fan/on or /fan/off
  -> metrics are logged
```

## Compared modes

### Mode A - Deterministic baseline

The deterministic baseline uses a fixed rule.

Example:

```text
if temperature > threshold:
    request fan_on
else:
    request fan_off or no action
```

This mode is used as the comparison anchor.

Step 9 collection command:

```powershell
python scripts/collect_metrics.py --mode deterministic --webhook-url "<deterministic-test-webhook-url>" --runs 3
```

### Mode B - Agent-enhanced path

The agent-enhanced path uses one minimal workflow/prompt setup to produce a structured action decision.

The output must follow the shared action contract and pass validation before execution.

This mode must stay minimal and must not expand into broad multi-agent architecture.

Step 9 collection command:

```powershell
python scripts/collect_metrics.py --mode agent --webhook-url "<agent-test-webhook-url>" --runs 3
```

### Mode C - Safety cases

Safety cases are based on the Step 8 safety design and case documentation.

Step 9 can record the expected safety outcomes, but this does not prove runtime
enforcement unless a later implementation adds and tests enforcement logic.

```powershell
python scripts/collect_metrics.py --mode safety --runs 1
```

## Minimum test cases

The first evaluation must include at least these cases:

| Case | Input | Expected result |
| --- | --- | --- |
| T1 | valid high temperature event | fan_on allowed |
| T2 | valid low temperature event | fan_off or no action |
| T3 | malformed sensor event | blocked or rejected |
| T4 | malformed action output | blocked |
| T5 | unsupported action | blocked or approval required |

Concrete Step 9 cases are stored in:

`evaluation/datasets/test-cases.json`

## Metrics to collect

For each run, collect:

- timestamp
- mode (deterministic or agent_enhanced)
- test case id
- input temperature
- action requested
- action allowed/blocked
- success/failure
- end-to-end latency
- CPU usage
- RAM usage
- thermal value or thermal collection status
- notes/errors

The raw CSV field definitions are documented in:

`evaluation/metrics/metrics-schema.md`

Latency is measured in `scripts/collect_metrics.py` with Python's
`time.perf_counter()` around the webhook HTTP request.

RAM and CPU are best-effort only. If Docker is available, the collector attempts
`docker stats --no-stream` against the n8n container. If Docker stats are not
available, resource fields are written as `not_available`.

Thermal data is not faked. On Windows/PC it is written as `not_available` unless
a local thermal source is available. Raspberry Pi thermal collection can be
added later in Step 10, for example with `vcgencmd measure_temp`.

## Optional Raspberry Pi Validation

Raspberry Pi validation is optional Tier 1.5 evidence. It is separate from the
primary PC/local evaluation.

Pi validation may use:

- the same temperature-to-fan scenario
- a simplified middleware-only scenario if n8n/Docker is too heavy
- limited CPU/RAM/thermal observations

Pi evidence should be saved under:

`evaluation/results/pi-validation/`

Do not claim Pi deployment or Pi measurement results unless they were actually
run on a Raspberry Pi. If Pi validation is not completed, the local PC results
remain the thesis baseline.

## Suggested result format

Raw results should be stored in:

`evaluation/results/raw/`

Processed summaries should be stored in:

`evaluation/results/processed/`

Suggested files:

- `evaluation/results/raw/run_01.csv`
- `evaluation/results/raw/run_02.csv`
- `evaluation/results/processed/summary_latency.csv`
- `evaluation/results/processed/summary_resources.csv`
- `evaluation/results/processed/safety_outcomes.csv`
- `evaluation/results/processed/baseline_vs_agent.csv`

Raw files are produced by `scripts/collect_metrics.py`.

Processed summaries are produced by `scripts/aggregate_results.py`.

## Minimum run count

The first acceptable evaluation target is:

- at least 5 runs per test case per mode, if time allows
- if time is limited, at least 3 runs per test case per mode

The exact number of runs must be documented in the Results chapter.

For quick smoke checks, one run per case is acceptable while verifying the
harness. Reportable results should use the minimum run count above where time
allows.

## Success criteria

The implementation is considered evaluation-ready when:

- both deterministic and agent-enhanced modes can run the same scenario
- results are saved in a repeatable format
- latency is recorded
- resource usage is recorded or clearly documented
- malformed or unsupported actions are blocked
- the results can be summarized in report tables

The Step 9 harness is considered ready when:

- `collect_metrics.py --help` works
- `aggregate_results.py --help` works
- raw CSV files can be written to `evaluation/results/raw/`
- processed summaries can be written to `evaluation/results/processed/`
- missing resource or thermal data is recorded as `not_available`, not invented

## Relationship to report

This protocol feeds:

- Chapter 3 - Methodology
- Chapter 5 - Measurement/Evaluation setup
- Chapter 6 - Results
- Chapter 7 - Discussion

## Scope note

This protocol is intentionally minimal.

It does not evaluate:

- multiple LLMs
- many devices
- broad multi-agent systems
- deep n8n internals
- heavy observability stacks

It also does not:

- create fake result data
- perform Raspberry Pi validation
- claim runtime safety enforcement from Step 8 documentation alone

The purpose is to support the narrowed new-yacoub thesis scope.
