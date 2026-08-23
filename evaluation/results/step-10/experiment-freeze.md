# Step 10 experiment freeze

- Freeze ID: `STEP10_EXPERIMENT_FREEZE_V1`
- Created: `2026-08-23T16:05:05.794Z`
- Git HEAD: `8073c1c3111b6be968fa38c2007d71dec36e2a4e`
- Repository state: `known_step10_artifacts_only`
- Evaluation manifest: `OBID-EVALUATION-CASES-V1`
- Evaluation protocol: `OBID-EVALUATION-PROTOCOL-V1`
- n8n: `1.123.37` / `n8nio/n8n:1.123.37|sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885`
- Model: `models/gemini-2.5-flash` with stored options `{}`
- Frozen Yacoub commit: `278318340bfa4e4650a97a2baba73f63bd868ed9`
- Core configurations: `CONFIG-BASELINE` and `CONFIG-OBID` only.
- Optional validator agent: `SKIP_FOR_CORE`.
- Planned counts: `70` core + `5` invalid-action + `10` HITL = `85`; automated latency subset `30`.

## Frozen repository artifacts

| Identity | Path | SHA-256 |
|---|---|---|
| `evaluation_manifest` | `evaluation/cases/obid-evaluation-cases.json` | `612a3c6cb6032ed4aa03eae87fa62e5632d61fcdb2cc0633c151bbf4d67aafb7` |
| `evaluation_protocol` | `evaluation/evaluation-protocol.md` | `27ecdd2d0b9bdd7110a2c25baee06803acefd4963a2cce00e931216a15f95117` |
| `sensor_schema` | `shared_interfaces/json-schema/sensor-event.schema.json` | `416cec7d396912672171e1fbfdce828820017c9218e2c418de3f784e329ee007` |
| `action_schema` | `shared_interfaces/json-schema/agent-action.schema.json` | `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b` |
| `baseline_workflow` | `cognitive_logic/baselines/yacoub/minimal-agent-baseline.json` | `ed8697e07eb83deaecac3879c82b860e2c4b8f597bde1bc355a3c5b863c15585` |
| `baseline_prompt` | `cognitive_logic/baselines/yacoub/system-prompt-v1.md` | `a5e24dc517d3bb91eb45ebebb6efd79bbc77bcf7197ecd9b3daf76fd1aab92cd` |
| `obid_v3_workflow` | `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json` | `1a09ee5a3199289c39845f9b97a3a3f516f277924d6a8fcb52da52780b0eaf78` |
| `obid_prompt` | `cognitive_logic/obid/prompts/system-prompt-v1.md` | `f8b4171e5d70df6be5aa136a63336dc8c32edca61036272a047b6fa3746cfec2` |
| `step8_runtime_safety` | `safety_layer/workflows/runtime-safety-v1.json` | `d179f0f4b3ef3977ab65456cc172854176e9dc56336a43e87b9bf92fea3ee378` |
| `step8_safety_harness` | `safety_layer/workflows/step-08-safety-harness.json` | `4417a3e66a6dc0d09b1e9318bfe7f308c2ec6a52f96ffe00ff04a0a5151a9c0c` |
| `step9_runtime_safety` | `safety_layer/workflows/runtime-safety-v2-hitl.json` | `8dbf1826f43cdea34d510ff53e90fed52e45c93d5ed29956cf3a6dbfd6de652d` |
| `step9_hitl_harness` | `safety_layer/hitl/workflows/step-09-hitl-harness.json` | `090715a02ed15ce0a385788fad8f25abceec7cd473422f63c9114909d850eaac` |
| `step9_retained_hitl_gate` | `safety_layer/hitl/workflows/runtime-hitl-v1.json` | `fd9ce59e033c6074d6688d9eb0037dff7afc3d882a74fea0743901dfa041d902` |
| `step9_report_gate` | `docs/report-notes/step-09-human-in-the-loop-runtime.md` | `ce5c7ba6c25c679c988116e69ff45ed732967589cbc7a62d9d85698316a118da` |

## Frozen Step 10 evidence tooling

| Identity | Path | SHA-256 |
|---|---|---|
| `step10_runner` | `evaluation/results/step-10/run_step10.py` | `17ba174ca172cf8c6c6257eea5888f30b699f3b2eda0ed2588e939aa2617e06d` |
| `credential_safe_extractor` | `evaluation/results/step-10/extract_n8n_execution.js` | `80aa43658c8634f6394f02c158c0d7f060854952e47e8e40d45a2ef809d4daea` |
| `result_processor` | `evaluation/results/step-10/process_results.py` | `942d7979e57ca5be9f0ecffec945a9f2667a082b362f6ae80bed7f0f0bfc6c41` |

## Live workflow identities

| Workflow | Active | Nodes | Credential attachment count | Credential-safe semantic SHA-256 |
|---|---:|---:|---:|---|
| `agent-minimal` | `true` | 12 | 1 | `2d1a7c1e01136b0e816c2d99c03e7d2832edd1a6c1ec959f36a889047137e457` |
| `obid-agent-v3-hitl` | `true` | 34 | 1 | `6d4206e8af3b60a4917c454a5d67fc0fb652b9908165362e3c56edb54c801457` |
| `runtime-safety-v1` | `false` | 10 | 0 | `143c21ab9a459ba4d8b5edfbc9d0fb6242b0921d0f47396db7c337975bbf6c91` |
| `runtime-safety-v2-hitl` | `false` | 13 | 0 | `3aa0b939545827c7f1a952071c432c5935e40402e98f2fd4081b69d4247c79c0` |
| `step-08-safety-harness` | `false` | 14 | 0 | `a56569b002d48b0f8ca15d897bd42bcb66158ea5b73150556c10c90e502b7420` |
| `step-09-hitl-harness` | `true` | 32 | 0 | `7e65c44735630b9936afe23bfa354bea3e2ee5d39153db923528979bbd10f1e6` |

The baseline live projection retains the documented n8n-packaging exception: its live model node omits `modelName`, while the frozen portable artifact explicitly records the same pinned default `models/gemini-2.5-flash`.

Credential attachment counts prove operational presence only. No credential identity or secret is recorded.

After primary run 1, semantic evaluated artifacts and frozen Step 10 evidence tooling must remain unchanged. Operational restoration may only restore the same frozen configuration and must be logged.
