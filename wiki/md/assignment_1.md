# Assignment 1: Multi-Operation Single Node Graph

This assignment involved creating a graph that can handle different operations based on the input state, all within a single node.

## The Task
Create a graph where you pass in:
- A list of integers (`values`)
- A name (`name`)
- An operation (`operation`) either `+` or `*`

The node must perform the calculation and return a formatted greeting with the answer.

## Key Implementation Details

### 1. Handling Logic within a Node
Using conditional logic (if/else) inside a node function allows the graph to be flexible without needing multiple nodes or conditional edges (which will be covered in later lessons).

```python
def calculator_node(state: AgentState) -> AgentState:
    if state['operation'] == "+":
        answer = sum(state['values'])
    elif state['operation'] == "*":
        answer = math.prod(state['values'])
    # ...
```

### 2. State Mapping
The input dictionary provided to `app.invoke()` must match the keys defined in the `AgentState` TypedDict.

```python
user_input = {
    "name": "Jack Sparrow",
    "values": [1, 2, 3, 4],
    "operation": "*"
}
```

## Cross-References
- [Lesson 2: Multiple Inputs and List Types](l2_single_node_2.md) - Similar use of lists and multiple state keys.

---
[Home](../index.md) | [Back to Lesson 2](l2_single_node_2.md)
