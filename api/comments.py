from fastapi import APIRouter

from core.database import session
from models.users import UserDB
from services.comments import comments_service
from schemes.comments import CreateComment


comments_router = APIRouter(prefix='/comments', tags=['comments'])


@comments_router.post('/')
def create_comment(user_id: int, request: CreateComment):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    comment = comments_service.add_comment(
                            email=email,
                            task_id=request.task_id,
                            text_message=request.text_message,
                            )
    return comment
