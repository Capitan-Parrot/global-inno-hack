from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from services.columns import columns_service
from services.users import users_services


columns_router = APIRouter(prefix="/columns", tags=["columns"])


@columns_router.get('getByBoard/{board_id}', status_code=status.HTTP_200_OK)
def get_column_by_id(user_id: int, board_id: str):
    """
    Get column by board_id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    columns = columns_service.get_columns_by_board_id(
        email=email,
        board_id=board_id
    )
    if not columns:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return columns
