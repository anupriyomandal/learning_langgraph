from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    pass

b = StateGraph(State)
b.add_node('a', lambda x: x)
b.add_edge(START, 'a')
b.add_edge('a', END)
app = b.compile()

try:
    png_data = app.get_graph().draw_mermaid_png()
    with open("test_graph.png", "wb") as f:
        f.write(png_data)
    print("Success: test_graph.png created")
except Exception as e:
    print(f"Error: {e}")
