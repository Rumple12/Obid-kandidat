# Step 10 raw-data manifest

- Lock ID: `STEP10_RAW_DATA_LOCK_V1`
- Locked at: `2026-08-23T16:29:39.486Z`
- Primary records: `85` (`70` core, `5` invalid-action, `10` HITL)
- Main automated latency records: `30`
- Unique primary IDs / no replacement: `PASS`
- JSONL parsing and privacy scan: `PASS`

## Frozen raw files

| Path | Bytes | SHA-256 |
|---|---:|---|
| `evaluation/results/step-10/experiment-freeze.json` | 7123 | `0f96744b31c5c6751df3498e9f42761d45decd2303d46aac99d909fcf0013cf7` |
| `evaluation/results/step-10/experiment-freeze.md` | 4794 | `ab1df6015958a9d9c121ac0bcff374cd3fd3bd18e2588b1877a4d577089ada96` |
| `evaluation/results/step-10/raw/planned-order.json` | 39500 | `56f3602a1af82ed3a049393a741be48ae6d505693ecc181556bb7fdeffccd5d5` |
| `evaluation/results/step-10/raw/run-order.csv` | 11165 | `096eef4b1d2ccdeba271206476087a2af4ab57ff373bbd5bbc6fd05f080e1604` |
| `evaluation/results/step-10/raw/run-records.jsonl` | 427652 | `54bc2c4058e6324b478c1c527f2cf2d3b5ea24e4fc0d41c1419577db466a16e6` |
| `evaluation/results/step-10/raw/attempt-events.jsonl` | 128842 | `a5ef39991790f8a29192a71ca7fd9d0fd64b98de7a13e21bb22e2d664f7c90bd` |
| `evaluation/results/step-10/raw/hitl-pending.jsonl` | 15985 | `71007709c2eb352078bf37723bac3fa7877c23815ffb39e30eb8c513838a0f31` |
| `evaluation/results/step-10/raw/operational-deviations.jsonl` | 1440 | `7f57913b9e1f16c22d57f00a6f5f3f928115e89faa16e46fe7d463f247dec764` |

Processed outputs must verify these hashes before reading observations. Raw files must not be rewritten after this lock.
