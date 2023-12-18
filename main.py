import telebot
import main_module

bot = telebot.TeleBot('6843284956:AAHBNPfGSoMJF1MQA0jtqcvVgfp-s18S4Lk')
films = ""
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Напиши название фильма, чтобы найти похожее')
    bot.register_next_step_handler(message, film)

def film (message):
    global films
    films = message.text.lower()
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
    match callback.data:
        case 'suzhet': #Сюжет
            bot.delete_message(callback.message.chat.id,callback.message.message_id)
            bot.send_message(callback.message.chat.id, 'Подождите...')
            bot.send_message(callback.message.chat.id, main_module.get_answer(films, "сюжет"), disable_web_page_preview=True)
        case 'atmos': #Атмосфера
            bot.delete_message(callback.message.chat.id,callback.message.message_id)
            bot.send_message(callback.message.chat.id, 'Подождите...')
            bot.send_message(callback.message.chat.id, main_module.get_answer(films, "атмосфера"), disable_web_page_preview=True)
        case 'ai': #Актерская игра
            bot.delete_message(callback.message.chat.id,callback.message.message_id)
            bot.send_message(callback.message.chat.id, 'Подождите...')
            bot.send_message(callback.message.chat.id, main_module.get_answer(films, "актерская игра"), disable_web_page_preview=True)
        case 'zhanr': #Жанр
            bot.delete_message(callback.message.chat.id,callback.message.message_id)
            bot.send_message(callback.message.chat.id, 'Подождите...')
            bot.send_message(callback.message.chat.id, main_module.get_answer(films, "жанр"), disable_web_page_preview=True)
        case 'spec': #Спецэфекты
            bot.delete_message(callback.message.chat.id,callback.message.message_id)
            bot.send_message(callback.message.chat.id, 'Подождите...')
            bot.send_message(callback.message.chat.id, main_module.get_answer(films, "спецэфекты"), disable_web_page_preview=True)
    bot.send_message(callback.message.chat.id, 'Напишите /start , чтобы начать сначала')
bot.infinity_polling()