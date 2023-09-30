import requests
from sqlalchemy.orm import Session

my_access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImxpemFfdmF0ZXJAeWFob28uY29tIiwidXNlcklkIjoiNjUxNzIyMDU4Nzk5ODJjMjBmMGI2Yjc3IiwiaWF0IjoxNjk2MDU1NDkzLCJleHAiOjE2OTYzNTU0OTN9.Reku1ISR-kjxPCl5NpUx5CnayQ4UcWnnxwYPwc9broQ'


class TaskService:
    API_URL = 'https://api.teamflame.ru/task'

    def get_task_by_id(self, task_id: str):
        access_token = my_access_token
        task = requests.get(
            url=self.API_URL + f'/{task_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return task

    def change_task_column(self, task_id: str, column_id: str):
        access_token = my_access_token
        response = requests.post(
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


task_service = TaskService()
task_service.change_task_column(task_id='6517220ff074f999078a71bd', column_id='6517220ff074f999078a71b2')