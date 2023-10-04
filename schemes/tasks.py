from pydantic import BaseModel


class TaskChangeColumn(BaseModel):
    task_id: str
    column_id: str


class CreateTask(BaseModel):
    name: str
    description: str | None
    column_id: str
    users: list[str] | None
