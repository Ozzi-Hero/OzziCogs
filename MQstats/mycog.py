from redbot.core import commands

class MQstats(commands.Cog):

    @commands.group()
    async def adcalc(self, ctx, might: int, health: int, defence: int):
        defence = defence / 100
        await ctx.send(might)
        await ctx.send(health)
        await ctx.send(defence)

    @MQstats.command(name="wise")
    async def MQstats_wise(self, ctx):
        await ctx.send("f")