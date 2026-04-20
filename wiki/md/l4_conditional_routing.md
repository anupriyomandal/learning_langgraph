# Lesson 4: Conditional Edges and Routing

In this lesson, we introduce **Conditional Edges**, which allow the graph to branch and make decisions dynamically based on the state.

## Key Concepts

### 1. `add_conditional_edges`
This method is used to define branching logic. It requires three arguments:
- **Source Node**: The node from which the branch originates.
- **Routing Function**: A function that analyzes the state and returns a decision key.
- **Mapping**: A dictionary mapping decision keys to target nodes.

### 2. Routing Logic
The routing function is a regular Python function. In this example, `decide_next_node` checks the `operation` field in the state to decide whether to add, subtract, or multiply.

```python
def decide_next_node(state: AgentState) -> str:
    if state['operation'] == "add":
        return "addition_operation"
    elif state['operation'] == "subtract":
        return "subtraction_operation"
    else:
        return "multiplication_operation"
```

## Code Highlight

```python
# Define the routing logic
workflow.add_conditional_edges(
    "router",
    decide_next_node,
    {
        "addition_operation": "add_node",
        "subtraction_operation": "subtract_node",
        "multiplication_operation": "multiply_node"
    }
)
```

## Workflow Visualization

The graph structure looks like this:
- **START** -> **router**
- **router** -> **add_node** (if operation is 'add')
- **router** -> **subtract_node** (if operation is 'subtract')
- **router** -> **multiply_node** (if operation is 'multiply')
- All operation nodes -> **END**

## Common Pitfalls
- **Missing Keys**: If the routing function returns a key that isn't in the mapping dictionary, LangGraph will raise an error.
- **Return Type**: The routing function should return a string that matches one of the keys in the mapping.

---
## Related Concepts
- [Conditional Edges](concept_conditional_edges.md)
- [State Management](concept_state.md)

---
[Back: Lesson 3: Sequential Nodes](l3_sequential_flow.md) | [Next: Assignment 2: Multi-Stage Routing](a2_chained_routers.md)
