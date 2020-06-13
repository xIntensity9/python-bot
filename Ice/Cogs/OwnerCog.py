import discord
from discord.ext import commands
import datetime


class OwnerCog(commands.Cog, name='Owner'):

    def __init__(self, bot):
        self.bot = bot

    # Shutdown closes program

    """Shuts down the bot"""

    @commands.command(aliases=['close', 'terminate', 'exit', 'closebot', 'quit'], pass_context=True)
    async def shutdown(self, ctx):
        if ctx.message.author.id == 356472972657295390:
            shutdownmsg = "Closing Bot!"
            embed = discord.Embed(title="**Shutdown**",
                                  description=('{}'.format(shutdownmsg)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
            exit()
        else:
            errormsg = 'You are not a developer!'
            embed = discord.Embed(title="**Error**",
                                  description=('{}'.format(errormsg)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    """Reload unloads and loads a certain extension"""

    @commands.command()
    async def reload(self, ctx, *, module: str):
        if ctx.message.author.id == 356472972657295390:
            try:
                ctx.bot.unload_extension(module)
                ctx.bot.load_extension(module)
            except Exception as e:
                reloadmsg = ('{}: {}'.format(type(e).__name__, e))
                embed = discord.Embed(title="**Error in Reload**",
                                      description=('{}'.format(reloadmsg)),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by'
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            else:
                reloadmsg = f'`{module}` has been reloaded!'
                embed = discord.Embed(title="**Reload**",
                                      description=('{}'.format(reloadmsg)),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
        else:
            errormsg = 'You are not a developer!'
            embed = discord.Embed(title="**Error**",
                                  description=('{}'.format(errormsg)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by'
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    """Unloads a certain extension"""

    @commands.command()
    async def unload(self, ctx, *, module: str):
        if ctx.message.author.id == 356472972657295390:
            try:
                ctx.bot.unload_extension(module)
            except Exception as e:
                unloadmsg = ('{}: {}'.format(type(e).__name__, e))
                embed = discord.Embed(title="**Error in Unload**",
                                      description=('{}'.format(unloadmsg)),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by'
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            else:
                unloadmsg = f'`{module}` has been unloaded!'
                embed = discord.Embed(title="**Unload**",
                                      description=('{}'.format(unloadmsg)),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
        else:
            errormsg = 'You are not a developer!'
            embed = discord.Embed(title="**Error**",
                                  description=('{}'.format(errormsg)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    """Loads a certain extension"""

    @commands.command()
    async def load(self, ctx, *, module: str):
        if ctx.message.author.id == 356472972657295390:
            try:
                ctx.bot.load_extension(module)
            except Exception as e:
                loadmsg = ('{}: {}'.format(type(e).__name__, e))
                embed = discord.Embed(title="**Error in Load**",
                                      description=('{}'.format(loadmsg)),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            else:
                loadmsg = f'`{module}` has been loaded!'
                embed = discord.Embed(title="**Load**",
                                      description=('{}'.format(loadmsg)),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
        else:
            errormsg = 'You are not a developer!'
            embed = discord.Embed(title="**Error**",
                                  description=('{}'.format(errormsg)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(OwnerCog(bot))
    print('HelpCog is loaded')
