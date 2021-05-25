import telebot, time
import os
import random
import telethon
import glob
import pprint

from telebot import types
TOKEN = "1587953913:AAFqTS6g9N7sfbURbqX7jEiybhnna_ydeHI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    a =['Rus', "Alg", "Geom","Lit","Ph","Biol", "Astro", "Geog","His", "Soc","Foreing", "Chem", "Com",'Phis', 'info']

    dic = {'Rus': 'Русский', "Alg": "Алгебра", "Geom": 'Геометрия', "Lit": 'Литература',
               "Ph": 'Физика', "Biol": 'Биология', "Astro": 'Астрономия', "Geog": 'География', "His": 'История',
           "Soc": 'Обществознание', "Foreing": 'Иностранный', "Chem": 'Химия', "Com": 'ИКТ', 'Phis': 'Физ/ра'}


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(a[0])
    item2 = types.KeyboardButton(a[1])
    item3 = types.KeyboardButton(a[2])
    item4 = types.KeyboardButton(a[3])
    item5 = types.KeyboardButton(a[4])
    item6 = types.KeyboardButton(a[5])
    item7 = types.KeyboardButton(a[6])
    item8 = types.KeyboardButton(a[7])
    item9 = types.KeyboardButton(a[8])
    item10 = types.KeyboardButton(a[9])
    item11 = types.KeyboardButton(a[10])
    item12 = types.KeyboardButton(a[11])
    item13 = types.KeyboardButton(a[12])
    item14 = types.KeyboardButton(a[13])
    item15 = types.KeyboardButton(a[14])

    markup.add(item1, item2, item3, item4,item5,item6,item7,item8,item9, item10, item11, item12, item13, item14,item15)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы вам помогать"
                                      ".".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

    bot.send_message(message.chat.id, "Напишите ваше домашнее задание(Нарпимер, Русский - параграф 55)")

    bot.send_message(message.chat.id, "Он запишется в текстовый файл, и все ваши предыдущие д/з по данному предмету тоже будут хранится там")

tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))
dic ={'Rus': 'Русский', "Alg":"Алгебра", "Geom" : 'Геометрия',"Lit": 'Литература' ,
      "Ph" : 'Физика',"Biol": 'Биология', "Astro": 'Астрономия', "Geog": 'География',"His": 'История',
      "Soc": 'Обществознание',"Foreing": 'Иностранный', "Chem": 'Химия', "Com": 'ИКТ','Phis': 'Физ/ра'}

@bot.message_handler(content_types=['text'])
def handle_text(message):

    if 'Рус' in message.text or 'рус' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Russian.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")



    if 'Алг' in message.text or 'алг' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Algebra.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")

    if 'Литер' in message.text or 'литер' in message.text :
        bot.delete_message(message.chat.id, message.message_id)
        with open(f"Literature.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")

    if 'Инос' in message.text or 'инос' in message.text:
        bot.delete_message(message.chat.id, message.message_id)
        with open(f"Foreing Language.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text) + "\n")



    if 'Геом' in message.text or 'геом' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Geometry.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")



    if 'геогр' in message.text or 'Геогр' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Geography.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")



    if 'физик' in message.text or 'Физик' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Physics.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")



    if 'био' in message.text or 'Био' in message.text :
        bot.delete_message(message.chat.id, message.message_id)
        with open(f"Biology.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")



    if 'физра' in message.text or 'Физра' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Physical culture.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")



    if 'Инфо' in message.text or 'инфо' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Computer Scince.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")

    if 'история' in message.text or 'История' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"History.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")

    if 'обществ' in message.text or 'Обществ' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Social Studies.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")

    if 'Хим' in message.text or 'хим' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Chemistry.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")

    if 'Астро' in message.text or 'астро' in message.text :
        bot.delete_message(message.chat.id, message.message_id)

        with open(f"Astronomy.txt", "a") as file:
            file.write(" Время и Дата: " + tconv(message.date) + " " + str(message.text)+"\n")

    if message.text == 'Rus':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Russian.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'русскому!')


    if message.text == 'Alg':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Algebra.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'алгебре!')

    if message.text == 'Geom':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Geometry.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'геометрии!')

    if message.text == 'Lit':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Literature.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'литературе!')

    if message.text == 'Ph':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Physics.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'физике!')
    if message.text == 'Biol':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Biology.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'биологии!')

    if message.text == 'Phis':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Physical culture.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'физкультуре!')

    if message.text == 'Geog':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Geography.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'географии!')

    if message.text == 'Soc':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Social Studies.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'обществознанию!')

    if message.text == 'His':
        bot.delete_message(message.chat.id, message.message_id)
        with open('History.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'истории!')


    if message.text == 'Com':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Computer Scince.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'информатике!')
    if message.text == 'Foreing':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Foreing Language.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'иностранному!')
    if message. text == 'info':
        bot.send_message(message.chat.id,
                         "Это значение клавиатуры, если вам непонятно значение клавиши" + '\n' + '\n'.join(
                             "{}: {}".format(k, v) for k, v in dic.items()))
    if message.text == 'Astro':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Astronomy.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'астрономии!')
    if message.text == 'Сhem':
        bot.delete_message(message.chat.id, message.message_id)
        with open('Chemistry.txt', 'r') as fp:
            data = fp.read()
            fp.seek(0, os.SEEK_END)
            if fp.tell():
                bot.send_message(message.chat.id, data)
                fp.seek(0)
            else:
                bot.send_message(message.chat.id, 'Напишите дз по '+ 'химии!')







@bot.message_handler(content_types=['text'])
def lol(message):
    a =['Rus', "Alg", "Geom","Lit","Ph","Biol", "Astro", "Geog","His", "Soc","Foreing", "Chem", "Com",'Phis']
    while message.text == 'Rus':
        @bot.message_handler(content_types=['text' or 'numbers'])
        def handle_text(message):
            a =['Rus', "Alg", "Geom","Lit","Ph","Biol", "Astro", "Geog","His", "Soc","Foreing", "Chem", "Com",'Phis']
            txt = message.text
bot.polling(none_stop=True)