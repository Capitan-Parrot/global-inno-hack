import telebot as telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove

from config import config
from services.auth import auth_service
from services.projects import project_service
from services.spaces import space_service
from services.boards import boards as board_service

# Объект бота
bot = telebot.TeleBot(token=config.bot_token.get_secret_value())


@bot.message_handler(commands=['start'])
def start(message):
    itembtn = telebot.types.InlineKeyboardButton('Войти в аккаунт TeamFlame')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(itembtn)
    bot.send_message(message.chat.id, """
Это бот Team Flame!

Мои пространства - посмотреть рабочие пространства""", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'Войти в аккаунт TeamFlame':
        sign_in(message)
    elif message.text == 'Мои пространства':
        my_spaces(message)


@bot.message_handler(commands=['Войти в аккаунт TeamFlame'])
def sign_in(message):
    bot.send_message(message.chat.id, "Please enter your email:", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, ask_password)


def ask_password(message):
    email = message.text
    bot.send_message(message.chat.id, "Please enter your password:")
    bot.register_next_step_handler(message, save_data, email)


def save_data(message, email):
    try:
        password = message.text
        tokens = auth_service.sign_in(message.from_user.id, email, password)
        itembtn = telebot.types.InlineKeyboardButton('Мои пространства')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(itembtn)
        bot.send_message(message.chat.id, "Вы успешно авторизованы")
        my_spaces(message)
    except KeyError:
        bot.send_message(message.chat.id, "User was not found. Please try again")
        bot.register_next_step_handler(message, start)


@bot.message_handler(commands=['Мои пространства'])
def my_spaces(message):

    spaces = space_service.get_spaces_by_user_id(message.from_user.id)
    markup = telebot.types.ReplyKeyboardMarkup()
    name_to_id = {}
    for space in spaces:
        markup.add(telebot.types.InlineKeyboardButton(text=space["name"]))
        name_to_id[space["name"]] = space["id"]
    bot.send_message(message.chat.id, "Ваши пространства:", reply_markup=markup)
    bot.register_next_step_handler(message, my_projects, name_to_id)


def my_projects(message, name_to_id):
    space_name = message.text
    space_id = name_to_id[space_name]
    projects = project_service.get_project_by_space_id(message.from_user.id, space_id)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    name_to_id = {}
    for project in projects:
        markup.add(telebot.types.InlineKeyboardButton(project["name"]))
        name_to_id[project["name"]] = project["id"]
    bot.send_message(message.chat.id, "Ваши проекты:", reply_markup=markup)
    bot.register_next_step_handler(message, my_boards, name_to_id)


def my_boards(message, name_to_id):
    if message.text == "Вернуться к пространствам":
        return my_spaces(message)
    project_name = message.text
    project_id = name_to_id[project_name]
    boards = board_service.get_board_by_project_id(message.from_user.id, project_id)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    name_to_id = {}
    for board in boards:
        markup.add(telebot.types.InlineKeyboardButton(board["name"]))
        name_to_id[board["name"]] = board["id"]
    bot.send_message(message.chat.id, "Ваши доски:", reply_markup=markup)
    bot.register_next_step_handler(message, get_tasks, name_to_id)


def get_tasks(message, name_to_id):
    board_name = message.text
    board_id = name_to_id[board_name]
    keyboard = types.InlineKeyboardMarkup()  # создаем клавиатуру
    webAppTest = types.WebAppInfo("https://useful-kite-settled.ngrok-free.app", user_id=message.from_user.id, board_id=board_id)  # создаем webappinfo - формат хранения url
    one_button = types.InlineKeyboardButton(text="Тестовая страница", web_app=webAppTest)  # создаем кнопку типа webapp
    keyboard.add(one_button)
    bot.send_message(message.chat.id, "Тестовая страница", reply_markup=keyboard)


if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
