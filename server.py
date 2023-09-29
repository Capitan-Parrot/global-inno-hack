import asyncio as asyncio
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
import bot
from config import config

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello from root!"}


if __name__ == "__main__":
    uvicorn.run(
        'app.__main__:app',
        host=config.server_host,
        port=config.server_port,
        reload=True
    )
    asyncio.run(bot.start_polling())