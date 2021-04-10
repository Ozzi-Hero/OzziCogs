from .mqstats import MQstats


def setup(bot):
    bot.add_cog(MQstats())