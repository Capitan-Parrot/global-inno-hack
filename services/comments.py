import requests
from sqlalchemy.orm import Session


class CommentServices:
    API_URL = 'https://api.teamflame.ru/comment'

    def add_comment(self, task_id: str, text_message: str):
        # access_token = ...
        requests.post(
            url=self.API_URL + '/create',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
            data={
                'task': task_id,
                'text': text_message,
            }
        )
