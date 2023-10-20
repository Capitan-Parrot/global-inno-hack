from pydantic import BaseModel


class TokenDBScheme(BaseModel):
    email: str
    refresh_token: str
    access_token: str
