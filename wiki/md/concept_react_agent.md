# Concept: The ReAct Framework (Reason + Act)

The **ReAct** (Reasoning and Acting) framework is a breakthrough architectural pattern that enables LLMs to solve complex tasks by interleaving reasoning traces with task-specific actions.

## 1. Core Philosophy
Traditional LLM usage often involves "one-shot" prompting where the model tries to solve everything in one go. ReAct breaks this down into a multi-step cycle:

1.  **Reasoning**: The model generates a "Thought" describing its understanding of the task and what it needs to do next.
2.  **Acting**: Based on the thought, the model executes an "Action" (a tool call).
3.  **Observation**: The environment (the tool) returns an "Observation" (result).
4.  **Repeat**: The model analyzes the observation and decides whether to continue reasoning or provide a final answer.

## 2. The Components of a ReAct Loop

### A. The Agent (The Brain)
Typically a Large Language Model (LLM) that has been trained or prompted to generate structured output (like JSON or function calls).

### B. Tools (The Hands)
Functions or APIs that the agent can invoke to interact with the world (e.g., search engines, calculators, database connectors).

### C. The Environment (The Context)
The state of the conversation and the observations received so far.

## 3. Why ReAct?
- **Transparency**: You can follow the agent's thought process (the "chain of thought").
- **Error Correction**: If a tool returns an error, the agent can reason about the error and try a different approach.
- **Dynamic Planning**: The agent doesn't need a hard-coded path; it creates its own path based on the information it discovers.

## 4. Implementation in LangGraph
In LangGraph, ReAct is implemented as a **cyclic graph**:
- **Node A**: The LLM (generates Thoughts/Actions).
- **Conditional Edge**: Checks if a tool call was requested.
- **Node B**: The `ToolNode` (executes the action and returns the Observation).
- **Edge**: Leads back to Node A to complete the loop.

---
## Related Concepts
- [Message Types](concept_messages.md)
- [Loops (Recurrent Graphs)](concept_loops.md)
- [add_messages Reducer](concept_add_messages.md)

---
[Back: Wiki Index](../index.md)
