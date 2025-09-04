from config import *
from create_db import DB_Manager
from telebot import TeleBot
import sqlite3

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я чат бот который поможет тебе если у тебя возникли вопросы. 
А также тут ты можешь забронировать столик.
""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, """Сдесь есть все доступные команды
/Questions
/Reserve  
""")

@bot.message_handler(commands=['Questions'])
def question_help(message):
    bot.send_message(message.chat.id, """Выбери вопрос который у тебя возник
/1 - Как забронировать столик?
/2 - Как оформить онлайн заказ?
/3 - Как отменить заказ?
/4 - Что делать, если товар пришел поврежденным?
/5 - Как связаться с вашей технической поддержкой?
/6 - Как узнать информацию о доставке?
""")

@bot.message_handler(commands=['1'])
def question_1(message):
    con = sqlite3.connect("help.db")
    with con:
        cur = con.cursor()
        question1 = cur.execute("SELECT answers FROM question WHERE id = 1")
    bot.send_message(message.chat.id, question1,)

@bot.message_handler(commands=['2'])
def question_2(message):
    con = sqlite3.connect("help.db")
    with con:
        cur = con.cursor()
        question2 = cur.execute("SELECT answers FROM question WHERE id = 2")
    bot.send_message(message.chat.id, question2,)

@bot.message_handler(commands=['3'])
def question_3(message):
    con = sqlite3.connect("help.db")
    with con:
        cur = con.cursor()
        question3 = cur.execute("SELECT answers FROM question WHERE id = 3")
    bot.send_message(message.chat.id, question3,)

@bot.message_handler(commands=['4'])
def question_4(message):
    con = sqlite3.connect("help.db")
    with con:
        cur = con.cursor()
        question4 = cur.execute("SELECT answers FROM question WHERE id = 4")
    bot.send_message(message.chat.id, question4,)

@bot.message_handler(commands=['5'])
def question_5(message):
    con = sqlite3.connect("help.db")
    with con:
        cur = con.cursor()
        question5 = cur.execute("SELECT answers FROM question WHERE id = 5")
    bot.send_message(message.chat.id, question5,)

@bot.message_handler(commands=['6'])
def question_6(message):
    con = sqlite3.connect("help.db")
    with con:
        cur = con.cursor()
        question6 = cur.execute("SELECT answers FROM question WHERE id = 6")
    bot.send_message(message.chat.id, question6,)    



@bot.message_handler(commands=['Reserve'])
def reserve(message):
    pass








if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()
