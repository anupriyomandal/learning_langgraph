from langgraph.graph import StateGraph, END, START
from typing import TypedDict

class AgentState(TypedDict):
    number1: int
    number2: int
    operation: str
    result: int

def add(state: AgentState) -> AgentState:
    print("--- Adding numbers ---")
    state['result'] = state['number1'] + state['number2']
    return state

def multiply(state: AgentState) -> AgentState:
    print("--- Multiplying numbers ---")
    state['result'] = state['number1'] * state['number2']
    return state

def subtract(state: AgentState) -> AgentState:
    print("--- Subtracting numbers ---")
    state['result'] = state['number1'] - state['number2']
    return state

def decide_next_node(state: AgentState) -> AgentState:
    if state['operation'] == "add":
        return "addition_node"
    elif state['operation'] == "multiply":
        return "multiplication_node"
    else:
        return "subtraction_node"   

if __name__ == '__main__':
    # 1. Initialize the Graph
    workflow = StateGraph(AgentState)
    
    # 2. Add multiple Nodes
    workflow.add_node("add_node", add)
    workflow.add_node("multiply_node", multiply)
    workflow.add_node("subtract_node", subtract)
    workflow.add_node("router", lambda state: state) # pass state

    # 1. Start -> Decide
    workflow.add_edge(START, "router")
    
    # 2. Conditional edges
    workflow.add_conditional_edges(
        "router",
        decide_next_node,
        {
            "addition_node": "add_node",
            "multiplication_node": "multiply_node",
            "subtraction_node": "subtract_node"
        }
    )

    workflow.add_node('add_node2', add)
    workflow.add_node('multiply_node2', multiply)
    workflow.add_node('subtract_node2', subtract)
    workflow.add_node('router2', lambda state: state)  
    
    workflow.add_conditional_edges(
        "router2",
        decide_next_node,
        {
            "addition_node": "add_node2",
            "multiplication_node": "multiply_node2",
            "subtraction_node": "subtract_node2"
        }
    )  
    
    # 3. Connect Nodes together (Sequential Flow)
    workflow.add_edge("add_node", "router2")
    workflow.add_edge("multiply_node", "router2")
    workflow.add_edge("subtract_node", "router2")
    
    workflow.add_edge("add_node2", END)
    workflow.add_edge("multiply_node2", END)
    workflow.add_edge("subtract_node2", END)


    
    # 5. Compile the Graph
    app = workflow.compile()
    
    # --- ADD THIS TO SHOW THE DIAGRAM ---
    print("\nGenerating Workflow Diagram...")
    try:
        # Generate PNG and save it
        png_data = app.get_graph().draw_mermaid_png()
        with open("assignment_2_graph.png", "wb") as f:
            f.write(png_data)
        print("Success: Diagram saved to 'assignment_2_graph.png'")
    except Exception as e:
        pass
        
    app.get_graph().print_ascii()
    # ------------------------------------
    
    # 6. Invoke the Graph and see the transformation
    print("\nInvoking graph...")
    state = AgentState(**{'number1': 10, 'number2': 5, 'operation': 'add', 'result': 0})
    result = app.invoke(state)
    
    print("\n--- Final State ---")
    print(result)
    
    print("\n--- Result Output ---")
    print(result['result'])

    # 7. Let's test another operation
    print("\nInvoking graph...")
    state['operation'] = 'multiply'
    result = app.invoke(state)
    
    print("\n--- Final State ---")
    print(result)
    
    print("\n--- Result Output ---")
    print(result['result'])
