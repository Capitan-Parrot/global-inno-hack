from fastapi import APIRouter

from core.database import session
from models.users import UserDB
from services.users import users_services

users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.get('/{flame_user_id}')
def get_user_by_id(user_id: int, flame_user_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    return users_services.get_user_by_id(email=email, user_id=flame_user_id)
