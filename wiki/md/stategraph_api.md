# StateGraph API Reference

This page summarizes the `StateGraph` methods and related objects we have encountered in the lessons so far.

## `StateGraph` Class
The core class used to define the structure of your workflow.

### `StateGraph(state_schema)`
Initializes the graph with a state schema (usually a `TypedDict`).
```python
workflow = StateGraph(AgentState)
```

### `add_node(name, action)`
Adds a new node to the graph.
- **`name`**: A unique string identifier for the node.
- **`action`**: A function (or runnable) that takes the state and returns an updated state.
```python
workflow.add_node("my_node", my_function)
```

### `add_edge(source, target)`
Creates a fixed path between two nodes.
- **`source`**: The name of the node where the edge starts.
- **`target`**: The name of the node where the edge ends.
```python
workflow.add_edge("node_a", "node_b")
```

### `add_conditional_edges(source, path, path_map)`
Creates a dynamic path based on logic.
- **`source`**: The name of the node where the branch starts.
- **`path`**: A function that takes the state and returns a key.
- **`path_map`**: A dictionary mapping keys to target node names.
```python
workflow.add_conditional_edges("router", router_func, {"a": "node_a", "b": "node_b"})
```

### `compile()`
Finalizes the graph structure and returns a compiled `CompiledGraph` (app) that can be executed.
```python
app = workflow.compile()
```

### `set_entry_point(node_name)` / `set_finish_point(node_name)`
*Legacy/Alternative methods* for defining the start and end of the graph. 
**Note**: It is now more common to use `add_edge(START, node_name)` and `add_edge(node_name, END)`.

---

## `CompiledGraph` (App) Methods
The object returned by `workflow.compile()`.

### `invoke(input_state)`
Runs the graph with the provided initial state.
```python
result = app.invoke({"count": 0})
```

### `get_graph()`
Returns the internal graph representation, useful for visualization.
```python
graph = app.get_graph()
```

---

## Visualization Methods
Methods called on the object returned by `get_graph()`.

### `print_ascii()`
Prints a simple ASCII representation of the graph to the terminal.
```python
app.get_graph().print_ascii()
```

### `draw_mermaid_png()`
Generates a PNG image of the graph using Mermaid.js.
```python
png_data = app.get_graph().draw_mermaid_png()
```

---
[Back to Wiki Index](../index.md)
