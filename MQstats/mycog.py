from redbot.core import commands

class Mycog(commands.Cog):

    @bot.group
    @commands.command()
    async def adcalc(self, ctx, might: int, health: int, defence: int):
        defence = defence / 100
        await ctx.send(might)
        await ctx.send(health)
        await ctx.send(defence)

    @adcalc.command()
    async def wise(self, ctx):
        await ctx.send("f")