import keyboard
import time
import threading
import pystray
import os
from PIL import Image
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

mouse = MouseController()
keyboards = KeyboardController()


def spammer():  # code inspired by mimky
    print('starting Anti-AFK in 5...')
    time.sleep(5)
    print('started')
    while True: 
        if not toggle_value:
            time.sleep(0.1)
            continue

        while True: 
            if not toggle_value:
                break
            for i in range(50):
                if not toggle_value:
                    continue
                time.sleep(0.01)
                keyboards.press('w')
            keyboards.release('w')
            time.sleep(1)

            for i in range(60):
                if not toggle_value:
                    continue
                time.sleep(0.01)
                keyboards.press('a')
            keyboards.release('a')
            time.sleep(1)

            for i in range(75):
                if not toggle_value:
                    continue
                time.sleep(0.01)
                keyboards.press('s')
            keyboards.release('s')
            time.sleep(1)

            for i in range(55):
                if not toggle_value:
                    continue
                time.sleep(0.01)
                keyboards.press('d')
            keyboards.release('d')
            time.sleep(1)
            
            for i in range(35):
                if not toggle_value:
                    continue
                time.sleep(0.01)
                keyboards.press(Key.space)
            keyboards.release(Key.space)
            time.sleep(1)

            if not toggle_value:
                continue
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(1)

            if not toggle_value:
                break


def spammer_thread():
    if toggle_value:
        spammer()


toggle_value = False
t = None


def on_quit():
    os._exit(0)


def toggle_bool():
    global toggle_value, t
    toggle_value = not toggle_value
    if toggle_value:
        print("Anti-AFK active.")
        if t is None:
            t = threading.Thread(target=spammer_thread)
            t.start()
    else:
        print("Anti-AFK inactive.")


def run_systray():
    image = Image.open("logo_anti_afk.png")
    menu = pystray.Menu(pystray.MenuItem('Quit', on_quit))
    icon = pystray.Icon("SL-Utils Anti-AFK", image, "SL-Utils Anti-AFK", menu)
    icon.run()


t_systray = threading.Thread(target=run_systray)
t_systray.start()

keyboard.add_hotkey('ctrl+x', lambda: toggle_bool())
keyboard.wait()
