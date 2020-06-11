#!pip install pipwin
#!pipwin install pyaudio
# !pip install ffmpeg-python
# !pip install pydub
#!pip install SpeechRecognition

import speech_recognition as sr
import sys
import pydub
pydub.AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"
sound = AudioSegment.from_mp3("Filename.mp3")
sound.export("converted_file.wav", format="wav")
r=sr.Recognizer()
filename="g.wav"
with sr.AudioFile(filename) as source:
    audio=r.record(source)
try:
    text=r.recognize_google(audio)
    print(text)
except Exception:
    print("Something went wrong")
