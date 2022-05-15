import telebot
import _sqlite3
import config
import sql
from telebot import types
import os
import glob

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    with open("212979.zip","rb") as misc:
        f=misc.read()
    bot.send_document(message.chat.id,f)


bot.polling()
