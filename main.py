""" todo telgram bot 
autor: Tricked111 """

from telebot import types,TeleBot
from datetime import date
from src.keybord import generate_start_button 
from src.database import create_connect,create_cursor,create_table,insert_data
import src.database as database
import sqlite3


API_TOKEN = ""
bot = TeleBot(API_TOKEN)


@bot.message_handler(commands = ['start'])
def start_command_handler(message: types.Message):
    bot.send_message(message.chat.id,
                     f"Hello {message.from_user.first_name}" 
                     "\nThis is TODO bot for you."
                     "\nPress /todo to start.")



@bot.message_handler(commands = ['todo'])
def todo_command_handler(message: types.Message):
    curs = create_cursor(message)
    
    #delete
    database.drop_table(curs)
    #delete
    
    
    create_table(curs)
    bot.send_message(message.chat.id,'Task list',reply_markup=generate_start_button())

@bot.message_handler(content_types = ["text"])
def task_list(message : types.Message):
    if message.text == "view task":
        bot.send_message(message.chat.id,"You are here!")



@bot.message_handler(content_types = ["text"])
def task_list(message : types.Message):
    curs = create_cursor(message)
    if message.text == "view task":
        insert_data(curs,"asd","ASD")
        bot.send_message(message.chat.id,f"{database.print_select(curs)}")


if __name__ == "__main__":
    bot.polling()