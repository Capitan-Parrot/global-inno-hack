import telebot as telebot
from telebot import types

from config import config
from services.auth import auth_service
from services.spaces import space_service

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
    elif message.text == 'my-spaces':
        my_spaces(message)


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


@bot.message_handler(commands=['my-spaces'])
def my_spaces(message):
    spaces = space_service.get_spaces_by_user_id(message.chat.id)
    keyboard = []
    for space in spaces:
        keyboard.append(telebot.types.InlineKeyboardButton(space["name"], callback_data=space["id"]))
    markup.keyboard = keyboard
    bot.send_message(message.chat.id, reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)