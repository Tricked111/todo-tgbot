import sqlite3
from telebot import types,TeleBot

def create_connect(message: types.Message) -> sqlite3.Cursor:
    return sqlite3.connect(f"src/{message.from_user.id}.db")

def create_cursor(message: types.Message):
    conn = create_connect(message)
    return conn.cursor()

#delete
def drop_table(c):
    c.execute("DROP TABLE tasks")
#delete


def create_table(c : sqlite3.Cursor):
        c.execute("""CREATE TABLE tasks (
                task text,
                date text
                    )""")

def insert_data(c : sqlite3.Cursor,text1,text2):
    c.execute("INSERT INTO tasks VALUES('{}','{}')".format(text1,text2))

def print_select(c : sqlite3.Cursor):
    c.execute("SELECT * FROM tasks")
    return c.fetchall()