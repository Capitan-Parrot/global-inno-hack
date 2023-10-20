import requests

from services.tokens import tokens_services


class ColumnsService():
    API_URL = 'https://api.teamflame.ru/column'

    def get_columns_by_board_id(self, email: str, board_id: str):
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        columns = requests.get(
            url=self.API_URL + f'/getByBoard/{board_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return columns.json()


columns_service = ColumnsService()
