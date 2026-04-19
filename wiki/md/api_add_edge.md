# API: `add_edge`

Creates a directed transition (a normal edge) between two nodes in the graph.

## Syntax
```python
workflow.add_edge(source, target)
```

## Parameters
- **`source`** (str): The name of the node where the edge starts.
- **`target`** (str): The name of the node where the edge ends.

## Special Constants
- **`START`**: Use as a source to define the entry point of the graph.
- **`END`**: Use as a target to define where the graph execution terminates.

## Example
```python
from langgraph.graph import START, END

# Define entry point
workflow.add_edge(START, "greeting_node")

# Define sequential flow
workflow.add_edge("greeting_node", "process_node")

# Define termination
workflow.add_edge("process_node", END)
```

## Notes
- Normal edges are deterministic; the graph will always follow this path once the source node completes.
- Both source and target must be either valid node names or special constants.

---
[Back to API Reference](stategraph_api.md) | [Back to Wiki Index](../index.md)
