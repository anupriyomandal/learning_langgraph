# API: `compile`

Finalizes the `StateGraph` and converts it into a `CompiledGraph` (often referred to as the `app`).

## Syntax
```python
app = workflow.compile()
```

## What it does
- Validates the graph structure (ensures entry points exist, no dangling nodes without END, etc.).
- Prepares the graph for execution by checking the state schema and reducers.
- Returns an object that can be invoked with a state dictionary.

## Notes
- Once a graph is compiled, you cannot add more nodes or edges to it.
- The resulting `app` object provides the `invoke` method for running the workflow.

---
[Back to API Reference](stategraph_api.md) | [Back to Wiki Index](../index.md)
