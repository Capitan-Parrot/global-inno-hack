import requests

from coordinator.core.database import session
from coordinator.models import TokenDB


class AuthService:
    API_URL = 'https://auth-api.teamflame.ru/auth'

<<<<<<< HEAD
    def sign_in(self, user_id, email, password):
=======
    def sign_in(self, email, password):
>>>>>>> 5015215601d75efd47783de213c792ae6725376d
        # , email: str, password: str
        # access_token = ...
        response = requests.post(
            url=self.API_URL + '/sign-in',
            data={
                'email': email,
                'password': password
            },
            headers={
                'accept': 'application/json'
            }
        )
        tokens = response.json()
<<<<<<< HEAD
        db_token = TokenDB(user_id=user_id,
=======
        db_token = TokenDB(email=email,
>>>>>>> 5015215601d75efd47783de213c792ae6725376d
                           access_token=tokens["tokens"]["accessToken"]["token"],
                           refresh_token=tokens["tokens"]["refreshToken"]["token"])
        session.add(db_token)
        session.commit()
        return tokens


auth_service = AuthService()

if __name__ == "__main__":
    auth_service.sign_in(123, "kondrandr2004@yandex.ru", "Qwerty2004")
