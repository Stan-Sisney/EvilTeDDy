from pynput import keyboard
import asyncio
from ollama import AsyncClient
#import pygame
from gtts import gTTS
#import io
import ollama
from time import sleep

global string
string = ""

async def chat():
  global string
  string=""
  bigmsg = ""
  msg = ""
  stream = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': 'What is 3 + 3?'}], stream=True,)

  #for chunk in stream:
   #print(chunk['message']['content'], end='', flush=True)
  #print(stream)
  msg = (stream)
   #print(msg)
  if len(bigmsg) < 25:
   print('waiting')
   bigmsg = msg
   print(bigmsg) 
  elif len(bigmsg) > 25:
   #global string
   #string = bigmsg
   print(bigmsg)
   bigmsg = ""
   #string = ""
   print('cleared')
   #print(part['message']['content'], end='', flush=True)
   #pass
   #return string;      
asyncio.run(chat())

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
listener = keyboard.Listener(on_release=on_release)
listener.start()

while listener.is_alive():
    print('key')
    sleep(5)


