from fastapi import APIRouter

from core.database import session
from services.auth import auth_service
from models.users import UserDB

<<<<<<< HEAD
@api_router.get()
async def a():
    pass
=======
api_router = APIRouter(prefix="/auth", tags=["auth"])


@api_router.get('/')
def sign_in(user_id: int, email: str, password: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    return auth_service.sign_in(email, password)
>>>>>>> 5015215601d75efd47783de213c792ae6725376d
