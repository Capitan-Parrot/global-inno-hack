from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from services.users import users_services
from services.projects import project_service


projects_router = APIRouter(prefix='/project', tags=['project'])


@projects_router.get(
        "/projectsBySpace/{space_id}",
        status_code=status.HTTP_200_OK
)
def get_project_by_space_id(user_id: int, space_id: str):
    """
    Get ptoject by space_id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    projects = project_service.get_project_by_space_id(
        email=email,
        space_id=space_id
    )
    if not projects:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return projects


@projects_router.get('/{project_id}', status_code=status.HTTP_200_OK)
def get_project_by_id(user_id: int, project_id: str):
    """
    Get project by id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    projects = project_service.get_project_by_id(
        email=email,
        project_id=project_id,
    )
    if not projects:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return projects
