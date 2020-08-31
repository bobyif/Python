import pynput

from pynput.keyboard import Key, Listener

def on_release(key):
    if key == Key.esc:
        break

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()