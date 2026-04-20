"""
Assignment 1:
Create a Graph where you pass in a single list of integers along with a name and an operation. 
If the operation is a "+", you add the elements and if it is a "*", you multiply the elements, all within the same node.

Input: {"name": "Jack Sparrow", "values": [1,2,3,4], "operation": "*"}
Output: "Hi Jack Sparrow, your answer is: 24"
"""

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
import math

class AgentState(TypedDict):
    name: str
    values: List[int]
    operation: str
    result: str

def calculator_node(state: AgentState) -> AgentState:
    """
    Performs addition or multiplication based on the operation key.
    """
    name = state['name']
    values = state['values']
    operation = state['operation']
    
    if operation == "+":
        answer = sum(values)
    elif operation == "*":
        answer = math.prod(values)
    else:
        answer = "Invalid operation"
    
    state['result'] = f"Hi {name}, your answer is: {answer}"
    return state

if __name__ == '__main__':
    # Initialize the graph
    workflow = StateGraph(AgentState)
    
    # Add the single node
    workflow.add_node("calculator", calculator_node)
    
    # Set entry and exit points
    workflow.set_entry_point("calculator")
    workflow.set_finish_point("calculator")
    
    # Compile the app
    app = workflow.compile()
    
    # Define input
    user_input = {
        "name": "Jack Sparrow",
        "values": [1, 2, 3, 4],
        "operation": "*"
    }
    
    # Invoke the app
    final_state = app.invoke(user_input)
    
    # Print the specific result string requested
    print(final_state['result'])
