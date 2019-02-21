import os
import numpy as np
import glob
from glob import glob
import shutil

dirlist = os.listdir("output/")

for artist in dirlist:
    music_list = os.listdir("output/" + artist + "/")
    for music in music_list:
        view_count = int(music.split("&_&")[0].split("=")[1])
        youtube_id = music.split("&_&")[1]
        num_wav = len(os.listdir("output/" + artist + "/" + music + "/"))
        if view_count > 1000000:
            for n in range(1,num_wav):
                shutil.copyfile("output/{}/{}/{}.png".format(artist,music, n),\
                    "learning_data/popular/{}_{}.png".format(youtube_id, n))
        else:
            for n in range(1, num_wav):
                shutil.copyfile("output/{}/{}/{}.png".format(artist,music, n),\
                    "learning_data/minor/{}_{}.png".format(youtube_id, n))

