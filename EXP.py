import asyncio
from ollama import AsyncClient
import pygame
from gtts import gTTS
import io
import ollama

stream = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
    )


buffer = io.BytesIO ()
for chunk in stream.iter_bytes(chunksize=4096):
  buffer.print(chunk['message']['content'], end='', flush=True)
buffer.seek(0)