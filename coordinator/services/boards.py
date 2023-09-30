import requests

from coordinator.core.database import session
from coordinator.models import TokenDB


class BoardsServise():
    API_URL = 'https://api.teamflame.ru/board'

    def get_board_by_project_id(self, user_id: int, project_id: str):
        token = session.query(TokenDB).filter_by(user_id=user_id).first()
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
                     user_id: int,
                     name: str,
                     space_id: str,
                     project_id: str):

        token = session.query(TokenDB).filter_by(user_id=user_id).first()
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


board_service = BoardsServise()