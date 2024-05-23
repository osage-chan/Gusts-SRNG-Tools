from depend import quickhooks
from detector import biome
from time import sleep
import config._config_1 as cf

last = ""
agreement = ""
def check():
    global last,agreement
    current = biome.get_biome()
    if current == agreement:
        if current != last:
            print("Biome changed:",current)
            if not (current.lower() in cf.biome_check_ignore):
                quickhooks.sendbiome(current,current.lower() in cf.biome_check_ping)
                #print(current,current.lower(),current.lower() in ignorelist)
        if current != "N/A":
            last = current
    else:
        print(current,"?")
    agreement = current