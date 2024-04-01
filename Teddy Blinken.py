import time
import random
from pynput import keyboard
from time import sleep
from adafruit_servokit import ServoKit

# 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
listener = keyboard.Listener(on_release=on_release)
listener.start()

while listener.is_alive():
    # eyes
    kit.servo[2].angle = 180
    time.sleep(.25)
    kit.servo[2].angle = 0
    
    #random.randrange(start, stop[, step])
    x = random.randrange(1,10,1)
    print(x)
   
    time.sleep(x)

