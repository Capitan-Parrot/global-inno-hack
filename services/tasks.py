import requests
from services.tokens import tokens_services


class TaskService:
    API_URL = 'https://api.teamflame.ru/task'

    def get_task_by_id(self, email: str, task_id: str) -> dict:
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        task = requests.get(
            url=self.API_URL + f'/{task_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return task.json()

    def change_task_column(
            self,
            email: str,
            task_id: str,
            column_id: str
            ) -> dict:

        token = tokens_services.get_token_by_email(email=email)
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

    def get_tasks_by_column_id(self, email: str, column_id: str) -> dict:
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        task = requests.get(
            url=self.API_URL + f'/getTasksByColumn/{column_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return task.json()

    def create_task(self,
                    email: str,
                    name: str,
                    description: str,
                    column_id: str,
                    users: list[str] | None,
                    ) -> dict:
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        task = requests.post(
            url=self.API_URL + '/create',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
            data={
                'name': name,
                'description': description,
                'columnId': column_id,
                'location': column_id,
                'users': users
            }
        )
        return task.json()


tasks_service = TaskService()
