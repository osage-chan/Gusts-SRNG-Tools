from discord_webhook import DiscordWebhook, DiscordEmbed
from time import time as tick
import _config as cf

link = cf.webhook_link
def rollfiftyk():
    webhook = DiscordWebhook(url=link, content=f"<@{cf.aura_check_ping_user_id}>")
    webhook.add_embed(DiscordEmbed(
        title="50k+ Roll",
        description=f"Tell gust to check RIGHT NOW <t:{round(tick())}:R>"
    ))
    webhook.execute()

def sendbiome(biome,ping):
    acping = f"<@&{cf.biome_check_ping_role_id}> "
    if not ping:
        acping = ""
    webhook = DiscordWebhook(url=link, content=acping)
    embed = DiscordEmbed(
        title=f"Biome Changed: {biome}",
        description=f"Join RIGHT NOW <t:{round(tick())}:R>"
    )
    embed.set_url("https://www.roblox.com/share?code=dbe5e54576aa384391a084d28c22fc08&type=Server")
    webhook.add_embed(embed)

    webhook.execute()