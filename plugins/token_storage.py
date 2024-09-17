# token_storage.py
token_storage = {}

def add_token(user_id, token):
    token_storage[token] = user_id

def remove_token(token):
    token_storage.pop(token, None)

def get_tokens_left(user_id):
    return sum(1 for t in token_storage.values() if t == user_id)
  
