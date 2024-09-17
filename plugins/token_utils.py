# token_utils.py
import jwt
import datetime

    def generate_token(user_id):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token valid for 1 hour
    payload = {'user_id': user_id, 'exp': expiration}
    return jwt.encode(payload, algorithm='HS256')

def decode_token(token):
    try:
        payload = jwt.decode(token, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
        
