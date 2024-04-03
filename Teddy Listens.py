import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    #text = r.recognize_sphinx(audio)
    text = r.recognize_google(audio)
    print("Teddy thinks you said " + text)
except sr.UnknownValueError:
    print("Teddy could not understand audio")
except sr.RequestError as e:
    print("Teddy error; {0}".format(e))