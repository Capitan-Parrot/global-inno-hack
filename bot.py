import asyncio
import logging

import telebot as telebot

from config import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = telebot.TeleBot(token=config.bot_token.get_secret_value())


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn = telebot.types.KeyboardButton('Sign-In')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "Welcome to my bot!", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Sign-In':
        bot.send_message(message.chat.id, "Please enter your email:")
        bot.register_next_step_handler(message, ask_password)


def ask_password(message):
    email = message.text
    bot.send_message(message.chat.id, "Please enter your password:")
    bot.register_next_step_handler(message, print_data, email)


def print_data(message, email):
    password = message.text
    bot.send_message(message.chat.id, f"Email: {email}\nPassword: {password}")


# Запуск процесса поллинга новых апдейтов
async def start_polling():
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(start_polling())