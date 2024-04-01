import io
#import pygame
#from gtts import gTTS
from pynput import keyboard
from time import sleep

#init a string var
#stark keybopard list
#build string up
#hit enter pass string to gtts
#play sound
#esc stops everything

x=""
y=""
def on_press(key):
    x=key    
    y=(x)
    print(y) 
    if key == keyboard.Key.enter:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press,) as listener:
    listener.join()

    