from fastapi import APIRouter, HTTPException
from starlette import status

from core.database import session
from services.auth import auth_service
from models.users import UserDB
from models.tokens import TokenDB


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get('/')
def sign_in(user_id: int, email: str, password: str):
    user = session.query(UserDB).filter_by(user_id=user_id).first()
    if user:
        return session.query(TokenDB).filter_by(email=user.email).first().access_token

    return auth_service.sign_in(user_id, email, password)
