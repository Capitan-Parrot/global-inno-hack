from fastapi import APIRouter

from core.database import session
from models.users import UserDB
from schemes.tasks import TaskChangeColumn, CreateTask
from services.tasks import tasks_service


tasks_router = APIRouter(prefix='/tasks', tags=['tasks'])


@tasks_router.get('/tasksByBoard/{task_id}')
async def get_task_by_id(user_id: int,  task_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    tasks = tasks_service.get_task_by_id(email=email, task_id=task_id)

    return tasks


@tasks_router.get('/getTasksByColumn/{column_id}')
async def get_task_by_column(user_id: int, column_id: str):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    tasks = tasks_service.get_tasks_by_column_id(
                                    email=email,
                                    column_id=column_id
                                    )
    return tasks


@tasks_router.post('/change_column')
async def change_column(user_id: int, request: TaskChangeColumn):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    task = tasks_service.change_task_column(
                                email=email,
                                task_id=request.task_id,
                                column_id=request.column_id
                            )
    return task


@tasks_router.post('/create')
async def create_task(user_id: int, request: CreateTask):
    email = session.query(UserDB).filter_by(user_id=user_id).first().email
    task = tasks_service.create_task(
        email=email,
        name=request.name,
        description=request.description,
        column_id=request.column_id,
        users=request.users,
    )
    return task
