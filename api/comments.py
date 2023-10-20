from fastapi import APIRouter
from fastapi import status
from services.users import users_services
from services.comments import comments_service
from schemes.comments import CreateComment


comments_router = APIRouter(prefix='/comments', tags=['comments'])


@comments_router.post('/', status_code=status.HTTP_201_CREATED)
def create_comment(user_id: int, request: CreateComment):
    """
    Create comment
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    comment = comments_service.add_comment(
        email=email,
        task_id=request.task_id,
        text_message=request.text_message,
    )
    return comment
