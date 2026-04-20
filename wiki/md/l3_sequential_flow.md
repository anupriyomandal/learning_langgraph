# Lesson 3: Sequential Graphs and Visualization

In this lesson, we moved beyond single nodes to create a sequential workflow where multiple nodes process the state in a specific order. We also learned how to visualize the graph structure in the terminal.

## Key Concepts

### 1. Multiple Nodes
A sequential graph consists of several nodes, each responsible for a part of the total processing logic.

```python
def get_details(state: AgentState) -> AgentState: ...
def process_status(state: AgentState) -> AgentState: ...
def create_report(state: AgentState) -> AgentState: ...

workflow.add_node("get_details", get_details)
workflow.add_node("process_status", process_status)
workflow.add_node("create_report", create_report)
```

### 2. Sequential Edges
Nodes are connected using `add_edge(source, target)`. This defines the flow of the state through the graph.

```python
workflow.add_edge(START, "get_details")
workflow.add_edge("get_details", "process_status")
workflow.add_edge("process_status", "create_report")
workflow.add_edge("create_report", END)
```

### 3. Graph Visualization
You can print an ASCII representation of the graph to verify its structure.

```python
app = workflow.compile()
app.get_graph().print_ascii()
```

> [!NOTE]
> This requires the `grandalf` package: `pip install grandalf`.

## Visual Output
The `print_ascii()` method produces a clear diagram of the flow:
```text
  +-----------+    
  | __start__ |    
  +-----------+    
         *         
  +-------------+  
  | get_details |  
  +-------------+  
         *         
+----------------+ 
| process_status | 
+----------------+ 
         *         
+---------------+  
| create_report |  
+---------------+  
         *         
    +---------+    
    | __end__ |    
    +---------+    
```

## Cross-References
- [State Management Concepts](concept_state.md)
- [Graph and Compilation Concepts](concept_stategraph.md)
- [Lesson 1: Basics of StateGraph](l1_basic_node.md) - Basic setup of a single node graph.
- [Assignment 1](a1_logic_nodes.md) - Moving complex logic into a single node vs. splitting it into multiple nodes.

---
[Home](../index.md) | [Back to Assignment 1](a1_logic_nodes.md) | [Next Lesson: (TBD)](#)
