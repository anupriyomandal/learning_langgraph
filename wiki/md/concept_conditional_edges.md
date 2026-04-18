# Concept: Conditional Edges

Conditional edges allow a LangGraph workflow to dynamically choose the next node based on the current state. Unlike standard edges (`add_edge`), which define a fixed path, conditional edges use a "routing function" to determine where to go next.

## How it Works

1. **Routing Function**: A function that takes the `State` as input and returns a string (the "path" or "key").
2. **Path Mapping**: A dictionary that maps the string returned by the routing function to a specific node in the graph.

## Syntax

```python
workflow.add_conditional_edges(
    "source_node",
    routing_function,
    {
        "path_a": "node_1",
        "path_b": "node_2",
        "default": "node_3"
    }
)
```

## Example

```python
def router(state: MyState):
    if state["score"] > 5:
        return "high"
    return "low"

workflow.add_conditional_edges(
    "evaluator",
    router,
    {
        "high": "success_node",
        "low": "retry_node"
    }
)
```

## Why use Conditional Edges?
- **Decision Making**: Branching logic (e.g., "if task complete, go to END, else go back to agent").
- **Error Handling**: Redirecting to a recovery node if an error is detected in the state.
- **Dynamic Routing**: Sending work to different specialized nodes based on input type.

---
[Back to Wiki Index](../index.md)
