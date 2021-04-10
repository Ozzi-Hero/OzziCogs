from redbot.core import commands

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

        if (healthremaining < adreThreshold):
            adbool = 'Yes'
        else:
            adbool = 'No'

        await ctx.send(f"Actual damage: {dmgActual}")
        await ctx.send(f"Health remaining: {healthremaining}")
        await ctx.send(f"Adrenaline threshold: {adreThreshold}")
        await ctx.send(f"Adrenaline activated? {adbool}")
