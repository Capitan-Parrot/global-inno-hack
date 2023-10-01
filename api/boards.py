from core.database import session
from models import BoardDB
from models.users import UserDB

from services.boards import board_service
from fastapi import APIRouter


boards_router = APIRouter(prefix='/board', tags=['board'])


@boards_router.get('/boardsByProject/{project_id}')
async def get_board_by_project_id(user_id: int, project_id: str):
    """
    Get board by project_id
    """
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    boards = board_service.get_board_by_project_id(email=email,
                                                   project_id=project_id)
    return boards


@boards_router.get('/boardsByUser')
async def get_board_by_user_id(user_id: int):
    """
    Get board by user_id
    User_id - id from message
    """
    board = session.query(BoardDB).filter_by(user_id=user_id).first()
    return board.board_id


@boards_router.get('/{board_id}')
async def get_board_by_id(user_id: int, board_id: str):
    """
    Get board by id
    """
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    return board_service.get_board_by_id(email=email, board_id=board_id)


@boards_router.post('/boardsToUser')
async def create_board_to_user(user_id: int, board_id: str):
    """
    Create board to user
    """
    board = session.query(BoardDB).filter_by(user_id=user_id).first()
    if not board:
        board = BoardDB(user_id=user_id, board_id=board_id)
    session.add(board)
    session.commit()
    return board
