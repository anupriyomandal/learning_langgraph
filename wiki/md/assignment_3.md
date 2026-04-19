# Assignment 3: Automatic Higher or Lower Game

This assignment involves creating a self-correcting loop that plays a "Higher or Lower" guessing game autonomously.

## The Challenge
Build a graph that:
1. Picks a random number between 1 and 20.
2. Makes a guess.
3. Receives a hint ("higher" or "lower").
4. Adjusts its bounds and guesses again.
5. Continues until the number is found or 7 attempts are reached.

## Key Implementation Details

### 1. Game State
The state tracks the bounds and the target, allowing the graph to "remember" the range it is searching in.
```python
class AgentState(TypedDict):
    player_name: str
    target: int
    guess: int
    lower_bound: int
    upper_bound: int
    correct: bool
```

### 2. Binary Search Logic
To solve the game efficiently, the `make_guess` node implements a binary search strategy by always guessing the midpoint of the current bounds.
```python
guess = (state['lower_bound'] + state['upper_bound']) // 2
```

### 3. State-Driven Routing
The `hint` node updates the `lower_bound` or `upper_bound` based on the comparison, and the `should_continue` router decides whether to loop back to the `guess` node.

## Workflow Visualization

The graph cycles between guessing and hinting until a termination condition is met.

![Assignment 3 Graph](../../assignment_3_graph.png)

## Lessons Learned
- **Dynamic State**: How to use state keys to refine logic over multiple iterations.
- **Loop Termination**: Implementing multiple exit conditions (Win vs. Max Attempts).
- **Strategy Implementation**: Encoding a search algorithm (Binary Search) within graph nodes.

---
## Related Concepts
- [Loops (Recurrent Graphs)](concept_loops.md)
- [Conditional Edges](concept_conditional_edges.md)

---
[Back: Lesson 5: Looping Graphs](l5_looping_graphs.md) | [Next: Wiki Index](../index.md)
