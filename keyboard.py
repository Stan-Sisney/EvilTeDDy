from pynput.keyboard import Listener

def on_press(key):
    # Handle key press events here
    print(f"Key pressed: {key}")

with Listener(on_press=on_press) as listener:
    listener.join()