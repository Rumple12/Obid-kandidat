# Raspberry Pi Validation Notes

This file prepares the optional Step 10 Raspberry Pi validation path for the
new-yacoub thesis.

Status: **documentation/preparation only**. No Raspberry Pi runtime validation
has been performed from this file.

## Purpose

Raspberry Pi validation is a later Tier 1.5 check. It can strengthen Yacoub's
edge-computing angle by showing whether the same or a simplified scenario can
run on resource-constrained hardware.

The PC-first local system remains the primary working system. Pi validation is
supporting evidence only and must not block final thesis completion.

## Expected Prerequisites

- Raspberry Pi available
- Raspberry Pi OS or compatible Linux
- Python runtime if running middleware directly
- Docker runtime if running n8n or Docker-based checks
- Network access between Pi, n8n, and middleware if split across devices
- Access to terminal logs or screenshots for evidence capture

## Basic System Checks

Run these on the Pi before validation:

```bash
uname -a
python --version
python3 --version
free -h
top
```

If Docker is used:

```bash
docker --version
docker compose version
docker ps
```

For a lighter process snapshot:

```bash
ps aux --sort=-%mem | head
```

## Thermal Collection

Preferred Pi thermal command:

```bash
vcgencmd measure_temp
```

If `vcgencmd` is unavailable, record:

```text
thermal_c=not_available
```

Do not invent or estimate thermal data.

## Minimal Validation Scenario

The preferred validation scenario is the same temperature-to-fan path:

```text
temperature event
  -> n8n workflow or simplified trigger
  -> middleware fan endpoint
  -> simulated fan action
  -> latency/resource note
```

Real GPIO is not required for Step 10. Simulated fan endpoints remain valid for
the optional Pi validation.

## Evidence To Capture

Save evidence under:

```text
evaluation/results/pi-validation/
```

Useful evidence:

- Pi model and OS/version
- deployment choice
- terminal commands run
- run count
- latency observations
- `free -h` output
- CPU/process observations
- thermal command output or `not_available`
- screenshots or terminal logs

## Limitations

- Limited run count is acceptable.
- A simplified scenario is acceptable if full n8n on Pi is too heavy.
- Pi validation must not expand into full deployment research.
- Pi validation must not introduce multiple devices or a new architecture.
- Local PC results remain the primary baseline if Pi validation cannot be completed.
