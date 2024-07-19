#DJ_Sona_Bot.py
#Works with YT links

import asyncio
import discord
from discord.ext import commands
import os
from help_cog import help_cog
from music_cog import music_cog
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='-dj ', intents = intents)

bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guild:\n')
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')
    
    await bot.change_presence(activity=discord.Game(name="This party's getting crazy!"))
    await bot.load_extension("help_cog")
    await bot.load_extension("music_cog")
    

bot.run(TOKEN)
    



