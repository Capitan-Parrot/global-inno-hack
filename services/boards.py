import requests

from core.database import session
from models.tokens import TokenDB


class BoardsServise():
    API_URL = 'https://api.teamflame.ru/board'

    def get_board_by_project_id(self, chat_id: int, project_id: str):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        boards = requests.get(
            url=self.API_URL + f'/boardsByProject/{project_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {token}',
            }
        )
        return boards.json()

    def create_board(self,
                     chat_id: int,
                     name: str,
                     space_id: str,
                     project_id: str):

        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        board = requests.post(
            url=self.API_URL + '/create',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {token}',
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
