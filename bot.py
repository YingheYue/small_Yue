from codecs import utf_8_encode
from encodings import utf_8, utf_8_sig
import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding=utf_8) as jFile:
    jdata = json.load(jFile)


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

    bot.run(jdata['TOKEN'])