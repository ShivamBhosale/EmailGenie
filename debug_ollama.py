import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen2.5:3b",
        "messages": [
            {
                "role": "user",
                "content": "Return a JSON object with keys subject, email_body, call_to_action."
            }
        ],
        "format": "json",
        "options": {
            "temperature": 0
        }
    },
    timeout=180
)

print("RAW RESPONSE JSON:")
print(response.json())
print("\n---\n")
print("RAW MESSAGE CONTENT:")
print(repr(response.json()["message"]["content"]))
