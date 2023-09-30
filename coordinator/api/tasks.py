from core.database import session
from models.users import UserDB

from services.tasks import tasks_service
from fastapi import FastApi, APIRouter


tasks_router = APIRouter(prefix='/boards', tags=['boards'])

@tasks_router.get('/tasksByBoard/{task_id}')
async def get_task_by_id(user_id: str,  task_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    tasks = tasks_service.get_task_by_id(email = email, task_id = task_id)

    return tasks