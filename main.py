import telebot
import _sqlite3
import config
import sql
from telebot import types
import os
import glob

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])  # команда старт
def start(m):
    mess = f'<b>Привет, {m.from_user.first_name}!</b>\nТут ты можешь найти работы наших учеников или загрузить свою\n(/upload)  (/find)'
    bot.send_message(m.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=["help"])  # команда помощи нуждающимся
def help(m):
    bot.send_message(m.chat.id, config.help_mess[0], parse_mode='html')


@bot.message_handler(commands=["upload"])  # команда загрузки новой работы
def upload(m):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да", callback_data='yes')
    item2 = types.InlineKeyboardButton("Нет", callback_data='no')
    markup.add(item1, item2)
    bot.send_message(m.chat.id, config.upload_mess[0], reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def otevet(call):

        if call.message:
            if call.data == 'yes':
                msg = bot.send_message(call.message.chat.id, 'Супер, тогда введи свой логин')

                @bot.message_handler()
                def reg(slogin):
                    bot.clear_step_handler(slogin)
                    bot.send_message(slogin.chat.id, 'Супер, теперь отправь мне файл', parse_mode='html')

                    @bot.message_handler(content_types=['document'])
                    def handle_docs_photo(message):
                        bot.clear_step_handler(message)

                        file_info = bot.get_file(message.document.file_id)
                        downloaded_file = bot.download_file(file_info.file_path)
                        len(glob.glob('C:/Users/lenovo/PycharmProjects/tele_bot/files/' + slogin.text + '/*'))
                        print(len(glob.glob('C:/Users/lenovo/PycharmProjects/tele_bot/files/' + slogin.text + '/*')))
                        src = 'C:/Users/lenovo/PycharmProjects/tele_bot/files/' + slogin.text + '/1.pptx'
                        with open(src, 'wb') as new_file:
                            new_file.write(downloaded_file)

                        bot.reply_to(message, "Пожалуй, я сохраню это")





            elif call.data == 'no':
                bot.send_message(call.message.chat.id,
                                 'Тогда нужно зарегестрироваться, введи свой логин фин университета')

                @bot.message_handler()
                def unreg(login):
                    bot.clear_step_handler(login)
                    bot.send_message(login.chat.id, 'Поздравляю!\nТы зарегестрировался, теперь отправь мне файл',
                                     parse_mode='html')

                    @bot.message_handler(content_types=['document'])
                    def handle_docs_photo(message):
                        bot.clear_step_handler(message)
                        file_info = bot.get_file(message.document.file_id)
                        downloaded_file = bot.download_file(file_info.file_path)
                        os.mkdir("c://Users/lenovo/PycharmProjects/tele_bot/files/" + login.text)
                        src = 'C:/Users/lenovo/PycharmProjects/tele_bot/files/' + login.text + '/1.pptx'
                        with open(src, 'wb') as new_file:
                            new_file.write(downloaded_file)

                        bot.reply_to(message, "Пожалуй, я сохраню это")


@bot.message_handler(commands=["find"])  # команда поиска работ (сделать поиск работы)
def find(m):
    bot.send_message(m.chat.id, config.find_mes[0], parse_mode='html')

    @bot.message_handler(content_types=['text'])
    def echo_all(message):

        with open("212979.zip", "rb") as file:
            f = file.read()

        bot.send_document(message.chat.id, f, "212979.zip")


bot.polling(none_stop=True, interval=0)
