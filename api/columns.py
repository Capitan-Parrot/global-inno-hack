from fastapi import APIRouter

from services.columns import columns_service
from core.database import session
from models.users import UserDB


columns_router = APIRouter(prefix="/columns", tags=["columns"])


@columns_router.get('getByBoard/{board_id}')
def get_column_by_id(user_id: int, board_id: int):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    return columns_service.get_columns_by_board_id(email=email,
                                                   board_id=board_id
                                                   )
