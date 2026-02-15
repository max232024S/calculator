import requests
import os
import json
from fastapi import FastAPI

API_KEY = os.getenv("OPENROUTER_API_KEY")
def calculator(content):
    response = requests.post(
        url = "https://openrouter.ai/api/v1/chat/completions",
        headers = {
            "Authorization" : f"Bearer {API_KEY}"
            
        },
        json = {
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {"role": "user",
                "content": content}
            ]
        })
    response.raise_for_status()
    print(response.json()["choices"][0]["message"]["content"])

while True:
    message = input("Enter your next message.")
    if message == "exit":
        break
    calculator(message)