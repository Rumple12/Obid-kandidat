# Controlled ReAct-style configuration v1

CONFIG-OBID uses one tool-calling AI Agent with an observable bounded cycle:

```text
valid event
-> temperature_threshold_tool
-> optional fan_status_tool when memory is cold
-> one final JSON decision envelope
```

The AI Agent node is `@n8n/n8n-nodes-langchain.agent` type version `3`.
Its hard `options.maxIterations` value is `3`. In the installed implementation,
each model response containing tool calls increments the iteration counter and
the next continuation is rejected when the incoming count is at least the
configured maximum. Three is therefore the smallest bound that permits two
sequential tool rounds followed by a final answer; parallel cold-start tool
calls finish within the same or a smaller bound.

`returnIntermediateSteps` is disabled. Tool names, inputs, results, call order,
and counts are observed from the tool nodes' stored execution data. This avoids
retaining model message-log internals or hidden reasoning. A successful agent
node completion, the configured bound, the observed tool-call count, and the
workflow execution status provide bounded-termination evidence.

No retry, self-repair, fallback model, recursive agent, or dynamic tool path is
configured. A formatting or tool-selection failure is retained as observed.
