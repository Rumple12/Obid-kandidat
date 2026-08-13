# Final Evidence Inventory

Inventory date: 2026-05-24

Status: Step 11 freeze inventory for the narrowed Tier 1.5 implementation.

This inventory lists the evidence that can support report writing after the
implementation freeze. Non-final setup attempts are listed separately so they
are not accidentally used as final result evidence.

## Final Workflow Exports

- `cognitive_logic/workflows/deterministic-baseline.json`
- `cognitive_logic/workflows/deterministic-baseline.md`
- `cognitive_logic/workflows/agent-minimal.json`
- `cognitive_logic/workflows/agent-minimal.md`

## Final Workflow Screenshots and Logs

Deterministic baseline evidence:

- `cognitive_logic/workflows/evidence/step-06-runtime-verification.md`
- `cognitive_logic/workflows/evidence/full tree.png`
- `cognitive_logic/workflows/evidence/fulltree_low.png`
- `cognitive_logic/workflows/evidence/step-06-high-temp-webhook-input.png`
- `cognitive_logic/workflows/evidence/step-06-high-temp-if-condition.png`
- `cognitive_logic/workflows/evidence/step-06-high-temp-fan-on-output.png`
- `cognitive_logic/workflows/evidence/high-temp_terminal.txt`
- `cognitive_logic/workflows/evidence/step-06-low-temp-webhook.png`
- `cognitive_logic/workflows/evidence/step-06-low-temp-if-condition.png`
- `cognitive_logic/workflows/evidence/step-06-low-temp-fan-off-output.png`
- `cognitive_logic/workflows/evidence/step-06-low-temp-fan-off-canva.png`
- `cognitive_logic/workflows/evidence/low-temo_terminal.txt`
- `cognitive_logic/workflows/evidence/no terminal log reason.txt`

Minimal agent workflow evidence:

- `cognitive_logic/workflows/evidence/step-07/step-07-runtime-verification.md`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-canvas.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-agent-output.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-parsed-action.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-high-temp-fan-on-output.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-canvas.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-agent-output.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-parsed-action.png`
- `cognitive_logic/workflows/evidence/step-07/step-07-low-temp-fan-off-output.png`

The Step 7 screenshots cover model setup, prompt/system-message setup,
structured JSON output, no-memory/stateless canvas setup, and `fan_on` /
`fan_off` middleware routing. No broad multi-agent architecture or model
benchmarking is claimed.

## Architecture Evidence

- `docs/architecture/README.md`
- `docs/ongoing/integration-contract.md`
- `docs/plans/implementation-plan.md`
- `docs/plans/new-yacoub-14-step-process.md`
- `docs/decisions.md`

No dedicated final architecture image file is currently present. The report can
use the text architecture in `docs/architecture/README.md` as the source for a
figure if a final diagram is needed.

## Local Runtime and Middleware Evidence

Local n8n / Docker:

- `infrastructure/docker/docker-compose.yml`
- `infrastructure/docker/README.md`
- `infrastructure/docker/evidence/n8n-runtime-proof-2026-04-25.txt`
- `infrastructure/docker/evidence/n8n-localhost-5678-success-2026-04-25.png`
- `docs/n8n-version.md`

Middleware:

- `middleware/api/app.py`
- `middleware/api/routes.py`
- `middleware/gpio/mock_sensor.py`
- `middleware/webhooks/n8n_sender.py`
- `middleware/tests/manual-test-notes.md`
- `middleware/tests/evidence/step-04-middleware-smoke-test-2026-04-25.txt`

## Shared Contract Evidence

- `shared_interfaces/json-schema/sensor-event.schema.json`
- `shared_interfaces/json-schema/agent-action.schema.json`
- `shared_interfaces/examples/sensor-event.example.json`
- `shared_interfaces/examples/fan-on.example.json`
- `shared_interfaces/examples/blocked-action.example.json`

## Safety Layer Evidence

- `safety_layer/policies/action-policy-v1.md`
- `safety_layer/parsers/output-validation-v1.md`
- `safety_layer/approvals/hitl-v1.md`
- `safety_layer/examples/allowed-case.md`
- `safety_layer/examples/blocked-case.md`
- `safety_layer/examples/risky-approval-case.md`

Important report note: the safety layer is specification/design evidence. It
does not prove production-grade runtime enforcement.

## Evaluation CSVs and Harness Evidence

Harness files:

- `evaluation/README.md`
- `evaluation/datasets/test-cases.json`
- `evaluation/metrics/metrics-schema.md`
- `scripts/collect_metrics.py`
- `scripts/aggregate_results.py`
- `docs/evaluation/evaluation-protocol.md`
- `evaluation/results/step-09-small-measurement-notes.md`

Raw CSV evidence:

- `evaluation/results/raw/run_20260429T165733Z_deterministic.csv`
- `evaluation/results/raw/run_20260429T165859Z_agent.csv`

Processed CSV evidence:

- `evaluation/results/processed/summary_latency.csv`
- `evaluation/results/processed/summary_resources.csv`
- `evaluation/results/processed/safety_outcomes.csv`
- `evaluation/results/processed/baseline_vs_agent.csv`

Setup / non-final evaluation evidence:

- `evaluation/results/raw/dump/run_20260429T165702Z_deterministic.csv`

The `raw/dump` file is a misconfigured-webhook/setup attempt and should not be
used as final result evidence.

## Raspberry Pi Validation Evidence

Final Step 10 Tier 1.5 files:

- `infrastructure/os/raspberry-pi-notes.md`
- `infrastructure/docker/pi-deployment-notes.md`
- `evaluation/results/pi-validation/README.md`
- `evaluation/results/pi-validation/pi-validation-notes.md`
- `evaluation/results/pi-validation/pi-startup-ip-transcript.md`
- `evaluation/results/pi-validation/pi-workflow-run-final.csv`
- `evaluation/results/pi-validation/pi-run-01.csv`
- `evaluation/results/pi-validation/2. Measure direct Pi middleware latency.png`
- `evaluation/results/pi-validation/3. Measure CPU_RAM of the middleware process.png`
- `evaluation/results/pi-validation/pi-temp-measurement.png`
- `evaluation/results/pi-validation/pi-high-temp-fan-on-canvas.png`
- `evaluation/results/pi-validation/pi-high-temp-fan-on-output.png`
- `evaluation/results/pi-validation/pi-low-temp-fan-off-canvas.png`
- `evaluation/results/pi-validation/pi-low-temp-fan-off-output.png`
- `evaluation/results/pi-validation/pi-terminal-high-temp-fan-on.png`
- `evaluation/results/pi-validation/pi-terminal-low-temp-fan-off.png`

Main full-workflow evidence:

- `evaluation/results/pi-validation/pi-workflow-run-final.csv`

That file records:

- `31.4 C -> fan_on`, HTTP `200`, success `true`, latency `437.003 ms`
- `24.5 C -> fan_off`, HTTP `200`, success `true`, latency `200.206 ms`

Supporting Pi evidence:

- startup/IP transcript: `evaluation/results/pi-validation/pi-startup-ip-transcript.md`
- observed Raspberry Pi IP: `10.131.76.89`
- middleware base URL: `http://10.131.76.89:8000`
- direct `fan_on` endpoint latency: `135.44 ms`
- direct `fan_off` endpoint latency: `233.27 ms`
- middleware CPU: `0.0 %`
- middleware MEM: `0.5 %`
- middleware RSS: `21048 KB`
- middleware RAM: `20.95 MB`
- thermal: `49.6 C`

Direct endpoint latency is supporting evidence only, not full n8n workflow
latency.

Pi non-final/setup files:

- `evaluation/results/pi-validation/non-final/pi-validation-notes-template.md`
- `evaluation/results/pi-validation/non-final/pi-validation-template.csv`
- `evaluation/results/pi-validation/non-final/x fail pi-workflow-run-success.csv`

These files are traceability material only and should not be used as final
report evidence.

## Report Notes From Steps 1-10

- `docs/report-notes/step-01-lock-scope.md`
- `docs/report-notes/step-02-repo-foundation.md`
- `docs/report-notes/step-03-local-n8n-baseline.md`
- `docs/report-notes/step-04-middleware-skeleton.md`
- `docs/report-notes/step-05-shared-contract.md`
- `docs/report-notes/step-06-deterministic-baseline.md`
- `docs/report-notes/step-07-minimal-agent-workflow.md`
- `docs/report-notes/step-08-minimum-safety-layer.md`
- `docs/report-notes/step-09-measurement-evaluation-harness.md`
- `docs/report-notes/step-10-raspberry-pi-validation.md`

Step 11 freeze note:

- `docs/report-notes/step-11-implementation-freeze.md`

## Remaining Evidence Gaps

These gaps are not blockers to the Step 11 freeze, but they should be handled
carefully during report writing:

- No standalone final architecture image file is present.
- Runtime safety enforcement is not implemented; Step 8 is safety design and
  case documentation only.
- No dedicated runtime logs prove malformed/risky actions are blocked by an
  implemented safety gate.
- The Step 9 measurement run count is small and should be described as limited
  evidence, not broad benchmarking.
- The workflow JSON files should be treated as the frozen repo artifacts; if an
  examiner requires exact n8n UI re-export proof, that should be handled as
  report evidence cleanup, not new architecture.
