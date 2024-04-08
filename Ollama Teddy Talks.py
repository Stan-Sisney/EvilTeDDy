import ollama
import io
import pygame
from gtts import gTTS

ollama.pull('mistral')
stream = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'do you like Mozart?'}],
    stream=False,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True) 