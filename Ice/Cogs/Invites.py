import discord
from discord.ext import commands
import datetime


class Invite(commands.Cog):
    """Invite bot to certain server"""

    @commands.command()
    @commands.cooldown(6, 12)
    async def invite(self, ctx):
        """Generate an invite link for this bot."""
        invite_minimal = ("[Invite with no Admin Perms](https://discordapp.com/oauth2/authorize?"
                          f"client_id={ctx.bot.user.id}&scope=bot)")
        invite_full = ("[Invite with Admin Perms](https://discordapp.com/oauth2/authorize?"
                       f"permissions=93190&client_id={ctx.bot.user.id}&scope=bot)")
        embed = discord.Embed(title="Invite Ice to your server with the following links!")
        embed.description = "\n".join((invite_minimal, invite_full))
        embed.color = discord.Color.blue()
        embed.set_footer(text='Bot made by'
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    """Invite users to Ice's Server"""

    @commands.command()
    @commands.cooldown(6, 12)
    async def server(self, ctx):
        serverlink = f"[Testing Server](https://discord.gg/fEuhY9K)"
        embed = discord.Embed(title="Join Ice's server from this link!")
        embed.description = "".join((serverlink))
        embed.color = discord.Color.blue()
        embed.set_footer(text='Bot made by'
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Invite())
    print("Invite is loaded")
