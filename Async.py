import ollama
import asyncio
from ollama import AsyncClient
from pynput import keyboard
from time import sleep

# declare my gloabl var
string = ""

#ollama.pull('mistral') #only needed if mistral is already dl

async def chat(): # async function
  
  global string  # ref the global variable 
  string = ""  # pull it into the function
  bigmsg = "" # string to be built up
  message = {'role': 'user', 'content': 'what is 3 +3?'}
  
  async for part in await AsyncClient().chat(model='mistral', messages=[message], stream=True):
    
    if len(message) < 25:
        print('waiting')
        bigmsg = bigmsg + part['message']['content']
        if len(bigmsg) > 25:
            string = bigmsg
            print(string)
            bigmsg = "" #empty big msg out                           
asyncio.run(chat())


print("i am here too")


"""async def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
listener = keyboard.Listener(on_release=on_release)
listener.start()

while listener.is_alive():
    print("hit esc to stop")
    print(string)
    sleep(5)

asyncio.run(on_release)"""