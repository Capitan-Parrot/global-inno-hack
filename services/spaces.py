import requests
from sqlalchemy.orm import Session


class SpaceRepositoty():
    API_URL = 'https://api.test-team-flame.ru/space'

    def get_spaces_by_user_id(self, db: Session, user_id: int):
        access_token = ...
        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces

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
