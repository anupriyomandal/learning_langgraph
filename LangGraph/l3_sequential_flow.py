"""
Lesson 3: Sequential Graph
Objectives:
1. Create multiple Nodes that sequentially process and update different parts of the state.
2. Connect Nodes together in a graph.
3. Invoke the Graph and see how the state is transformed step-by-step.
"""

from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class AgentState(TypedDict):
    name: str
    age: int
    status: str
    report: str

def get_details(state: AgentState) -> AgentState:
    """Sets initial details."""
    print("--- Running get_details ---")
    # In a real scenario, this might fetch from a DB or user input
    state['name'] = 'Anupriyo'
    state['age'] = 21
    return state

def process_status(state: AgentState) -> AgentState:
    """Processes status based on age."""
    print("--- Running process_status ---")
    if state['age'] >= 18:
        state['status'] = "Adult"
    else:
        state['status'] = "Minor"
    return state

def create_report(state: AgentState) -> AgentState:
    """Finalizes the report."""
    print("--- Running create_report ---")
    state['report'] = f"Agent {state['name']} is a {state['status']} (Age: {state['age']})"
    return state

if __name__ == '__main__':
    # 1. Initialize the Graph
    workflow = StateGraph(AgentState)
    
    # 2. Add multiple Nodes
    workflow.add_node("get_details", get_details)
    workflow.add_node("process_status", process_status)
    workflow.add_node("create_report", create_report)
    
    # 3. Connect Nodes together (Sequential Flow)
    workflow.add_edge(START, "get_details")
    workflow.add_edge("get_details", "process_status")
    workflow.add_edge("process_status", "create_report")
    workflow.add_edge("create_report", END)
    
    # 4. Compile the Graph
    app = workflow.compile()
    
    # --- ADD THIS TO SHOW THE DIAGRAM ---
    print("\nWorkflow Diagram:")
    app.get_graph().print_ascii()
    # ------------------------------------
    
    # 5. Invoke the Graph and see the transformation
    print("\nInvoking graph...")
    result = app.invoke({'name': '', 'age': 0, 'status': '', 'report': ''})
    
    print("\n--- Final State ---")
    print(result)
    
    print("\n--- Report Output ---")
    print(result['report'])