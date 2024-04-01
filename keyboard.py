from pynput import keyboard
from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
listener = keyboard.Listener(on_release=on_release)
listener.start()

while listener.is_alive():
    kit.servo[2].angle = 180
    sleep(.25)
    kit.servo[2].angle = 0
    sleep(3)