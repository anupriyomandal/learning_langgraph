# Concept: Human-in-the-Loop (HITL)

Human-in-the-Loop (HITL) refers to patterns where an autonomous graph pauses to wait for human input, approval, or feedback before continuing.

## Patterns of Interaction

### 1. Internal Human Node (Pausing the Graph)
In this pattern, you define a `human_node` inside the graph. When the graph reaches this node, it stops execution and waits for a manual trigger (or uses a tool like `input()` in CLI apps).

**Pros**: Everything stays within the graph structure.
**Cons**: Can be tricky to manage with complex UI frameworks or web backends.

### 2. External Human Loop (Atomic Invocation)
In this pattern, the graph only handles the "Brain" and "Action" cycles. The human interaction is managed by a `while` loop *outside* the graph.

```python
# The loop lives outside the graph
while True:
    user_input = input("...")
    # Graph is called for a single "turn"
    result = app.invoke({"messages": [HumanMessage(content=user_input)]})
    print(result['messages'][-1].content)
```

**Pros**: Much easier for building interactive CLI dashboards or web apps. Zero flicker/repetition.
**Cons**: Graph state must be carefully maintained manually if not using checkpointers.

## Advanced HITL: Breakpoints
LangGraph supports native breakpoints where you can:
- **Interrupt before a node**: Stop to review the state before the LLM takes an action.
- **Interrupt after a node**: Stop to review the result before moving to the next stage.
- **Modify State**: A human can "edit" the graph's memory before it resumes.

---
[Related: Lesson 9: Project Drafter](l9_project_drafter.md) | [Related: State Management](concept_state.md)
