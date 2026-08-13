# Step 10 Raspberry Pi Validation Evidence

Status: Tier 1.5 Raspberry Pi validation completed for the middleware/action
endpoint side.

Created: 2026-05-05

## Validation Scope

This evidence records the optional Tier 1.5 Raspberry Pi validation path. The
primary Tier 1 system remains the local PC-based n8n and middleware baseline.

In this run:

- n8n ran locally on the PC.
- The Raspberry Pi ran the Python middleware/action endpoint side.
- The middleware was started on the Raspberry Pi with:

```bash
MIDDLEWARE_HOST=0.0.0.0 python3 -m middleware.api.app
```

- The n8n production webhook successfully called the Raspberry Pi middleware.
- Full system deployment to the Raspberry Pi was not attempted.

## Main Full-Workflow Evidence

The main full-workflow measurement evidence is:

- `pi-workflow-run-final.csv`

That file records n8n production webhook calls from the PC to the Raspberry Pi
middleware.

Observed full-workflow results:

| Test case | Input | Expected action | Observed action | HTTP status | Success | Full workflow latency |
| --- | ---: | --- | --- | ---: | --- | ---: |
| deterministic_high_temp | 31.4 C | fan_on | fan_on | 200 | true | 437.003 ms |
| deterministic_low_temp | 24.5 C | fan_off | fan_off | 200 | true | 200.206 ms |

## Supporting Direct Middleware Evidence

Direct Raspberry Pi middleware endpoint latency was also measured:

| Endpoint action | Direct endpoint latency |
| --- | ---: |
| fan_on | 135.44 ms |
| fan_off | 233.27 ms |

This direct endpoint latency is supporting evidence only. It is not the full
n8n workflow latency because it does not include n8n webhook execution and
workflow routing.

## CPU, RAM, and Thermal Evidence

Observed middleware process:

```text
python3 -m middleware.api.app
```

Resource observation:

| Metric | Value |
| --- | ---: |
| CPU | 0.0 % |
| MEM | 0.5 % |
| RSS | 21048 KB |
| Middleware RAM | 20.95 MB |

Thermal observation:

```text
vcgencmd measure_temp
temp=49.6'C
```

Recorded `thermal_c`: 49.6

## Evidence Files

Screenshots and captured files saved under this folder include:

- `pi-workflow-run-final.csv`
- `pi-run-01.csv`
- `2. Measure direct Pi middleware latency.png`
- `3. Measure CPU_RAM of the middleware process.png`
- `pi-temp-measurement.png`
- `pi-high-temp-fan-on-canvas.png`
- `pi-high-temp-fan-on-output.png`
- `pi-low-temp-fan-off-canvas.png`
- `pi-low-temp-fan-off-output.png`
- `pi-terminal-high-temp-fan-on.png`
- `pi-terminal-low-temp-fan-off.png`

## Interpretation

This validates that the PC-hosted n8n workflow can call the Raspberry Pi-hosted
middleware/action endpoint side for the same deterministic high-temperature and
low-temperature scenarios used in the local baseline.

The validation strengthens the edge-computing discussion but does not replace
the PC-first baseline. It also does not claim that n8n itself was deployed on
the Raspberry Pi.
