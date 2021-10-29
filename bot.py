import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!y')

@bot.event
async def on_ready():
    print(">>bot is online<<")
bot.run('OTAzNjc5MDk2MjkzMjk0MTQw.YXwevg.K9CkFX8ZWiM4vWvov7obXfyYNfk')