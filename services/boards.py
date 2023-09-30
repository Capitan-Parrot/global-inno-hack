import requests

from core.database import session
from models import TokenDB


class BoardsService():
    API_URL = 'https://api.teamflame.ru/board'

    def get_board_by_project_id(self, email: str, project_id: str):
        token = session.query(TokenDB).filter_by(email=email).first()
        access_token = token.access_token
        boards = requests.get(
            url=self.API_URL + f'/boardsByProject/{project_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return boards.json()

    def create_board(self,
                     email: str,
                     name: str,
                     space_id: str,
                     project_id: str):

        token = session.query(TokenDB).filter_by(email=email).first()

        access_token = token.access_token
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


board_service = BoardsService()
