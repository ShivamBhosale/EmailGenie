import requests
import json
from prompts import STRUCTURED_EMAIL_PROMPT

ollame_url = "http://localhost:11434/api/generate"
MODEL = "llama3.2:latest"

def generate_email(tone, purpose, key_points):
    prompt = STRUCTURED_EMAIL_PROMPT.format(
        tone=tone,
        purpose=purpose,
        key_points=key_points
    )

    response = requests.post(
        ollame_url,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    raw_response = response.json()["response"]
    
    return json.loads(raw_response)