import requests

from sqlalchemy.orm import Session
from services import spaces
from services import projects


my_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZGlvbnpha3JhdWxza2lqQGdtYWlsLmNvbSIsInVzZXJJZCI6IjY1MTJmOWVmODc5OTgyYzIwZjBhNGExZiIsImlhdCI6MTY5NjA1NTgwNCwiZXhwIjoxNjk2MzU1ODA0fQ.im7Mi9N-e79mF3kedbKFJeYcuSl7Sk9kj6yfo3bJ4s8"


class BoardsServise():
    API_URL = 'https://api.teamflame.ru/board'

    def get_board_by_project_id(self, project_id: str):
        access_token = my_access_token
        boards = requests.get(
            url=self.API_URL + f'/boardsByProject/{project_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return boards.json()


boards = BoardsServise()
