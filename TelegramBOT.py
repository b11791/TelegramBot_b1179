import json

import telebot
import random
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)
with open('data.json', 'r', encoding='utf-8') as JasonNewstead:
    data = json.load(JasonNewstead)

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
    btn1 = types.InlineKeyboardButton(text="🎧 Жанры", callback_data="genres")
    btn2 = types.InlineKeyboardButton(text="🚨 Помощь", callback_data="help")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f"👋 Привет, <b>{message.from_user.first_name}</b>\n "
                                      f"Я бот-установщик песен плейлиста @b1179\n"
                                      f"---------------------------------\n"
                                      f"🎙Треки отсортированы по жанрам, исполнителям и альбомам. "
                                      f"Да, как бы странно это не выглядело, у некоторых исполнителей здесь может встречаться по одной песне (мне лень добалять ещё).\n\n"
                                      f"Если нашли баг, это фича и так задумано. Ну а если реально, то можете писать сразу 🤖 боту, сообщения логируются",
                     parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda cb: cb.data == 'back')
def go_back(callback):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="🎧 Жанры", callback_data="genres")
    btn2 = types.InlineKeyboardButton(text="🚨 Помощь", callback_data="help")
    markup.row(btn1, btn2)
    bot.send_message(callback.message.chat.id, f"👋 Привет, <b>{callback.message.from_user.first_name}</b>\n "
                                      f"Я бот-установщик песен плейлиста @b1179\n"
                                      f"---------------------------------\n"
                                      f"🎙Треки отсортированы по жанрам, исполнителям и альбомам. "
                                      f"Да, как бы странно это не выглядело, у некоторых исполнителей здесь может встречаться по одной песне (мне лень добалять ещё).\n\n"
                                      f"Если нашли баг, это фича и так задумано. Ну а если реально, то можете писать сразу 🤖 боту, сообщения логируются",
                     parse_mode="html", reply_markup=markup)
    # bot.delete_message(callback.message.chat.id, callback.message.message_id)

@bot.message_handler(commands=["help"])
def do_help_command(message):
    bot.delete_message(message.chat.id, message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Гайд 📜", callback_data="guide")
    btn2 = types.InlineKeyboardButton(text="Назад ↩", callback_data="back")
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, f"~ Нажимай кнопки по подсказкам\n"
                                      f"~ Если бот долго не отвечает, значит он либо грузит контент, либо выключен\n"
                                      f"~ Бот также отвечает на типичные фразы нетипичными ответами\n"
                                      f"~ Если нашел(-а) ошибку, например трек не загружается или что-то ещё, пиши этому"
                                      f" же боту (он конечно же бредово ответит, но я все равно увижу)\n"
                                      f"~ Если не знаешь что делать с треками, то ниже мини гайд 👇\n\n"
                                      f"Разработчик - @b1179",
                     parse_mode="html", reply_markup=markup)




@bot.callback_query_handler(func=lambda cb: cb.data == 'help')
def do_help(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Гайд 📜", callback_data="guide")
    btn2 = types.InlineKeyboardButton(text="Назад ↩", callback_data="back")
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(callback.message.chat.id, f"~ Нажимай кнопки по подсказкам\n"
                                      f"~ Если бот долго не отвечает, значит он либо грузит контент, либо выключен\n"
                                      f"~ Бот также отвечает на типичные фразы нетипичными ответами\n"
                                      f"~ Если нашел(-а) ошибку, например трек не загружается или что-то ещё, пиши этому"
                                      f" же боту (он конечно же бредово ответит, но я все равно увижу)\n"
                                      f"~ Если не знаешь что делать с треками, то ниже мини гайд 👇\n\n"
                                      f"Разработчик - @b1179",
                     parse_mode="html", reply_markup=markup)

@bot.callback_query_handler(func=lambda cb: cb.data == 'guide')
def get_guide(callback):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Дальше ⏩", callback_data="android1")
    btn2 = types.InlineKeyboardButton(text="Назад ↩", callback_data="help")
    markup.row(btn1, btn2)
    bot.send_message(callback.message.chat.id, "💻 Если у тебя комп, то тут всё понятно.\n\n"
                                               "<em><b>Правой кнопкой мыши на трек</b></em> > <em><b>Сохранить как</b></em> > <em><b>И дальше трек в ту"
                                               " папку куда тебе нужно</b></em>. Единственное припятсвие - твоё воображение\n"
                                               "Музыку можно использовать, начиная от простого желания её послушать"
                                               " и заканчивая применением в каком нибудь монтаже. Этот бот хорош тем, что быстро сортирует "
                                               "песни (хоть и из моего плейлиста), но всё же быстро и без вирусов 👾\n\n"
                                               "📱 В случае с кирпичами, всё гораздо сложнее и разнообразнее...",
                    parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda cb: cb.data == 'android1')
def phones(callback):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Дальше ⏩", callback_data="android2")
    btn2 = types.InlineKeyboardButton(text="Назад ↩", callback_data="guide")
    markup.row(btn1, btn2)
    with open("tracks/Images/Guide.jpg", "rb") as image:
        bot.send_photo(callback.message.chat.id, image)
    bot.send_message(callback.message.chat.id, "Присутствие файловых менеджеров "
                                               "упрощает жизнь. C IOS в этом плане противоположный случай.\n"
                                               "Не исключено, что я ошибаюсь и файловые менеджеры присутствуют и на них."
                                               " Так или иначе на Андроидах ими можно свободно пользоваться\n"
                                               "📁 Файловый менеджер можно <b>либо</b> скачать в каком нибудь Play Market, "
                                               "<b>либо</b> он сразу уже будет встроен. Я юзаю Сх и тебе тоже советую, ибо"
                                               " вещь проверенная.\n\n"
                                               "Заходим в проводник и идём по этому пути 👇\n"
                                               "<em><b>Основная память>Android(если у вас андроид)>data>org.telegram.messenger>files>Telegram>Telegram Audio</b></em>",
                     parse_mode="html", reply_markup=markup)

@bot.callback_query_handler(func=lambda cb: cb.data == 'android2')
def go_files(callback):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Назад ↩", callback_data="android1")
    markup.row(btn1)
    with open("tracks/Images/1.jpg", "rb") as image:
        bot.send_photo(callback.message.chat.id, image)
    bot.send_message(callback.message.chat.id, "Теперь выбираем нужные песни(или аудио) и переносим их в нужную папку.\n"
                                               "Есть mp3-плеер? Вообще шедеврально, закидывай их туда\n"
                                               "Если же нет, то советую скачать т.к в проводнике слушать как-то не очень.\n"
                                               "Ну или на крайняк создай где тебе удобно папку и закинь их туда, надо же их где-то держать\n\n"
                                               "Вообщем-то и всё, как их применять решать тебе.",
                    parse_mode="html", reply_markup=markup)


########################################################################################################################
@bot.callback_query_handler(func=lambda cb: cb.data == 'genres')
def get_genres(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    genres_id = data['genres'].keys()
    buttons = [
        [types.InlineKeyboardButton(text=data['genres'][genre_id]['name'], callback_data=f'genre_{genre_id}')]
        for genre_id in genres_id
    ]
    buttons.append([types.InlineKeyboardButton(text="Назад ↩", callback_data="back")])
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"💽 Выбери интересующее направление или"
                                               f" нажми <b>НАЗАД</b>, чтобы вернуться назад\n\n"
                                               f"/help - Помощь/Обратная связь 💬",
                     parse_mode="html", reply_markup=markup)

    # bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('genre_'))
def get_singers(callback):
    _, genre_id = callback.data.split('_')
    singers_groups_id = data['genres'][genre_id]['singers/groups'].keys()
    buttons = [
        [types.InlineKeyboardButton(text=data["genres"][genre_id]["singers/groups"][singer_group_id]["name"],
                                    callback_data=f'singergroup_{genre_id}_{singer_group_id}')]
        for singer_group_id in singers_groups_id
    ]
    buttons.append([types.InlineKeyboardButton(text="Назад ↩", callback_data="genres")])
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id, f"Выбери Исполнителя🎸Группу или нажми <b>НАЗАД</b>,"
                                               f" чтобы вернуться назад\n\n"
                                               f"/help - Помощь/Обратная связь 💬",
                     parse_mode="html", reply_markup=markup)
    # bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('singergroup_'))
def get_songs_or_albums(callback):
    _, genre_id, singer_group_id = callback.data.split('_')
    photo_path = data['genres'][genre_id]['singers/groups'][singer_group_id]["photo"]
    with open(photo_path, "rb") as photo:
        bot.send_photo(callback.message.chat.id, photo)
    if 'songs' in data['genres'][genre_id]['singers/groups'][singer_group_id].keys():
        songs_id = data["genres"][genre_id]["singers/groups"][singer_group_id]["songs"].keys()
        buttons = [
            [types.InlineKeyboardButton(
                text=data["genres"][genre_id]["singers/groups"][singer_group_id]["songs"][song_id]["name"],
                callback_data=f'song_{genre_id}_{singer_group_id}_{song_id}')]
            for song_id in songs_id
        ]
        buttons.append([types.InlineKeyboardButton(text="Назад ↩", callback_data=f"genre_{genre_id}")])
        markup = design_buttons(buttons)
        bot.send_message(callback.message.chat.id,
                         f"Песни/Треки <em><b>{data['genres'][genre_id]['singers/groups'][singer_group_id]['name']}</b></em>. Нажми <b>НАЗАД</b>, чтобы вернуться назад\n\n"
                         f"/help - Помощь/Обратная связь 💬\n"
                         f"P.S Сорян за скорость загрузки 🐌треков, сервера как никак¯\_(ツ)_/¯",
                         parse_mode="html", reply_markup=markup)
    elif 'albums' in data['genres'][genre_id]['singers/groups'][singer_group_id].keys():
        albums_id = data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"].keys()
        buttons = [
            [types.InlineKeyboardButton(
                text=data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["name"],
                callback_data=f'album_{genre_id}_{singer_group_id}_{album_id}')]
            for album_id in albums_id
        ]
        buttons.append([types.InlineKeyboardButton(text="Назад ↩", callback_data=f"genre_{genre_id}")])
        markup = design_buttons(buttons)
        bot.send_message(callback.message.chat.id,
                         f"Альбомы <em><b>{data['genres'][genre_id]['singers/groups'][singer_group_id]['name']}</b></em>. Нажми <b>НАЗАД</b>, чтобы вернуться назад\n\n"
                         f"/help - Помощь/Обратная связь 💬",
                         parse_mode="html", reply_markup=markup)
    # bot.delete_message(callback.message.chat.id, callback.message.message_id)

@bot.callback_query_handler(func=lambda cb: cb.data.startswith('album_'))
def get_album_songs(callback):
    _, genre_id, singer_group_id, album_id = callback.data.split('_')
    album_songs_id = data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["songs"].keys()
    photo_path = data['genres'][genre_id]['singers/groups'][singer_group_id]["albums"][album_id]["cover"]
    with open(photo_path, "rb") as photo:
        bot.send_photo(callback.message.chat.id, photo)
    buttons = [
        [types.InlineKeyboardButton(text=data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["songs"][album_song_id]["name"],
                                    callback_data=f'albumsong_{genre_id}_{singer_group_id}_{album_id}_{album_song_id}')]
        for album_song_id in album_songs_id
    ]
    buttons.append(
        [types.InlineKeyboardButton(text="Назад ↩", callback_data=f"singergroup_{genre_id}_{singer_group_id}")])
    markup = design_buttons(buttons)
    bot.send_message(callback.message.chat.id,
                     f"Альбом <em><b>{data['genres'][genre_id]['singers/groups'][singer_group_id]['albums'][album_id]['name']}</b></em>. Нажми <b>НАЗАД</b>, чтобы вернуться назад\n\n"
                     f"/help - Помощь/Обратная связь 💬\n"
                     f"P.S Сорян за скорость загрузки 🐌треков, сервера как никак¯\_(ツ)_/¯",
                     parse_mode="html", reply_markup=markup)
    # bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('albumsong_'))
def get_album_song(callback):
    _, genre_id, singer_group_id, album_id, album_song_id = callback.data.split('_')
    song_path = data["genres"][genre_id]["singers/groups"][singer_group_id]["albums"][album_id]["songs"][album_song_id][
        "src"]
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text="Назад ↩", callback_data=f"album_{genre_id}_{singer_group_id}_{album_id}")
    markup.row(back)
    bot.send_message(callback.message.chat.id, "⏳")
    with open(song_path, "rb") as audio:
        bot.send_audio(callback.message.chat.id, audio, reply_markup=markup, timeout=60)
    bot.delete_message(callback.message.chat.id, callback.message.message_id + 1)
        # bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.callback_query_handler(func=lambda cb: cb.data.startswith('song_'))
def get_song(callback):
    _, genre_id, singer_group_id, song_id = callback.data.split('_')
    song_path = data["genres"][genre_id]["singers/groups"][singer_group_id]["songs"][song_id]["src"]
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text="Назад ↩", callback_data=f"singergroup_{genre_id}_{singer_group_id}")
    markup.row(back)
    bot.send_message(callback.message.chat.id, "⏳")
    with open(song_path, "rb") as audio:
        bot.send_audio(callback.message.chat.id, audio, reply_markup=markup, timeout=60)
    bot.delete_message(callback.message.chat.id, callback.message.message_id+1)
    # bot.delete_message(callback.message.chat.id, callback.message.message_id)

########################################################################################################################
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.reply_to(message, "Стикер крутой, не спорю, но все же выбери нужную тебе категорию🤗.")


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


bot.polling(none_stop=True)