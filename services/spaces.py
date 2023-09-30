import requests

from core.database import session
from models import TokenDB


class SpaceService():
    API_URL = 'https://api.teamflame.ru/space'

    def get_spaces_by_user_id(self, chat_id: int):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {token}',
            }
        )
        return spaces.json()

    def get_spaces_by_id(self, chat_id: int, space_id: str):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        spaces = requests.get(
            url=self.API_URL + f'/{space_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {token}',
            }
        )
        return spaces


space_service = SpaceService()
