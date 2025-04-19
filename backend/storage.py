import json
from pathlib import Path


TOKEN_FILE = Path("fcm_tokens.json")

def save_token(token: str):
    tokens = get_all_tokens()
    if token not in tokens:
        tokens.append(token)
        with open(TOKEN_FILE, "w") as f:
            json.dump(tokens, f)

def get_all_tokens():
    
    if not TOKEN_FILE.exists():
        return []
    with open(TOKEN_FILE, "r") as f:
        return json.load(f)
