# src/nodes.py

from tools import query_db

def handle_input(state):
    print("Input received:", state.messages[-1]['content'])
    # Add logic to process the input
    return state

def process_data(state):
    # Example: Fetching response based on user's last query
    user_query = state.messages[-1]['content']  # Assuming the last message contains the query
    response = query_db("SELECT response FROM users WHERE query = ?", [user_query], one=True)
    if response:
        state.session_data['response'] = response[0]  # Assuming 'response' is the fetched column
    else:
        state.session_data['response'] = "Sorry, I can't help with that right now."
    return state

def generate_response(state):
    response_data = state.session_data.get('response')
    if response_data:
        response_message = f"I found something that might help: {response_data}"
    else:
        response_message = "I couldn't find any information related to your query. Can I help with something else?"
    state.messages.append({'content': response_message})
    return state

