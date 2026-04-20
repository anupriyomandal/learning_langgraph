from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    messages: str
    name: str

def process_node(state: AgentState) -> AgentState:
    state['messages'] = f"Hello {state['name']}"
    return state

if __name__ == '__main__':
    workflow = StateGraph(AgentState)
    workflow.add_node('process_node', process_node)
    workflow.set_entry_point('process_node')
    workflow.set_finish_point('process_node')

    app = workflow.compile()

    result = app.invoke({'name': 'Anupriyo'})
    print(result['messages'])