# Final Architecture - Frozen Tier 1.5

```mermaid
flowchart LR
  Input["Temperature event / test input<br/>simulated sensor values"]

  subgraph Middleware["Python middleware API<br/>PC baseline or Raspberry Pi Tier 1.5 endpoint"]
    Status["GET /status"]
    SensorEvent["POST /sensor-event<br/>receive event and push to n8n webhook"]
    FanOn["POST /fan/on<br/>simulated fan action"]
    FanOff["POST /fan/off<br/>simulated fan action"]
    NoGPIO["No real GPIO hardware<br/>no physical fan controlled"]
  end

  subgraph Contracts["Shared JSON contract layer"]
    SensorContract["sensor-event.schema.json<br/>sensor event examples"]
    ActionContract["agent-action.schema.json<br/>fan-on and blocked-action examples"]
  end

  subgraph Safety["Minimum safety / validation design"]
    Validation["One validation rule<br/>allowed, blocked, and risky cases"]
    Approval["Human approval checkpoint<br/>for risky or malformed action output"]
  end

  subgraph PC["PC host - local thesis runtime"]
    N8N["Docker Compose n8n<br/>local PC runtime<br/>localhost:5678"]

    subgraph Workflows["Two frozen n8n workflow paths"]
      Baseline["Deterministic baseline workflow<br/>fixed threshold rule"]
      Agent["Minimal agent-enhanced workflow<br/>one prompt set<br/>stateless / no memory"]
    end

    Eval["Evaluation harness<br/>scripts/collect_metrics.py<br/>scripts/aggregate_results.py"]
    CSV["CSV results<br/>evaluation/results/raw<br/>evaluation/results/processed<br/>evaluation/results/pi-validation"]
  end

  subgraph Pi["Raspberry Pi Tier 1.5 validation"]
    PiMiddleware["Python middleware/action endpoint<br/>runs on Raspberry Pi"]
    PiNoN8N["n8n is not deployed on Raspberry Pi"]
    PiNoGPIO["Fan action remains simulated<br/>no real GPIO hardware"]
  end

  Input --> SensorEvent
  SensorEvent --> SensorContract
  SensorContract --> N8N
  N8N --> Baseline
  N8N --> Agent
  Baseline --> ActionContract
  Agent --> ActionContract
  ActionContract --> Validation
  Validation --> Approval
  Approval --> FanOn
  Approval --> FanOff
  FanOn --> NoGPIO
  FanOff --> NoGPIO

  N8N -. "Tier 1.5 workflow call" .-> PiMiddleware
  PiMiddleware --> PiNoGPIO
  PiNoN8N -. "workflow runtime remains on PC" .-> N8N

  Eval -. "runs deterministic, agent, and safety cases" .-> N8N
  Eval -. "checks middleware status" .-> Status
  Eval -. "collects Pi latency, CPU, RAM, and thermal path evidence" .-> PiMiddleware
  Eval --> CSV

  classDef runtime fill:#eef6ff,stroke:#3b6ea8,color:#111827;
  classDef contract fill:#f1f8e9,stroke:#5b8c3a,color:#111827;
  classDef safety fill:#fff4e5,stroke:#b7791f,color:#111827;
  classDef evidence fill:#f7f7f7,stroke:#666,color:#111827;
  classDef limitation fill:#fff1f2,stroke:#be123c,color:#111827;

  class N8N,Baseline,Agent,Status,SensorEvent,FanOn,FanOff,PiMiddleware runtime;
  class SensorContract,ActionContract contract;
  class Validation,Approval safety;
  class Eval,CSV evidence;
  class NoGPIO,PiNoGPIO,PiNoN8N limitation;
```

**Caption:** Frozen Tier 1.5 architecture for the final thesis implementation. The diagram shows the temperature-event path, PC-hosted Docker n8n workflows, shared JSON contracts, minimum safety/validation boundary, Python middleware endpoints, evaluation harness, and Raspberry Pi validation split.

This is the final frozen architecture used for Chapter 5. It represents the narrowed new-yacoub implementation state after the implementation freeze: one deterministic baseline workflow, one minimal agent-enhanced workflow, one shared contract boundary, one minimum safety/approval design, and one measurable evaluation loop.

The Raspberry Pi part represents Tier 1.5 validation only. n8n remains deployed on the PC through Docker, while the Python middleware/action endpoint can run on the Raspberry Pi for validation evidence. This is not a full n8n-on-Pi deployment, and the fan action remains simulated with no real GPIO hardware or physical fan control.
