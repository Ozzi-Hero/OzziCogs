from redbot.core import commands

from redbot.core import checks, commands
from redbot.core.utils.chat_formatting import box, pagify
from asyncio import sleep

class Mycog(commands.Cog):

    @commands.command()
    async def adcalc(self, ctx):
        await ctx.send("Welcome to the adrenaline optimisation module")

        #Might integer collection
        await ctx.send("Please send your might")
        mightStr = await self.bot.wait_for("message", timeout=120, check=check)
        #float conversion and comma removal
        await sleep(0.2)

        #HP integer collection
        await ctx.send("Please send your HP")
        hpStr = await self.bot.wait_for("message", timeout=120, check=check)
        #float conversion and comma removal
        await sleep(0.2)

        #Defence integer collection
        await ctx.send("Please send your def %")
        defStr = await self.bot.wait_for("message", timeout=120, check=check)
        #int conversion and % removal
        #float conversion

        await ctx.send(mightStr)
        await ctx.send(hpStr)
        await ctx.send(defStr)

