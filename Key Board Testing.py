from pynput import keyboard

def on_press(key):
    print(f"Key pressed: {key}")
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.start()