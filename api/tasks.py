from core.database import session
from models.users import UserDB

from services.tasks import tasks_service
from fastapi import APIRouter


tasks_router = APIRouter(prefix='/tasks', tags=['tasks'])


@tasks_router.get('/tasksByBoard/{task_id}')
async def get_task_by_id(user_id: int,  task_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    tasks = tasks_service.get_task_by_id(email=email, task_id=task_id)

    return tasks


@tasks_router.get('/getTasksByColumn/{column_id}')
async def get_task_by_column(user_id: int, column_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    tasks = tasks_service.get_tasks_by_column_id(email=email, column_id=column_id)
    return tasks


