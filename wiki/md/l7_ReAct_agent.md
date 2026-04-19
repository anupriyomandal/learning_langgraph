# Lesson 7: ReAct Agent with LangGraph

This lesson introduces the **ReAct** (Reason + Act) pattern, which is one of the most powerful architectural patterns for building autonomous AI agents.

## Key Concepts

### 1. The ReAct Loop
ReAct stands for **Reason + Act**. The cycle works as follows:
- **Reason**: The LLM thinks about the task and generates a thought process.
- **Act**: The LLM decides to use a specific tool (function) to gather information.
- **Observe**: The tool's output is fed back into the LLM as a `ToolMessage`.
- **Iterate**: The cycle repeats until the LLM decides it has enough information to provide a final answer.

### 2. Message Reducers (`add_messages`)
In a multi-turn ReAct agent, maintaining the conversation history is crucial. We use `Annotated` and the `add_messages` reducer to automatically append new messages to the state rather than overwriting them.

```python
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
```

### 3. Binding Tools
We use `.bind_tools(tools)` to inform the LLM about the available functions. The LLM can then choose to return a "tool call" instead of a text response.

```python
model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)
```

### 4. The `ToolNode` and `tools_condition`
LangGraph provides prebuilt components for the "Act" part:
- **`ToolNode`**: A node that automatically executes the tools requested by the LLM.
- **`tools_condition`**: A router that checks if the LLM's last message contains tool calls.

## Workflow Visualization
The graph features a recurrent loop between the `model_node` and `tool_node`.

![Lesson 7 Graph](../../assignment_4_graph.png)

## Rich Streaming Output
To improve developer visibility into the ReAct process, we implemented a colored streaming output using the `Rich` library:
- [bold blue]Human Message[/bold blue]: User query.
- [bold yellow]AI Tool Call[/bold yellow]: The LLM's decision to use a tool.
- [bold cyan]Tool Output[/bold cyan]: The result of the function execution.
- [bold green]AI Response[/bold green]: The final answer provided to the user.

---
## Related Concepts
- [Nodes vs. Edges](concept_nodes_vs_edges.md)
- [State Management](stategraph_api.md)
- [Loops (Recurrent Graphs)](concept_loops.md)

---
[Back: Assignment 4: Interactive Chatbot](assignment_4.md) | [Next: Wiki Index](../index.md)
