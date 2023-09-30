from fastapi import APIRouter

from core.database import session
from services.projects import project_service
from models.users import UserDB


api_router = APIRouter(prefix='/project', tags=['project'])


@api_router.get("/projectsBySpace/{space_id}")
def get_project_by_space_id(user_id: int, space_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    return project_service.get_project_by_space_id(
                                            email=email,
                                            space_id=space_id
                                            )
