import requests
from sqlalchemy.orm import Session
import random

my_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZGlvbnpha3JhdWxza2lqQGdtYWlsLmNvbSIsInVzZXJJZCI6IjY1MTJmOWVmODc5OTgyYzIwZjBhNGExZiIsImlhdCI6MTY5NjA1NTgwNCwiZXhwIjoxNjk2MzU1ODA0fQ.im7Mi9N-e79mF3kedbKFJeYcuSl7Sk9kj6yfo3bJ4s8"


class SpaceService():
    API_URL = 'https://api.teamflame.ru/space'
    token = my_access_token

    def spaces_by_user_id(self, db: Session=None, user_id: int=None):
        '''
        Get list of spaces, created by user or smth like that
        '''
        
        spaces = requests.get(
            url=self.API_URL + '/spacesByUserId',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }
        )
        return spaces.json()
    
    def get_sidebar_data(self, db: Session=None, user_id: str=None):
        '''
        List of all spaces where the user is
        '''
        spaces = requests.get(
            url=self.API_URL + '/get-sidebar-data',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }
        ).json()

        print('Your spaces:')
        

        for _space in spaces:
            print(_space['name'], _space['id'])
            
        return spaces
    

    def get_all_space_tasks(self, id: str=None):

        space_id = "65172175f074f999078a6e3d"

        spaces = requests.get(
            url=self.API_URL + '/get-all-space-tasks/' + space_id,
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }
        ).json()

        return spaces
    

    def create(self, members: list, name: str="Test Space"):
        '''
        Create space where members is list of emails 
        '''
        result= requests.post(
            url=self.API_URL + '/create',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            },
            data={
                "name": name,
                "logo": "",
                "color": "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)]),
                "invites": members
            }
        ).json()

        return result
    
    def update_space(self):
        '''
        Update main info about space
        '''
 
        result= requests.post(
            url=self.API_URL + '/update' + '65172175f074f999078a6e3d',
            headers={
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            },
            # data={
            #     "name": name,
            #     "logo": logo,
            #     "color": color,
            #     "desription": desription
            # }
        ).json()

        return result
    



invites =  [
    "rodionzakraulskij@gmail.com",

]

ss = SpaceService()
result = ss.update_space()

print(result)

# space_id = result['id']

