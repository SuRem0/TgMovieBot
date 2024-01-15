import telebot
import main_module
from conf import KEY

bot = telebot.TeleBot(KEY)
users = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Напиши название фильма, чтобы найти похожее')
    bot.register_next_step_handler(message, film)

def film (message):
    global users
    users[message.chat.id] = message.text.lower(); print(users[message.chat.id]);
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Сюжет', callback_data='suzhet')
    btn2 = telebot.types.InlineKeyboardButton('Атмосфера', callback_data='atmos')
    btn3 = telebot.types.InlineKeyboardButton('Актерская игра', callback_data='ai')
    btn4 = telebot.types.InlineKeyboardButton('Жанр', callback_data='zhanr')
    btn5 = telebot.types.InlineKeyboardButton('Спецэфекты', callback_data='spec')
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id, 'Почему вам понравился фильм?',reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_massage(callback):
    global users
    bot.delete_message(callback.message.chat.id,callback.message.message_id)
    bot.send_message(callback.message.chat.id, 'Подождите...')
    match callback.data:
        case 'suzhet': #Сюжет
            bot.send_message(callback.message.chat.id, main_module.get_answer(users[callback.message.chat.id], "сюжет"), disable_web_page_preview=True)
        case 'atmos': #Атмосфера
            bot.send_message(callback.message.chat.id, main_module.get_answer(users[callback.message.chat.id], "атмосфера"), disable_web_page_preview=True)
        case 'ai': #Актерская игра
            bot.send_message(callback.message.chat.id, main_module.get_answer(users[callback.message.chat.id], "актерская игра"), disable_web_page_preview=True)
        case 'zhanr': #Жанр
            bot.send_message(callback.message.chat.id, main_module.get_answer(users[callback.message.chat.id], "жанр"), disable_web_page_preview=True)
        case 'spec': #Спецэфекты
            bot.send_message(callback.message.chat.id, main_module.get_answer(users[callback.message.chat.id], "спецэфекты"), disable_web_page_preview=True)
    bot.send_message(callback.message.chat.id, 'Напишите /start , чтобы начать сначала')
bot.infinity_polling()