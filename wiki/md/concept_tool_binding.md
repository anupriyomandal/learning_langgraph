# Concept: Tool Binding

Tool binding is the process of informing a Large Language Model (LLM) about the existence and schema of external functions it can "call". In LangGraph, this is typically done using the LangChain `.bind_tools()` method.

## How it Works
When you bind tools to a model, the tool's docstring and arguments are converted into a JSON schema (e.g., OpenAI Tool Calling schema) and sent to the LLM as part of the system/user prompt.

### Basic Example
```python
@tool
def get_weather(city: str):
    """Get the current weather for a specific city."""
    return f"The weather in {city} is sunny."

# Bind the tool to the model
model = ChatOpenAI(model="gpt-4o").bind_tools([get_weather])
```

## Why Bind Tools?
1. **Schema Generation**: Automatically generates the complex JSON structure needed by LLM APIs.
2. **Autonomous Routing**: The model can decide *when* to call a tool based on the user's intent.
3. **Structured Output**: Ensures the model provides arguments in the correct types (int, str, etc.).

## Common Pitfalls
- **Missing Docstrings**: The LLM uses the docstring to understand *why* it should use the tool. Without it, the model may never call it.
- **Vague Argument Names**: Use descriptive names like `target_temperature` instead of `val`.
- **Too Many Tools**: Binding dozens of tools can confuse the model and increase token costs.

---
[Related: ReAct Framework](concept_react_agent.md) | [Related: ToolNode](concept_tool_node.md)
