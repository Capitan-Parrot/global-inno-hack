import requests

from coordinator.core.database import session
from coordinator.models import TokenDB


class AuthService:
    API_URL = 'https://auth-api.teamflame.ru/auth'

    def sign_in(self, user_id, email, password):
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
        db_token = TokenDB(user_id=user_id,
                           access_token=tokens["tokens"]["accessToken"]["token"],
                           refresh_token=tokens["tokens"]["refreshToken"]["token"])
        session.add(db_token)
        session.commit()
        return tokens


auth_service = AuthService()

if __name__ == "__main__":
    auth_service.sign_in(123, "kondrandr2004@yandex.ru", "Qwerty2004")
