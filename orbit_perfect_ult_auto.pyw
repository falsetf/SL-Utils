import os
import pyautogui
import time
import keyboard
import pystray
from PIL import Image
import threading

# even though this is intended to be a pyw, print statements are still present for debugging purposes.

# keep track of the number of times the image is detected in a row
count = 0
counter_2 = 0


def on_quit(icon, item):
    icon.stop()
    os._exit(0)


def orbit_ult():
    keyboard.press('q')
    keyboard.release('q')
    time.sleep(0.25)
    keyboard.press('shift')
    keyboard.release('shift')


image_files = ["orbit.png", "orbit2.png", "orbit3.png", "orbit4.png", "orbit5.png", "orbit6.png"]


def locate_images():
    locations = []

    for image_file in image_files:
        locations.extend(list(pyautogui.locateAllOnScreen(image_file, grayscale=True, confidence=0.75, region=(0, 540, 960, 540))))

    return locations


def main_loop():
    global count, counter_2
    while True:
        locations = locate_images()

        # if img is detected 3 times, bind left alt to orbit_ult()
        if locations:
            print("Orbit detected.")
            print(locations)
            count += 1
            if count == 3 and keyboard.parse_hotkey_combinations('alt'):
                keyboard.add_hotkey('alt', lambda: orbit_ult())
                count = 0
                print("Orbit active.")
        # if the img is not detected 3 times, unbind left alt
        else:
            print(locations)
            counter_2 += 1
            if counter_2 == 3:
                try:
                    if keyboard.parse_hotkey_combinations('alt'):
                        keyboard.unhook_all()
                        print("Orbit inactive.")
                except ValueError:
                    pass
                counter_2 = 0
            else:
                print("Orbit not detected.")

        # wait 1 second before checking again
        time.sleep(1)


def run_systray():
    image = Image.open("logo_orbit.png")
    menu = pystray.Menu(pystray.MenuItem('Quit', on_quit))
    icon = pystray.Icon("SL-Utils Perfect Orbit Ult", image, "SL-Utils Perfect Orbit Ult", menu)
    icon.run()


if __name__ == "__main__":
    main_loop_thread = threading.Thread(target=main_loop)
    main_loop_thread.daemon = True
    main_loop_thread.start()
    run_systray()
