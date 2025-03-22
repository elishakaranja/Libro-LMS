import requests
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # loading the key from .env for security 

def get_book_recommendations(book_title):
    """
    Uses Gemini API to generate book recommendations based on a given title.
    Returning only book titles.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"#constructing the API request. Attaching the key at the end for authentication

    headers = {
        "Content-Type": "application/json" #This is telling the API that we're sending JSON data in the body 
    }

    prompt = f"Suggest 5 books similar to '{book_title}'. Only return a comma-separated list of book titles."#This is the instruction Prompt for the AI

    data = {
        "contents": [{
            "parts": [{"text": prompt}]        }] #This wraps the prompt in the required format for the API it follows the contents structure that Gemini API expects.
    }

    try:
        response = requests.post(url, headers=headers, json=data)# Sends a POST request to the Gemini API. 
        """ url is the API endpoint"""
        """headers is the JSON format"""
        """json=data is the request body containing the prompt"""
        response.raise_for_status()  # Raises an error if the request fails

        result = response.json()# processing the response
        suggestions = result["candidates"][0]["content"]["parts"][0]["text"]
        """This digs into the JSON response to extract the AI-generated book list."""
        
        return suggestions.split(", ")  # Convert to a Python list by splitting at each comma 

    except requests.exceptions.RequestException as e:
        print(f"Error fetching book recommendations: {e}")
        return ["No recommendations available"]

