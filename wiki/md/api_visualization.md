# API: Visualization Methods

Methods used to generate visual representations of the graph for debugging and documentation.

## `print_ascii`
Prints a simple text-based diagram directly to the terminal.
```python
app.get_graph().print_ascii()
```

## `draw_mermaid_png`
Generates a high-quality PNG image using Mermaid.js.
```python
png_data = app.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png_data)
```

## `draw_mermaid`
Returns the raw Mermaid syntax string.
```python
mermaid_str = app.get_graph().draw_mermaid()
```

---
[Back to API Reference](stategraph_api.md) | [Back to Wiki Index](../index.md)
