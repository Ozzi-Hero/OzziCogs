from .khutils import KHutils


def setup(bot):
    bot.add_cog(KHutils(bot))