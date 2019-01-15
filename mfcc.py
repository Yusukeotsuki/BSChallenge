import librosa.display
import matplotlib.pyplot as plt

# Load a flac file from 0(s) to 60(s) and resample to 4.41 KHz
filename = "filename"
y, sr = librosa.load(filename, sr=4410, offset=0.0, duration=60.0)
librosa.display.waveplot(y=y, sr=sr)


# n_mels is number of Mel bands to generate
n_mels=128
# hop_length is number of samples between successive frames.
hop_length=2068
# n_fft is length of the FFT window
n_fft=2048
# Passing through arguments to the Mel filters
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, hop_length=hop_length, n_fft=n_fft)

log_S = librosa.power_to_db(S, ref_power=np.max)
print(log_S.shape)

plt.figure(figsize=(12, 4))
librosa.display.specshow(data=log_S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel spectrogram')
plt.tight_layout()

