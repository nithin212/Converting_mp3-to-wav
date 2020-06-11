#!pip install pipwin
#!pipwin install pyaudio
# !pip install ffmpeg-python
# !pip install pydub


import pydub
pydub.AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"
sound = AudioSegment.from_mp3("Filename.mp3")
sound.export("converted_file.wav", format="wav")
