from fastapi import APIRouter

from core.database import session
from services.projects import project_service
from models.users import UserDB


api_router = APIRouter(prefix='/project', tags=['project'])


@api_router.get("/projectsBySpace/{space_id}")
def get_projects_by_space_id(user_id: int, space_id: str):
    '''
    user_id - id of user in current messanger system
    
    space_id 
    
    return list of projects
    '''
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    projects = project_service.get_project_by_space_id(email, space_id)
    return projects
