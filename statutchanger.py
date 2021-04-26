import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

import random
import asyncio

bot = commands.Bot(command_prefix="!",help_command=None, intents=intents)

memberss = []

## CONFIG ##

token = ""

delay = 5

MessageBeforeTheNameOfMember = "Hey "

## CONFIG END


@bot.event
async def on_ready():

    print("Bot connected")

    global memberss

    for guild in bot.guilds:
        for member in guild.members:
            memberss.append(member)

        while True:
            
            memberchoose = random.choice(memberss)
            await bot.change_presence(activity=discord.Game(name=str(MessageBeforeTheNameOfMember)+str(memberchoose)))
            await asyncio.sleep(delay)



    

bot.run(str(token))
