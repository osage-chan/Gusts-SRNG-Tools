from depend import quickhooks
from detector import biome
from time import sleep
import _config as cf

last = ""

while True:
    sleep(cf.biome_check_time_seconds)
    current = biome.get_biome()
    if current != last:
        print("Biome changed:",current)
        if not (current.lower() in cf.biome_check_ignore):
            quickhooks.sendbiome(current,current.lower() in cf.biome_check_ping)
            #print(current,current.lower(),current.lower() in ignorelist)
    if current != "N/A":
        last = current
    