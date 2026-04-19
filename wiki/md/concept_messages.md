# Concept: LangGraph Message Types

LangGraph (via LangChain) uses a specific hierarchy of message objects to communicate between nodes and the LLM. Understanding these types is essential for building structured agentic workflows.

## 1. BaseMessage
The abstract base class for all message types. It contains the core attributes shared by all messages:
- `content`: The string or list of content in the message.
- `additional_kwargs`: Metadata and extra information (like tool call details).
- `id`: A unique identifier for the message.

## 2. SystemMessage
A message used to provide high-level instructions or "persona" to the LLM. It is typically sent at the beginning of a conversation to set the rules and boundaries.
- **Usage**: Defining the assistant's role, restricted tools, or output format.

## 3. HumanMessage
Represents input from a human user. This is what triggers the initial response from the graph.

## 4. AIMessage
Represents a response from the LLM. It can contain:
- **Plain Text**: The final answer to the user.
- **Tool Calls**: Requests to execute specific functions (tools).

## 5. ToolMessage
A specific message type used to pass the results of a tool execution back to the LLM.
- **Requirement**: Must include a `tool_call_id` that matches the ID in the preceding `AIMessage`'s tool call.
- **Purpose**: Allows the LLM to "observe" the result of its action and continue reasoning.

---
## Related Concepts
- [add_messages Reducer](concept_add_messages.md)
- [ReAct Agent](l7_ReAct_agent.md)

---
[Back: Wiki Index](../index.md)
