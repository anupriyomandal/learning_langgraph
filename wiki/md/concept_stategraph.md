# Concept: StateGraph and Compilation

The **StateGraph** is the core class used to define the structure of your workflow. It acts as a blueprint for how data moves through your system.

## 1. The Blueprint (`StateGraph`)
You initialize a `StateGraph` by passing it the state schema (usually your `TypedDict`).

```python
from langgraph.graph import StateGraph
workflow = StateGraph(AgentState)
```

## 2. Nodes and Edges
- **Nodes**: Individual processing steps (Python functions).
- **Edges**: The paths between nodes.
  - `START`: A special constant indicating where the graph begins.
  - `END`: A special constant indicating where the graph terminates.

## 3. Compilation
Before a graph can be executed, it must be **compiled**. Compilation validates the graph structure (ensuring there's an entry point and no dead ends) and returns a "Runnable" application.

```python
app = workflow.compile()
```

## 4. Invocation
Once compiled, you use `.invoke()` to start the process, passing in the initial state.

```python
final_state = app.invoke({"name": "User"})
```

---
[Back to Wiki Home](../index.md)
