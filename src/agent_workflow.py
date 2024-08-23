# agent_workflow.py
from langchain_ollama import ChatOllama
from langgraph.graph import MessagesState, START, END, StateGraph
from langgraph.prebuilt import ToolNode
from PIL import Image
import io
from tools import process_data, search, translate

# Set up the tools
tools = [search, process_data, translate]
tool_node = ToolNode(tools)

# Set up the ChatOllama model
model = ChatOllama(model="qwen2:0.5b")
model = model.bind_tools(tools)

# Define nodes and conditional edges
def should_continue(state):
    messages = state["messages"]
    last_message = messages[-1]
    # Determine whether to continue based on whether a tool was called
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"

def call_model(state):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}

# Define the workflow graph
workflow = StateGraph(MessagesState)

# Define the nodes in the graph
workflow.add_node("agent", call_model)
workflow.add_node("action", tool_node)

# Set the entry point as `agent`
workflow.add_edge(START, "agent")

# Add conditional edges from the agent node
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END,
    },
)

# Add normal edges
workflow.add_edge("action", "agent")

# Compile the graph
app = workflow.compile()

# Save the graph visualization to a file
graph_image_path = "agent_workflow_visualization.png"
graph_bytes = app.get_graph().draw_mermaid_png()

# Convert bytes to an image and save
image = Image.open(io.BytesIO(graph_bytes))
image.save(graph_image_path)

# Display the graph image
image.show()

print(f"Graph image saved at {graph_image_path}")
