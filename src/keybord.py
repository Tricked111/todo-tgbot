from ctypes import resize
from gc import callbacks
from unittest.mock import call
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton


EMTPY_FIELD = '1'

def generate_start_button():
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    keybord.add(*[KeyboardButton(f"{i}") for i in range (1,4)])
    return keybord

def back_button():
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    keybord.add(KeyboardButton("Back to menu"))
    return keybord


def confirm_button():
    keybord = InlineKeyboardMarkup()
    keybord.add(InlineKeyboardButton("Edit",callback_data="edit"),
                InlineKeyboardButton("Confirm",callback_data="confirm"))
    return keybord


def edit_date():
    keybord = InlineKeyboardMarkup()
    keybord.add(InlineKeyboardButton("Edit date",callback_data="edit_date"))
    return keybord

def create_confirm():
    keybord = InlineKeyboardMarkup()

    keybord.add(InlineKeyboardButton("edit",callback_data = "back_to_write"),InlineKeyboardButton("confirm",callback_data = "confirm"))
    keybord.add(InlineKeyboardButton("change date",callback_data = "change_date"))
    
    return keybord