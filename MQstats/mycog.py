from redbot.core import commands

class Mycog(commands.Cog):


    @commands.command()
    async def test(self, ctx, test: int):
        await ctx.send(f"Your number is {test}")