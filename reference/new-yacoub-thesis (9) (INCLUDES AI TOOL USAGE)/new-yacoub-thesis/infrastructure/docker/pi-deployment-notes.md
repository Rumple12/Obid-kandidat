# Raspberry Pi Deployment Notes

This file documents possible Raspberry Pi validation paths for Step 10.

Status: **documentation/preparation only**. No new Docker Compose file is added
for Pi in this step.

## Deployment Choices

### 1. Middleware On Pi, n8n On PC

Recommended first Pi validation path.

```text
Raspberry Pi:
  middleware/api/app.py

PC/Docker host:
  n8n Docker baseline
```

This keeps n8n on the already-working local Docker setup while testing the
middleware/action side on Pi hardware.

### 2. Middleware And n8n On Pi

Use only if the Pi has enough CPU, RAM, storage, and thermal headroom.

The existing Compose file may need adaptation for:

- arm64 image availability
- available RAM
- storage location
- startup time
- thermal behavior

Do not make this the first Pi validation path unless the simpler split setup is
already stable.

### 3. Simplified Pi Measurement

Use if Docker or n8n is too heavy for the available Pi.

Possible simplified checks:

- run only the Python middleware on Pi
- call `/status`, `/fan/on`, and `/fan/off`
- record latency with local scripts or terminal timing
- collect CPU/RAM/thermal observations

This still supports the thesis as optional edge validation evidence.

## Recommended First Path

Recommended Step 10 path:

```text
n8n remains on PC/Docker host
middleware runs on Raspberry Pi
n8n HTTP Request nodes call the Pi IP address
fan action remains simulated
```

Example URL change in n8n:

```text
http://<pi-ip-address>:8000/fan/on
http://<pi-ip-address>:8000/fan/off
```

## Network Notes

`host.docker.internal` is useful when n8n runs inside Docker Desktop and calls a
service on the Windows host.

It may not apply when:

- middleware runs on a Raspberry Pi
- n8n runs on Linux Docker
- n8n and middleware are split across different machines

Use one of these instead:

- actual Raspberry Pi IP address
- Docker network alias if both services run in the same Docker network
- Linux host gateway mapping if needed and explicitly documented

## Compose File Caution

Do not add a Pi-specific Compose file until it is actually needed.

Before running n8n on Pi, check:

```bash
uname -m
docker --version
docker compose version
free -h
vcgencmd measure_temp
```

Record any Compose changes as Pi validation notes, not as a redesign of the
local baseline.

## Scope Boundaries

Pi validation is Tier 1.5 optional evidence.

It must not:

- replace the PC-first baseline
- add multiple devices
- add Prometheus/Grafana
- add MCP
- modify n8n core
- become full deployment research
