import requests
from sqlalchemy.orm import Session


my_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZGlvbnpha3JhdWxza2lqQGdtYWlsLmNvbSIsInVzZXJJZCI6IjY1MTJmOWVmODc5OTgyYzIwZjBhNGExZiIsImlhdCI6MTY5NjA1NTgwNCwiZXhwIjoxNjk2MzU1ODA0fQ.im7Mi9N-e79mF3kedbKFJeYcuSl7Sk9kj6yfo3bJ4s8"


class ProjectService():
    API_URL = 'https://api.teamflame.ru/project'

    def get_project_by_space_id(self, space_id: str, db: Session = None):
        access_token = my_access_token
        spaces = requests.get(
            url=self.API_URL + '/projectsBySpace/' + space_id,
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }

        )

        return spaces.json()


projects = ProjectService()
