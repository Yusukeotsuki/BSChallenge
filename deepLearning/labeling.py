import os
import numpy as np
import glob
from glob import glob
import shutil

dirlist = os.listdir("../Perfume/")

for element in dirlist:
    view_count = int(element.split("&_&")[0].split("=")[1])
    youtube_id = element.split("&_&")[1]
    num_wav = len(os.listdir("../Perfume/" + element + "/"))
    if view_count > 1000000:
        for n in range(1,num_wav):
            shutil.copyfile("../Perfume/{}/{}.png".format(element, n),\
                    "learning_data/popular/{}_{}.png".format(youtube_id, n))
    else:
        for n in range(1, num_wav):
            shutil.copyfile("../Perfume/{}/{}.png".format(element, n),\
                    "learning_data/miner/{}_{}.png".format(youtube_id, n))

