from typing import TypedDict, Dict
from langgraph.graph import StateGraph, START, END

if __name__ == '__main__':
    class AgentState(TypedDict):
        """
        Represents the state of the agent.
        """
        messages: str
    
    def process_node(state: AgentState) -> AgentState:
        state['messages'] = f"Hello {state['messages']}"
        return state
    
    workflow = StateGraph(AgentState)
    workflow.add_node("process_node", process_node)
    
    # Define entry and exit points
    workflow.add_edge(START, "process_node")
    workflow.add_edge("process_node", END)
    
    # Compile the workflow into a runnable app
    app = workflow.compile()

    # Invoke the compiled app
    result = app.invoke({'messages': 'Anupriyo'})
    print(result)   