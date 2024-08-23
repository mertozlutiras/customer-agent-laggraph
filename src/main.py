# main.py

from langgraph import StateGraph, END
from agent_state import AgentState
from src.nodes import handle_input, process_data, generate_response

# Initialize the StateGraph with the defined AgentState
graph = StateGraph(AgentState)

# Adding nodes to the graph using imported functions
graph.add_node("input", handle_input)
graph.add_node("process", process_data)
graph.add_node("response", generate_response)

# Define edges to control flow between nodes
graph.add_edge("input", "process")
graph.add_edge("process", "response")
graph.set_entry_point("input")
graph.add_edge("response", END)

# Compile the graph
compiled_graph = graph.compile()

# Example test invocation
test_state = AgentState()
test_state.messages.append({'content': 'Hello, how can I help you?'})
compiled_graph.invoke(test_state)
