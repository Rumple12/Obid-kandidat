# Pi Validation Notes Template

Template only. This is not real Pi validation evidence until filled from an
actual Raspberry Pi run.

## Hardware Used

- Raspberry Pi model:
- RAM:
- Storage:
- Power supply:
- Network connection:

## OS / Version

Commands:

```bash
uname -a
python --version
python3 --version
```

Observed output:

```text
TBD from real Pi run
```

## Deployment Choice

Selected path:

- [ ] middleware on Pi, n8n on PC
- [ ] middleware and n8n on Pi
- [ ] simplified Pi measurement only

Notes:

```text
TBD from real Pi run
```

## Commands Run

```bash
free -h
top
ps aux --sort=-%mem | head
vcgencmd measure_temp
```

If Docker was used:

```bash
docker --version
docker compose version
docker ps
```

## Observed Limitations

- CPU:
- RAM:
- Thermal:
- Network:
- Docker/n8n startup:
- Other:

## Validation Outcome

- [ ] succeeded
- [ ] skipped
- [ ] partially completed

Reason:

```text
TBD from real Pi run
```

## Evidence Files

List any CSVs, screenshots, or terminal logs saved in this folder:

- TBD
