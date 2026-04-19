# Process Flow Diagram: Project Drafter (Lesson 9)

This document details the interaction between the **External Human Loop** and the **Internal LangGraph Reasoning Cycle**.

## 1. High-Level Architecture

```mermaid
graph TD
    %% External Loop
    LOOP[While True: Human Loop]
    UI[render_ui - Rich Dashboard]
    INPUT[/User Input/]
    INVOKE[app.invoke - Atomic Cycle]

    %% Internal Graph
    START((START))
    MN[model_node - The Brain]
    TN[tool_node - The Hands]
    ROUTER{Router}
    CONTINUE{Continue?}
    END((END))

    %% Connections
    LOOP --> UI
    UI --> INPUT
    INPUT --> INVOKE
    
    INVOKE --> START
    START --> MN
    MN --> ROUTER
    ROUTER -- "Tool Calls" --> TN
    ROUTER -- "Final Response" --> END
    
    TN --> CONTINUE
    CONTINUE -- "Needs Update" --> MN
    CONTINUE -- "Saved" --> END
    
    END --> LOOP

    %% Styling
    subgraph External_Loop [External Dashboard Loop]
        LOOP
        UI
        INPUT
    end

    subgraph Internal_Graph [Internal LangGraph Reasoning]
        START
        MN
        TN
        ROUTER
        CONTINUE
        END
    end

    style External_Loop fill:#000,stroke:#666,stroke-dasharray: 5 5,color:#fff
    style Internal_Graph fill:#000,stroke:#9333ea,stroke-dasharray: 5 5,color:#fff
    style MN fill:#4f46e5,stroke:#fff,stroke-width:2px,color:#fff
    style TN fill:#0d9488,stroke:#fff,stroke-width:2px,color:#fff
```

## 2. Key Differences from Standard ReAct
- **Persistence**: The state is passed back and forth between the loop and the graph.
- **UI Decoupling**: The terminal is cleared and updated only once per turn by the loop, preventing the "thinking" node from causing flicker.
- **Atomic Execution**: The graph doesn't wait for humans; it runs until it either hits a final answer or finishes its tool sequence.

---
[Back to Lesson 9](l9_project_drafter.md) | [Wiki Index](../index.md)
