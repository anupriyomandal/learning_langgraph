# Lesson 1.1: Single Node with Multiple State Keys

In this lesson, we expanded on the single node graph by using a state with multiple keys and exploring alternative ways to define entry and exit points.

## Key Concepts

### 1. State with Multiple Keys
The `AgentState` can contain multiple fields. When invoking the graph, you can provide initial values for any of these fields.

```python
class AgentState(TypedDict):
    messages: str
    name: str
```

In `l1_1_multi_key_state.py`, we provide `name` and the node updates `messages`:
```python
def process_node(state: AgentState) -> AgentState:
    state['messages'] = f"Hello {state['name']}"
    return state
```

### 2. Alternative Entry/Exit Definitions
Instead of using `add_edge(START, "node")` and `add_edge("node", END)`, you can use explicit methods:

```python
workflow.set_entry_point('process_node')
workflow.set_finish_point('process_node')
```

- **`set_entry_point(node_name)`**: Specifies which node should run first.
- **`set_finish_point(node_name)`**: Specifies that after this node runs, the graph should terminate (unless there are other edges).

### 3. State Persistence (Partial Updates)
When a node returns a dictionary, LangGraph updates the state. If the state is a `TypedDict`, the returned keys overwrite or add to the existing state.

---
## Cross-References
- [Lesson 1: Basics of StateGraph](l1_basic_node.md) - Basic setup of a single node graph.
- [State Definition](l1_basic_node.md#1-state-definition) - How `TypedDict` is used for state.

---
[Home](../index.md) | [Back to Lesson 1](l1_basic_node.md)
