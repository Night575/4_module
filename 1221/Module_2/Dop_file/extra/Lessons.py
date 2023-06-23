from telebot import TeleBot
from telebot.types import (Message,
                           ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
import random

bot  = TeleBot("5616239671:AAGI251N-5UlbYZ9hKUwvEhALJZZFNaihCI")
BASE_FILE_DIR = r"C:\PycharmProject\1221\Dop_file\extra"

def game_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    button1 = KeyboardButton("/шутеры")
    button2 = KeyboardButton("/стратегии")
    button3 = KeyboardButton("/симуляторы")
    button4 = KeyboardButton("/гонки")
    button5 = KeyboardButton("/назад")

    keyboard.add(button1, button2, button3, button4, button5)

    return keyboard




def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn1 = KeyboardButton("/cats")
    btn2 = KeyboardButton("/poem")
    btn3 = KeyboardButton("/stickers")
    btn4 = KeyboardButton("/music")
    btn5 = KeyboardButton("/games")
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    return keyboard

@bot.message_handler(commands=["start", "help"])
def welcome(message: Message):
    keyboard = welcome_keyboard()
    bot.send_message(message.from_user.id, "Привет!Выбери следующие команды:", reply_markup=keyboard)


@bot.message_handler(commands=["cats"])
def cats(message: Message):
    random_img_number = random.randint(1, 9)
    random_img = open(fr"{BASE_FILE_DIR}\{random_img_number}.jpg", "rb")
    bot.send_photo(message.from_user.id, random_img)

@bot.message_handler(commands=["music"])
def music(message: Message):
    audio = open(fr"{BASE_FILE_DIR}\happy.mp3", "rb")
    bot.send_audio(message.from_user.id, audio)

@bot.message_handler(commands=["poem"])
def poem(message: Message):
    bot.send_message(message.from_user.id, "Села муха на варенье, вот и все стихотворенье!")
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="Перейте", url="https://stihi.ru")
    keyboard.add(button)
    bot.send_message(message.from_user.id, "Больше стихотворений здесь:", reply_markup=keyboard)


@bot.message_handler(commands=["stickers"])
def stickers(message: Message):
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEG-Btjpcs2ZXzBjfTj6ddsRN7_s7DHSQAC7SEAAhJfMUnrzNRmv8hqiSwE")


@bot.message_handler(commands=["games"])
def Games(message: Message):
    keyboard = game_keyboard()
    bot.send_message(message.from_user.id, "Выберите жанр:", reply_markup=keyboard)

@bot.message_handler(commands=["шутеры"])
def shooter(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton(text="Team Fortress 2",
                                    url="https://store.steampowered.com/app/440/Team_Fortress_2/")
    button_2 = InlineKeyboardButton(text="PUBG: BATTLEGROUNDS",
                                    url="https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/")
    button_3 = InlineKeyboardButton(text="DayZ", url="https://store.steampowered.com/app/221100/DayZ/")
    keyboard.add(button_1, button_2, button_3)

    bot.send_message(message.from_user.id, "Переходи и играй!", reply_markup=keyboard)

@bot.message_handler(commands=["стратегии"])
def strategi(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton(text="Hearts of Iron IV", url="https://store.steampowered.com/app/394360/Hearts_of_Iron_IV/")
    button_2 = InlineKeyboardButton(text="Cities: Skylines", url="https://store.steampowered.com/app/255710/Cities_Skylines/")
    keyboard.add(button_1, button_2)

    bot.send_message(message.from_user.id, "Переходи и играй!", reply_markup=keyboard)


@bot.message_handler(commands=["симуляторы"])
def simulators(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton(text="Euro Truck Simulator 2", url="https://store.steampowered.com/app/227300/Euro_Truck_Simulator_2/")
    button_2 = InlineKeyboardButton(text="SnowRunner", url="https://store.steampowered.com/app/1465360/SnowRunner/")
    keyboard.add(button_1, button_2)

    bot.send_message(message.from_user.id, "Переходи и играй!", reply_markup=keyboard)


@bot.message_handler(commands=["гонки"])
def race(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton(text="Assetto Corsa", url="https://store.steampowered.com/app/244210/Assetto_Corsa/")
    button_2 = InlineKeyboardButton(text="BeamNG.drive", url="https://store.steampowered.com/app/284160/BeamNGdrive/")
    keyboard.add(button_1, button_2)

    bot.send_message(message.from_user.id, "Переходи и играй!", reply_markup=keyboard)



@bot.message_handler(commands=["назад"])
def back(message: Message):
    welcome(message)





bot.polling()
