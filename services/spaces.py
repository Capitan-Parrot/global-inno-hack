import requests

my_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZGlvbnpha3JhdWxza2lqQGdtYWlsLmNvbSIsInVzZXJJZCI6IjY1MTJmOWVmODc5OTgyYzIwZjBhNGExZiIsImlhdCI6MTY5NjA1NTgwNCwiZXhwIjoxNjk2MzU1ODA0fQ.im7Mi9N-e79mF3kedbKFJeYcuSl7Sk9kj6yfo3bJ4s8"

from core.database import session
from models import TokenDB


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
        return spaces.json()



space_service = SpaceService()
