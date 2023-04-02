import os
import time
import keyboard
import pystray
from PIL import Image
import threading


def on_quit(icon, item):
    icon.stop()
    os._exit(0)


def orbit_ult():
    keyboard.press('q')
    keyboard.release('q')
    time.sleep(0.25)
    keyboard.press('shift')
    keyboard.release('shift')


def on_key_event(event):
    if event.event_type == 'down' and event.name == 'alt':
        orbit_ult()


def hotkey_listener():
    keyboard.hook(on_key_event)
    keyboard.wait()


def run_systray():
    image = Image.open("logo_orbit.png")
    menu = pystray.Menu(pystray.MenuItem('Quit', on_quit))
    icon = pystray.Icon("SL-Utils Perfect Orbit Ult", image, "SL-Utils Perfect Orbit Ult", menu)
    icon.run()


if __name__ == "__main__":
    hotkey_thread = threading.Thread(target=hotkey_listener, daemon=True)
    hotkey_thread.start()
    run_systray()
