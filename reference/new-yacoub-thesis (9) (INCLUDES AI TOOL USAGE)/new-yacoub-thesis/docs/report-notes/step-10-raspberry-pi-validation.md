# Step 10 - Raspberry Pi Validation

## What was built / validated

- Optional Tier 1.5 Raspberry Pi validation evidence was added under `evaluation/results/pi-validation/`.
- The validation used a split setup:
  - n8n stayed on the PC.
  - The Raspberry Pi ran the Python middleware/action endpoint side.
- The Raspberry Pi middleware was started with:

```bash
MIDDLEWARE_HOST=0.0.0.0 python3 -m middleware.api.app
```

- The production n8n webhook on the PC successfully called the Raspberry Pi middleware.
- This was not a full Raspberry Pi deployment of the whole system.
- The fan action endpoint remained simulated middleware behavior; no real GPIO or physical fan hardware was used.

## Why it matters for the thesis

This strengthens the edge-computing angle without changing the main PC-first thesis scope. It shows that the already working PC-hosted n8n workflow can call a Raspberry Pi-hosted middleware/action endpoint for the same temperature-to-fan scenario.

The evidence supports the thesis discussion around constrained hardware and deployment feasibility while keeping Raspberry Pi validation as Tier 1.5 support evidence, not the primary baseline.

## Evidence produced

- `infrastructure/os/raspberry-pi-notes.md`
- `infrastructure/docker/pi-deployment-notes.md`
- `evaluation/results/pi-validation/README.md`
- `evaluation/results/pi-validation/pi-validation-notes.md`
- `evaluation/results/pi-validation/pi-startup-ip-transcript.md`
- `evaluation/results/pi-validation/pi-run-01.csv`
- `evaluation/results/pi-validation/pi-workflow-run-final.csv`
- `evaluation/results/pi-validation/2. Measure direct Pi middleware latency.png`
- `evaluation/results/pi-validation/3. Measure CPU_RAM of the middleware process.png`
- `evaluation/results/pi-validation/pi-temp-measurement.png`
- `evaluation/results/pi-validation/pi-high-temp-fan-on-canvas.png`
- `evaluation/results/pi-validation/pi-high-temp-fan-on-output.png`
- `evaluation/results/pi-validation/pi-low-temp-fan-off-canvas.png`
- `evaluation/results/pi-validation/pi-low-temp-fan-off-output.png`
- `evaluation/results/pi-validation/pi-terminal-high-temp-fan-on.png`
- `evaluation/results/pi-validation/pi-terminal-low-temp-fan-off.png`

`pi-workflow-run-final.csv` records the final full-workflow latency evidence:

- high temperature `31.4 C` produced `fan_on`, HTTP `200`, success `true`, full workflow latency `437.003 ms`
- low temperature `24.5 C` produced `fan_off`, HTTP `200`, success `true`, full workflow latency `200.206 ms`

`pi-run-01.csv` records the same successful production webhook run in the Step 9-style result format, including the input temperatures, expected and observed actions, HTTP status, success flag, latency fields, and observed simulated middleware responses.

Direct Raspberry Pi middleware endpoint latency is supporting evidence only:

- `fan_on`: `135.44 ms`
- `fan_off`: `233.27 ms`

CPU/RAM/thermal evidence from `pi-validation-notes.md`:

- observed middleware process: `python3 -m middleware.api.app`
- CPU: `0.0 %`
- MEM: `0.5 %`
- RSS: `21048 KB`
- middleware RAM: `20.95 MB`
- thermal command: `vcgencmd measure_temp`
- observed thermal value: `49.6 C`

Startup/IP evidence from `pi-startup-ip-transcript.md`:

- observed Raspberry Pi IP: `10.131.76.89`
- middleware startup command: `MIDDLEWARE_HOST=0.0.0.0 python3 -m middleware.api.app`
- middleware base URL: `http://10.131.76.89:8000`
- n8n HTTP node action URLs:
  - `http://10.131.76.89:8000/fan/on`
  - `http://10.131.76.89:8000/fan/off`

## Report chapters it feeds

- Chapter 4 - Choice of approach: PC-first development with Raspberry Pi as later Tier 1.5 validation.
- Chapter 5 - Implementation: split deployment note where PC-hosted n8n calls Raspberry Pi-hosted middleware.
- Chapter 6 - Results: optional Pi validation results, full workflow latency, and limited Pi resource/thermal observations.
- Chapter 7 - Discussion: practical edge-computing limitations, split deployment tradeoffs, and why the PC baseline remains primary.

## Limitations or assumptions

- This is Tier 1.5 Raspberry Pi validation only.
- n8n was not deployed on the Raspberry Pi.
- The whole system was not moved to the Raspberry Pi.
- The Raspberry Pi ran only the middleware/action endpoint side.
- The middleware action remained simulated; no real GPIO or physical fan was controlled.
- The full workflow latency values come from `pi-workflow-run-final.csv`.
- Direct endpoint latency is supporting evidence only and should not be treated as full workflow latency.
- `pi-workflow-run-final.csv` preserves the workflow-run collection fields where `thermal_c` is `not_available`; `pi-run-01.csv` records the supporting Pi thermal value `49.6 C`.
- The run count is limited and should be interpreted as validation evidence, not broad benchmarking.
- This step does not expand into Tier 2 deployment work.
- Step 11 freeze work was not started here.

## Evidence cleanup status

- The Raspberry Pi startup/IP transcript gap is closed by `evaluation/results/pi-validation/pi-startup-ip-transcript.md`.
- Optional repeated Pi runs if stronger final report tables are needed.
- A concise screenshot set selected for the thesis appendix, avoiding template and failed setup files.
- Any future evidence would need to stay within Tier 1.5 unless the scope is explicitly changed.
