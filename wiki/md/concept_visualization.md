# Concept: Graph Visualization

Visualizing the workflow is crucial for debugging and understanding complex LangGraph structures. LangGraph provides several methods to generate diagrams.

## 1. ASCII Diagram
The simplest way to see the graph structure in the terminal.

```python
app.get_graph().print_ascii()
```

## 2. Mermaid PNG
Generates a high-quality PNG image using Mermaid.js. By default, this uses a web service (mermaid.ink) to render the image.

```python
# Generate PNG data
png_data = app.get_graph().draw_mermaid_png()

# Save to file
with open("graph.png", "wb") as f:
    f.write(png_data)
```

## 3. Mermaid String
Returns the raw Mermaid syntax string, which can be pasted into the [Mermaid Live Editor](https://mermaid.live/).

```python
mermaid_string = app.get_graph().draw_mermaid()
print(mermaid_string)
```

## 4. Professional Diagrams (Local)
For offline or more advanced visualization, you can install `pygraphviz`.
```bash
pip install pygraphviz
```
Once installed, LangGraph will use it locally to generate diagrams.

---
[Back to Wiki Index](../index.md)
