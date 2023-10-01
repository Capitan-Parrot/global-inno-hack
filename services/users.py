import requests

from core.database import session
from models.tokens import TokenDB


class UsersService():
    API_URL = 'https://api.teamflame.ru/user'

    def get_user_by_id(self, email: str, user_id: str):
        token = session.query(TokenDB).filter_by(email=email).first()
        access_token = token.access_token
        user = requests.get(
            url=self.API_URL + f'/{user_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return user.json()


users_services = UsersService()
