import requests

from core.database import session
from models import TokenDB


class ColumnsService():
    API_URL = 'https://api.teamflame.ru/column'

    def get_columns_by_board_id(self, email: str, board_id: str):
        token = session.query(TokenDB).filter_by(email=email).first()
        access_token = token.access_token
        columns = requests.get(
            url=self.API_URL + f'/getByBoard/{board_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return columns.json()
