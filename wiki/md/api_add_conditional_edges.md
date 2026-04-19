# API: `add_conditional_edges`

Creates dynamic transitions between nodes based on the current state. This allows for branching and looping.

## Syntax
```python
workflow.add_conditional_edges(source, path, path_map)
```

## Parameters
- **`source`** (str): The name of the node where the branching logic originates.
- **`path`** (Callable): A "routing function" that:
    - Receives the current `State`.
    - Returns a string (the decision key).
- **`path_map`** (dict): A dictionary mapping the keys returned by the `path` function to specific target nodes.

## Example
```python
def router(state: MyState) -> str:
    if state["score"] > 5:
        return "pass"
    return "fail"

workflow.add_conditional_edges(
    "evaluator",
    router,
    {
        "pass": "success_node",
        "fail": "retry_node"
    }
)
```

## Notes
- If the routing function returns a key not present in the `path_map`, the graph will raise an error.
- Conditional edges are often used with `END` to create termination conditions in loops.

---
[Back to API Reference](stategraph_api.md) | [Back to Wiki Index](../index.md)
