from redbot.core import commands
import discord

class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @commands.command()
    async def createchannel(self, ctx, name):
        guild = ctx.message.guild
        await guild.create_text_channel(name, category=category)