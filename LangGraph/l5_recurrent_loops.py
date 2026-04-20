from langgraph.graph import StateGraph, END, START
from typing import TypedDict, Dict, List
import random


class AgentState(TypedDict):
    name: str
    numbers: List[int]
    count: int

def greeting(state: AgentState) -> AgentState:
    """Greets the user."""
    print("--- Greeting ---")
    state['name'] = f'Hi there, {state['name']}'
    state['count'] = 1
    return state

def random_number(state: AgentState) -> AgentState:
    """Generates a random number and adds it to the list."""
    print("--- Generating random number --- Loop: ", state['count'])
    state['numbers'].append(random.randint(1, 100))
    state['count'] += 1
    return state

def decide_next_node(state: AgentState) -> AgentState:
    """Decides the next node based on the count."""
    if state['count'] <= 5:
        return "add_number"
    else:
        return "end"

if __name__ == '__main__':
    # 1. Initialize the Graph
    workflow = StateGraph(AgentState)
    
    # 2. Add multiple Nodes
    workflow.add_node("greeting", greeting)
    workflow.add_node("add_number", random_number)
    workflow.add_node("decide_next_node", lambda state: state)
    
    
    # 3. Connect Nodes together (Sequential Flow)
    workflow.add_edge(START, "greeting")
    workflow.add_edge("greeting", "add_number")
    workflow.add_edge("add_number", "decide_next_node")
    # Add conditional edges to create a loop
    # If decide_next_node returns "add_number", it goes back to "add_number" node
    # If it returns "end", it terminates the graph
    workflow.add_conditional_edges(
        "decide_next_node",  # Source node
        decide_next_node,     # Routing function
        {
            "add_number": "add_number", # Result of routing function -> Target node
            "end": END                  # Result of routing function -> END
        }
    )
    
    # 4. Compile the Graph
    app = workflow.compile()
    
    # --- ADD THIS TO SHOW THE DIAGRAM ---
    print("\nGenerating Workflow Diagram...")
    try:
        # Generate PNG and save it
        png_data = app.get_graph().draw_mermaid_png()
        with open("l5_looping_graphs_graph.png", "wb") as f:
            f.write(png_data)
        print("Success: Diagram saved to 'l5_looping_graphs_graph.png'")
    except Exception as e:
        pass
        
    app.get_graph().print_ascii()
    # ------------------------------------
    
    # 5. Invoke the Graph and see the transformation
    print("\nInvoking graph...")
    state = AgentState(**{'name': 'Anupriyo', 'numbers': [], 'count': 0})
    result = app.invoke(state)
    
    print("\n--- Final State ---")
    print(result)