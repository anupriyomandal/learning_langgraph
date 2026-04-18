# Concept: State Management

In LangGraph, the **State** is the single source of truth that is passed between nodes. Each node receives the current state, performs some logic, and returns an updated version of the state.

## 1. Defining State with `TypedDict`
The most common way to define state is using a `TypedDict`. This provides type hinting and structure for the data flowing through your graph.

```python
from typing import TypedDict, List

class AgentState(TypedDict):
    messages: str
    history: List[str]
```

## 2. State Updates
When a node returns a dictionary, LangGraph merges it into the existing state. 
- By default, existing keys are **overwritten**.
- You can define custom "reducer" functions (using `Annotated`) to specify how keys should be updated (e.g., appending to a list instead of overwriting).

## 3. Why it matters
State management allows your agent to:
- "Remember" what happened in previous steps.
- Accumulate results over multiple nodes.
- Maintain a structured history of messages or decisions.

---
[Back to Wiki Home](../index.md)
