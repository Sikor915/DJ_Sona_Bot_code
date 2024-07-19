import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
        ```
        Commands:
        -dj help: Displays this message
        -dj play <song>: Plays the song
        -dj pause: Pauses the song
        -dj resume: Resumes the song
        -dj skip: Skips the current song
        -dj queue: Displays the current songs in queue
        -dj clear: Clears the queue
        -dj disconnect: Disconnects the bot from the voice channel
        ```
        """
        
        self.text_channel_text = []        

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)
    
        #await self.send_to_all(self.help_message)
        
    async def send_to_all(self, msg):
        for channel in self.text_channel_text:
            await channel.send(msg)
            
    @commands.command(name="help", help="Displays the help message")
    async def help(self, ctx):
        await ctx.send(self.help_message)
        
async def setup(bot):
    await bot.add_cog(help_cog(bot))

