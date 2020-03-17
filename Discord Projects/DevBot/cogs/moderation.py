import discord
from discord.ext import commands
import asyncio
import datetime
import os
import sys
import traceback
import json
import random


class ModCog(commands.Cog, name='Moderation'):

    def __init__(self, bot):
        self.bot = bot

    # kick
    @commands.command(aliases=['boot'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="**Kick**",
                              description=f'{member.mention} was kicked...',
                              color=discord.Color.red())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.member.kick(reason=reason)

    # ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title="**Ban**",
                              description=f'{member.mention} was banned...',
                              color=discord.Color.dark_red())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.member.ban(reason=reason)

    #unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user=ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                embed = discord.Embed(title="**Unban**",
                                      description=f'{user.mention} was unbanned!',
                                      color=discord.Color.green())
                embed.set_footer(text='Bot made by'
                                      'Aidan | XxBossxX#6216')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.guild.unban(user)
                await ctx.send(embed=embed)



    # Purge a.k.a remove messages
    @commands.command(aliases=['remove'])
    async def purge(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title="**Purge**",
                              description=f'{amount} lines were remove!',
                              color=discord.Color.dark_green())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    """#mute
    @commands.command(aliases=['silence'])
    async def mute(self, ctx, member: discord.Member, * ):"""

    @commands.command(pass_context=True)
    async def mute(ctx, member: discord.Member):
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
            role = discord.utils.get(member.server.roles, name='Muted')
            await commands.add_roles(member, role)
            embed = discord.Embed(title="User Muted!",
                                  description="**{0}** was muted by **{1}**!".format(member, ctx.message.author),
                                  color=0xff00f6)
            await commands.say(embed=embed)
        else:
            embed = discord.Embed(title="Permission Denied.",
                                  description="You don't have permission to use this command.", color=0xff00f6)
            await commands.say(embed=embed)

def setup(bot):
    bot.add_cog(ModCog(bot))
    print('Moderation is loaded')
