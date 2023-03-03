import speech_recognition as speech_r
import pyaudio
import wave
import librosa

CHUNK = 1024 # определяет форму ауди сигнала
FRT = pyaudio.paInt16 # шестнадцатибитный формат задает значение амплитуды
CHAN = 1 # канал записи звука
RT = 44100 # частота
REC_SEC = 5 #длина записи
OUTPUT = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FRT,channels=CHAN,rate=RT,input=True,frames_per_buffer=CHUNK) # открываем поток для записи
print("rec")
frames = [] # формируем выборку данных фреймов
for i in range(0, int(RT / CHUNK * REC_SEC)):
    data = stream.read(CHUNK)
    frames.append(data)
print("done")

stream.stop_stream() # останавливаем и закрываем поток
stream.close()
p.terminate()

w = wave.open(OUTPUT, 'wb')
w.setnchannels(CHAN)
w.setsampwidth(p.get_sample_size(FRT))
w.setframerate(RT)
w.writeframes(b''.join(frames))
w.close()

r = speech_r.Recognizer()
sample = speech_r.WavFile('C:\\Users\\rewrewrew\\PycharmProjects\\pythonProject1\\output.wav')
type(sample)

# Create audio data
with sample as source:
    audiodata = r.record(sample)
type(audiodata)

with sample as audio:
    content = r.record(audio)
    r.adjust_for_ambient_noise(audio)

# Extract text
text = r.recognize_google(audio_data=audiodata, language='ru-RU')

print(text)

