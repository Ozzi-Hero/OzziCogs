from redbot.core import commands
from decimal import *
import discord

class MQstats(commands.Cog):

    @commands.command()
    async def adcalc(self, ctx, might: str, health: str, defence: str):
        """Returns multiple statistics for bubble damage, set health, and adrenaline optimisation"""

        might = int(str.replace(might, ",", ""))
        health = int(str.replace(health, ",", ""))
        defence = int(str.replace(defence, "%", ""))


        defence = defence / 100
        coeff = 2.79

        dmg = might / coeff
        dmgShielded = dmg * defence

        dmgActual = dmg - dmgShielded

        healthremaining = health - dmgActual
        adreThreshold = health * 0.2

        adreProcReq = healthremaining - adreThreshold + 1

        if (healthremaining <= 0):
            adbool = "MF you're dead"
        elif (healthremaining < adreThreshold):
            adbool = "Yes"
        else:
            adbool = 'No'

        #await ctx.send(f"Damage from bubble: {round(dmgActual):,}")
        #await ctx.send(f"Health remaining: {round(healthremaining):,}")
        #await ctx.send(f"Adrenaline threshold: {round(adreThreshold):,}")
        #await ctx.send(f"Adrenaline activated? {adbool}")
        #if (adbool == 'No'):
        #    await ctx.send(f"Required HP decrease to proc adrenaline: {round(adreProcReq)}")

        embed = discord.Embed(
            title = 'Optimisation Results',
            description = f'Results for {ctx.author.mention}',
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/782630973358866472/830777511411449877/DRD.png')
        embed.add_field(
            name = f'**Damage from bubble:**\n{round(dmgActual)}\n\n**Health remaining:**\n{round(healthremaining)}',
            value = ' ',#round(dmgActual),
            inline = True
        )
        embed.add_field(
            name = '**Health remaining:**',
            value = round(healthremaining),
            inline = True
        )
        embed.add_field(
            name = '**Adrenaline threshold:**',
            value = round(adreThreshold),
            inline = True
        )
        embed.add_field(
            name = '**Adrenaline activated?**',
            value = adbool,
            inline = True
        )

        if (adbool == 'No'):
            embed.add_field(
                name = '**Required HP decrease to proc adrenaline:**',
                value = round(adreProcReq),
                inline = False
            )
        await ctx.send(embed=embed)

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
    async def embedtest(self, ctx):

        member = discord.Member
        author = ctx.author

        mention = str.replace(author.mention, "!", "")
        embed = discord.Embed(
            title = 'Optimisation Results',
            description = f'Results for {mention}',
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/799283401311256596/5a83148aecf7ab49cd67c10792398459.png?size=1024')
        embed.add_field(
            name = 'Field test',
            value = 'abc',
            inline = False
        )
        await ctx.send(embed=embed)
