import pytesseract
import config
import config._config_1
import config._config_screenshots
from depend.screenshotter import screenshot

pytesseract.pytesseract.tesseract_cmd = config._config_1.tesseract_exe_path

def get_ui_title():
    return pytesseract.image_to_string(screenshot().crop(config._config_screenshots.ui_title_bbox))