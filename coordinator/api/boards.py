from core.database import session
from models.users import UserDB

from services.boards import board_service
from fastapi import FastApi, APIRouter


router = APIRouter(prefix='/board', tags=['board'])


@router.get('/boardsByProject/{id}')
async def get_board_by_project_id(user_id: int, project_id: str):
    '''
    user_id - id of user in current messanger system

    project_id 

    Returns list of boards with information about them
    '''
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    boards = board_service.get_board_by_project_id(email, project_id)

    return boards

