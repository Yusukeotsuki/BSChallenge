import pyaudio
import sys
import time
import wave
import matplotlib.pyplot as plt

class Record:

    def __init__(self):
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 3


    def recording(self, file_path):
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


