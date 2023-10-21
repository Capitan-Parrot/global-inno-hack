import requests
from services.tokens import tokens_services


class CommentServices:
    API_URL = 'https://api.teamflame.ru/comment'

    def add_comment(self, email: str, task_id: str, text_message: str):
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        new_comment = requests.post(
            url=self.API_URL + '/create',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
            json={
                'task': task_id,
                'text': text_message,
            }
        )
        return new_comment.json()


comments_service = CommentServices()
