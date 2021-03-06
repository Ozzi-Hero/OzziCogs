from redbot.core import commands
import discord

class KHutils(commands.Cog):
    """Knighthood utility commands for DreadKnights"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summonboss(self, ctx, guild: str, boss: str, weakness: str, resistance: str):
        """Summon announcement command"""

        if(guild == 'Knights'):
            guild = '<@&896762237337878559>'
            thumbnailURL = 'https://cdn.discordapp.com/attachments/895686824947765300/906453442426454016/DRDKLogo.png'
        elif(guild == 'Fighters'):
            guild = '<@&895736777137086474>'
            thumbnailURL = 'https://cdn.discordapp.com/attachments/895686824947765300/906454209161994260/DRDFLogo.png'

        summonEmbed = discord.Embed(
            title = 'Boss Info',
            description = 'New boss summoned!',
            colour = discord.Colour.green()
            )

        summonEmbed.set_thumbnail(url=thumbnailURL)

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
        channel = ctx.bot.get_channel(channelID)
        await channel.send(guild, allowed_mentions=discord.AllowedMentions(roles=True), embed=summonEmbed)