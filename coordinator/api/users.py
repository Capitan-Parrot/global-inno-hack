from fastapi import FastAPI, APIRouter


users_router = APIRouter(prefix='user', tags=['user'])
