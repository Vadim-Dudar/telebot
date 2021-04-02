import dou_parce
import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

	bot.reply_to(message, "Hi let's start!\nI'm bot wich parce dou.ua.\nSend me link for page")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    dou = dou_parce.Parce(message.text)
    dou.parce()
    

bot.polling()