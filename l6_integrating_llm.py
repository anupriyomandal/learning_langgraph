from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
console = Console()

class AgentState(TypedDict):
    query: str
    response: str

def gpt_reponse(state: AgentState) -> AgentState:
    """Calls OpenAI to get a response."""
    print("--- Calling OpenAI ---")
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": state['query']}
        ]
    )
    state['response'] = resp.choices[0].message.content
    return state

def markdown_viewer(state: AgentState) -> AgentState:
    """Renders the LLM response in proper markdown in the terminal."""
    print("\n--- LLM Response (Markdown) ---")
    md = Markdown(state['response'])
    console.print(md)
    return state

# 1. Initialize Graph
workflow = StateGraph(AgentState)

# 2. Add Nodes
workflow.add_node("gpt_reponse", gpt_reponse)
workflow.add_node("markdown_viewer", markdown_viewer)

# 3. Connect Nodes
workflow.add_edge(START, "gpt_reponse")
workflow.add_edge("gpt_reponse", "markdown_viewer")
workflow.add_edge("markdown_viewer", END)

# 4. Compile
app = workflow.compile()

# --- Visualization ---
print("Workflow Structure:")
app.get_graph().print_ascii()

# 5. Run
state = AgentState(query="Tell me about LangGraph using markdown formatting (headers, lists, bold text).", response="")
result = app.invoke(state)