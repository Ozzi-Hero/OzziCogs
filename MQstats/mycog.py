from redbot.core import commands

class Mycog(commands.Cog):


    @commands.command()
    async def test(self, ctx):
        await ctx.send("f")