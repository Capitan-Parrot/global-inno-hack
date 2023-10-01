import requests

from core.database import session
from models import TokenDB, UserDB


class AuthService:
    API_URL = 'https://auth-api.teamflame.ru/auth'

    def sign_in(self, email, password):
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
        db_token = session.query(TokenDB).filter_by(email=email).first()
        if not db_token:
            db_token = TokenDB(email=email)
        db_token.refresh_token = tokens["tokens"]["refreshToken"]["token"]
        db_token.access_token = tokens["tokens"]["accessToken"]["token"]
        session.add(db_token)
        session.commit()
        return tokens


auth_service = AuthService()

if __name__ == "__main__":
    auth_service.sign_in(123, "kondrandr2004@yandex.ru", "Qwerty2004")
