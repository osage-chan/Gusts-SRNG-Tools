#guhw on discord!#
##################
### HOW ##########
##################

## YOU NEED TO RESTART THE BOTS IF YOU CHANGE SOMETHING RELATED TO THEM

# FILENAME - DESC
#### TECHNICAL EXPLANATION

# biomebot.py - Self-explanatory.
#### Reads the text at the bottom left.

# rollbot.py -  Run to get pinged everytime the roll cutscene plays. 
#### Checks if your screen fades to black.

##################
### GLOBALS ######
##################

webhook_link = "https://discord.com/api/webhooks/0000000000000000000/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaa23232323232323"

# Check tutorial/read.md if you don't know what to do with this one.
biome_bbox = (0,1309,477,1352)

tesseract_exe_path = "C:/Program Files/Tesseract-OCR/tesseract.exe"

##################
### WAIT TIMES ###
##################
## Setting these too quick MAY break your pc's disk.

biome_check_time_seconds = 5
# Default: 5

aura_check_time_seconds = 0.25
# Default: 0.25

##################
### Biome Ping ###
##################
# rollbot.py
biome_check_ping_role_id = 0000000000000000000

# Will ping with the message if these biomes are found
# all lowercase.
biome_check_ping = [
    "corruption",
    "starfall",
    "null",
    "glitched"
]

# Will not send a message if these biomes are found
# all lowercase.
biome_check_ignore = [
    "n/a", # N/A is used if it could not detect the current biome.
    "normal",
    "snowy",
    "rainy",
    "windy"
]

##################
### Aura Bot #####
##################
# rollbot.py

# Who to ping whenever an aura cutscene is detected.
aura_check_ping_user_id = 0000000000000000000

# How black should a pixel on your screen be to be considered in the cutscene?
# Example: if you set this to 10, the RGB needs to be less than 10.
aura_check_sensitivity = 10
# Default: 10

# How many black pixels should be on your screen to be considered in the roll cutscene?
aura_check_percentage = 95
# Default: 95