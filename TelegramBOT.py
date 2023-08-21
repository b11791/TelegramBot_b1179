import telebot
import random
from telebot import types
import os
import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome_user(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Жанры", callback_data="zhanr")
    btn2 = types.InlineKeyboardButton(text="📀 Все песни", callback_data="songs")
    btn3 = types.InlineKeyboardButton(text="Помощь", callback_data="help")
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, f"👋 Привет, <b>{message.from_user.first_name}</b>\n "
                                      f"Здесь будет описание",
                     parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=["help"])
def go_help(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Назад", callback_data="back")
    markup.row(btn1)
    bot.send_message(message.chat.id, f"Здесь будет гайд\n"
                                      f"Обратная связь - @b1179",
    parse_mode="html", reply_markup=markup)


# @bot.callback_query_handler(func=lambda callback: True)
# def user_clicked(callback):
#     if callback.data == "zhanr":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Pop-Jazz", callback_data="p-j")
#         btn2 = types.InlineKeyboardButton(text="Remixes-Phonk-Rap", callback_data="r-p-r")
#         btn3 = types.InlineKeyboardButton(text="Rock", callback_data="rock")
#         btn4 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         markup.row(btn1, btn2)
#         markup.row(btn3, btn4)
#         bot.send_message(callback.message.chat.id, "Выберите направление музыки", reply_markup=markup)
#
#     elif callback.data == "songs":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Да, скачать все песни", callback_data="3gb")
#         btn3 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         btn2 = types.InlineKeyboardButton(text="Помощь", callback_data="help")
#         markup.row(btn1)
#         markup.row(btn2, btn3)
#         bot.send_message(callback.message.chat.id, "Вы уверенны, что хотите скачать 3гб?", reply_markup=markup)
#
#     elif callback.data == "help":
#         go_help(callback.message)
#
#     elif callback.data == "back":
#         welcome_user(callback.message)
#
#     elif callback.data == "3gb":
#         music = os.path.join("tracks")
#         for root, subFolder, files in os.walk(music):
#             for item in files:
#                 if item.endswith(".mp3"):
#                     path = os.path.abspath(os.path.join(root, item))
#                     print(f"{item} - {path}")
#                     with open(path, "rb") as audio:
#                         bot.send_audio(callback.message.chat.id, audio)
#
#     elif callback.data == "p-j":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="ABBA", callback_data="abba")
#         btn2 = types.InlineKeyboardButton(text="Amy Winehouse", callback_data="amy")
#         btn3 = types.InlineKeyboardButton(text="Bjork", callback_data="bjork")
#         btn4 = types.InlineKeyboardButton(text="Duran Duran", callback_data="duran")
#         btn5 = types.InlineKeyboardButton(text="Kasabian", callback_data="kasab")
#         btn6 = types.InlineKeyboardButton(text="Morten Harket", callback_data="morten")
#         btn7 = types.InlineKeyboardButton(text="The Bee Gees", callback_data="bee gees")
#         btn8 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         markup.row(btn1, btn2)
#         markup.row(btn3, btn4)
#         markup.row(btn5, btn6)
#         markup.row(btn7, btn8)
#         bot.send_message(callback.message.chat.id, "Выберите Группу/Исполнителя", reply_markup=markup)
#
#     elif callback.data == "abba":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Dancing Queen", callback_data="dance")
#         btn2 = types.InlineKeyboardButton(text="Gimme Gimme", callback_data="gimme")
#         btn3 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         markup.row(btn1, btn2)
#         markup.row(btn3)
#         with open(os.path.join("tracks", "Images", "Abba_.jpg"), "rb") as file:
#             image_mes = bot.send_photo(callback.message.chat.id, file)
#             print(image_mes.message_id)
#             mes = bot.send_message(callback.message.chat.id, f"Песни группы <b><em>ABBA</em></b>",
#                              parse_mode="html",
#                              reply_markup=markup)
#             print(mes.message_id)
#
#
#     elif callback.data == "dance":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "ABBA", "DancingQueen.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "gimme":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "ABBA", "GimmeGimme.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "amy":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Back To Black", callback_data="ambacktobl")
#         btn2 = types.InlineKeyboardButton(text="You Know I'm No Good", callback_data="youknow")
#         btn3 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         markup.row(btn1, btn2)
#         markup.row(btn3)
#         with open(os.path.join("tracks", "Images", "AmyWinehouse_.jpg"), "rb") as file:
#             bot.send_photo(callback.message.chat.id, file)
#             bot.send_message(callback.message.chat.id, f"Песни <b><em>Amy Winehouse</em></b>",
#                              parse_mode="html",
#                              reply_markup=markup)
#
#     elif callback.data == "ambacktobl":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Amy Winehouse", "BackToBlack.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "youknow":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Amy Winehouse", "YouKnowImNoGood.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "bjork":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Army Of Me", callback_data="armyof")
#         btn2 = types.InlineKeyboardButton(text="Play Dead", callback_data="playd")
#         btn3 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         markup.row(btn1, btn2)
#         markup.row(btn3)
#         with open(os.path.join("tracks", "Images", "Bjork_.jpg"), "rb") as file:
#             bot.send_photo(callback.message.chat.id, file)
#             bot.send_message(callback.message.chat.id, f"Песни <b><em>Bjork</em></b>",
#                              parse_mode="html",
#                              reply_markup=markup)
#
#     elif callback.data == "armyof":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Bjork", "ArmyOfMe.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "playd":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Bjork", "PlayDead.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "duran":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="All You Need Is Now", callback_data="allyoun")
#         btn2 = types.InlineKeyboardButton(text="Astronaut", callback_data="astro")
#         btn3 = types.InlineKeyboardButton(text="Big Thing", callback_data="bigth")
#         btn4 = types.InlineKeyboardButton(text="Notorious", callback_data="notor")
#         btn5 = types.InlineKeyboardButton(text="Red Carpet Massacre", callback_data="redcarp")
#         btn6 = types.InlineKeyboardButton(text="Seven And The Ragged Tiger", callback_data="sevenandthe")
#         btn7 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         markup.row(btn1, btn2)
#         markup.row(btn3, btn4)
#         markup.row(btn5, btn6)
#         markup.row(btn7)
#         bot.send_message(callback.message.chat.id, "Выберите Альбом", reply_markup=markup)
#
#     elif callback.data == "allyoun":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="All You Need Is Now", callback_data="allyouneed")
#         btn2 = types.InlineKeyboardButton(text="Being Followed", callback_data="beingf")
#         btn3 = types.InlineKeyboardButton(text="Blame The Machines", callback_data="blamet")
#         btn4 = types.InlineKeyboardButton(text="Girl Panic", callback_data="girlp")
#         btn5 = types.InlineKeyboardButton(text="Leave A Light On", callback_data="leaveal")
#         btn6 = types.InlineKeyboardButton(text="Mediterranea", callback_data="medit")
#         btn7 = types.InlineKeyboardButton(text="Networker Nation", callback_data="network")
#         btn8 = types.InlineKeyboardButton(text="Other People's Lives", callback_data="otherpeop")
#         btn9 = types.InlineKeyboardButton(text="Runway Runaway", callback_data="runway")
#         btn10 = types.InlineKeyboardButton(text="Safe", callback_data="safe")
#         btn11 = types.InlineKeyboardButton(text="The Man Who Stole A Leopard", callback_data="stolealeop")
#         btn12 = types.InlineKeyboardButton(text="Too Bad You're So Beautiful", callback_data="toobad")
#         btn13 = types.InlineKeyboardButton(text="Назад", callback_data="back")
#         markup.row(btn1, btn2)
#         markup.row(btn3, btn4)
#         markup.row(btn5, btn6)
#         markup.row(btn7, btn8)
#         markup.row(btn9, btn10)
#         markup.row(btn11, btn12)
#         markup.row(btn13)
#         with open(os.path.join("tracks", "Images", "AllYouNeedIsNow_.jpg"), "rb") as file:
#             bot.send_photo(callback.message.chat.id, file)
#         bot.send_message(callback.message.chat.id, "Песни альбома <b><em>All You Need Is Now</em></b> группы <b>Duran Duran</b>", reply_markup=markup, parse_mode="html")
#
#     elif callback.data == "allyouneed":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "AllYouNeedIsNow.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "beingf":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "BeingFollowed.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "blamet":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "BlameTheMachines.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "girlp":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "GirlPanic.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "leaveal":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "LeaveALightOn.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "medit":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "Mediterranea.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "network":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "NetworkerNation.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "otherpeop":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "OtherPeoplesLives.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "runway":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "RunwayRunaway.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "safe":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "Safe.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "stolealeop":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "TheManWhoStoleALeopard.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     elif callback.data == "toobad":
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
#         markup.row(btn1)
#         with open(os.path.join("tracks", "Pop-Jazz", "Duran Duran", "AllYouNeedIsNow", "TooBadYoureSoBeautiful.mp3"), "rb") as file:
#             bot.send_audio(callback.message.chat.id, file, reply_markup=markup)
#
#     bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.message_handler()
def messaging(message):
    with open("users_comments.txt", "a", encoding="utf-8") as file:
        file.write(f"{message.from_user.first_name}({message.from_user.username}): {message.text}\n")
    another_mes = True

    if random.randint(1, 10) == 1:
        if message.from_user.is_premium != None:
            bot.send_message(message.chat.id, "Ты чего богатый такой?💸\n Купи мне тоже премку пж")
            another_mes = False

    if "как дел" in message.text.lower():
        answers = ["Нормально.", "Отлично.", "Топ", "Пельмени..."]
        bot.reply_to(message, random.choice(answers))
    elif "прив" in message.text.lower() or "даров" in message.text.lower() or "ку" in message.text.lower():
        answers = ["Я ЩАС СНИМУ ТРУСЫ", "Привет!?", "🤨Здоровались же"]
        bot.reply_to(message, random.choice(answers))
    elif another_mes:
        answers = ["Опять эти интернет-мошенники со своими приколами...", "Это база"]
        bot.reply_to(message, random.choice(answers))


bot.polling(none_stop=True, timeout=60)