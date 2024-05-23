import config
import config._config_screenshots
from depend.screenshotter import screenshot



def is_open():
    r,g,b = screenshot().crop(config._config_screenshots.chat_button_bbox).resize((1,1),3).getpixel((0,0))
    return r>200 and g>200 and b>200