from fastapi import APIRouter

from core.database import session
from services.projects import project_service
from models.users import UserDB


projects_router = APIRouter(prefix='/project', tags=['project'])


@projects_router.get("/projectsBySpace/{space_id}")
def get_project_by_space_id(user_id: int, space_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    return project_service.get_project_by_space_id(
                                            email=email,
                                            space_id=space_id
                                            )


@projects_router.get('/{project_id}')
def get_project_by_id(user_id: int, project_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    return project_service.get_project_by_id(
                                    email=email,
                                    project_id=project_id,
                                    )
