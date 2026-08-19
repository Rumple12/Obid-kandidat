# Raspberry Pi Validation Results

This folder contains optional Step 10 Raspberry Pi validation evidence.

Status: **Tier 1.5 Raspberry Pi validation evidence added**.

Pi validation is optional Tier 1.5 support evidence. The local PC result remains
the primary baseline; this folder supports the edge-computing discussion by
showing that the PC-hosted n8n workflow can call the Raspberry Pi-hosted
middleware/action endpoint side.

## Final Evidence Set

Use these files as the final Step 10 evidence set:

- `pi-validation-notes.md`
- `pi-startup-ip-transcript.md`
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

`pi-workflow-run-final.csv` records the final full-workflow run:

- `31.4 C -> fan_on`, HTTP `200`, success `true`, latency `437.003 ms`
- `24.5 C -> fan_off`, HTTP `200`, success `true`, latency `200.206 ms`

`pi-run-01.csv` records the supporting Tier 1.5 summary, including direct
middleware latency, CPU/RAM observations, and thermal evidence.

`pi-startup-ip-transcript.md` records the observed Pi IP, middleware startup
command, middleware base URL, and the PC-hosted n8n HTTP action URLs used for
the Tier 1.5 split validation.

## Non-Final Files

Templates and failed setup attempts are kept in `non-final/`.

These files are useful for traceability, but they are not final report evidence:

- `non-final/pi-validation-notes-template.md`
- `non-final/pi-validation-template.csv`
- `non-final/x fail pi-workflow-run-success.csv`

## Evidence To Save

Useful Pi evidence includes:

- Pi model and hardware notes
- OS/version
- deployment choice
- commands run
- terminal logs
- screenshots if available
- latency observations
- CPU/RAM observations
- thermal output from `vcgencmd measure_temp` or `not_available`

## Interpretation

Pi results should be interpreted as optional Tier 1.5 validation.

The successful validation strengthens the edge-computing discussion, but the
already-working local PC system remains the primary thesis baseline.

## No Fake Results

Do not add invented Pi measurements.

Do not use template or failed-run files as final report evidence.
