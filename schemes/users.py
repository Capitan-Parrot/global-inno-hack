from pydantic import BaseModel


class SignInRequest(BaseModel):
    email: str
    password: str
