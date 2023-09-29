import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import WebAppInfo

from config import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Web', web_app=WebAppInfo(url="https://teamflame.ru/"))
        ],
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("https://teamflame.ru/", reply_markup=markup)


# Запуск процесса поллинга новых апдейтов
async def start_polling():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_polling())