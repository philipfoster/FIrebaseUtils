import firebase_admin
from firebase_admin import credentials, auth


class FirebaseAdmin:

    def __init__(self):
        cred = credentials.Certificate("../res/keys/service-account-credentials.json")
        self._app = firebase_admin.initialize_app(cred)

    def generate_custom_token(self, email):
        user = auth.get_user_by_email(email, self._app)
        token = auth.create_custom_token(user.uid, app=self._app).decode('utf-8')
        return token
