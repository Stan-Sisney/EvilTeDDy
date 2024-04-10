import ollama
import asyncio
from ollama import AsyncClient
from pynput import keyboard
from time import sleep

global string 
string = ""

#ollama.pull('mistral') #only needed if mistral is already dl
async def chat():
  global string
  bigmsg = ""
  message = {'role': 'user', 'content': 'what is 3 +3?'}
  async for part in await AsyncClient().chat(model='mistral', messages=[message], stream=True):
    
    if len(message) < 25:
        print('waiting')
        bigmsg = bigmsg + part['message']['content']
        if len(bigmsg) > 25:
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