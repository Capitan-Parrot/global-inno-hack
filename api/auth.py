from fastapi import APIRouter
from fastapi import status
from core.database import session
from services.auth import auth_service
from services.users import users_services
from models.users import UserDB
from schemes.users import SignInRequest
from schemes.tokens import TokenDBScheme


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post('/', status_code=status.HTTP_200_OK)
def sign_in(user_id: int, request: SignInRequest) -> TokenDBScheme:
    """
        Sign in by email and password
    """
    user = users_services.get_user_by_user_id(user_id=user_id)
    if not user:
        user = UserDB(email=request.email, user_id=user_id)
        session.add(user)
    response_token = auth_service.sign_in(request.email, request.password)
    token = TokenDBScheme(
        email=user.email,
        refresh_token=response_token["tokens"]["refreshToken"]["token"],
        access_token=response_token["tokens"]["accessToken"]["token"]
    )
    session.commit()
    return token
