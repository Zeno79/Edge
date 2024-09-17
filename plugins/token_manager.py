# token_manager.py
import random
import string

# Dictionary to store tokens and their status
tokens = {}

def generate_token(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def add_token():
    token = generate_token()
    tokens[token] = True  # Mark token as valid
    return token

def use_token(token):
    if tokens.get(token):
        tokens[token] = False  # Mark token as used
        return True
    return False

def tokens_left():
    return sum(1 for used in tokens.values() if used)
  
