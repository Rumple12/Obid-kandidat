# Theory Background Flow

```mermaid
flowchart TB
  subgraph TOP[" "]
    direction LR
    A["Sensor / event"] --> B["Workflow orchestration"] --> C{"Decision"}
    C --> D["Deterministic rule"]
    C --> E["Agent-enhanced step"]
    D --> F["Structured action"]
    E --> F
  end

  subgraph BOTTOM[" "]
    direction LR
    G["JSON contract"] --> H["Validation / HITL"] --> I["Middleware API"] --> J["IoT-style action endpoint"]
  end

  %% Row-to-row connector represents Structured action continuing to JSON contract.
  TOP --> BOTTOM

  classDef node fill:#f8fafc,stroke:#475569,color:#111827;
  classDef decision fill:#eef6ff,stroke:#3b6ea8,color:#111827;
  classDef boundary fill:#fff4e5,stroke:#b7791f,color:#111827;
  classDef action fill:#fff1f2,stroke:#be123c,color:#111827;
  style TOP fill:transparent,stroke:transparent;
  style BOTTOM fill:transparent,stroke:transparent;

  class A,B,D,E,F,G node;
  class C decision;
  class H boundary;
  class I,J action;
```

**Purpose:** This is a compact conceptual theory/background diagram for Chapter 2. It shows the general event-to-action pattern used in the thesis: sensor or event input, workflow orchestration, deterministic or agent-enhanced decision, structured action output, JSON contract, validation/HITL boundary, middleware/API boundary, and IoT-style action endpoint.

**Caption for thesis:** Conceptual event-to-action pattern used to frame the thesis. Sensor input is handled by workflow orchestration, converted into a deterministic or agent-enhanced action, checked through a contract and validation boundary, and routed through middleware before reaching an IoT-style endpoint.

This is not the final architecture diagram and not runtime evidence. It is intended to support the theory and related-work discussion.
