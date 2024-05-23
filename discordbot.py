from nextcord.ext import commands,tasks
import nextcord

import config._config_bot
import mods
import config
import config._config_1
import detector
import detector.biome
import mods.antiafk
import mods.biome

bot = commands.Bot(intents=nextcord.Intents.all(),activity=nextcord.Activity(
    name="my sanity go down on Sol's RNG",
    type=nextcord.ActivityType.listening,
))

enabled = {
    "antiafk": False,
    "biomechecker": False,
}

async def check(interaction: nextcord.Interaction):
    if interaction.user.id in config._config_bot.owner_ids:
        return True
    await interaction.send("Nuh uh uh!",ephemeral=True)
 
@bot.slash_command(description="Turns AntiAFK on, but never off.")
async def anti_afk(interaction: nextcord.Interaction):
    if await check(interaction):
        if enabled["antiafk"]:
            await interaction.send("i didnt ask (it's already running)")
        else:
            await interaction.send("anti-afking")
        enabled["antiafk"] = True

@bot.slash_command(description="Toggles Biome Announcer")
async def biome_announcer(interaction: nextcord.Interaction,toggle: bool):
    if await check(interaction):
        enabled["biomechecker"] = toggle
        if toggle:
            await interaction.send("Turned on biome announcer.")
        else:
            await interaction.send("Turned off biome announcer.")

@bot.slash_command(description="Gets the biome")
async def get_biome(interaction: nextcord.Interaction):
    await interaction.send(detector.biome.get_biome())

@tasks.loop(seconds=config._config_1.biome_check_time_seconds)
async def do_biome_announce():
    if enabled["biomechecker"]:
        mods.biome.check()

@tasks.loop(seconds=10)
async def do_antiafk():
    if enabled["antiafk"]:
        mods.antiafk.galaw()

@bot.event
async def on_ready():
    do_biome_announce.start()
    do_antiafk.start()
    print("ready")

bot.run(config._config_bot.bot_token)