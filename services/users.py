import requests

from models import UserDB
from core.database import session
from services.tokens import tokens_services


class UsersService():
    API_URL = 'https://api.teamflame.ru/user'

    def get_user_by_id(self, email: str, user_id: str) -> dict:
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        user = requests.get(
            url=self.API_URL + f'/{user_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return user.json()

    def get_user_by_user_id(self, user_id: str):
        user = session.query(UserDB).filter_by(user_id=user_id).first()
        return user


users_services = UsersService()
