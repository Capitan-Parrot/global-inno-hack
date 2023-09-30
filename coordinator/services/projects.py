import requests

from coordinator.core.database import session
from coordinator.models import TokenDB


class ProjectService():
    API_URL = 'https://api.teamflame.ru/project'

<<<<<<< HEAD
    def get_project_by_space_id(self, user_id: int, space_id: str):
        token = session.query(TokenDB).filter_by(user_id=user_id).first()
=======
    def get_project_by_space_id(self, email: str, space_id: str):
        token = session.query(TokenDB).filter_by(email=email).first()
>>>>>>> 5015215601d75efd47783de213c792ae6725376d
        access_token = token.access_token
        spaces = requests.get(
            url=self.API_URL + f'/projectsBySpace/{space_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces.json()


project_service = ProjectService()
