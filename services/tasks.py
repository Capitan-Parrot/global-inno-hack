import requests


class TaskService:
    API_URL = 'https://api.teamflame.ru/task'

    def get_task_by_id(self, chat_id: int, task_id: str):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        access_token = token.access_token
        task = requests.get(
            url=self.API_URL + f'/{task_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return task.json()

    def change_task_column(self, chat_id: int, task_id: str, column_id: str):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        access_token = token.access_token
        task = requests.post(
            url=self.API_URL + f'/change-column/{task_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
            data={
                'columnId': column_id,
                'location': task_id
            }
        )
        return task.json()


task_service = TaskService()
