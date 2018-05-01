from src.firebaseadmin import FirebaseAdmin
from src.firebaseclient import FirebaseClient


class TokenGenerator:
    """
        This class provides utility methods for generating firebase auth tokens
    """
    def __init__(self):
        self._admin = FirebaseAdmin()
        self._client = FirebaseClient()

    def get_token_for_email(self, email):
        token = self._admin.generate_custom_token(email)
        user = self._client.sign_in_with_custom_token(token)
        return user
