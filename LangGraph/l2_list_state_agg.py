from typing import TypedDict, List
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    numbers : List[int]
    name : str
    result : str

def process_values(state: AgentState) -> AgentState:
    """This function handles mulitple inputs."""
    state['result'] = f'Hi {state['name']}! Your sum is {sum(state['numbers'])}'
    return state

if __name__ == '__main__':
    
    workflow = StateGraph(AgentState)
    workflow.add_node("process_values", process_values)
    workflow.set_entry_point('process_values')
    workflow.set_finish_point('process_values')

    app = workflow.compile()
    result = app.invoke({'numbers': [1,2,3], 'name': 'Anupriyo'})
    print(result)   