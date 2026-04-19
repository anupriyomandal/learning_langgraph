# Lesson 9: Autonomous Project Drafter with Human-in-the-Loop

This lesson combines all previously learned concepts—State Management, Tool Integration, LLM Routing, and Rich Rendering—into a cohesive, autonomous document-drafting application. It introduces the pattern of **External Human Loops** using `app.invoke()`.

## Core Objectives
- Implement a robust autonomous agent that uses tools to build a document iteratively.
- Design a high-fidelity CLI dashboard using the **Rich** library's `Layout` system.
- Solve UI sequencing issues by managing the human input loop outside the LangGraph execution.
- Use `app.invoke()` to execute atomic AI reasoning cycles (Reason -> Act -> Reason).

## Key Components

### 1. External Human Loop
Instead of placing a `human_node` inside the graph (which can complicate UI refreshes and state streaming), we handle user input in a standard Python `while` loop. The graph is called atomically using `app.invoke()`.

```python
while True:
    render_ui(messages)
    user_input = console.input("...")
    messages.append(HumanMessage(content=user_input))
    
    # The graph runs internally: Model -> Tools -> Model
    result = app.invoke({"messages": messages})
    messages = list(result["messages"])
```

### 2. State-Driven UI with Rich
The UI uses `rich.layout.Layout` to split the terminal into a header and a draft preview. This ensures that the draft remains persistent and visible while the AI "thinks" or uses tools.

### 3. Tool-Based Drafting
The agent is equipped with two tools:
- `update(content)`: Modifies the global `document_content`.
- `save(filename)`: Writes the draft to a physical `.txt` file and signals the loop to terminate.

## Graph Architecture
The graph follows a classic **ReAct** pattern but exits to the user when it requires new instructions:
`START` -> `model_node` -> `router` -> `tool_node` -> `should_continue` -> `model_node` or `END`.

## Lessons Learned
- **UI Sequencing**: Managing the screen clear/refresh cycle is critical for a "Premium" feel. Redundant refreshes cause terminal flicker.
- **Atomic Invocation**: Using `app.invoke()` is often cleaner than `app.stream()` for CLI apps where you only want to update the screen after a full "turn" is complete.
- **Global vs. State**: While LangGraph manages message state, global variables (like `document_content`) can still be useful for data that doesn't need to be in the LLM's context window but needs to be displayed to the user.

---
## Building On
This project is built upon:
- **[Lesson 7: ReAct Agent](l7_ReAct_agent.md)**: The underlying reasoning pattern.
- **[Lesson 6: Rich Integration](l6_integrating_llm.md)**: Enhancing terminal output.
- **[Assignment 4: Chatbot](assignment_4.md)**: Persistent CLI interaction.

## Related Concepts
- [State Management](concept_state.md)
- [ReAct Framework](concept_react_agent.md)
- [add_messages (Reducer)](concept_add_messages.md)

---
[Back: Lesson 8: Pure LangGraph ReAct](l8_pure_langgraph_react.md) | [Next: Wiki Index](../index.md)
