import requests
from sqlalchemy.orm import Session

from core.database import session
from models import TokenDB

my_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZGlvbnpha3JhdWxza2lqQGdtYWlsLmNvbSIsInVzZXJJZCI6IjY1MTJmOWVmODc5OTgyYzIwZjBhNGExZiIsImlhdCI6MTY5NjA1NTgwNCwiZXhwIjoxNjk2MzU1ODA0fQ.im7Mi9N-e79mF3kedbKFJeYcuSl7Sk9kj6yfo3bJ4s8"


class SpaceService():
    API_URL = 'https://api.teamflame.ru/space'

    def get_spaces_by_user_id(self, chat_id: int = None):
        tokens = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        access_token = tokens.access_token
        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        spaces = spaces.json()
        print(spaces)
        return spaces

    def get_spaces_by_id(self, space_id: str):
        access_token = my_access_token
        spaces = requests.get(
            url=self.API_URL + f'/{space_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces


space_service = SpaceService()
