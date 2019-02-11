import pyaudio
import sys
import time
import wave
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import glob
import os

class Record:

    def __init__(self):
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 3

    def recording(self, file_path):
        self.infile_path = file_path
        chunk          = self.chunk
        FORMAT         = self.FORMAT
        CHANNELS       = self.CHANNELS
        RATE           = self.RATE
        RECORD_SECONDS = self.RECORD_SECONDS

        p = pyaudio.PyAudio()
        stream = p.open(
            format = FORMAT,
            channels = CHANNELS,
            rate = RATE,
            input = True,
            frames_per_buffer = chunk
        )

        frames = []

        for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
            data = stream.read(chunk)
            frames.append(data)

        stream.close()
        p.terminate()
        data = b''.join(frames)
        
        wav = wave.open(file_path, "wb")
        wav.setnchannels(1)
        wav.setsampwidth(p.get_sample_size(FORMAT))
        wav.setframerate(44100)
        wav.writeframes(b''.join(frames))
        wav.close()


    def calc_mfcc(self, file_path):
        y, sr = librosa.load(self.infile_path, sr=4410, offset = 0.0)
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
        plt.savefig(file_path)

