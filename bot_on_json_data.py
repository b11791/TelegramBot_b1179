import json

import telebot
import random
from telebot import types
import os
import config


bot = telebot.TeleBot(config.TOKEN)
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

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
    btn2 = types.InlineKeyboardButton(text="Помощь", callback_data="help")
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, f"👋 Привет, <b>{message.from_user.first_name}</b>\n "
                                      f"Здесь будет описание",
                     parse_mode="html", reply_markup=markup)
    bot.delete_message(message.chat.id, message.message_id)


@bot.callback_query_handler(func=lambda cb: cb.data == 'help')
def do_help(callback):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Назад", callback_data="back")
    markup.row(btn1)
    bot.send_message(callback.message.chat.id, f"Здесь будет гайд\n"
                                        f"Обратная связь - @b1179",
                     parse_mode="html", reply_markup=markup)

    bot.delete_message(callback.message.chat.id, callback.message.message_id)



########################################################################################################################
@bot.callback_query_handler(func=lambda cb: cb.data == 'genres')
def get_genres(callback):
    genres_id = data['genres'].keys()
    buttons = [
        [types.InlineKeyboardButton(text=data['genres'][genre_id]['name'], callback_data=f'genre_{genre_id}')]
        for genre_id in genres_id
    ]
    buttons.append([types.InlineKeyboardButton(text="Назад", callback_data="back")])
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"Выберите Жанр Музыки",
                     parse_mode="html", reply_markup=markup)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)

@bot.callback_query_handler(func=lambda cb: cb.data.startswith('genre_'))
def get_singers(callback):
    _, genre_id = callback.data.split('_')
    singers_groups_id = data['genres'][genre_id]['singers/groups'].keys()
    buttons = [
        [types.InlineKeyboardButton(text=data["genres"][genre_id]["singers/groups"][singer_group_id]["name"], callback_data=f'singergroup_{genre_id}_{singer_group_id}')]
        for singer_group_id in singers_groups_id
    ]
    buttons.append([types.InlineKeyboardButton(text="Назад", callback_data="genres")])
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"Выберите Исполнителя/Группу",
                     parse_mode="html", reply_markup=markup)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)

@bot.callback_query_handler(func=lambda cb: cb.data.startswith('singergroup_'))
def get_songs_or_albums(callback):
    _, genre_id, singer_group_id = callback.data.split('_')
    photo_path = data['genres'][genre_id]['singers/groups'][singer_group_id]["photo"]
    with open(photo_path, "rb") as photo:
        bot.send_photo(callback.message.chat.id, photo)
    photo_id = bot.send_photo(callback.message.chat.id, photo).message_id
    if 'songs' in data['genres'][genre_id]['singers/groups'][singer_group_id].keys():
        songs_id = data["genres"][genre_id]["singers/groups"][singer_group_id]["songs"].keys()
        buttons = [
            [types.InlineKeyboardButton(text=data["genres"][genre_id]["singers/groups"][singer_group_id]["songs"][song_id]["name"],
            callback_data=f'song_{genre_id}_{singer_group_id}_{song_id}')]
            for song_id in songs_id
        ]
        buttons.append([types.InlineKeyboardButton(text="Назад", callback_data=f"genre_{genre_id}")])
        markup = design_buttons(buttons)
        bot.send_message(callback.message.chat.id, f"Песни/Треки <b>{data['genres'][genre_id]['singers/groups'][singer_group_id]['name']}</b>",
                     parse_mode="html", reply_markup=markup)
    else:
        albums_id = data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"].keys()
        buttons = [
            [types.InlineKeyboardButton(text=data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["name"],
            callback_data=f'album_{genre_id}_{singer_group_id}_{album_id}')]
            for album_id in albums_id
        ]
        buttons.append([types.InlineKeyboardButton(text="Назад", callback_data=f"genre_{genre_id}")])
        markup = design_buttons(buttons)
        bot.send_message(callback.message.chat.id, f"Альбомы <b>{data['genres'][genre_id]['singers/groups'][singer_group_id]['name']}</b>",
                     parse_mode="html", reply_markup=markup)
    bot.delete_message(callback.message.chat.id, photo_id)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('album_'))
def get_albums(callback):
    _, genre_id, singer_group_id, album_id = callback.data.split('_')
    album_songs_id = data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["songs"].keys()
    photo_path = data['genres'][genre_id]['singers/groups'][singer_group_id]["albums"][album_id]["cover"]
    with open(photo_path, "rb") as photo:
        bot.send_photo(callback.message.chat.id, photo)
    photo_id = bot.send_photo(callback.message.chat.id, photo).message_id
    buttons = [
        [types.InlineKeyboardButton(text=data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["songs"][album_song_id]["name"],
        callback_data=f'albumsong_{genre_id}_{singer_group_id}_{album_id}_{album_songs_id}')]
        for album_song_id in album_songs_id
    ]
    buttons.append([types.InlineKeyboardButton(text="Назад", callback_data=f"singergroup_{genre_id}_{singer_group_id}")])
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"Альбом <em><b>{data['genres'][genre_id]['singers/groups'][singer_group_id]['albums'][album_id]['name']}</b></em>",
                 parse_mode="html", reply_markup=markup)
    bot.delete_message(callback.message.chat.id, photo_id)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)

@bot.callback_query_handler(func=lambda cb: cb.data.startswith('albumsong_'))
def get_album_song(callback):
    _, genre_id, singer_group_id, album_id, album_song_id = callback.data.split('_')
    song_path = data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["songs"][album_song_id]["src"]
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text="Назад", callback_data=f"album_{genre_id}_{singer_group_id}_{album_id}")
    markup.row(back)
    with open(song_path, "rb") as audio:
        bot.send_audio(callback.message.chat.id, audio, reply_markup=markup)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)

@bot.callback_query_handler(func=lambda cb: cb.data.startswith('song_'))
def get_song(callback):
    _, genre_id, singer_group_id, song_id = callback.data.split('_')
    song_path = data["genres"][genre_id]["singers/groups"][singer_group_id]["songs"][song_id]["src"]
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text="Назад", callback_data=f"album_{genre_id}_{singer_group_id}")
    markup.row(back)
    with open(song_path, "rb") as audio:
        bot.send_audio(callback.message.chat.id, audio, reply_markup=markup)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)

########################################################################################################################
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