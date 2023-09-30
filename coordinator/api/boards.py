from core.database import session
from models.users import UserDB

from services.boards import board_service
from fastapi import FastApi, APIRouter


router = APIRouter(prefix='/boards', tags=['boards'])


@router.get('/boardsByProject/{id}')
async def get_board_by_project_id(user_id: int, project_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    boards = board_service.get_board_by_project_id(email, project_id)

    return boards


@router.post('/create')
async def create_board(user_id: int, name: str, space_id: str, project_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    result  = board_service.create_board(email, name, space_id, project_id)
    
    return result
