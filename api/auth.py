from fastapi import APIRouter

from core.database import session
from services.auth import auth_service
from models.users import UserDB
from models.tokens import TokenDB


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get('/')
def sign_in(user_id: int, email: str, password: str):
    user = session.query(UserDB).filter_by(user_id=user_id).first()
    if not user:
        user = UserDB(user_id=user_id, email=email)
        session.add(user)
        return auth_service.sign_in(email, password)
    token = session.query(TokenDB).filter_by(email=user.email).first().access_token
    return token
    
