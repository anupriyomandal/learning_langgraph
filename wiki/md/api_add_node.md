# API: `add_node`

Adds a new node to the graph. Each node represents a discrete unit of work.

## Syntax
```python
workflow.add_node(name, action)
```

## Parameters
- **`name`** (str): A unique string identifier for the node. This name is used to reference the node in edges.
- **`action`** (Callable): A function, lambda, or Runnable that defines the node's behavior. It must:
    - Take the current `State` as input.
    - Return a dictionary with updated state keys.

## Example
```python
def my_node_func(state: MyState) -> MyState:
    state["count"] += 1
    return state

workflow.add_node("counter", my_node_func)
```

## Notes
- You cannot add two nodes with the same name to the same graph.
- The node function can be a regular function or a lambda for simple pass-through logic.

---
[Back to API Reference](stategraph_api.md) | [Back to Wiki Index](../index.md)
