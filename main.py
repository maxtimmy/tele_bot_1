import telebot

bot = telebot.TeleBot('5353284511:AAFck4j-xd1L9EoKKn5f1COpqPNnsUL7CuA')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'даров, твари')

bot.polling(none_stop=True, interval=0)