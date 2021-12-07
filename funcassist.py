
import librosa
audio_path = librosa.util.example_audio_file()
# or uncomment the line below and point it at your favorite song:
audio_path = 'D:\Audio\Arijit singh audio\Arijit Singh Mega Hits (100 Songs) [DJMaza.Life]\49 - Jiya - Arijit Singh [DJMaza.Life]'
y, sr = librosa.load(audio_path)
y_percussive = librosa.effects.hpss(y)
tempo, beats = librosa.beat.beat_track(y=y_percussive, sr=sr)