import discord
from discord.ext import commands
import asyncio
import datetime


class HelpCog(commands.Cog, name='Help'):
    """Displays this help command."""

    def init(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *cog):
        embed = discord.Embed(title='Bot Help', description='Created by Aidan | XxBossxX#6216', color=0xff003d)

        embed.set_footer(text='!help for more info')

        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="Fun [6]", value="`eightball`, `roll`, `flip`, `fact`, `joke`,`say`")
        embed.add_field(name="Moderation [5]", value="`ban/unban`, `kick`, `purge`, `changeprefix`,`mute`")
        embed.add_field(name="Public [4]", value="`help`, `ping`, `time`")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))
    print('Help is loaded')

