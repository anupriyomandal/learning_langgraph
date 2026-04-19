# Concept: Edges

Edges are the connectors in a LangGraph workflow. They define how the state moves from one node to another, creating the "graph" structure.

## Types of Edges

### 1. Normal Edges (`add_edge`)
A normal edge defines a fixed, direct path between two nodes. When the source node finishes execution, the destination node is immediately queued.

```python
workflow.add_edge("source_node", "destination_node")
```

### 2. Conditional Edges (`add_conditional_edges`)
Conditional edges allow for dynamic routing. A routing function inspects the state and returns a key, which is then mapped to a specific node.

```python
workflow.add_conditional_edges(
    "source_node",
    routing_function,
    {
        "key_a": "node_a",
        "key_b": "node_b"
    }
)
```

## Special Nodes & Edges

### `START`
The `START` constant is used to define the entry point of the graph. It is technically a virtual node that you draw an edge *from*.
```python
from langgraph.graph import START
workflow.add_edge(START, "first_node")
```

### `END`
The `END` constant represents the terminal state of the graph. When an edge points to `END`, the graph execution stops.
```python
from langgraph.graph import END
workflow.add_edge("last_node", END)
```

## Cycle Management (Loops)
Edges can point back to nodes that have already been executed, creating a **Cycle**. This is how iterative behaviors (like agentic loops) are implemented.

## Key Rules for Edges
- **Source must exist**: You cannot add an edge from a node that hasn't been added to the graph using `add_node`.
- **Connectivity**: Every node (except those pointing to `END`) should have at least one outgoing edge to ensure the graph doesn't hang.
- **Entrypoint**: A graph must have exactly one entry point defined via `START`.

---
## Related Concepts
- [Nodes vs. Edges](concept_nodes_vs_edges.md)
- [Conditional Edges](concept_conditional_edges.md)
- [Loops (Recurrent Graphs)](concept_loops.md)

---
[Back to Wiki Index](../index.md)
