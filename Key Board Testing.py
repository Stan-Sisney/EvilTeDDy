#import keyboard
"""import tty
import sys
import termios
orig_settings = termios.tcgetattr(sys.stdin)

tty.setcbreak(sys.stdin)
x = 0 
while x != chr(27): #esc
    x=sys.stdin.read(1)[0]
    print("Ya",x)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)"""

from pynput import keyboard

def on_press(key):
    print(f"Key pressed: {key}")
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.start()



"""
running =True
price=""

while running:
    if keyboard.is_pressed("1"):
        price+="1"
    if keyboard.is_pressed("2"):
        price+="2"
    if keyboard.is_pressed("Enter"):
        running=False

subtotal=int(price)
print(subtotal)
subtotal=float(subtotal)/100

print("Subtotal: {}".format(subtotal))
"""