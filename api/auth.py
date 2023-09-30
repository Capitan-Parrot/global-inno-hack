from fastapi import APIRouter, HTTPException
from starlette import status

from core.database import session
from services.auth import auth_service
from models.users import UserDB


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get('/')
def sign_in(user_id: int, email: str, password: str):
    user = session.query(UserDB).filter_by(email=email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь уже существует",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = UserDB(email=email, user_id=user_id)
    session.add(user)
    session.commit()
    return auth_service.sign_in(email, password)
