from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from config import config
from api.main import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello from root!"}


if __name__ == "__main__":
    uvicorn.run(
        'server:app',
        host=config.server_host,
        port=config.server_port,
        reload=True
    )
