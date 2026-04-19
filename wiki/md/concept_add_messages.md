# Concept: add_messages (The Message Reducer)

`add_messages` is a specialized **Reducer Function** provided by LangGraph to handle the state of message lists efficiently.

## Why do we need it?
By default, when a node returns a value for a state key (e.g., `{"messages": [new_msg]}`), LangGraph **overwrites** the existing value. For chat history, we want to **append** to the list instead of replacing it.

## How it works
When you define your state using `Annotated`, you can specify `add_messages` as the reducer:

```python
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
```

### Key Behaviors:
1.  **Appending**: New messages are appended to the existing list.
2.  **Updating**: If a new message has the same `id` as an existing message, it **replaces** the old one. This is useful for "editing" previous messages or handling complex state updates.
3.  **Deduplication**: It automatically handles message identity to prevent accidental duplicates in the history.

## Role in ReAct Agents
In a ReAct loop, the agent keeps generating new `AIMessages` and receiving `ToolMessages`. The `add_messages` reducer ensures the conversation history grows incrementally, allowing the LLM to remember its previous thoughts and observations.

---
## Related Concepts
- [Message Types](concept_messages.md)
- [State Management](stategraph_api.md)

---
[Back: Wiki Index](../index.md)
