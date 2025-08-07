import requests

messages = [
    "Hi, I'm Namrata",
    "Can you recommend a room?",
    "What makes it special?",
    "Are there other options?"
]

for msg in messages:
    print(f"User: {msg}")
    response = requests.post("http://127.0.0.1:8000/chat", json={"message": msg})
    print("AI:", response.json())
