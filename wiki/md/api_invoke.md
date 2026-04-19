# API: `invoke`

Executes the compiled graph with an initial set of inputs.

## Syntax
```python
result = app.invoke(input_state)
```

## Parameters
- **`input_state`** (dict): A dictionary matching the state schema defined when the `StateGraph` was initialized.

## Returns
- **`result`** (dict): The final state of the graph after all nodes have completed and execution reaches `END`.

## Example
```python
initial_state = {"user_name": "Alice", "count": 0}
final_state = app.invoke(initial_state)

print(final_state["count"])
```

## Notes
- `invoke` is synchronous and blocks until the graph finishes.
- The returned dictionary contains the cumulative updates from all nodes visited during the run.

---
[Back to API Reference](stategraph_api.md) | [Back to Wiki Index](../index.md)
