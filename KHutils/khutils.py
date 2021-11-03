from redbot.core import commands
import discord

class KHutils(commands.Cog):
    """Knighthood utility commands for DreadKnights"""

    @commands.command()
    async def summonboss(self, ctx, guild=str, boss=str, weakness=str, resistance=str):
        """Summon announcement command"""

        if(guild == 'Knights'):
            guild = '<@896762237337878559>'
        elif(guild == 'Fighters'):
            guild = '<@895736777137086474>'

        summonEmbed = discord.Embed(
            title = 'Boss Info',
            description = 'New boss summoned!',
            colour = discord.Colour.green()
            )

        summonEmbed.set_thumbnail(url=ctx.guild.icon_url)

        summonEmbed.add_field(
            name = '**Boss Summoned:**',
            value = boss,
            inline = True
            )

        summonEmbed.add_field(
            name = '**Boss Weakness:**',
            value = weakness,
            inline = True
            )

        summonEmbed.add_field(
            name = '**Boss Resistance:**',
            value = resistance,
            inline = True
            )

        channelID = 903341457178509373
        channel = discord.Clienta.get_channel(channelID)
        await channel.send(guild, embed=summonEmbed)