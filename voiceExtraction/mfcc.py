import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

def calc_mfcc(infile_path,outfile_path):
    y, sr = librosa.load(infile_path, sr=4410, offset = 0.0)
    n_mels = 128
    hop_length = 2068
    n_fft = 2048
    S = librosa.feature.melspectrogram(y=y, \
            sr=sr,n_mels=n_mels, hop_length=hop_length, n_fft=n_fft)
    log_S = librosa.power_to_db(S, np.max)
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(data=log_S, \
            sr=sr, hop_length=hop_length, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    plt.savefig(outfile_path)
"""
for i in range(0,11):
    infile = "voiceExtraction/data/test_output/" + str(i) + ".wav"
    outfile = str(i) + ".png"
    calc_mfcc(infile,outfile)
"""
"""

note

データベースの構造は以下を想定した方が今後扱いやすい
と考えられるため、それを守って作ってくれると良いと思う

data ----input----- --artist1-----music1--------------1.wav
                    |           |            |
                    |           |            |
                    |           |            ---------2.wav
                    |           |            |...
                    |           |
                    |           |
                    |           ---music2...
                    |           |...
                    |
                    |
                    ---artist2---....
                    |
                    |...

（インプット配下に


"""
cwd = os.getcwd()
artists_list = os.listdir(cwd + "/data/input/")
for artist in artists_list:
    music_list = os.listdir(cwd + "/data/input/" + artist + "/")
    for music in music_list:
        wavfiles = os.listdir("{}/data/input/{}/{}/".format(cwd, artist, music))
        for wavfile in wavfiles:
            infile_path  = "{}/data/input/{}/{}/{}".format(cwd, artist, music, wavfile)
            outfile_path = "{}/data/output/{}/{}/{}.png".format(cwd, artist, music, wavfile.replace(".wav", ""))
            print(infile_path)
            print(outfile_path)
