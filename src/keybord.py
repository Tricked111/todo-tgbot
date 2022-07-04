from gc import callbacks
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton


EMTPY_FIELD = '1'

def generate_start_button():
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    
    keybord.add(KeyboardButton("view task"),
                KeyboardButton("create task"))
    
    keybord.add( KeyboardButton("view calendar"))

    return keybord