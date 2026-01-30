def validate_email(email: dict) -> bool:
    required = {"subject", "email_body", "call_to_action"}

    if not isinstance(email, dict):
        raise ValueError("Email must be a dictionary")

    if not required.issubset(email.keys()):
        raise ValueError("Missing required fields")

    for key in required:
        if not isinstance(email[key], str) or not email[key].strip():
            raise ValueError(f"{key} must be a non-empty string")

    return True
