import random
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List

class AgentState(TypedDict):
    player_name: str
    target: int
    guess: int
    guesses: List[int]
    attempts: int
    lower_bound: int
    upper_bound: int
    hint: str
    correct: bool

def setup_game(state: AgentState) -> AgentState:
    """Initializes the target number and game bounds."""
    print(f"--- Setting up game for {state['player_name']} ---")
    state['target'] = random.randint(1, 20)
    state['lower_bound'] = 1
    state['upper_bound'] = 20
    state['attempts'] = 0
    state['guesses'] = []
    state['correct'] = False
    return state

def make_guess(state: AgentState) -> AgentState:
    """Makes a guess based on the current bounds (Binary Search Strategy)."""
    # Simple binary search strategy: guess the midpoint
    guess = (state['lower_bound'] + state['upper_bound']) // 2
    
    # Safety check: avoid repeating the same guess if bounds haven't changed enough
    # This shouldn't happen with strict binary search, but good for robustness
    if guess in state['guesses']:
        if state['hint'] == "higher":
            guess += 1
        else:
            guess -= 1
            
    state['guess'] = guess
    state['guesses'].append(guess)
    state['attempts'] += 1
    print(f"Attempt {state['attempts']}: Guessing {guess} (Range: {state['lower_bound']}-{state['upper_bound']})")
    return state

def provide_hint(state: AgentState) -> AgentState:
    """Evaluates the guess and provides a hint."""
    if state['guess'] == state['target']:
        state['hint'] = "correct"
        state['correct'] = True
        print("--- Correct! ---")
    elif state['guess'] < state['target']:
        state['hint'] = "higher"
        state['lower_bound'] = state['guess'] + 1
        print("Hint: Higher")
    else:
        state['hint'] = "lower"
        state['upper_bound'] = state['guess'] - 1
        print("Hint: Lower")
    return state

def should_continue(state: AgentState) -> str:
    """Decides whether to continue guessing or stop."""
    if state['correct']:
        return "won"
    if state['attempts'] >= 7:
        return "lost"
    return "continue"

if __name__ == '__main__':
    # 1. Initialize the Graph
    workflow = StateGraph(AgentState)
    
    # 2. Add Nodes
    workflow.add_node("setup", setup_game)
    workflow.add_node("guess", make_guess)
    workflow.add_node("hint", provide_hint)
    
    # 3. Connect Nodes
    workflow.add_edge(START, "setup")
    workflow.add_edge("setup", "guess")
    workflow.add_edge("guess", "hint")
    
    # 4. Add Conditional Edges (The Loop)
    workflow.add_conditional_edges(
        "hint",
        should_continue,
        {
            "continue": "guess", # Loop back to guess
            "won": END,          # Game over - Win
            "lost": END          # Game over - Max attempts reached
        }
    )
    
    # 5. Compile the Graph
    app = workflow.compile()
    
    # --- Visualization ---
    print("\nGenerating Workflow Diagram...")
    try:
        png_data = app.get_graph().draw_mermaid_png()
        with open("assignment_3_graph.png", "wb") as f:
            f.write(png_data)
        print("Success: Diagram saved to 'assignment_3_graph.png'")
    except Exception:
        pass
    app.get_graph().print_ascii()
    
    # 6. Run the Game
    print("\nStarting the Game...")
    initial_state = {
        "player_name": "Student",
        "guesses": [],
        "attempts": 0,
        "lower_bound": 1,
        "upper_bound": 20,
        "hint": "",
        "correct": False
    }
    result = app.invoke(initial_state)
    
    print("\n--- Game Result ---")
    if result['correct']:
        print(f"Success! The number was {result['target']}. Guessed in {result['attempts']} attempts.")
    else:
        print(f"Failed. The number was {result['target']}. Max attempts reached.")
    print(f"All Guesses: {result['guesses']}")