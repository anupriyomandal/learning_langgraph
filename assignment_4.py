import os
import random
from typing import TypedDict, List, Dict, Any
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from langgraph.graph import StateGraph, START, END

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
console = Console()

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

def gpt_reponse(state: AgentState) -> AgentState:
    """Generates a response using OpenAI, maintaining history."""
    # Prepare messages including history
    messages = state.get('messages', [])
    messages.append({"role": "user", "content": state['query']})
    
    # Call LLM
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    answer = resp.choices[0].message.content
    state['response'] = answer
    
    # Update history in state
    messages.append({"role": "assistant", "content": answer})
    state['messages'] = messages
    return state

def display_response(state: AgentState) -> AgentState:
    """Renders the response in the terminal."""
    console.print("\n[bold green]Assistant:[/bold green]")
    md = Markdown(state['response'])
    console.print(md)
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
