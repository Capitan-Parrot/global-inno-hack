import requests

from coordinator.core.database import session
from coordinator.models import TokenDB


class SpaceService():
    API_URL = 'https://api.teamflame.ru/space'

    def get_spaces_by_user_id(self, email: str):
        token = session.query(TokenDB).filter_by(email=email).first()
        access_token = token.access_token
        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces.json()

    def get_spaces_by_id(self, email: str, space_id: str):
        token = session.query(TokenDB).filter_by(email=email).first()
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
