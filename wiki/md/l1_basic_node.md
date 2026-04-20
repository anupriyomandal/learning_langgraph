# Lesson 1: Single Node Graph

In this lesson, we learned how to create a basic LangGraph workflow with a single node.

## Key Concepts

### 1. State Definition
The `State` defines the data structure that is passed between nodes. It's typically a `TypedDict`.

```python
from typing import TypedDict

class AgentState(TypedDict):
    messages: str
```
*Learn more about [State Management](concept_state.md).*


### 2. Nodes
A node is just a Python function that takes the current state and returns an updated state (or a subset of it).

```python
def process_node(state: AgentState) -> AgentState:
    state['messages'] = f"Hello {state['messages']}"
    return state
```

### 3. StateGraph
The `StateGraph` is used to define the structure of the workflow.

```python
from langgraph.graph import StateGraph

workflow = StateGraph(AgentState)
workflow.add_node("process_node", process_node)
```
*Learn more about [StateGraph and Compilation](concept_stategraph.md).*


### 4. Entry and Exit Points
You must explicitly define where the graph starts and ends using the `START` and `END` constants from `langgraph.graph`.

```python
from langgraph.graph import START, END

# Define entry and exit points
workflow.add_edge(START, "process_node")
workflow.add_edge("process_node", END)
```

#### Alternative Methods
As seen in [Lesson 1.1](l1_1_multi_key_state.md), you can also use:
- `workflow.set_entry_point("node_name")`
- `workflow.set_finish_point("node_name")`


### 5. Compilation and Invocation
Before running the graph, you must compile it. This returns a runnable object (often referred to as an "app" or "compiled graph").

```python
# Compile the workflow
app = workflow.compile()

# Invoke the compiled app
result = app.invoke({'messages': 'User'})
```

## Common Pitfalls
- **Missing Entry Point**: A graph must have an entry point defined via `add_edge(START, "node_name")`.
- **Invoking the Graph Object**: You cannot call `.invoke()` on the `StateGraph` object directly; you must call `.compile()` first and then invoke the result.
- **Legacy/Invalid Methods**: Avoid using non-existent methods like `.start_node()` or `.end_node()`. Use the edge system with `START` and `END` instead.

---
[Home](../index.md) | [Next Lesson: Multiple State Keys](l1_1_multi_key_state.md)
