"""
## ReAct Agent with LangGraph

ReAct stands for Reason + Act.
It is a framework that allows LLMs to reason about a task and decide which actions to take.

Key Concepts:
- **Reason**: The LLM generates a thought process to solve the problem.
- **Act**: The LLM decides to use a tool (function) to gather information.
- **Observe**: The output of the tool is fed back into the LLM, and the cycle repeats until the task is complete.

Objectives:
1. Learn how to create Tools in langgraph
2. How to create a ReAct Graph
3. Work with different types of Messages such as Tool Messages
4. Test Out Robustness of our Graph

"""

from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage # The foundational class for all message types in LangGraph
from langchain_core.messages import SystemMessage # Message for providing instructions to the LLM
from langchain_core.messages import ToolMessage # Passes data back to the LLM after it calls the tool
from langchain_openai import ChatOpenAI # To create a chat model
from langchain_core.tools import tool # decorator to create tools 
from langgraph.graph.message import add_messages # Helper function to add messages to the state 
from langgraph.graph import StateGraph, START, END # To build our graph and define the start and end points
from langgraph.prebuilt import ToolNode, tools_condition # to create a tool node and condition to check if tool is called


load_dotenv()

# Annotated - provides additional context without affecting the type itself.
# Sequence - To automatically handle the state updates for sequences such as by adding new messages to chat history.

# email = Annotated[str, "This has to be a valid email address"]

# add_messages is a Reducer Function
# Reducer Function
# Rule that contains how updates from the node are combined with the existing state.
# Tells us how to merge new data into the current state
# Without a Reducer, updates would've replaced the existing values entirely !

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    

@tool
def add(a: int, b: int) -> int:
    """This is an addion function that adds two numbers and returns the sum."""
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """This is a subtraction function that subtracts two numbers and returns the difference."""
    return a - b

@tool
def divide(a: int, b: int) -> int:
    """This is a division function that divides two numbers and returns the quotient."""
    return a / b

@tool
def multiply(a: int, b: int) -> int:
    """This is a multiplication function that multiplies two numbers and returns the product."""
    return a * b

tools = [add, subtract, divide, multiply]

model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)

def model_call(state : AgentState) -> AgentState:
    system_prompt = SystemMessage(content = "You are an AI assistant, please answer my question to the best of your ability, always use the tools.")
    response = model.invoke([system_prompt] + state['messages'])
    return {"messages" : [response]}

def should_continue(state : AgentState) -> str:
    response = state['messages'][-1]
    if not response.tool_calls:
        return "end"
    else:
        return "continue"

workflow = StateGraph(AgentState)

workflow.add_node("model_node", model_call)
workflow.add_node("tool_node", ToolNode(tools = tools))

workflow.add_edge(START, "model_node")
workflow.add_conditional_edges(
    "model_node",
    should_continue,
    {
        "continue": "tool_node",
        "end": END
    }
)
workflow.add_edge("tool_node", "model_node")

app = workflow.compile()

from rich.console import Console
from rich.panel import Panel
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

console = Console()

def print_stream(stream):
    for s in stream:
        message = s['messages'][-1]
        
        if isinstance(message, tuple):
            # Handle tuple format (e.g., ('user', 'query'))
            role, content = message
            console.print(Panel(content, title=f"[bold blue]Human Message ({role})[/bold blue]", border_style="blue"))
        
        elif isinstance(message, HumanMessage):
            console.print(Panel(message.content, title="[bold blue]Human Message[/bold blue]", border_style="blue"))
            
        elif isinstance(message, AIMessage):
            if message.tool_calls:
                # If AI is calling a tool
                for tool_call in message.tool_calls:
                    content = f"Function: [bold yellow]{tool_call['name']}[/bold yellow]\nArguments: {tool_call['args']}"
                    console.print(Panel(content, title="[bold yellow]AI Tool Call[/bold yellow]", border_style="yellow"))
            if message.content:
                # If AI is providing a final response
                console.print(Panel(message.content, title="[bold green]AI Response[/bold green]", border_style="green"))
                
        elif isinstance(message, ToolMessage):
            console.print(Panel(f"Output: {message.content}", title="[bold cyan]Tool Output[/bold cyan]", border_style="cyan"))

print_stream(app.stream(
    {
        "messages": [('user', 'Add 40 + 12 and multiply the sum by 3. Also tell me a joke please')]
    }, 
    stream_mode="values"
))