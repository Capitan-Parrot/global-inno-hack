import requests

from sqlalchemy.orm import Session
import random

from coordinator.core.database import session
from coordinator.models import TokenDB

my_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZGlvbnpha3JhdWxza2lqQGdtYWlsLmNvbSIsInVzZXJJZCI6IjY1MTJmOWVmODc5OTgyYzIwZjBhNGExZiIsImlhdCI6MTY5NjA1NTgwNCwiZXhwIjoxNjk2MzU1ODA0fQ.im7Mi9N-e79mF3kedbKFJeYcuSl7Sk9kj6yfo3bJ4s8"


class SpaceService():
    API_URL = 'https://api.teamflame.ru/space'
    token = my_access_token



    def get_spaces_by_user_id(self, chat_id: int):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        access_token = token.access_token

        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }
        )
        return spaces.json()



    def get_spaces_by_id(self, chat_id: int, space_id: str):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        access_token = token.access_token

        spaces = requests.get(
            url=self.API_URL + '/get-sidebar-data',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }
        ).json()

        print('Your spaces:')

        for _space in spaces:
            print(_space['name'], _space['id'])
            
        return spaces
    

    def get_all_space_tasks(self, id: str=None):

        space_id = "65172175f074f999078a6e3d"

        spaces = requests.get(
            url=self.API_URL + '/get-all-space-tasks/' + space_id,
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }
        ).json()

        return spaces
    
    def create_space(self):

        result = requests.post(
            url=self.API_URL + '/get-all-space-tasks/' + space_id,
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            },
            data={
                "name": "Test space",
                "logo": "https://play-lh.googleusercontent.com/ZyWNGIfzUyoajtFcD7NhMksHEZh37f-MkHVGr5Yfefa-IX7yj9SMfI82Z7a2wpdKCA=w240-h480-rw",
                "color": "#ffffff",
                "invites": [
                    "rodionzakraulskij@gmail.com"
                ]
            }
        ).json()
        return result
    

sr = SpaceService()
result = sr.get_spaces_by_user_id()[0]

space_id = result['id']
print(space_id)
