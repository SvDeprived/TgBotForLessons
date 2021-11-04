import telebot
from telebot import types
import sqlite3

token = "2068347693:AAHtCFQwCXWG8iheXu4dye4vpxaaW6yuBds"
bot = telebot.TeleBot(token)

conn = sqlite3.connect('fds.db', check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, на какую неделю ты хочешь узнать расписание пар ?',
    reply_markup=keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Четная')
    button2 = types.KeyboardButton('Нечетная')
    markup.add(button1,button2)
    return markup

def keyboardeven():
    buttn1 = types.KeyboardButton('Понедельник 📖')
    buttn2 = types.KeyboardButton('Вторник 📖')
    buttn3 = types.KeyboardButton('Среда 📖')
    buttn4 = types.KeyboardButton('Четверг 📖')
    buttn5 = types.KeyboardButton('Пятница 📖')
    button5 = types.KeyboardButton('🔁 Вернуться к неделям 🔁')
    markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(buttn1).add(buttn2).add(buttn3).add(buttn4).add(buttn5).add(button5)
    return(markup2)

def keyboardodd():
    butn1 = types.KeyboardButton('📖 Понедельник')
    butn2 = types.KeyboardButton('📖 Вторник')
    butn3 = types.KeyboardButton('📖 Среда')
    butn4 = types.KeyboardButton('📖 Четверг')
    butn5 = types.KeyboardButton('📖 Пятница')
    button5 = types.KeyboardButton('🔁 Вернуться к неделям 🔁')
    markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(butn1).add(butn2).add(
        butn3).add(butn4).add(butn5).add(button5)
    return markup3

def returner():
    rtrn = types.KeyboardButton('🔁 Вернуться к выбору недели 🔁')
    markup6 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(rtrn)
    return markup6

@bot.message_handler(content_types=['text'])
def manipulator(message):
    if message.text == 'Четная':
        bot.send_message(message.chat.id, 'Выбери день недели', reply_markup=keyboardeven())
    elif message.text == 'Нечетная':
        bot.send_message(message.chat.id, 'Выбери день недели', reply_markup=keyboardodd())
    elif message.text == '🔁 Вернуться к неделям 🔁':
        bot.send_message(message.chat.id, 'На какую неделю ты хочешь узнать расписание пар ?',reply_markup=keyboard())
    elif message.text == '🔁 Вернуться к выбору недели 🔁':
        bot.send_message(message.chat.id, 'На какую неделю ты хочешь узнать расписание пар ?', reply_markup=keyboard())
    elif message.text == '📖 Понедельник':
        cursor.execute('SELECT Lesson1 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == '📖 Вторник':
        cursor.execute('SELECT Lesson2 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == '📖 Среда':
        cursor.execute('SELECT Lesson3 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == '📖 Четверг':
        cursor.execute('SELECT Lesson4 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == '📖 Пятница':
        cursor.execute('SELECT Lesson5 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == 'Понедельник 📖':
        cursor.execute('SELECT Lesson11 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == 'Вторник 📖':
        cursor.execute('SELECT Lesson12 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == 'Среда 📖':
        cursor.execute('SELECT Lesson13 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == 'Четверг 📖':
        cursor.execute('SELECT Lesson14 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    elif message.text == 'Пятница 📖':
        cursor.execute('SELECT Lesson15 FROM Rasp')
        x = cursor.fetchone()
        bot.send_message(message.chat.id, x, reply_markup = returner())
    else:
        bot.send_message(message.chat.id, 'Прости, но я создан для выдачи расписания, а не общения. Да, мир бывает жесток... Лучше спроси у меня расписание')
        bot.send_message(message.chat.id, 'На какую неделю ты хочешь узнать расписание пар ?',reply_markup=keyboard())



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Чтобы узнать расписание на день, достаточно написать /start, либо нажать на одноименную кнопку и правильно нажимать на следующие кнопки :)')

@bot.message_handler(commands=['button'])
async def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("button")
    markup.add(item1)
    await message.answer("Выберите действие", reply_markup=markup)

bot.infinity_polling()
