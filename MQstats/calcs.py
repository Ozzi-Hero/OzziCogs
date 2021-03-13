from redbot.core import commands
import discord

from redbot.core import Config, checks, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box, pagify
from asyncio import sleep

class Mycog(commands.Cog):

    #@commands.command()
    #async def adcalc(self, ctx):
     #   await ctx.send("Welcome to the adrenaline optimisation module")
#
 #       #Might level collection
  #      await ctx.send("Please send your might")

    @commands.command()
    async def test(self, ctx, args1, args2, args3):
        await ctx.send(f"1. {args1}\n2. {args2}\n3. {args3}")
