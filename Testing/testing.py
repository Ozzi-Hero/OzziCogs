from redbot.core import commands
import discord

class Testing(commands.Cog):

    @commands.command()
    async def test(self, ctx):

        await ctx.message.reply(discord.Guild.icon)