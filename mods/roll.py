from detector.roll import is_black
from depend import quickhooks
from time import sleep
from time import time as tick
import config._config_1 as cf

last = tick()-9
def check():
    if tick()-last > 10:
        perc = is_black()
        sleep(cf.aura_check_time_seconds)
        print(perc)
        if perc > cf.aura_check_percentage:
            last = tick()
            quickhooks.rollfiftyk()