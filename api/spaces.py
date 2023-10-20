from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from services.users import users_services
from services.spaces import space_service


spaces_router = APIRouter(prefix='/spaces', tags=['spaces'])


@spaces_router.get('/spacesByUserId/{user_id}', status_code=status.HTTP_200_OK)
async def get_spaces_by_user_id(user_id: int):
    """
    Get spaces by user_id
    User_id - id from messager
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    spaces = space_service.get_spaces_by_user_id(email)
    if not spaces:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return spaces


@spaces_router.get('/{space_id}', status_code=status.HTTP_200_OK)
def get_spaces_by_id(user_id: int, space_id: str):
    """
    Get spaces by id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    spaces = space_service.get_spaces_by_id(email=email, space_id=space_id)
    if not spaces:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return spaces
