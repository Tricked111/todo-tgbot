""" todo telgram bot 
autor: Tricked111 """

from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot import types,TeleBot
from src.keybord import generate_start_button
from src.database import create_connect,create_cursor,create_table,insert_data,today_task
import src.database as database
import sqlite3
import src.keybord as key
import datetime

API_TOKEN = ""
bot = TeleBot(API_TOKEN)
id : types.Message
curs : sqlite3.Cursor





@bot.message_handler(commands = ['start'])
def start_command_handler(message: types.Message):
    global id,curs
    id = message
    curs = create_cursor(id)
    create_table(curs)
    
    bot.send_message(message.chat.id,
                     f"Hello {message.from_user.first_name}" 
                     "\nThis is TODO bot for you."
                     "\nPress /todo to start.")

@bot.message_handler(commands = ['todo'])
def todo_command_handler(message: types.Message):
    bot.send_message(message.chat.id,'Menu:\n1.View tasks\n2.Create task\n3.View calendar',reply_markup=generate_start_button())

@bot.message_handler(content_types=['text'])
def start_command(message : types.Message):
    if message.text == "1":
        pass
        show_tasks(message) 
    if message.text == "2":
        msg = bot.send_message(message.chat.id,"Write task",reply_markup=key.back_button())
        bot.register_next_step_handler(msg,create_task)
    if message.text == "3":
         bot.send_message(message.chat.id,"3tut")
    if message.text == "Back to menu":
        todo_command_handler(message)




def show_tasks(message: types.Message):
    global curs
    
    bot.send_message(message.chat.id,"Task list",reply_markup=key.back_button())
    bot.send_message(message.chat.id,f"Today:\n{today_task(curs)}")
    




def create_task(message : types.Message):
    if message.text == "Back to menu":
        todo_command_handler(message)
    else:
        bot.send_message(message.chat.id,
                        f"Today",reply_markup=key.edit_date())
        bot.send_message(message.chat.id,
                        f"{message.text}",
                        reply_markup=key.confirm_button())



@bot.callback_query_handler(func=lambda call : call.data == "edit")
def back_to_edit(call : types.CallbackQuery):
    msg = bot.send_message(call.message.chat.id,"Write task")
    bot.register_next_step_handler(msg,create_task)


@bot.callback_query_handler(func=lambda call : call.data == "confirm")
def confirm(call : types.CallbackQuery):
    global curs
    insert_data(curs,datetime.date.today(),call.message.text)
    bot.send_message(call.message.chat.id,"Task was addet!!")
    todo_command_handler(call.message)

@bot.callback_query_handler(func=lambda call : call.data == "edit_date")
def back_to_edit(call : types.CallbackQuery):
    pass



if __name__ == "__main__":
    bot.infinity_polling()