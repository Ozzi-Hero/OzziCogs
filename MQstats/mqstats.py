from redbot.core import commands
import discord.py

class MQstats(commands.Cog):

    @commands.command()
    async def adcalc(self, ctx, might: int, health: int, defence: int):
        defence = defence / 100
        coeff = 2.79

        dmg = might / coeff
        dmgShielded = dmg * defence

        dmgActual = dmg - dmgShielded

        healthremaining = health - dmgActual
        adreThreshold = health * 0.2

        #adreActivatedBool = bool(healthremaining < adreThreshold)

        embed=discord.Embed()
        embed.add_field(name = "Bubble damage", value = dmgActual, inline = False)
        embed.add_field(name = "Health remaining:", value = healthremaining, inline=False)
        #if (adreActivatedBool):
         #   embed.add_field(name = "Adrenaline activated?", value = "Yes", inline = False)
        #else:
         #   embed.add_field(name = "Adrenaline activated?", value = "No", inline = False)
        await ctx.send(embed=embed)
