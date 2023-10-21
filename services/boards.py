import requests
from services.tokens import tokens_services
from models import BoardDB
from core.database import session


class BoardsService():
    API_URL = 'https://api.teamflame.ru/board'

    def get_board_by_id(self, email: str, board_id: str):
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        board = requests.get(
            url=self.API_URL + f'/{board_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return board.json()

    def get_board_by_project_id(self, email: str, project_id: str):
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        boards = requests.get(
            url=self.API_URL + f'/boardsByProject/{project_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return boards.json()

    def get_board_by_user_id(self, user_id: int):
        board = session.query(BoardDB).filter_by(user_id=user_id).first()
        return board

    def create_board(self,
                     email: str,
                     name: str,
                     space_id: str,
                     project_id: str):

        token = tokens_services.get_token_by_email(email=email)

        access_token = token.access_token
        board = requests.post(
            url=self.API_URL + '/create',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
            json={
                'name': name,
                'spaceId': space_id,
                'projectId': project_id,
                'location': space_id,
            }
        )

        return board.json()


board_service = BoardsService()
