from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from services.users import users_services


users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.get('/{flame_user_id}', status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int, flame_user_id: str):
    """
    Get user by id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    user = users_services.get_user_by_id(email=email, user_id=flame_user_id)
    if not user:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return user
