import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"

def generate_email(tone: str, purpose: str, key_points: str) -> dict:
    prompt = f"""
Generate a professional email.

Tone: {tone}
Purpose: {purpose}
Key points: {key_points}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "format": {
                "type": "object",
                "properties": {
                    "subject": {"type": "string"},
                    "email_body": {"type": "string"},
                    "call_to_action": {"type": "string"}
                },
                "required": ["subject", "email_body", "call_to_action"]
            },
            "options": {
                "temperature": 0.2
            }
        },
        timeout=120
    )

    response.raise_for_status()

    # With Qwen, this is a REAL dict (not a string)
    return response.json()["message"]["content"]
