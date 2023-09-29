from sqlalchemy import Column, Integer, String, Boolean

from .base import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    chat_id = Column(Integer)

    