import os
import httpx
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful DevOps assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = httpx.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
