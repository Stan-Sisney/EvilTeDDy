import speech_recognition as sr
import pyaudio

for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print(name, " ", index)
    pass

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    #r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.record(source, duration=3)

# recognize speech using Sphinx
try:
    #text = r.recognize_sphinx(audio)
    text = r.recognize_google(audio)
    print("Teddy thinks you said " + text)
except sr.UnknownValueError:
    print("Teddy could not understand audio")
except sr.RequestError as e:
    print("Teddy error; {0}".format(e))