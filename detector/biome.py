from depend.screenshotter import screenshot
from depend import quickhooks
import pytesseract
import re
import _config as cf

pytesseract.pytesseract.tesseract_cmd = cf.tesseract_exe_path
#bbox = (0,1309,477,1352)
bbox = cf.biome_bbox
biomeregex = r"\[ (.+) \]"

def get_biome():
    biomeimg = screenshot().crop(bbox)
    regex = re.findall(biomeregex,pytesseract.image_to_string(biomeimg))
    if len(regex) > 0:
        return regex[0]
    return 'N/A'