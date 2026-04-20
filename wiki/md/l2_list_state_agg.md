# Lesson 2: Multiple Inputs and List Types

In this lesson, we explored using complex types like `List` within the `AgentState` and handling multiple input values in a single node.

## Key Concepts

### 1. Complex State Types
The `AgentState` can use standard Python types like `List`, `Dict`, etc., from the `typing` module.

```python
from typing import List

class AgentState(TypedDict):
    numbers : List[int]
    name : str
    result : str
```

### 2. Processing Multiple Inputs
A single node can access multiple keys from the state to perform more complex logic, such as aggregations.

```python
def process_values(state: AgentState) -> AgentState:
    # Accessing both 'name' and 'numbers' from state
    state['result'] = f"Hi {state['name']}! Your sum is {sum(state['numbers'])}"
    return state
```

### 3. Invocation with Multiple Initial Values
When invoking the app, we pass a dictionary containing all the necessary initial data.

```python
result = app.invoke({'numbers': [1, 2, 3], 'name': 'Anupriyo'})
```

## Cross-References
- [Lesson 1.1: Multiple State Keys](l1_1_multi_key_state.md) - Introduction to using more than one key in `AgentState`.
- [State Definition](l1_basic_node.md#1-state-definition) - Basics of `TypedDict` in LangGraph.

---
[Home](../index.md) | [Back to Lesson 1.1](l1_1_multi_key_state.md) | [Next Lesson: (TBD)](#)
