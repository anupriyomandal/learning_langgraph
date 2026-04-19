# Lesson 8: Pure LangGraph ReAct Agent (No LangChain)

While LangGraph is built by the LangChain team and integrates seamlessly with LangChain primitives, it is **not strictly dependent** on them. This lesson demonstrates how to build a ReAct agent using only LangGraph and the raw OpenAI client.

## Why use Pure LangGraph?
- **Reduced Dependencies**: Avoid importing the entire LangChain ecosystem if you only need the graph orchestration.
- **Custom Logic**: More control over how tool calling and message history are handled.
- **Interoperability**: Easier to integrate with other libraries or raw API clients.

## Key Implementation Differences

### 1. State Definition
Instead of `Annotated[Sequence[BaseMessage], add_messages]`, we use a standard list of dictionaries, which is the format expected by the raw OpenAI API.

```python
class AgentState(TypedDict):
    messages: List[Dict[str, Any]]
```

### 2. Manual Tool Management
In Lesson 7, we used `ToolNode`. Here, we manually parse `tool_calls` from the OpenAI response and execute the corresponding Python functions.

```python
def call_tools(state):
    tool_calls = state['messages'][-1].get("tool_calls", [])
    for tool_call in tool_calls:
        # ... parse and execute ...
        state['messages'].append({
            "tool_call_id": tool_call['id'],
            "role": "tool",
            "name": name,
            "content": result
        })
    return state
```

### 3. Model Binding
Instead of `.bind_tools()`, we pass the tool JSON schema directly into the `client.chat.completions.create` call.

## Workflow Visualization
The logic remains identical to the ReAct pattern:
`START` -> `Agent (LLM)` -> `Router` -> `Tools` -> `Agent`.

![Lesson 8 Graph](../../assignment_4_graph.png)

## Lessons Learned
- LangGraph is a **generic orchestration engine**.
- You can bring your own data types and LLM clients.
- The tradeoff for "Pure" implementation is more boilerplate code for tool parsing and state merging.

---
## Building On
This lesson is a direct extension of:
- **[Lesson 7: ReAct Agent](l7_ReAct_agent.md)**: The core Reason + Act pattern.
- **[Lesson 6: LLM Integration](l6_integrating_llm.md)**: Understanding how LLMs drive graph logic.

## Related Concepts
- [ReAct Framework](concept_react_agent.md)
- [Message Types](concept_messages.md)

---
[Back: Lesson 7: ReAct Agent](l7_ReAct_agent.md) | [Next: Wiki Index](../index.md)
