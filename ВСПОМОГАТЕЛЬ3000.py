import os

music = os.path.abspath(os.path.join(os.path.sep, "Users", "Вадим", "PycharmProjects", "Main_IDE", "tracks"))
for root, subFolder, files in os.walk(music):
    for item in files:
        if item.endswith(".mp3"):
            tracks.append(item)