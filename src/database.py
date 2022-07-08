import datetime
import sqlite3
from telebot import types,TeleBot

def create_connect(message: types.Message) -> sqlite3.Cursor:
    return sqlite3.connect(f"src/data/{message.from_user.id}.db",check_same_thread=False)

def create_cursor(message: types.Message):
    conn = create_connect(message)
    return conn.cursor()

def create_table(c : sqlite3.Cursor):
        c.execute("""CREATE TABLE if not EXISTS tasks (
                data text,
                task text
                    )""")

def insert_data(c : sqlite3.Cursor, data : datetime , text: str):
    c.execute("INSERT INTO tasks VALUES('{}','{}')".format(data,text))

def today_task(c : sqlite3.Cursor):
    c.execute("SELECT data,task FROM tasks WHERE data = :date",{'date': str(datetime.date.today())})
    data_from_table = c.fetchall()
    if data_from_table == []: return "nothing"

    list = []

    for i in data_from_table: list.append(i[1])

    x = ['{0}. {1}'.format(index+1,item) for index,item in enumerate(list)] 

    return '\n'.join(x)

