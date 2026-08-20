# Step 3 report-support note

## Step

Step 3 — Bring up Obid's n8n environment and verify Yacoub compatibility

## Status

Step 3 passed re-audit after two minor documentation repairs. The Obid local n8n runtime is operational, and the runtime compatibility prerequisites were verified. Step 4 shared-interface behavior has **not** been tested. The audit verdict is a completion review, not experimental evidence.

## What Step 3 established

Step 3 established:

- one minimal local Dockerized n8n service;
- a pinned n8n version and reproducible Compose configuration;
- persistent local n8n storage;
- verified HTTP and UI availability;
- verified owner/application initialization persistence;
- the node capabilities required by the inherited workflow exports;
- the Docker-to-host name-resolution prerequisite;
- a provenance-labelled runtime manifest and verification record; and
- safe verification commands that avoid exposing environment secrets.

These results concern the local runtime prerequisite only, not sensor-to-action integration.

## Runtime configuration

| Item | Verified configuration |
| --- | --- |
| Compose project | `obid-step3` |
| Container | `obid-n8n` |
| Image | `n8nio/n8n:1.123.37` |
| Host port | `5678` |
| Container port | `5678/tcp` |
| Storage | n8n default local SQLite |
| Named volume | `obid-n8n-data` |
| Mount | `/home/node/.n8n` |
| Timezone | `Europe/Stockholm` through `GENERIC_TIMEZONE` and `TZ` |
| Diagnostics | disabled |
| Version notifications | disabled |

The setup intentionally excludes PostgreSQL, Redis, Prometheus, Grafana, MCP, a reverse proxy, Raspberry Pi deployment, and a middleware service. This preserves the smallest runtime needed for the thesis and avoids introducing infrastructure outside Step 3.

## Environment and version evidence

| Item | Observed value |
| --- | --- |
| Host | Windows 11 |
| Docker context | `desktop-linux` |
| Docker CLI | `29.5.2` |
| Docker Engine | `29.5.2` |
| Docker Compose | `v5.1.3` |
| Requested image | `n8nio/n8n:1.123.37` |
| Resolved image identifier/digest | `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Runtime-reported n8n version | `1.123.37` |

The actual running n8n version was verified independently of the image tag by invoking the runtime version command inside the container. Docker and node-package versions are separate observations and are not the n8n runtime version.

## Yacoub compatibility

The authoritative inherited comparison source is `Rumple12/new-yacoub-thesis` at frozen commit `278318340bfa4e4650a97a2baba73f63bd868ed9`.

Yacoub's frozen runtime used the same relevant assumptions:

- n8n `1.123.37`;
- one local n8n service;
- port `5678`;
- default SQLite persistence;
- a named Docker volume;
- Stockholm timezone; and
- disabled diagnostics and version notifications.

Obid intentionally reproduced these compatibility assumptions rather than redesigning the runtime. Narrow Obid-specific differences are:

- Obid-specific Compose project, container, and volume names;
- an explicit requirement for a private, ignored local encryption key; and
- an explicit `TZ` setting alongside `GENERIC_TIMEZONE`.

These differences preserve ownership separation and do not alter the intended workflow compatibility boundary.

## Provenance

### `YACOUB_INHERITED` / `REFERENCE_ONLY`

Yacoub owns the prior pinned n8n configuration, Docker/runtime assumptions, inherited workflow exports, and prior runtime verification/evidence.

### `OBID_CREATED`

Obid owns the active Step 3 Compose configuration, the local Obid runtime instance, runtime manifest, Step 3 verification evidence, and newly generated compatibility observations.

Using the same compatible n8n version and configuration approach does not transfer authorship of Yacoub's prior work to Obid.

## Startup and UI verification

Docker Desktop was initially not running. This recoverable preflight failure was retained in the evidence. After Docker Desktop was started, Compose validation succeeded, the n8n container started, HTTP returned `200`, and the UI was reachable.

### Before owner initialization

The fresh instance showed `Set up owner account`.

### After private owner initialization and restart

Both `/` and `/setup` resolved to `/signin`, and the owner-setup prompt was absent. No owner identity, password, cookie, credential, or secret was captured.

## Persistence verification

The non-destructive persistence sequence was:

1. n8n state used named volume `obid-n8n-data`.
2. `docker compose down` was performed without `-v`.
3. The named volume remained present.
4. `docker compose up -d` recreated the container.
5. The same volume remounted at `/home/node/.n8n`.
6. n8n returned as version `1.123.37`.
7. HTTP returned `200`.
8. Initialized application state remained, demonstrated by `/signin` behavior instead of fresh owner setup.

- Named-volume persistence: `VERIFIED`
- Application/owner initialization persistence: `VERIFIED`

This verifies persisted initialization, not the content or validity of owner credentials. Credentials were neither inspected nor disclosed.

## Required node capability

Step 3 inspected the frozen Yacoub workflow exports without importing or executing them.

Required built-in capabilities verified as available:

- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.if`
- `n8n-nodes-base.set`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`

Required LangChain capability:

- `@n8n/n8n-nodes-langchain.chainLlm`

Also verified as available:

- Google Gemini Chat Model node: `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`

Observed installed package versions were:

- `n8n-nodes-base` `1.121.25`
- `@n8n/n8n-nodes-langchain` `1.122.27`

These are package versions inside the n8n image, not the n8n runtime version, which is `1.123.37`. Step 3 did not configure a Gemini credential, select the exact Gemini model, or establish generation settings. Those remain Step 6 responsibilities.

## Docker-to-host networking prerequisite

`host.docker.internal` resolved inside the running n8n container to `192.168.65.254`.

This verifies only the Docker-to-host name-resolution prerequisite. It does **not** verify middleware reachability, `/status`, `/sensor-event`, `/fan/on`, `/fan/off`, or end-to-end forwarding. Those checks belong to Step 4.

## Secret-handling and audit repair

Step 3 uses an ignored real `.env`, a public `.env.example` containing placeholders only, and a private local encryption key that is not stored in evidence.

The audit identified a documentation risk: generic `docker inspect obid-n8n` output could expose environment values. The documentation was repaired to use narrow `docker inspect --format` commands for image, port, and mount metadata. No secret exposure occurred, and no real key is reproduced in this note.

## Runtime warnings / deviations

### Version deviation

None.

### Port deviation

None.

### Recoverable startup issue

Docker Desktop was initially stopped and was started before runtime verification.

### n8n warnings

Future-facing deprecation warnings were observed for areas including SQLite pool configuration, task runners, Code-node environment access, and Git bare-repository behavior. They did not block Step 3, and no speculative configuration expansion was introduced.

## Evidence / source artifacts

- `infrastructure/docker/docker-compose.yml`
- `infrastructure/docker/.env.example`
- `infrastructure/docker/README.md`
- `infrastructure/docker/runtime-manifest.md`
- `infrastructure/docker/evidence/step-03-runtime-verification.md`
- `docs/collaboration/handoff-verification-checklist.md`

Repository checkpoints:

- Initial runtime: `8dbebf2c6e1b8648a47397983c27cf9ace517ad7`
- Persistence continuation: `a86f8c4f9f8164b3f5fee6544a5ed06b713df978`
- Documentation repair: `d1435d9cb09c77b276e52a3c950658ca8c125482`

The audit exists as Codex/thread review; this note does not invent a separate committed audit artifact.

## Handoff checklist result

Step 3 completed:

- `[CHECK-S3-01]` exact Obid n8n version;
- `[CHECK-S3-02]` frozen Yacoub version comparison;
- `[CHECK-S3-03]` required node availability; and
- `[CHECK-S3-04]` compatibility decision.

Step 4–6 checks and the provenance/adoption prerequisite checks remain unticked until their assigned steps.

## Thesis chapters supported

- Chapter 3 — reproducible environment/setup and verification method;
- Chapter 4 — platform choice and the Yacoub/Obid compatibility boundary;
- Chapter 5 — local n8n runtime implementation/setup; and
- Appendix — runtime manifest, version/environment details, and reproducibility commands.

Step 3 contributes no reliability-comparison results for RQ1–RQ3.

## What Step 3 did NOT establish

Step 3 did not:

- run or copy Yacoub middleware;
- prove middleware reachability;
- test `/status`;
- test `/sensor-event`;
- test `/fan/on`;
- test `/fan/off`;
- configure `N8N_WEBHOOK_URL` end to end;
- import deterministic or agent baselines;
- adopt schemas;
- configure Gemini credentials or model settings;
- implement prompts, tools, ReAct behavior, or memory;
- implement runtime validation or policy;
- implement HITL;
- create evaluation cases;
- run thesis evaluation; or
- deploy Raspberry Pi hardware.

This boundary prevents later reporting from confusing runtime compatibility with end-to-end integration.

## Next-step dependency

Step 3 leaves the repository ready for `Step 4 — Establish the Yacoub-compatible integration test boundary`.

Step 4 will test the actual seams:

```text
sensor/middleware event
→ Obid n8n boundary
→ Yacoub-compatible action boundary
```

It will do so without yet adding Obid agent intelligence. No Step 4 work was begun in this note.
