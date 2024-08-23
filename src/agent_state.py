# agent_state.py

from typing import List, Dict, Any

class AgentState:
    def __init__(self):
        self.messages: List[Dict[str, Any]] = []
        self.session_data: Dict[str, Any] = {}
        self.language: str = 'en'  # Default language set to English

    def update_messages(self, new_message: Dict[str, Any]):
        self.messages.append(new_message)
