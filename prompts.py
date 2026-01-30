STRUCTURED_EMAIL_PROMPT = """
You are a professional business writing assistant.

Generate a professional email using the information below.
Return the output in valid JSON ONLY.
Do not include explanations or extra text.

Required JSON schema:
{
  "subject": string,
  "email_body": string,
  "call_to_action": string
}

Tone: {tone}
Purpose: {purpose}
Key points: {key_points}

JSON Output:
"""
