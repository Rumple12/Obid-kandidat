# Raspberry Pi Startup and IP Transcript

Status: Step 10 evidence cleanup for the Tier 1.5 Raspberry Pi validation.

This file records the observed startup and network details for the Raspberry Pi
validation setup. It documents the setup already used by the existing Step 10
evidence files and does not add new measurements.

## Observed Setup

- The Raspberry Pi was used only for middleware/action endpoint validation.
- n8n stayed on the PC.
- Observed Raspberry Pi IP: `10.131.76.89`.
- The Python middleware was started on the Raspberry Pi with:

```bash
MIDDLEWARE_HOST=0.0.0.0 python3 -m middleware.api.app
```

- The middleware was reachable at:

```text
http://10.131.76.89:8000
```

- The PC-hosted n8n HTTP nodes called:

```text
http://10.131.76.89:8000/fan/on
http://10.131.76.89:8000/fan/off
```

## Scope Notes

- The fan action remained simulated middleware behavior.
- No real GPIO hardware was controlled.
- No physical fan was controlled.
- Full n8n-on-Pi deployment was not attempted.
- The full workflow stayed split: n8n on the PC, middleware/action endpoint on
  the Raspberry Pi.

## Related Evidence

This transcript summary belongs with the existing Step 10 evidence:

- `pi-validation-notes.md`
- `pi-workflow-run-final.csv`
- `pi-run-01.csv`
- `pi-terminal-high-temp-fan-on.png`
- `pi-terminal-low-temp-fan-off.png`
- `2. Measure direct Pi middleware latency.png`
- `3. Measure CPU_RAM of the middleware process.png`
- `pi-temp-measurement.png`
