from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from core.database import session
from models import BoardDB
from services.users import users_services
from services.boards import board_service


boards_router = APIRouter(prefix='/board', tags=['board'])


@boards_router.get('/boardsByProject/{project_id}',
                   status_code=status.HTTP_200_OK
                   )
def get_board_by_project_id(user_id: int, project_id: str):
    """
    Get board by project_id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    boards = board_service.get_board_by_project_id(
        email=email,
        project_id=project_id
    )
    if not boards:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return boards


@boards_router.get('/boardsByUser',
                   )
def get_board_by_user_id(user_id: int):
    """
    Get board by user_id
    User_id - id from message
    """
    board = board_service.get_board_by_user_id(user_id=user_id)
    if not board:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return board


@boards_router.get('/{board_id}', status_code=status.HTTP_200_OK)
async def get_board_by_id(user_id: int, board_id: str):
    """
    Get board by id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    board = board_service.get_board_by_id(email=email, board_id=board_id)
    if not board:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return board


@boards_router.post('/boardsToUser', status_code=status.HTTP_201_CREATED)
async def create_board_to_user(user_id: int, board_id: str):
    """
    Create board to user
    """
    board = board_service.get_board_by_user_id(user_id=user_id)
    if not board:
        board = BoardDB(user_id=user_id, board_id=board_id)
    board.board_id = board_id
    session.add(board)
    session.commit()
    return board
