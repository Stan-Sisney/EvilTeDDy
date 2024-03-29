from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

def speak(txt, lang='en'):
    gTTS(text=txt, lang=lang).write_to_fp(voice := NamedTemporaryFile())
    playsound(voice.name)
    voice.close()

txt = "Spank me, Daddy"
speak(txt)