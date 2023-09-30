from sqlalchemy import Column, Integer, String, Boolean

from .base import Base


class BoardDB(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    board_id = Column(String)
