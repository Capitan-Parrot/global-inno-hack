import requests

from coordinator.core.database import session
from coordinator.models import TokenDB


class CommentServices:
    API_URL = 'https://api.teamflame.ru/comment'

<<<<<<< HEAD
    def add_comment(self, user_id: int, task_id: str, text_message: str):
        token = session.query(TokenDB).filter_by(user_id=user_id).first()
=======
    def add_comment(self, email: str, task_id: str, text_message: str):
        token = session.query(TokenDB).filter_by(email=email).first()
>>>>>>> 5015215601d75efd47783de213c792ae6725376d
        access_token = token.access_token
        new_comment = requests.post(
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
        return new_comment.json()


comments = CommentServices()
