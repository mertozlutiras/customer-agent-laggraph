# src/tools.py
import requests
import sqlite3
from langchain_core.tools import tool
from deep_translator import GoogleTranslator

# Database query function
def query_db(query, args=(), one=False):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Define the process_data as a tool
@tool
def process_data(user_query: str):
    """Fetch a response from the database based on the user's query."""
    response = query_db("SELECT response FROM users WHERE query = ?", [user_query], one=True)
    if response:
        return response[0]  # Return the fetched response
    else:
        return "Sorry, I can't help with that right now."

# Real search function using Google Custom Search API
@tool
def search(query: str):
    """Perform a real web search using Google Custom Search API."""
    api_key = "YOUR_GOOGLE_API_KEY"  # Replace with your actual API key
    search_engine_id = "YOUR_SEARCH_ENGINE_ID"  # Replace with your actual Search Engine ID
    
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": 1  # Number of results to return
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        search_results = response.json().get("items", [])
        if search_results:
            first_result = search_results[0]
            title = first_result.get("title")
            snippet = first_result.get("snippet")
            link = first_result.get("link")
            return f"Title: {title}\nSnippet: {snippet}\nLink: {link}"
        else:
            return "No results found."
    else:
        return f"Search failed with status code {response.status_code}"

# Translation tool using deep-translator
@tool
def translate(text: str, dest_language: str = 'en'):
    """Translate text to the specified language using deep-translator."""
    translation = GoogleTranslator(source='auto', target=dest_language).translate(text)
    return translation
