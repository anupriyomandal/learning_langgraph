# Concept: Nodes vs. Edges

In LangGraph, a workflow is defined as a directed graph. The two primary building blocks of this graph are **Nodes** and **Edges**. Understanding the distinction between them is fundamental to building effective stateful applications.

## 1. Nodes (The "Workers")
Nodes represent the **computational steps** or units of work in your graph.

- **What they are**: In Python, a node is typically a function or a runnable that takes the current `State` as input and returns an updated `State`.
- **Purpose**: To perform actions (API calls, calculations, data processing) and transform the state.
- **Responsibility**: "What should be done?"
- **Syntax**: 
  ```python
  workflow.add_node("node_name", my_function)
  ```

## 2. Edges (The "Paths")
Edges define the **control flow** or the transition logic between nodes. See [Edges](concept_edges.md) for a detailed breakdown.

- **What they are**: They are the connections that determine which node should execute after the current one finishes.
- **Purpose**: To route the state from one node to another.
- **Responsibility**: "Where should we go next?"
- **Types**:
    - **Normal Edges**: A direct, fixed path from Node A to Node B.
    - **Conditional Edges**: A dynamic path where a "routing function" decides the next node based on the current state.
- **Syntax**:
  ```python
  workflow.add_edge("node_a", "node_b") # Normal
  workflow.add_conditional_edges("node_a", router_func, mapping) # Conditional
  ```

## Key Differences

| Feature | Node | Edge |
| :--- | :--- | :--- |
| **Analogy** | A room where work happens. | A hallway connecting rooms. |
| **Logic** | Contains business logic/tasks. | Contains routing/flow logic. |
| **State Interaction** | Receives and **modifies** the state. | Receives state to **inspect** (in conditional edges) but does not modify it. |
| **Execution** | Performs the actual computation. | Orchestrates the sequence of computation. |

## Special Edges
- **`START`**: A special edge from the beginning of the graph to the first node (the entry point).
- **`END`**: A special edge from a node to the termination point of the graph.

---
[Back to Wiki Index](../index.md)
