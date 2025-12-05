from pynput.keyboard import Key, Listener, KeyCode
from tkinter import *
import pygame

root = Tk()
root.title('Lizard')

def stopButtonEvent():
    root.destroy()

stop_button = Button(root, text= "Stop", command=stopButtonEvent)
stop_button.pack()

root.iconify()

pygame.mixer.init()

def on_press(key = KeyCode):
    try:
        if (type(key) == KeyCode):
            if key == KeyCode.from_char('l') or key == KeyCode.from_char('L'):
                pygame.mixer.music.load('lizard-button-sound.mp3')
                pygame.mixer.music.play(loops=0)
        else:
            pass
    except Exception as e:
        print(f"An exeption occured: {e}")


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        #Close (Redundant?)
        root.destroy()
        # Stop listener
        return False

# Collect events until released
listener  = Listener(
        on_press=on_press,
        on_release=on_release)
listener.start()

root.mainloop()

