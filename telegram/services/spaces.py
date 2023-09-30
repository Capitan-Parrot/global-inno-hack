import requests
<<<<<<<< HEAD:telegram/services/spaces.py
========

from coordinator.core.database import session
from coordinator.models import TokenDB
>>>>>>>> 1f061139b67a62876ee623b396aa9dc6e708928e:coordinator/services/spaces.py


class SpaceService():
    API_URL = 'https://api.teamflame.ru/space'

    def get_spaces_by_user_id(self, user_id: int):
        token = session.query(TokenDB).filter_by(user_id=user_id).first()
        access_token = token.access_token
        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces.json()

    def get_spaces_by_id(self, user_id: int, space_id: str):
        token = session.query(TokenDB).filter_by(user_id=user_id).first()
        access_token = token.access_token
        spaces = requests.get(
            url=self.API_URL + f'/{space_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces


space_service = SpaceService()
