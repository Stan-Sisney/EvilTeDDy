import time
import random
from pynput import keyboard
from time import sleep

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
listener = keyboard.Listener(on_release=on_release)
listener.start()

while listener.is_alive():
    
    #random.randrange(start, stop[, step])
    x = random.randrange(1,10,1)
    print(x)
   
    time.sleep(x)

