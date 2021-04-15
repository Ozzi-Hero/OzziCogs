from redbot.core import commands
from decimal import *
import discord

class MQstats(commands.Cog):

    @commands.command()
    async def adcalc(self, ctx, might: str, health: str, defence: str):
        """Returns multiple statistics for bubble damage, set health, and adrenaline optimisation"""

        #String conversions with error checking
        try:
            might = int(str.replace(might, ",", ""))
            health = int(str.replace(health, ",", ""))
            defence = int(str.replace(defence, "%", ""))

        #Calculations
        defence = defence / 100
        coeff = 2.79

        dmg = might / coeff
        dmgShielded = dmg * defence

        dmgActual = dmg - dmgShielded

        healthremaining = health - dmgActual
        adreThreshold = health * 0.2

        adreProcReq = healthremaining - adreThreshold + 1

        #Health checking for string set
        if (healthremaining <= 0):
            adbool = "MF you're dead"
        elif (healthremaining < adreThreshold):
            adbool = "Yes"
        else:
            adbool = 'No'

        #Embed colour setting
        if (adbool == 'Yes'):
            embedColour = discord.Colour.green()
        else:
            embedColour = discord.Colour.red()

        #Embed initialisation
        embed = discord.Embed(
            title = 'Optimisation Results',
            description = f'Results for {ctx.author.mention}',
            colour = embedColour
        )

        #Setting thumbnail URL with exception for DMs or any errors
        try:
            thumbnailURL = ctx.guild.icon_url
        except:
            thumbnailURL = ctx.author.avatar_url

        embed.set_thumbnail(url=thumbnailURL)
        embed.add_field(
            name = '**Damage from bubble:**',
            value = f'{round(dmgActual):,}',
            inline = True
        )
        embed.add_field(
            name = '**Health remaining:**',
            value = f'{round(healthremaining):,}',
            inline = True
        )
        embed.add_field(
            name = '**Adrenaline threshold:**',
            value = f'{round(adreThreshold):,}',
            inline = False
        )
        embed.add_field(
            name = '**Adrenaline activated?**',
            value = adbool,
            inline = False
        )

        if (adbool == 'No'):
            embed.add_field(
                name = '**Required HP decrease to proc adrenaline:**',
                value = f'{round(adreProcReq):,}',
                inline = False
            )
        await ctx.message.reply(embed=embed)

    @adcalc.error
    async def adcalc_error(self, ctx, error):
        if isinstance(error, ValueError):
            await ctx.message.reply('Please only use numbers, commas, or "%" signs when you use the command, try again')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.reply('Might, HP, and defence are all required inputs, try again')

    @commands.command()
    async def ascalc(self, ctx, type: str, speed: str):
        """Returns the time taken to finish your last hit combo based off your weapon type and AS"""

        speed = float(str.replace(speed, "%", ""))
        speed = speed / 100
        type = str.lower(type)

        if (type == 'axe'):
            basespeed = 2.143
        elif (type == 'sword'):
            basespeed = 2.080
        elif (type == 'staff'):
            basespeed = 2.005
        elif (type == 'spear'):
            basespeed = 1.948
        elif (type == 'hammer'):
            basespeed = 1.938

        getcontext().prec = 4
        finalspeed = Decimal(basespeed) - (Decimal(basespeed / 2) * Decimal(speed))

        await ctx.send(f"Your LHC time is {finalspeed}s")

    @commands.command()
    async def barscalc(self, ctx, bubbletype: str, barsleft: int):
        """Returns how much health bubble has left based on bars and bubble type."""

        bubbletype = str.lower(bubbletype)
        if bubbletype == 'weak':
            bubblehealth = 25000
        elif bubbletype == 'wise':
            bubblehealth = 30000
        else:
            bubblehealth = 125000

        await ctx.send(f'**Health left on bubble:**\n{(barsleft * bubblehealth):,}')
