import os
import random
from typing import TypedDict, List, Dict, Any
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.theme import Theme
from langgraph.graph import StateGraph, START, END

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Custom theme for Markdown rendering
custom_theme = Theme({
    "markdown.strong": "bold cyan",
    "markdown.h1": "bold magenta",
    "markdown.h2": "bold blue"
})
console = Console(theme=custom_theme)

class AgentState(TypedDict):
    query: str
    response: str
    messages: List[Dict[str, Any]]

def get_query(state: AgentState) -> AgentState:
    """Prompts the user for input."""
    console.print("\n[bold cyan]User:[/bold cyan] ", end="")
    user_input = input()
    state['query'] = user_input
    return state

from rich.live import Live

def gpt_reponse(state: AgentState) -> AgentState:
    """Generates a streaming response using OpenAI and renders it as Markdown in real-time."""
    messages = state.get('messages', [])
    messages.append({"role": "user", "content": state['query']})
    
    console.print("\n[bold green]Assistant:[/bold green]")
    
    full_response = ""
    # Use Rich Live to render markdown as it streams
    with Live(Markdown(full_response), console=console, refresh_per_second=10) as live:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                live.update(Markdown(full_response))
    
    state['response'] = full_response
    messages.append({"role": "assistant", "content": full_response})
    state['messages'] = messages
    return state

def display_response(state: AgentState) -> AgentState:
    """Renders the final response (redundant now but kept for state sync)."""
    # We already printed during streaming, so this node just ensures state consistency
    return state

def router(state: AgentState) -> str:
    """Decides whether to continue or exit."""
    if state['query'].lower() in ["exit", "quit", "bye"]:
        return "exit"
    return "continue"

# --- Graph Definition ---
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("get_query", get_query)
workflow.add_node("gpt_reponse", gpt_reponse)
workflow.add_node("display_response", display_response)

# Add Edges
workflow.add_edge(START, "get_query")

# Routing after user input
workflow.add_conditional_edges(
    "get_query",
    router,
    {
        "continue": "gpt_reponse",
        "exit": END
    }
)

# After response, show it and go back for more input
workflow.add_edge("gpt_reponse", "display_response")
workflow.add_edge("display_response", "get_query")

# Compile
app = workflow.compile()

if __name__ == "__main__":
    console.print("[bold reverse] Interactive LangGraph Chatbot [/bold reverse]")
    console.print("Type 'exit' to quit.\n")
    
    # Initialize state
    initial_state = {
        "query": "",
        "response": "",
        "messages": []
    }
    
    # Run the interactive loop
    # Note: app.invoke will run until it hits END. 
    # Since we loop back to get_query, it stays alive as long as router says "continue".
    app.invoke(initial_state)
