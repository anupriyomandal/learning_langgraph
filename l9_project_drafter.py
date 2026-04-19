from typing import TypedDict, Sequence, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, SystemMessage, ToolMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.rule import Rule

load_dotenv()
console = Console()

# Declaring a global variable which stores the document
document_content = ''

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


# ─── TOOLS ─────────────────────────────────────────────────────────────────────

@tool
def update(content: str) -> str:
    """Updates the content of the document with the provided content"""
    global document_content
    document_content = content
    return 'Document updated successfully.'

@tool
def save(filename: str) -> str:
    """Saves the content of the document to a text file."""
    if not filename.endswith('.txt'):
        filename = filename + '.txt'
    global document_content
    with open(filename, 'w') as f:
        f.write(document_content)
    return f"Saved to {filename}"


model = ChatOpenAI(model="gpt-4o-mini").bind_tools([update, save])


# ─── UI ────────────────────────────────────────────────────────────────────────

def render_ui(messages: list):
    """Render the UI once — shows draft preview."""
    console.clear()
    console.print(Rule("[bold magenta]✨ PROJECT DRAFTER ✨[/bold magenta]", style="blue"))

    # Draft preview or greeting
    if document_content:
        console.print(Panel(
            Markdown(document_content),
            title="[bold yellow]📄 Draft[/bold yellow]",
            border_style="yellow",
            padding=(0, 1),
        ))
    else:
        console.print("\n  [bold green]I'm a helpful agent that helps you draft insightful documents.[/bold green]\n")

    # Show AI's last response if available
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and msg.content:
            console.print(f"  [bold green]AI →[/bold green] {msg.content}")
            break

    console.print()  # breathing room before prompt


# ─── GRAPH NODES ───────────────────────────────────────────────────────────────
# The graph only handles: model reasoning → tool execution → loop back
# Human input is handled OUTSIDE the graph in the main loop.

def model_node(state: AgentState) -> AgentState:
    """AI reasoning node."""
    system_prompt = SystemMessage(
        content=(
            "You are a professional document drafter. "
            "Use the 'update' tool to write/rewrite the draft. "
            "Use the 'save' tool when the user is satisfied and wants to finish."
        )
    )
    all_messages = [system_prompt] + list(state['messages'])
    response = model.invoke(all_messages)
    return {'messages': [response]}

def should_continue(state: AgentState) -> str:
    """After tools: end if saved, otherwise loop back to model."""
    for message in reversed(state['messages']):
        if isinstance(message, ToolMessage) and 'saved' in message.content.lower():
            return 'end'
    return 'continue'

def router(state: AgentState) -> str:
    """After model: use tools or return to human."""
    last = state["messages"][-1]
    if last.tool_calls:
        return "tool_node"
    return END


# ─── GRAPH ─────────────────────────────────────────────────────────────────────

workflow = StateGraph(AgentState)
workflow.add_node("model_node", model_node)
workflow.add_node("tool_node", ToolNode(tools=[update, save]))

workflow.add_edge(START, "model_node")
workflow.add_conditional_edges("model_node", router, {"tool_node": "tool_node", END: END})
workflow.add_conditional_edges("tool_node", should_continue, {"continue": "model_node", "end": END})

app = workflow.compile()


# ─── MAIN LOOP ─────────────────────────────────────────────────────────────────
# Simple, explicit human-in-the-loop:
#   1. Render the UI
#   2. Get user input
#   3. app.invoke() — runs the full AI cycle atomically
#   4. Check if done, otherwise repeat

def run():
    messages = []

    while True:
        # 1. Render UI with current state
        render_ui(messages)

        # 2. Get user input
        try:
            user_input = console.input("[bold white on magenta] ▶ [/bold white on magenta] [bold cyan]What next?[/bold cyan] ")
        except (EOFError, KeyboardInterrupt):
            break

        # Add user message to history
        messages.append(HumanMessage(content=user_input))

        # 3. Run the graph — model reasons, uses tools, loops internally
        with console.status("[bold green]Thinking…[/bold green]"):
            result = app.invoke({"messages": messages})

        # 4. Update our message history with everything the graph produced
        messages = list(result["messages"])

        # 5. Check if the save tool was used — if so, we're done
        saved = any(
            isinstance(m, ToolMessage) and 'saved' in m.content.lower()
            for m in messages
        )
        if saved:
            render_ui(messages)
            console.print(Panel(
                "[bold green]✅ Done! Your document has been saved.[/bold green]",
                border_style="green",
                expand=False,
            ))
            break


if __name__ == '__main__':
    run()
