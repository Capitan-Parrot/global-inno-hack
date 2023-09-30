import requests
from sqlalchemy.orm import Session


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

    def create_board(self, name: str, space_id: str, project_id: str):
        access_token = my_access_token
        board = requests.post(
            url=self.API_URL + '/create',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
            data={
                'name': name,
                'spaceId': space_id,
                'projectId': project_id,
                'location': space_id,
            }
        )

        return board.json()


boards = BoardsServise()
