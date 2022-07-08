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



""" def confirm_or_edit(message: types.Message):
    global curs
    if message.text == "Edit":
        msg = bot.send_message(message.chat.id,"Write task",reply_markup=key.back_button())
        bot.register_next_step_handler(msg,create_task)
    if message.text == "Confirm":
        #insert_data(curs,f"{text}")
        todo_command_handler(message) """


""" @bot.message_handler(commands = ['todo'])
def todo_command_handler(message: types.Message):
    bot.send_message(message.chat.id,'Task list',reply_markup=generate_start_button())
    


@bot.callback_query_handler(func=lambda call: call.data == "view")
def view_state(call : types.CallbackQuery):
    pass



@bot.callback_query_handler(func=lambda call: call.data == "create")
def create_stae(call : types.CallbackQuery):
    msg = bot.send_message(call.message.chat.id,'Send task',reply_markup=generate_create_task_req())
    bot.register_next_step_handler(msg,write_task)

    #if call.data == "back_menu":
    #    bot.send_message(call.message.chat.id, "TEST")

def write_task(message : types.Message):
    bot.send_message(message.chat.id,f'Today: {message.text}',reply_markup=key.create_confirm())
    #bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
    #                      text=f'Today: {message.text}', reply_markup=key.create_confirm())

@bot.callback_query_handler(func=lambda call: call.data == "cal")
def cal_state(call : types.CallbackQuery):
    pass


@bot.callback_query_handler(func=lambda call:True)
def back(call : types.CallbackQuery):
    if call.data == "back_to_start":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Task list:', reply_markup=generate_start_button()) """
    



""" @bot.callback_query_handler(func=lambda call: True)
def task_manage(call: types.CallbackQuery):
    global id,curs
    if call.data == "view":
        bot.send_message(call.message.chat.id,f'View task: {print_select(curs)}')

    elif call.data == "create":
        msg = bot.send_message(call.message.chat.id,'Send task',reply_markup=generate_create_task_req())
        bot.register_next_step_handler(msg,write_task)
    
    #elif call.data == "cal":
    #    bot.send_message(call.message.chat.id,'cal TODO')
   
    elif call.data == "back_to_start":
        bot.send_message(call.message.chat.id,"Main menu")
        todo_command_handler(id)
    
    elif call.data == "back_to_write":
        msg = bot.send_message(call.message.chat.id,'Send task',reply_markup=generate_create_task_req())
        bot.register_next_step_handler(msg,write_task)
    
    elif call.data == "confirm":
        bot.send_message(call.message.chat.id,f"Apply to task list\n\n{call.message.text}")
        insert_data(curs,call.message.text)
        todo_command_handler(id)

def write_task(message : types.Message):
    bot.send_message(message.chat.id,f'Today: {message.text}',reply_markup=key.create_confirm()) """









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
    bot.infinity_polling()