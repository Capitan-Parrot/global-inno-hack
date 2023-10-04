from fastapi import APIRouter

from core.database import session
from services.auth import auth_service
from models.users import UserDB
from schemes.users import SignInRequest


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post('/')
def sign_in(user_id: int, request: SignInRequest):
    """
        Sign in by email and password
    """
    user = session.query(UserDB).filter_by(user_id=user_id).first()
    if not user:
        user = UserDB(email=request.email, user_id=user_id)
        session.add(user)
    tokens = auth_service.sign_in(request.email, request.password)
    session.commit()
    return tokens
