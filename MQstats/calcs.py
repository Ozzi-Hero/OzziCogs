from redbot.core import commands

class Mycog(commands.Cog):


    @commands.command()
    async def test(self, ctx, args1, args2, args3):
        await ctx.send("f")
