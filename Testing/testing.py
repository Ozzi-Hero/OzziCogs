from redbot.core import commands

class Testing(commands.Cog):

    @commands.command()
    async def test(self, ctx):

        await ctx.message.reply("I can do stuff!")