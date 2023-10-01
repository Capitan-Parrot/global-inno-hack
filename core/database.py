from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config


def get_url():
    user = config.postgres_user
    password = config.postgres_password
    server = config.postgres_server
    db = config.postgres_db
    return f"postgresql://{user}:{password}@{server}/{db}"


engine = create_engine(get_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
