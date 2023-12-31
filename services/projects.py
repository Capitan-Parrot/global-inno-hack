import requests
from services.tokens import tokens_services


class ProjectService():
    API_URL = 'https://api.teamflame.ru/project'

    def get_project_by_space_id(self, email: str, space_id: str):
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        spaces = requests.get(
            url=self.API_URL + f'/projectsBySpace/{space_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return spaces.json()

    def get_project_by_id(self, email: str, project_id: str):
        token = tokens_services.get_token_by_email(email=email)
        access_token = token.access_token
        projects = requests.get(
            url=self.API_URL + f'/{project_id}',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}',
            }
        )
        return projects.json()


project_service = ProjectService()
