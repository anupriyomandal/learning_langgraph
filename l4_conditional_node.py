from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    number1: int
    number2: int
    operation: str
    result: int

def adder(state: AgentState) -> AgentState:
    """Adds the two numbers"""
    print("--- Adding numbers ---")
    state['result'] = state['number1'] + state['number2']
    return state

def multiplier(state: AgentState) -> AgentState:
    """Multiplies the two numbers"""
    print("--- Multiplying numbers ---")
    state['result'] = state['number1'] * state['number2']
    return state

def subtractor(state: AgentState) -> AgentState:
    """Subtracts the two numbers"""
    print("--- Subtracting numbers ---")
    state['result'] = state['number1'] - state['number2']
    return state

def decide_next_node(state: AgentState) -> AgentState:
    """Decides the next node based on the operation"""
    if state['operation'] == "add":
        return "addition_operation"
    elif state['operation'] == "subtract":
        return "subtraction_operation"
    else:
        return "multiplication_operation"

if __name__ == '__main__':
    # 1. Initialize the Graph
    workflow = StateGraph(AgentState)
    
    # 2. Add multiple Nodes
    workflow.add_node("add_node", adder)
    workflow.add_node("multiply_node", multiplier)
    workflow.add_node("subtract_node", subtractor)
    workflow.add_node("router", lambda state: state) # pass state

    # 1. Start -> Decide
    workflow.add_edge(START, "router")
    
    # 2. Conditional edges
    workflow.add_conditional_edges(
        "router",
        decide_next_node,
        {   # THIS IS IN THE FORMAT OF A EDGE NAME : NODE NAME
            "addition_operation": "add_node",
            "subtraction_operation": "subtract_node",
            "multiplication_operation": "multiply_node"
        }
    )   
    
    # 3. Connect Nodes together (Sequential Flow)
    workflow.add_edge("add_node", END)
    workflow.add_edge("multiply_node", END)
    workflow.add_edge("subtract_node", END)
    
    # 5. Compile the Graph
    app = workflow.compile()
    
    # --- ADD THIS TO SHOW THE DIAGRAM ---
    print("\nWorkflow Diagram:")
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
    state = AgentState(**{'number1': 10, 'number2': 5, 'operation': 'multiply', 'result': 0})
    result = app.invoke(state)
    
    print("\n--- Final State ---")
    print(result)
    
    print("\n--- Result Output ---")
    print(result['result'])