# StateGraph API Reference

This page summarizes the `StateGraph` methods and related objects we have encountered in the lessons so far.

## `StateGraph` Class
The core class used to define the structure of your workflow.

- [`add_node`](api_add_node.md): Add a unit of work.
- [`add_edge`](api_add_edge.md): Create fixed paths.
- [`add_conditional_edges`](api_add_conditional_edges.md): Create dynamic routing.
- [`compile`](api_compile.md): Finalize graph structure.

## `CompiledGraph` (App) Methods
The object returned by `workflow.compile()`.

- [`invoke`](api_invoke.md): Run the graph.
- [`get_graph`](api_visualization.md): Access the graph for visualization.

## Visualization Methods
- [`print_ascii`](api_visualization.md)
- [`draw_mermaid_png`](api_visualization.md)

---
[Back to Wiki Index](../index.md)
