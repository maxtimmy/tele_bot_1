import telebot
import _sqlite3
import config
import sql
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])  # команда старт
def start(m, res=False):
    mess = f'<b>Привет, {m.from_user.first_name}!</b>\nТут ты можешь найти работы наших учеников (/find) или загрузить свою(/upload)'
    bot.send_message(m.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=["help"])  # команда помощи нуждающимся
def download(m, res=False):
    mess = '/upload - загрузить свою работу\n/find - найти нужный тебе материал'
    bot.send_message(m.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=["upload"])  # команда загрузки новой работы
def download(m, res=False):
    mess = 'Ты уже загружал работы в нашего бота?'

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да", callback_data='yes')
    item2 = types.InlineKeyboardButton("Нет", callback_data='no')
    markup.add(item1, item2)
    bot.send_message(m.chat.id, mess, reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def otevet(call):
        try:
            if call.message:
                if call.data == 'yes':
                    bot.send_message(call.message.chat.id, 'Супер')  # сделать загрузку работы
                elif call.data == 'no':
                    bot.send_message(call.message.chat.id, 'жаль')  # Сделать регистрацию

        except Exception as e:
            print(repr(e))


@bot.message_handler(commands=["find"])  # команда поиска работ (сделать поиск работы)
def find(m):
    mess = 'ЗДЕСЬ ДОЛЖЕН БЫТЬ ТЕКСТ'
    bot.send_message(m.chat.id, mess, parse_mode='html')


@bot.message_handler()  # заглушка если какой-то имбицил не будет слать команду
def unknowcomand(m):
    mess = 'Незивестная команда\nНапиши /help и получи инструкцию'
    bot.send_message(m.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True, interval=0)
