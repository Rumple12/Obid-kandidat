# Metrics Schema

This file documents the Step 9 CSV fields used by the lightweight evaluation
harness.

## Raw Result Fields

`scripts/collect_metrics.py` writes these fields:

- `timestamp_utc`
- `mode`
- `test_case_id`
- `run_index`
- `webhook_url`
- `input_temperature`
- `expected_action`
- `observed_action`
- `expected_safety_result`
- `observed_safety_result`
- `http_status`
- `success`
- `latency_ms`
- `cpu_percent`
- `ram_usage`
- `ram_percent`
- `thermal_c`
- `observed_response`
- `error`
- `notes`

## Success Field

For workflow modes:

- `true` means the HTTP request succeeded and the observed action matched the
  expected action.
- `false` means the request failed or the expected action could not be observed
  in the response.

For safety mode:

- `not_applicable` means the row records Step 8 expected behavior only. Step 8
  does not yet provide runtime enforcement evidence.

## Resource Fields

CPU/RAM are best effort.

If Docker is available, the collector tries:

```text
docker stats --no-stream
```

If Docker stats are unavailable, CPU/RAM fields are written as:

```text
not_available
```

Thermal data must not be faked. On Windows/PC, `thermal_c` is normally:

```text
not_available
```

Raspberry Pi thermal collection can be added later in Step 10, for example via
`vcgencmd measure_temp`.

## Processed Summary Files

`scripts/aggregate_results.py` writes:

- `summary_latency.csv`
- `summary_resources.csv`
- `safety_outcomes.csv`
- `baseline_vs_agent.csv`
