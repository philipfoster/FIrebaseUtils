import json

import pyrebase


class FirebaseClient:

    def __init__(self):
        with open('../res/keys/client-data.json', 'r') as my_file:
            data = my_file.read().replace('\n', '')

        json_data = json.loads(data)
        json_data["serviceAccount"] = "../res/keys/service-account-credentials.json"
        self._firebase = pyrebase.initialize_app(json_data)

    def sign_in_with_custom_token(self, token):
        """
        Sign in with a firebase admin custom auth token
        :return: a dictionary with the authenticated user's information
            The dictionary contains the following entries:
                - kind
                - idToken (to authenticate with)
                - refreshToken
                - expiresIn
                - isNewUser
        :param token: the firebase custom auth token from the admin SDK
        """
        user = self._firebase.auth().sign_in_with_custom_token(token)
        return user

    def generate_custom_token(self, email):
        return self._firebase.auth().create_custom_token(auth.get_user_by_email(email).uid)