import threading
import ollama
import io
import pygame
from gtts import gTTS

# only need to start the pygame mixer once
pygame.mixer.init()

# stuff needed to share between threads
words = []
speak_text = ""

# the ollama stream function, its own thread
def ollama_stream():
    stream = ollama.chat(
        model='mistral',
        messages=[{'role': 'user', 'content': 'Tell me a story?'}],
        stream=True,
    )

    for chunk in stream:
        word = chunk['message']['content'].strip() + " "
        words.append(word)
        print(word, end='', flush=True)

# create and start the ollama thread
stream_thread = threading.Thread(target=ollama_stream, daemon=True)
stream_thread.start()

# the speak function which will be its own thread
def speak():
    with io.BytesIO() as f:
        gTTS(text=speak_text, lang='en').write_to_fp(f)
        f.seek(0)
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

# go through the words list and see if it is big enough to send to the speak thread
speak_thread = threading.Thread(target=speak, daemon=True)
pos = 0
# Coulnt find a good way to stop this loop
# so need to manually stop program
while True:
    size = len(words) - pos
    # if the thread is not running and the next batch is ready start the thread
    if not speak_thread.is_alive() and size >= 5:
        speak_text = ""
        for i in range(pos, len(words)):
            speak_text += words[i]
        pos += size
        speak_thread = threading.Thread(target=speak, daemon=True)
        speak_thread.start()

# this is to catch the last bit of the text
# never gets to this point tho
for i in range(len(words) - pos, len(words)):
  speak_text = ""
  for i in range(pos, len(words)):
    speak_text += words[i]
  speak()