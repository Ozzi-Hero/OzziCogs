from redbot.core import commands
import discord

class Testing(commands.Cog):

    @commands.command()
    async def test(self, ctx):

        embed = discord.embed(
            title = 'test',
            value = 'test'
        )

        await ctx.message.reply(embed=embed)