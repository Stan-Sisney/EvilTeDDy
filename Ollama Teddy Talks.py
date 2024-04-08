import ollama
import io
import pygame
from gtts import gTTS
import asyncio
from ollama import AsyncClient

#ollama.pull('mistral')
stream = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'what is 3+3?'}],
    stream=False,)

x =(stream['message']['content'])

def speak(my_text):
    with io.BytesIO() as f:
        gTTS(text=my_text, lang='en').write_to_fp(f)
        f.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

speak(x)