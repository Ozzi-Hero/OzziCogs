from redbot.core import commands

class Testing(commands.Cog):

    @commands.command()
    async def mycom(self, ctx):

        await ctx.Message.reply("I can do stuff!")