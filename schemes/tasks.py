from pydantic import BaseModel


class TaskChangeColumn(BaseModel):
    task_id: str
    column_id: str


class CreateTask(BaseModel):
    name: str
    description: str | None
    columnId: str
    users: list[str] | None
