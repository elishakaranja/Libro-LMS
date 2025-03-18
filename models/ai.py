import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test OpenAI connection
try:
    client = openai.Client(api_key=openai.api_key)  # New OpenAI client
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, AI!"}],
        temperature=0,
    )
    print(response.choices[0].message.content)  # New response format
except Exception as e:
    print(f"Error: {e}")
