from redbot.core import commands
import discord

from redbot.core import Config, checks, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box, pagify
from asyncio import sleep

class Mycog(commands.Cog):

    @commands.command()
    async def adcalc(self, ctx):
        await ctx.send("Welcome to the adrenaline optimisation module")

        #Might level collection
        await ctx.send("Please send your might")
        
        #Member object
        pred = MessagePredicate.valid_member(ctx)
        await bot.wait_for("message", check=pred)
        member = pred.result

        await ctx.send(member.mention)
