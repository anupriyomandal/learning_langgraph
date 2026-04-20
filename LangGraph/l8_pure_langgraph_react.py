import os
import json
from typing import TypedDict, List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from langgraph.graph import StateGraph, START, END

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
console = Console()

# --- 1. Define Tools ---
# In pure OpenAI, tools are defined as JSON schemas
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Adds two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiplies two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    }
]

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

available_tools = {
    "add": add,
    "multiply": multiply
}

# --- 2. Define State ---
class AgentState(TypedDict):
    messages: List[Dict[str, Any]]

# --- 3. Define Nodes ---

def call_model(state: AgentState) -> AgentState:
    """Calls the OpenAI model directly without LangChain."""
    console.print("\n[bold yellow]--- Calling Model ---[/bold yellow]")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=state['messages'],
        tools=tools_schema,
        tool_choice="auto"
    )
    
    message = response.choices[0].message
    # Convert message object to dict for state
    msg_dict = message.model_dump()
    # Ensure tool_calls are serializable if they exist
    state['messages'].append(msg_dict)
    
    if message.content:
        console.print(Panel(message.content, title="AI Response", border_style="green"))
    
    return state

def call_tools(state: AgentState) -> AgentState:
    """Executes tools manually based on model response."""
    console.print("[bold cyan]--- Calling Tools ---[/bold cyan]")
    
    last_message = state['messages'][-1]
    tool_calls = last_message.get("tool_calls", [])
    
    for tool_call in tool_calls:
        function_name = tool_call['function']['name']
        function_args = json.loads(tool_call['function']['arguments'])
        
        console.print(f"Executing: [bold]{function_name}[/bold] with {function_args}")
        
        # Execute the actual python function
        function_to_call = available_tools[function_name]
        result = function_to_call(**function_args)
        
        # Add the result to messages in the required format
        state['messages'].append({
            "tool_call_id": tool_call['id'],
            "role": "tool",
            "name": function_name,
            "content": str(result)
        })
        
        console.print(f"Result: [bold green]{result}[/bold green]")
        
    return state

def should_continue(state: AgentState) -> str:
    """Routes based on whether tool calls exist."""
    last_message = state['messages'][-1]
    if last_message.get("tool_calls"):
        return "continue"
    return "end"

# --- 4. Build Graph ---
workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)
workflow.add_node("tools", call_tools)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "end": END
    }
)
workflow.add_edge("tools", "agent")

app = workflow.compile()

# --- 5. Run ---
if __name__ == "__main__":
    initial_messages = [
        {"role": "system", "content": "You are a helpful assistant. Use tools for math."},
        {"role": "user", "content": "Add 10 and 5, then multiply the result by 2."}
    ]
    
    console.print(Panel("Goal: Add 10 and 5, then multiply the result by 2.", title="Task", border_style="blue"))
    
    app.invoke({"messages": initial_messages})
