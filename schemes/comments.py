from pydantic import BaseModel


class CreateComment(BaseModel):
    task_id: str
    text_message: str
