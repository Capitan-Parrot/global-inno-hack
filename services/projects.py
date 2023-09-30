import requests


class ProjectService():
    API_URL = 'https://global-inno-hack-dd509ac0d0a4.herokuapp.com/project'

    def get_project_by_space_id(self, user_id: int, space_id: str):
        project = requests.get(
            url=self.API_URL + f'/projectsBySpace/{space_id}',
            params={"user_id": user_id},
            headers={
                'accept': 'application/json',
            }
        )
        print(project.url)
        return project.json()


project_service = ProjectService()
