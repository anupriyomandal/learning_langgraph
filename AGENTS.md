# Agent Instructions: LangGraph Learning Repository

This repository is dedicated to learning and documenting LangGraph concepts through progressive lessons.

## Project Goal
Build a comprehensive knowledge base and a collection of working examples for LangGraph, starting from basic single-node graphs to complex multi-agent systems.

## Instructions for Agents

### 1. Maintain the Wiki Structure
The wiki is stored in the `wiki/` folder. All detailed documentation should reside in `wiki/md/`.
- **Index**: Always keep `wiki/index.md` updated with the latest lessons.
- **Cross-Referencing**: When adding a new lesson, check existing `.md` files in `wiki/md/` for related concepts and add cross-references. **Every new lesson must include links to the previous lessons it builds upon.**
- **Naming Convention**: 
    - Source code: `l<lesson_number>_<descriptive_topic>.py` (e.g., `l1_basic_node.py`).
    - Wiki files: `l<lesson_number>_<descriptive_topic>.md` (e.g., `l1_basic_node.md`).
    - Concept files: `concept_<name>.md` (e.g., `concept_state.md`).

### 2. Documenting Concepts
When a new core LangGraph feature is introduced (e.g., Checkpointers, Persistence, Custom Reducers):
- Create a standalone `concept_<name>.md` file if it doesn't exist.
- Explain the theory and provide a generic code example.
- Link this concept from all relevant lesson files.

### 3. Documenting Lessons
For every new `.py` file created or modified:
- Analyze the new LangGraph features being introduced.
- Create a corresponding `.md` file in `wiki/md/`.
- Include:
    - **Key Concepts**: Explain the new LangGraph components (e.g., `StateGraph`, `START`, `END`, `set_entry_point`, `ConditionalEdges`).
    - **Code Snippets**: Highlight the relevant parts of the code.
    - **Common Pitfalls**: Document any errors encountered and how they were fixed.
    - **Links**: Include "Back" and "Next" links at the bottom of the page.

### 3. API Consistency
LangGraph has evolved. Always prioritize the latest stable API:
- Use `from langgraph.graph import START, END` for edges when possible.
- Ensure `workflow.compile()` is used and the resulting `app` is invoked (not the graph object).
- When encountering legacy methods (like `.start_node()`), correct them and document the correction in the wiki.

### 4. Code Execution
Before documenting a lesson, always execute the Python script using the local virtual environment to ensure it works as expected.
```bash
./.venv/bin/python3 <filename>.py
```

### 5. Maintain the Presentation
A monochromatic HTML/CSS presentation is stored in `Presentation/index.html`.
- **New Slides**: When a significant new concept or lesson is added, consider adding a new slide to the presentation.
- **Visual Consistency**: Ensure the presentation maintains its minimalist, monochromatic aesthetic.
- **Linkage**: Ensure the presentation remains linked from the Wiki Index.

---
*This file serves as a guide for AI agents assisting in this repository.*
