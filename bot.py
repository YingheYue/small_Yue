import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!y ',intents = intents)


@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(903714164286033920)
    await channel.send(f'{member}跑了進來')

@bot.event 
async def on_member_remove(member):
    print(f'{member}離開')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('OTAzNjc5MDk2MjkzMjk0MTQw.GTHSBu.lR8CCPZaLOwvTL9jsZVQ6SMktf-88OB4LSLW1c')