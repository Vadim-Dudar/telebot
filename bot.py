import dou_parce
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("Let's go parcing 😁")
    # markup.add(item1)

    bot.send_message(message.chat.id, "Hi let's start!\nI'm bot wich parce dou.ua.\nSend me link for page")
    bot.send_message(message.chat.id, 'Ok.\nGive me just url for page')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        dou = dou_parce.Parce(message.text)
        dou.parce()
        bot.send_document(message.chat.id, open('sample.json'))
    except requests.exceptions.InvalidURL:
        bot.send_message(message.chat.id, 'I can parce only dou.ua ☹️')
        
    

bot.polling()