# Memory Choice v1

Chosen memory strategy: **stateless execution / no memory**.

## Reason

The new-yacoub scope is intentionally narrow:

- one temperature-event path
- one fan-action path
- one minimal agent-enhanced workflow
- one baseline-vs-agent comparison
- PC-first development before Raspberry Pi validation

The Step 7 workflow only needs the current event payload to choose between
`fan_on` and `fan_off`. Keeping the agent stateless makes the behavior easier
to inspect, repeat, and compare with the deterministic baseline.

## Fit With Edge And Resource Constraints

No memory is the simplest option for the thesis because it:

- avoids storing unnecessary state
- reduces runtime and configuration complexity
- keeps resource use low for later Raspberry Pi validation
- avoids turning the project into a memory-strategy comparison
- keeps the Obid-compatible layer minimal

## Deferred Work

Window buffer memory, long-term memory, vector stores, and multi-agent memory
patterns are out of scope for this narrowed implementation.

If a future version needs history-aware behavior, that should be documented as
future work after the Yacoub-complete vertical slice is stable.
