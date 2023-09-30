import requests


class SpaceService():
    API_URL = 'https://global-inno-hack-dd509ac0d0a4.herokuapp.com/spaces'

    def get_spaces_by_user_id(self, user_id: int):
        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId/' + str(user_id),
            headers={
                'accept': 'application/json'
            }
        )
        return spaces.json()

    def get_spaces_by_id(self, user_id: int, space_id: str):
        spaces = requests.get(
            url=self.API_URL + f'/{space_id}',
            params={
                'user_id': user_id
            },
            headers={
                'accept': 'application/json',
            }
        )
        return spaces


space_service = SpaceService()
