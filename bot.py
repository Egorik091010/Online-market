from config import *
from create_db import DB_Manager
from telebot import TeleBot
import sqlite3

bot = TeleBot(TOKEN)

conn = sqlite3.connect("help.db", check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я чат бот который поможет тебе если у тебя возникли вопросы. 
/help - нажми на эту команду и узнаешь больше обо мне
""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, """Выбери нужную тебе категорию
/Frequently - Самые задаваемые вопросы
/Contacs - Наши контакты
/Geoposition - Наша геолокация   
/Question - Если ваш вопрос не совпадает с часто задаваемыми                     
""")
    

@bot.message_handler(commands=['Frequently'])
def frequently(message):
    bot.send_message(message.chat.id, """Выбери вопрос который у тебя возник
/1 - Как забронировать столик?
/2 - Как оформить онлайн заказ?
/3 - Как отменить заказ?
/4 - Что делать, если товар пришел поврежденным?
/5 - Как связаться с вашей технической поддержкой?
/6 - Как узнать информацию о доставке?
""")

@bot.message_handler(commands=['Contacs'])
def contacs(message):
    bot.send_message(message.chat.id, """Наши контакты:
    email - restourante@gmail.com
    Tel - 896755284""")

@bot.message_handler(commands=['Geoposition'])
def geoposition(message):
    bot.send_message(message.chat.id, "Мы находимся здесь - ")


@bot.message_handler(content_types=['Question'])
def handle_message(message):
    bot.send_message(message.chat.id, 'Напиши свой вопрос во такому типу:' \
    'Меня зовут так-то, и свой вопрос')
    user_id = message.chat.id
    username = message.from_user.username
    name = message.from_user.name
    user_text = message.text

    # сохраняем в БД
    cursor.execute("INSERT INTO feedback (id, username, name, question) VALUES (?, ?, ?, ?)",
                   (user_id, username,name,  user_text))
    conn.commit()

    bot.send_message(user_id, f"✅ Сообщение сохранено в базе!\nТы написал: {user_text}, Наш человек в скором времени вам ответит")



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












if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()
