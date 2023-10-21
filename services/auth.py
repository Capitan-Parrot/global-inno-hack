import requests

from core.database import session
from models import TokenDB
from services.tokens import tokens_services


class AuthService:
    API_URL = 'https://auth-api.teamflame.ru/auth'

    def sign_in(self, email: str, password: str):
        response = requests.post(
            url=self.API_URL + '/sign-in',
            json={
                'email': email,
                'password': password,
            },
            headers={
                'accept': 'application/json'
            }
        )
        tokens = response.json()
        db_token = tokens_services.get_token_by_email(email=email)
        if not db_token:
            db_token = TokenDB(email=email)
        db_token.refresh_token = tokens["tokens"]["refreshToken"]["token"]
        db_token.access_token = tokens["tokens"]["accessToken"]["token"]
        session.add(db_token)
        session.commit()
        return tokens


auth_service = AuthService()
