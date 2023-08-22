import telebot
import random
from telebot import types
import os
import config


bot = telebot.TeleBot(config.TOKEN)


def design_buttons(buttons):
    markup = types.InlineKeyboardMarkup()
    if len(buttons) % 2 == 0:
        for ind, btn in enumerate(buttons):
            if ind % 2 == 0:
                btn1 = btn
            elif ind % 2 != 0:
                btn2 = btn
                markup.row(btn1[0], btn2[0])
    else:
        for ind, btn in enumerate(buttons):
            if ind % 2 == 0 and buttons[-1] != btn:
                btn1 = btn
            elif ind % 2 != 0 and buttons[-1] != btn:
                btn2 = btn
                markup.row(btn1[0], btn2[0])
            else:
                markup.row(btn[0])
    return markup


@bot.message_handler(commands=["start"])
def welcome_user(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Жанры", callback_data="genres")
    btn2 = types.InlineKeyboardButton(text="📀 Все песни", callback_data="songs")
    btn3 = types.InlineKeyboardButton(text="Помощь", callback_data="help")
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, f"👋 Привет, <b>{message.from_user.first_name}</b>\n "
                                      f"Здесь будет описание",
                     parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda cb: cb.data == 'genres')
def get_genres(callback):
    genres = os.listdir('tracks/')
    genres.remove('Images')
    buttons = [
        [types.InlineKeyboardButton(text=genre, callback_data=f'genre_{genre}')]
        for genre in genres
    ]
    buttons.append([types.InlineKeyboardButton(text="Назад", callback_data="back")])
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"Жанры:",
                     parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('genre_'))
def get_singers(callback):
    genre = callback.data.split('_')[-1]
    singers = os.listdir(f'tracks/{genre}/')
    buttons = [
        [types.InlineKeyboardButton(text=singer, callback_data=f'singer_{genre}_{singer}')]
        for singer in singers
    ]
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"Певцы жанра:",
                     parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('singer_'))
def get_albums(callback):
    ...


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('singer_'))
def get_songs(callback):
    _, genre, singer = callback.data.split('_')
    songs = os.listdir(f'tracks/{genre}/{singer}/')
    buttons = [
        [types.InlineKeyboardButton(text=song, callback_data=f'song_{genre}_{singer}_{song}')]
        for song in songs
    ]
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"Песни певца:",
                     parse_mode="html", reply_markup=markup)


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