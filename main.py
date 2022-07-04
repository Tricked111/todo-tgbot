""" todo telgram bot 
autor: Tricked111 """

from telebot import types,TeleBot
from datetime import date
from src.keybord import generate_start_button 


API_TOKEN = "5597070596:AAEgZMwOzZLp7IQHqurC0BUi7m5I8wrcm9w"
bot = TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start_command_handler(message: types.Message):
    bot.send_message(message.chat.id,
                     f"Hello {message.from_user.first_name}" 
                     "\nThis is TODO bot for you."
                     "\nPress /todo to start.")

@bot.message_handler(commands = ['todo'])
def todo_command_handler(message: types.Message):
    bot.send_message(message.chat.id,'Task list',reply_markup=generate_start_button())

@bot.message_handler(content_types = ["text"])
def task_list(message : types.Message):
    if message.text == "view task":
        bot.send_message(message.chat.id,"You are here!")



if __name__ == "__main__":
    bot.polling()