# Verified Step 4 Boundary Map

**Verified:** 2026-08-20

**Mode:** active n8n production webhooks (`/webhook/`), not test/listen mode (`/webhook-test/`)

## Inbound seam

```text
Host test client
  |
  | POST http://127.0.0.1:8000/sensor-event
  v
Actual Yacoub middleware
  | clean detached source at commit 278318340bfa4e4650a97a2baba73f63bd868ed9
  | actual bind: 0.0.0.0:8000 (runtime override of source default 127.0.0.1:8000)
  |
  | N8N_WEBHOOK_URL
  | POST http://127.0.0.1:5678/webhook/obid-yacoub-compat
  v
Obid n8n container: obid-n8n / n8n 1.123.37
  |
  +-- Receive Yacoub sensor event
  +-- Record inbound boundary (field copy only; no validation or decision)
```

The middleware and n8n both run on the same Docker Desktop host from the host-side perspective, so middleware forwarding uses `127.0.0.1:5678`. The inbound production webhook returned HTTP 200 to the middleware.

## Outbound seam

```text
Host test client
  |
  +-- POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-on
  |     -> Obid n8n HTTP Request
  |     -> POST http://host.docker.internal:8000/fan/on
  |
  +-- POST http://127.0.0.1:5678/webhook/obid-yacoub-compat-fan-off
        -> Obid n8n HTTP Request
        -> POST http://host.docker.internal:8000/fan/off
              |
              v
        Actual Yacoub middleware
              |
              +-- inherited simulated fan state
```

`host.docker.internal:8000` was reachable from inside `obid-n8n`. Host-side verification used `GET http://127.0.0.1:8000/status`. The shared middleware routes remain exactly:

- `GET /status`
- `POST /sensor-event`
- `POST /fan/on`
- `POST /fan/off`

The two additional n8n action-trigger webhook paths are Obid-owned disposable test plumbing, not additions to the Yacoub middleware contract.

## Provenance boundary

```text
YACOUB_INHERITED: middleware code, normalization, forwarding, routes, simulated state
SHARED_INTERFACE: sensor/action semantics and middleware endpoint meanings
OBID_CREATED: n8n Step 4 workflow, test triggers, observations, plan, map, evidence
TEST_DOUBLE: absent
```

