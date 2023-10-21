from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from services.users import users_services
from schemes.tasks import TaskChangeColumn, CreateTask
from services.tasks import tasks_service


tasks_router = APIRouter(prefix='/tasks', tags=['tasks'])


@tasks_router.get('/tasksByBoard/{task_id}', status_code=status.HTTP_200_OK)
async def get_task_by_id(user_id: int,  task_id: str):
    """
    Get tasks by id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    tasks = tasks_service.get_task_by_id(email=email, task_id=task_id)
    if not tasks:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return tasks


@tasks_router.get(
        '/getTasksByColumn/{column_id}',
        status_code=status.HTTP_200_OK
)
async def get_task_by_column(user_id: int, column_id: str):
    """
    Get task by column id
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    tasks = tasks_service.get_tasks_by_column_id(
        email=email,
        column_id=column_id
    )
    if not tasks:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return tasks


@tasks_router.post('/change_column', status_code=status.HTTP_201_CREATED)
async def change_column(user_id: int, request: TaskChangeColumn):
    """
    Change status of task
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    task = tasks_service.change_task_column(
        email=email,
        task_id=request.task_id,
        column_id=request.column_id
    )
    return task


@tasks_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_task(user_id: int, request: CreateTask):
    """
    Create a task
    """
    email = users_services.get_user_by_user_id(user_id=user_id).email
    task = tasks_service.create_task(
        email=email,
        name=request.name,
        description=request.description,
        column_id=request.columnId,
        users=request.users,
    )
    return task
