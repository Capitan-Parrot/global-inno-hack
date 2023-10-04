from sqlalchemy import Column, Integer, String

from .base import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    email = Column(String)
