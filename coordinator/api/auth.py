from fastapi import FastApi, APIRouter

app = FastApi()
api_router = APIRouter()

@api_router.get()
