import _sqlite3

conn = _sqlite3.connect("telebot.db")
cusor = conn.cursor()


def add_name(a):
    print(a)
