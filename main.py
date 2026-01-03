
import telebot
from config import TG_API_TOKEN

bot = telebot.TeleBot(token=TG_API_TOKEN)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    text = 'chem mogu pomoch'
    if message.text == '/start':
        text = 'privet !ja tvoi bot.chem mogu pomoch?' + text



    bot.send_message(message.chat.id,text)
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.reply_to(message, ' Vau,ochen krutoj sticker!')

@bot.message_handler(func=lambda message : len(message.text.split()) == 5)
def five_words(message):
    bot.send_message(message.chat.id, 'a ja mogu napisat shest slob :) ')


bot.infinity_polling()