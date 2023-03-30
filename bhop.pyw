import keyboard
import time
import threading
import pystray
import os
import win32gui
from PIL import Image


def on_quit():
    os._exit(0)


def bunny_hop():
    while keyboard.is_pressed('space'):
        keyboard.press('space')
        keyboard.release('space')
        time.sleep(0.01)


def handle_bunny_hop(hotkey=None):
    bunny_hop()


def set_hotkeys(action):
    keys = ['', 'ctrl+', 'shift+', 'tab+', 'right_ctrl+', 'right_shift+', 'alt+']
    for key in keys:
        hotkey = key + 'space'
        if action == "add":
            keyboard.add_hotkey(hotkey, handle_bunny_hop, args=(hotkey,))
        elif action == "remove":
            keyboard.remove_hotkey(handle_bunny_hop)


def run_systray():
    image = Image.open("logo_bhop.png")
    menu = pystray.Menu(pystray.MenuItem('Quit', on_quit))
    icon = pystray.Icon("SL-Utils B-Hop", image, "SL-Utils B-Hop", menu)
    icon.run()


t = threading.Thread(target=run_systray)
t.start()

active_window_name = ""
target_window_name = "Shatterline"
hotkeys_set = False

while True:
    current_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if current_window_name != active_window_name:
        active_window_name = current_window_name
        if active_window_name == target_window_name and not hotkeys_set:
            set_hotkeys("add")
            hotkeys_set = True
        elif active_window_name != target_window_name and hotkeys_set:
            set_hotkeys("remove")
            hotkeys_set = False
    time.sleep(1)
