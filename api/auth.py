from fastapi import APIRouter

from core.database import session
from services.auth import auth_service
from models.users import UserDB
from models.tokens import TokenDB


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post('/')
def sign_in(user_id: int, email: str, password: str):
    user = session.query(UserDB).filter_by(user_id=user_id).first()
    if not user:
        user = UserDB(email=email, user_id=user_id)
        session.add(user)
    tokens = auth_service.sign_in(email, password)
    session.commit()
    return tokens
