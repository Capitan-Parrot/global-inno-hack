from core.database import session
from models.users import UserDB

from services.spaces import space_service
from fastapi import APIRouter


spaces_router = APIRouter(prefix='/spaces', tags=['spaces'])


@spaces_router.get('/spacesByUserId/{user_id}')
async def get_spaces_by_user_id(user_id: int):
    """
    Get spaces by user_id
    User_id - id from messager
    """
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    spaces = space_service.get_spaces_by_user_id(email)
    return spaces


@spaces_router.get('/{space_id}')
def get_spaces_by_id(user_id: int, space_id: str):
    """
    Get spaces by id
    """
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    spaces = space_service.get_spaces_by_id(email=email, space_id=space_id)
    return spaces
