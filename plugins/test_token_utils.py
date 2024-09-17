# test_token_utils.py
import unittest
from token_utils import generate_token, decode_token
from token_storage import add_token, remove_token, get_tokens_left

class TestTokenFunctions(unittest.TestCase):
    def test_generate_and_decode_token(self):
        user_id = 'test_user'
        token = generate_token(user_id)
        self.assertIsNotNone(token)
        payload = decode_token(token)
        self.assertEqual(payload['user_id'], user_id)

    def test_token_storage(self):
        user_id = 'test_user'
        token = generate_token(user_id)
        add_token(user_id, token)
        self.assertEqual(get_tokens_left(user_id), 1)
        remove_token(token)
        self.assertEqual(get_tokens_left(user_id), 0)

if __name__ == '__main__':
    unittest.main()
  
