from time import sleep
import config
import config._config_screenshots
from depend import utils
from depend.screenshotter import screenshot
from detector import chat, ui
import pynput

mouse = pynput.mouse.Controller()

def get():
    if ui.get_ui_title().lower() == "storage":
        print("Screenshotting...")
        screenshot().crop(658,364,1896,1076).save("temporary/auras.png")
        return "temporary/auras.png"
    elif chat.is_open():
        x,y = utils.center_bbox(config._config_screenshots.chat_button_bbox)
        print("Chat is open. Clicking...")
        mouse.position = (x,y)
        sleep(0.1)
        mouse.press(pynput.mouse.Button.left)
        sleep(0.1)
        mouse.release(pynput.mouse.Button.left)
        return get()
    else:
        x,y = config._config_screenshots.storage_button
        print("Storage UI is closed. Opening...")
        mouse.position = (x,y)
        sleep(0.1)
        mouse.press(pynput.mouse.Button.left)
        sleep(0.1)
        mouse.release(pynput.mouse.Button.left)
        return get()