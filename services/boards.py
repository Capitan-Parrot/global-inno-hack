import requests


class BoardsServise():
    API_URL = 'https://global-inno-hack-dd509ac0d0a4.herokuapp.com/board'

    def get_board_by_project_id(self, user_id: int, project_id: str):
        boards = requests.get(
            url=self.API_URL + f'/boardsByProject/{project_id}',
            params={"user_id": user_id},
            headers={
                'accept': 'application/json',
            }
        )
        return boards.json()

    def board_to_user(self, user_id: int, board_id: str):
        boards = requests.post(
            url=self.API_URL + f'/boardsToUser',
            params={"user_id": user_id,
                    "board_id": board_id},
            headers={
                'accept': 'application/json',
            }
        )
        return boards.json()


board_service = BoardsServise()
