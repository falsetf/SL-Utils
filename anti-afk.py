import keyboard
import time
import threading
import pystray
import os
from PIL import Image

toggle_value = False
t = None


def on_quit():
    os._exit(0)


def toggle_bool():
    global toggle_value, t
    toggle_value = not toggle_value
    if toggle_value:
        t = threading.Thread(target=anti_afk)
        t.start()


def anti_afk():
    while toggle_value:
        print("Anti-AFK active.")
        try:
            time.sleep(5)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.press('a')
            time.sleep(1)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.release('a')
            time.sleep(5)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.press('d')
            time.sleep(1)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.release('d')
            time.sleep(5)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.press('space')
            time.sleep(1)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.release('space')
            time.sleep(5)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.press('w')
            time.sleep(1)
            if not toggle_value:
                print("Anti-AFK inactive.")
                break
            keyboard.release('w')
        except RuntimeError:
            pass


def run_systray():
    image = Image.open("logo_anti_afk.png")
    menu = pystray.Menu(pystray.MenuItem('Quit', on_quit))
    icon = pystray.Icon("SL-Utils Anti-AFK", image, "SL-Utils Anti-AFK", menu)
    icon.run()


t = threading.Thread(target=run_systray)
t.start()

keyboard.add_hotkey('ctrl+x', lambda: toggle_bool())
keyboard.wait()
