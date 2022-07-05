from ctypes import resize
from gc import callbacks
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton


EMTPY_FIELD = '1'

def generate_start_button():
    keybord = InlineKeyboardMarkup(row_width=2)#,one_time_keyboard = True)
    
    keybord.add(InlineKeyboardButton("view task",callback_data="view"),
                InlineKeyboardButton("create task",callback_data="create"))
    
    keybord.add(InlineKeyboardButton("view calendar",callback_data="cal"))

    return keybord


def generate_create_task_req():
    keybord = InlineKeyboardMarkup()
    #keybord_screen = ReplyKeyboardMarkup(resize_keyboard = True)

    #keybord_screen.add(KeyboardButton("todo"),KeyboardButton("todo"),KeyboardButton("todo"))

    keybord.add(InlineKeyboardButton("back",callback_data = "back_to_start"))
    
    return keybord

def create_confirm():
    keybord = InlineKeyboardMarkup()

    keybord.add(InlineKeyboardButton("edit",callback_data = "back_to_write"),InlineKeyboardButton("confirm",callback_data = "confirm"))
    keybord.add(InlineKeyboardButton("change date",callback_data = "change_date"))
    
    return keybord