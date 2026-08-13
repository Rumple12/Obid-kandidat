**Begränsad delning**

**Project Proposed by:** Stefan Forsström

# Agentic AI and the IoT

## Background





> \[!IMPORTANT]

> This file summarizes the original supervisor brief and broader thesis context.

> In the new-yacoub thesis mode, it must be interpreted through the narrowed implementation plan.

> Any broader agentic or comparative possibilities mentioned here are not automatically in scope.







"Agentic AI" refers to systems that pursue goals with limited supervision by planning, calling tools, and acting autonomously-often coordinating multiple sub-agents. This goes beyond chat "copilots" toward proactive, goal-seeking automation, raising questions about reliability, oversight, and cost. The n8n platform now ships opinionated building blocks for agents (AI Agent node, memory, tool connectors) plus operational guardrails (deterministic steps, human-in-the-loop nodes, logs) and first-class Evaluations for AI Workflows to measure quality in production. These features make n8n a practical testbed for agentic research.

## Problem Specification

Investigate how far agentic AI built in n8n can be pushed technically and operationally by designing one or more agents for IoT scenarios. Use n8n's AI Agent node, memory, and tool connectors to plan, act, and optionally coordinate multi-agent workflows. As well as integrate external tools/data via where appropriate. Quantify reliability, tool-use correctness, latency/cost, and the efficiency. Compare single-agent vs multi-agent designs on the same task.

## Suggested Method

Look into the different ways of implementing an efficient agentic AI IoT solution on typical IoT devices, like using Raspberry Pi devices. Choose a relevant scenario, build something small to prove the concept to verify and evaluate if the chosen solution can be used. Evaluate with different devices and models, performance, scalability, and overhead. Back up your evaluation with mathematical modelling/analysis if possible.

## Relevant Articles

\[1] Hosseini S, Seilani H. The role of agentic ai in shaping a smart future: A systematic review. Array. 2025 May 8:100399.

\[2] Sapkota R, Roumeliotis KI, Karkee M. Ai agents vs. agentic ai: A conceptual taxonomy, applications and challenges. arXiv preprint arXiv:2505.10468. 2025 May 15.

\[3] Barra FL, Rodella G, Costa A, Scalogna A, Carenzo L, Monzani A, Corte FD. From prompt to platform: an agentic AI workflow for healthcare simulation scenario design. Advances in Simulation. 2025 May 16;10(1):29.

\[4] Dresselhaus N. Case Study: Local LLM-Based NER with n8n and Ollama.

\[5] Pajo P. Multi-Agentic Platforms: Architectures, Applications, and Emerging Research Frontiers in Collaborative AI Systems.

