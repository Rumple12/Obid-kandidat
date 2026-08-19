Use this content:



\# Step 07 Runtime Verification — Minimal Agent Workflow



\## Test environment



\- n8n running locally through Docker at `http://localhost:5678`

\- Middleware running locally with `python -m middleware.api.app`

\- Middleware reachable from Dockerized n8n through `http://host.docker.internal:8000`

\- Model used: Google Gemini Chat Model

\- Memory strategy: stateless / no memory

\- Workflow file: `cognitive\_logic/workflows/agent-minimal.json`



\## Runtime status



Runtime verification succeeded.



The Step 7 workflow was imported into n8n, connected to a Google Gemini Chat Model, and tested with both high-temperature and low-temperature events.



\## High-temperature test



Input:



```json

{

&#x20; "sensor\_id": "temp\_sensor\_1",

&#x20; "timestamp": "2026-04-25T20:00:00Z",

&#x20; "type": "temperature",

&#x20; "value": 31.4,

&#x20; "unit": "C"

}



Expected result:



Agent chooses fan\_on

Structured action contains action\_id = fan\_on

Workflow routes to POST middleware fan on

Middleware returns status = ok, action = fan\_on, fan = on, simulated = true



Evidence files:



step-07-high-temp-canvas.png

step-07-high-temp-agent-output.png

step-07-high-temp-parsed-action.png

step-07-high-temp-fan-on-output.png

Low-temperature test



Input:



{

&#x20; "sensor\_id": "temp\_sensor\_1",

&#x20; "timestamp": "2026-04-25T20:05:00Z",

&#x20; "type": "temperature",

&#x20; "value": 24.5,

&#x20; "unit": "C"

}



Expected result:



Agent chooses fan\_off

Structured action contains action\_id = fan\_off

Workflow routes to POST middleware fan off

Middleware returns status = ok, action = fan\_off, fan = off, simulated = true



Evidence files:



step-07-low-temp-canvas.png

step-07-low-temp-agent-output.png

step-07-low-temp-parsed-action.png

step-07-low-temp-fan-off-output.png

Limitations

This step does not implement safety approval or policy enforcement. That belongs to Step 8.

This step does not compare multiple models.

This step does not use memory; execution is stateless by design.

This step does not measure latency or resource usage yet. Measurement belongs to Step 9.

Result



Step 7 verifies that the system can support a minimal agent-enhanced workflow that produces structured action output and calls the same middleware endpoints as the deterministic baseline.





Only write \*\*“Runtime verification succeeded”\*\* if both high-temp and low-temp tests worked.



If low-temp has not been tested yet, write:



```md

Runtime verification is partially complete. High-temperature `fan\_on` was verified, but low-temperature `fan\_off` still needs evidence.

