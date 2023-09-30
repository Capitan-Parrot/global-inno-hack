import asyncio as asyncio
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from telegram.bot import bot
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


async def run_telebot():
    bot.infinity_polling(none_stop=True)


# Запустите Telebot в асинхронном режиме
telebot_task = asyncio.ensure_future(run_telebot())

if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host=config.server_host,
        port=config.server_port,
        reload=True
    )
