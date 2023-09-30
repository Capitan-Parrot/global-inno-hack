import telebot as telebot
from telebot import types

from config import config
from services.auth import auth_service

# Объект бота
bot = telebot.TeleBot(token=config.bot_token.get_secret_value())
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

@bot.message_handler(commands=['start'])
def start(message):
    itembtn = telebot.types.InlineKeyboardButton('sign-in')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "Welcome to my bot!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'sign-in':
        sign_in(message)


@bot.message_handler(commands=['sign-in'])
def sign_in(message):
    bot.send_message(message.chat.id, "Please enter your email:")
    bot.register_next_step_handler(message, ask_password)


def ask_password(message):
    email = message.text
    bot.send_message(message.chat.id, "Please enter your password:")
    bot.register_next_step_handler(message, save_data, email)


def save_data(message, email):
    password = message.text
    tokens = auth_service.sign_in(message.chat.id, email, password)
    itembtn = telebot.types.InlineKeyboardButton('sign-in')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "You are logged in", reply_markup=markup)



# Запуск процесса поллинга новых апдейтов

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)