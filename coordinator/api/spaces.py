from core.database import session
from models.users import UserDB

from services.spaces import space_service
from fastapi import FastApi, APIRouter


router = APIRouter(prefix='/spaces', tags=['spaces'])

@router.get('/spacesByUserId/{user_id}')
async def get_spaces_by_user_id(user_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    spaces = space_service.get_spaces_by_user_id(email)

    return spaces