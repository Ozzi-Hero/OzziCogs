from redbot.core import commands
import discord

class KHutils(commands.Cog):
    """Knighthood utility commands for DreadKnights"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summonboss(self, ctx, guild: str, boss: str, weakness: str, resistance: str, mentions: discord.AllowedMentions = roles):
        """Summon announcement command"""

        if(guild == 'Knights'):
            guild = '<@&896762237337878559>'
        elif(guild == 'Fighters'):
            guild = '<@&895736777137086474>'

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

        channel = ctx.bot.get_channel(895737127474724934)
        await channel.send(guild, allowed_mentions=mentions, embed=summonEmbed)