import requests


class CommentServices:
    API_URL = 'https://api.teamflame.ru/comment'

    def add_comment(self, chat_id: int, task_id: str, text_message: str):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
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
