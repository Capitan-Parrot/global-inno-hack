from fastapi import APIRouter

from core.database import session
from services.auth import auth_service
from models.users import UserDB


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get('/')
def sign_in(user_id: int, email: str, password: str):
    return auth_service.sign_in(user_id, email, password)
