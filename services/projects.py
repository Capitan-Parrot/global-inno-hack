import requests

from core.database import session
from models.tokens import TokenDB


class ProjectService():
    API_URL = 'https://api.teamflame.ru/project'

    def get_project_by_space_id(self, chat_id: int, space_id: str):
        token = session.query(TokenDB).filter_by(chat_id=chat_id).first()
        spaces = requests.get(
            url=self.API_URL + f'/projectsBySpace/{space_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {token}',
            }
        )
        return spaces.json()


projects = ProjectService()
