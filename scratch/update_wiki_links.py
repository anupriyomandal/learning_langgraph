import os

replacements = {
    "01_single_node_graph.md": "l1_basic_node.md",
    "l1_single_node_1.md": "l1_1_multi_key_state.md",
    "l2_single_node_2.md": "l2_list_state_agg.md",
    "assignment_1.md": "a1_logic_nodes.md",
    "l3_sequential_nodes.md": "l3_sequential_flow.md",
    "l4_conditional_node.md": "l4_conditional_routing.md",
    "assignment_2.md": "a2_chained_routers.md",
    "l5_looping_graphs.md": "l5_recurrent_loops.md",
    "assignment_3.md": "a3_binary_search_game.md",
    "l6_integrating_llm.md": "l6_llm_rich_ui.md",
    "assignment_4.md": "a4_interactive_chatbot.md",
    "l7_ReAct_agent.md": "l7_react_tools.md",
    "l7_ReAct_agent_pfd.md": "l7_react_tools_pfd.md",
    "l8_pure_langgraph_react.md": "l8_pure_react_no_langchain.md",
    "l9_project_drafter.md": "l9_drafter_external_loop.md",
    "l9_project_drafter_pfd.md": "l9_drafter_external_loop_pfd.md",
    
    "l1_single_node.py": "l1_basic_node.py",
    "l1_single_node_1.py": "l1_1_multi_key_state.py",
    "l2_single_node_2.py": "l2_list_state_agg.py",
    "assignment_1.py": "a1_logic_nodes.py",
    "l3_sequential_nodes.py": "l3_sequential_flow.py",
    "l4_conditional_node.py": "l4_conditional_routing.py",
    "assignment_2.py": "a2_chained_routers.py",
    "l5_looping_graphs.py": "l5_recurrent_loops.py",
    "assignment_3.py": "a3_binary_search_game.py",
    "l6_integrating_llm.py": "l6_llm_rich_ui.py",
    "assignment_4.py": "a4_interactive_chatbot.py",
    "l7_ReAct_agent.py": "l7_react_tools.py",
    "l8_pure_langgraph_react.py": "l8_pure_react_no_langchain.py",
    "l9_project_drafter.py": "l9_drafter_external_loop.py"
}

wiki_dir = "wiki/md"
for filename in os.listdir(wiki_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(wiki_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
        
        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filename}")
