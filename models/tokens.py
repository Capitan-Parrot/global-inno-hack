from sqlalchemy import Column, Integer, String, Boolean

from .base import Base


class TokenDB(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer)
    refresh_token = Column(String)
    access_token = Column(String)

