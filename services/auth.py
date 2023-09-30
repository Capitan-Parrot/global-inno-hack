import requests
from sqlalchemy.orm import Session

from core.database import get_db
from models import TokenDB


class AuthService:
    API_URL = 'https://auth-api.teamflame.ru/auth'

    def sign_in(self, chat_id, email, password):
        # , email: str, password: str
        # access_token = ...
        responce = requests.post(
            url=self.API_URL + '/sign-in',
            data={
                'email': email,
                'password': password
            },
            headers={
                'accept': 'application/json'
            }
        )
        tokens = responce.json()
        db = get_db()
        db_token = TokenDB(access_token=tokens.accessToken.token,
                           refresh_token=tokens.refreshToken.token)
        db.add(db_token)
        return tokens

    def get_spaces_by_id(self, db: Session, space_id: str):
        access_token = ...
        spaces = requests.get(
            url=self.API_URL + f'/{space_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces


auth_service = AuthService()
auth_service.sign_in()
