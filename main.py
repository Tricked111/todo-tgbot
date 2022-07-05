""" todo telgram bot 
autor: Tricked111 """

from email import message
from telebot import types,TeleBot
from datetime import date, datetime
from src.keybord import generate_start_button,generate_create_task_req
from src.database import create_connect,create_cursor,create_table,insert_data,print_select
import src.database as database
import sqlite3
import src.keybord as key


API_TOKEN = "5597070596:AAEgZMwOzZLp7IQHqurC0BUi7m5I8wrcm9w"
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
    bot.send_message(message.chat.id,'Task list',reply_markup=generate_start_button())


@bot.callback_query_handler(func=lambda call: True)
def task_manage(call: types.CallbackQuery):
    global id,curs
    if call.data == "view":
        bot.send_message(call.message.chat.id,f'View task: {print_select(curs)}')

    elif call.data == "create":
        msg = bot.send_message(call.message.chat.id,'Send task',reply_markup=generate_create_task_req())
        bot.register_next_step_handler(msg,write_task)
    
    elif call.data == "cal":
        bot.send_message(call.message.chat.id,'cal TODO')
   
    elif call.data == "back_to_start":
        todo_command_handler(id)
    
    elif call.data == "back_to_write":
        msg = bot.send_message(call.message.chat.id,'Send task',reply_markup=generate_create_task_req())
        bot.register_next_step_handler(msg,write_task)
    
    elif call.data == "confirm":
        bot.send_message(call.message.chat.id,f"Apply to task list\n\n{call.message.text}")
        insert_data(curs,"date.today()",call.message.text)
        todo_command_handler(id)

def write_task(message : types.Message):
    bot.send_message(message.chat.id,f'Today: {message.text}',reply_markup=key.create_confirm())









""" @bot.message_handler(content_types = ["text"])
def task_list(message : types.Message):
    curs = create_cursor(message)
    if message.text == "view task":
        #x = datetime.datetime(2020, 5, 17)
        #print(x)
        #insert_data(curs,f"{x}",'asd')
        bot.send_message(message.chat.id,"V")    
        pass
    elif message.text == "create task":
        msg = bot.send_message(message.chat.id,"Write task",reply_markup=generate_create_task_req())
        #bot.reply_to
        #bot.edit_message_reply_markup(message.chat.id,None,reply_markup = key.test())
        #bot.edit_message_reply_markup()
        #bot.register_next_step_handler(msg,write_task)
    elif message.text == "view calendar":
        pass
    else:
        bot.send_message(message.chat.id,"None")    

def write_task(message : types.Message):
    pass
    #bot.edit_message_reply_markup(message.chat.id,message.id,reply_markup = key.test())
    #pass
    #now = date.today()
    #print(now)
    #bot.send_message(message.chat.id, f"Task:\nTodaty: {message.text}",reply_markup = generate_create_task_req())
    #bot.send_message(message.chat.id,None,reply_markup = generate_start_button()) """




if __name__ == "__main__":
    #curs = sqlite3.connect(f"src/test.db")
    #c = curs.cursor()
    #create_table(c)
    #insert_data(c,"date.today()","call.message.text")
    #print(print_select(c))


    bot.polling()