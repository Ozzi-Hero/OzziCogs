from redbot.core import commands

class MQstats(commands.Cog):

    @commands.command()
    async def adcalc(self, ctx, might: int, health: int, defence: int):
        defence = defence / 100
        await ctx.send(might)
        await ctx.send(health)
        await ctx.send(defence)