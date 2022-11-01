import pynput
import time

def on_press(key):
    if key == pynput.keyboard.Key.shift:
        time.sleep(0.25)
        pynput.keyboard.Controller().press(pynput.keyboard.KeyCode.from_char('q'))

def on_release(key):
    if key == pynput.keyboard.Key.shift:
        time.sleep(0.25)
        pynput.keyboard.Controller().release(pynput.keyboard.KeyCode.from_char('q'))

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()