import discord
from discord.ext import commands
import asyncio
import datetime


class Error1Cog(commands.Cog, name='Error1'):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, 'on_error'):
                return
            else:
                embed = discord.Embed(title=f'Error in {ctx.command}',
                                      description=f'`{ctx.command.qualified_name} {ctx.command.signature}` \n{error}',
                                      color=0x43780)  # This color is a blue
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text='Bot made by'
                                      'Aidan | XxBossxX#6216')
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Error in {ctx.command}', description=f'{error}', color=0x43780)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='Bot made by'
                                  'Aidan | XxBossxX#6216')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Error1Cog(bot))
    print('Error1 is loaded')
