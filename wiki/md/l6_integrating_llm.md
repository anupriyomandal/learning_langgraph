# Lesson 6: Integrating LLMs and Rich Rendering

This lesson demonstrates how to integrate Large Language Models (LLMs) like OpenAI's GPT into a LangGraph workflow and how to use external libraries like `Rich` to enhance terminal output.

## Key Concepts

### 1. LLM as a Node
In LangGraph, an LLM call is just another node in the graph. It takes the current state (containing a query), makes an API call, and updates the state with the response.

```python
def gpt_reponse(state: AgentState) -> AgentState:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": state['query']}]
    )
    state['response'] = resp.choices[0].message.content
    return state
```

### 2. Output Formatting Nodes
Separating the "Logic" (getting the response) from the "Presentation" (rendering it) is a best practice. We created a `markdown_viewer` node specifically for rendering.

### 3. Using the Rich Library
The `rich` library allows for beautiful, formatted output in the terminal, including tables, progress bars, and full Markdown support.

```python
from rich.console import Console
from rich.markdown import Markdown

def markdown_viewer(state: AgentState) -> AgentState:
    md = Markdown(state['response'])
    Console().print(md)
    return state
```

## Workflow Structure
The graph flows sequentially from query initialization to LLM processing, and finally to beautiful rendering.

![Lesson 6 Graph](../../assignment_3_graph.png) 
*(Note: Re-using visualization pattern from previous lessons)*

## Lessons Learned
- **Environmental Variables**: Using `.env` files to manage secrets like `OPENAI_API_KEY`.
- **Node Modularity**: Keeping the LLM call separate from the display logic makes the graph easier to test and modify.
- **Terminal Aesthetics**: Improving the developer experience (DX) with proper formatting.

---
## Related Concepts
- [Nodes vs. Edges](concept_nodes_vs_edges.md)
- [State Management](stategraph_api.md)

---
[Back: Assignment 3: Automatic Higher or Lower Game](assignment_3.md) | [Next: Wiki Index](../index.md)
