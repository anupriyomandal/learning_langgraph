# Concept: Loops (Recurrent Graphs)

One of the most powerful features of LangGraph is the ability to create loops. This allows a graph to repeat certain steps until a specific condition is met, enabling iterative behaviors like agentic reasoning, self-correction, or data collection.

## How Loops Work

Loops are implemented using **Conditional Edges** where one of the target nodes in the mapping is a node that has already been visited (or leads back to one).

## Implementation Pattern

1. **Routing Function**: Define a function that checks the state to decide whether to continue looping or exit.
2. **Back-Edge**: In the conditional edge mapping, map one of the decision keys back to an earlier node.

### Example

```python
def should_continue(state: MyState):
    if state["iterations"] < 3:
        return "repeat"
    return "end"

workflow.add_conditional_edges(
    "evaluator",
    should_continue,
    {
        "repeat": "agent_node", # Loop back to the agent
        "end": END              # Exit the graph
    }
)
```

## Key Considerations
- **Termination Condition**: Always ensure there is a clear exit path to avoid infinite loops.
- **State Updates**: Ensure the state is updated in a way that eventually triggers the exit condition (e.g., incrementing a counter, achieving a confidence score).
- **Recursion Limits**: Some graph executors may have limits on the number of steps to prevent runaway processes.

---
[Back to Wiki Index](../index.md)
