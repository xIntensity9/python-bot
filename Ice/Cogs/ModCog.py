import discord
from discord.ext import commands
import datetime
import time

snipes = dict()
server_config = dict()


class ModCog(commands.Cog, name='Moderation'):

    def __init__(self, bot):
        self.bot = bot

    # Kick, kicks the user from the server, requires kick perms
    @commands.command(aliases=['boot', '409'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="**Kick**",
                              description=f'{member.mention} has been kicked!',
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Ban, bans the user from the server, requires ban perms
    @commands.command(aliases=['banish', 'permaboot', '410'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title="**Ban**",
                              description=f'{member.mention} has been banned!',
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Unban, unbans the user from the server
    @commands.command(aliases=['unbanish'])
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                embed = discord.Embed(title="**Unban**",
                                      description=f'{user.mention} was unbanned!',
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.guild.unban(user)
                await ctx.send(embed=embed)

    # Warning, needs ban and kick perms
    @commands.command(aliases=['warning'])
    @commands.has_permissions(ban_members=True)
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx , member: discord.Member, *, message):
        embed = discord.Embed(title="**Warning**",
                              description=f'{member.mention} You have been warned by `{ctx.author}`\n\n***{message}***',
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await member.send(embed=embed)

        embed1 = discord.Embed(title="**Warn**",
                               description=f'Warning was successfully sent to {member.mention}!',
                               color=discord.Color.blue())
        embed1.set_footer(text='Bot made by xIntensity#4217')
        embed1.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed1)

    # Purge, removes a requested amount of messages
    @commands.command(aliases=['remove', 'clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):  # default purge amount, it will remove 1 line which is the executed command
        await ctx.channel.purge(limit=amount + 1)
        author = ctx.message.author
        embed = discord.Embed(title="**Purge**",
                              description=f'{amount} lines were removed! Requested by `{author}`',
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        await ctx.send(embed=embed)
        time.sleep(1)
        await ctx.channel.purge(limit=1)

    # Softban, bans and unbans a user instantly, removing all their messages
    @commands.command(alises=['softbanish'])
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=None)
        await member.unban()
        softbanmsg = f'{member.mention} was softbanned...'
        author = ctx.message.author
        embed = discord.Embed(title="**Softbn**",
                              description=softbanmsg,
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed.embed)

    # deafen, makes it so that user cannot hear anything
    @commands.command(alises=['deaf'])
    @commands.has_permissions(manage_roles=True)
    async def deafen(self, ctx, member: discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Deafen":
                await member.add_roles(role)
                embed = discord.Embed(title="**Deafen**",
                                      description="{} was deafened by {}".format(member.mention, ctx.author.mention),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                return

                overwrite = discord.PermissionsOverwrite(read_messages=False)
                newRole = await guild.create_role(name="Deafened")

                for channel in guild.text_channels:
                    await channel.set_permissions(newRole, overwrite=overwrite)

                await member.add_roles(newRole)
                embed = discord.Embed(title="**Deafen**",
                                      description="{} was deafened by {}".format(member.mention, ctx.author.mention),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

    # undeafen, removes undeafen role
    @commands.command(aliases=['undeaf'])
    @commands.has_permissions(manage_roles=True)
    async def undeafen(self, ctx, member: discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Deafen":
                await member.remove_roles(role)
                embed = discord.Embed(title="**Undeafen**",
                                      description="{} was undeafened by {}".format(member.mention, ctx.author.mention),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by'
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                return

    # RoleAdd, adds an existing role to a user
    @commands.command(alises=['roleadd'])
    @commands.has_permissions(administrator=True)
    async def addrole(self, ctx, member: discord.Member, *, role1):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == role1:
                await member.add_roles(role)
                embed = discord.Embed(title="**Add Role**",
                                      description="{} gave {} the role `{}`".format(ctx.author.mention, member.mention,
                                                                                    role1),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by'
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                return

    # Roleremove
    @commands.command(aliases=['roleremove'])
    @commands.has_permissions(administrator=True)
    async def removerole(self, ctx, member: discord.Member, *, role1):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == role1:
                await member.remove_roles(role)
                embed = discord.Embed(title="**Remove Role**",
                                      description="{} had the role `{}` removed by {}".format(member.mention,
                                                                                              role1,
                                                                                              ctx.author.mention),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by'
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                return

    # Mute, makes it so that the requested user cannot talk
    @commands.command(aliases=['silence', '403'])
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)
                embed = discord.Embed(title="**Mute**",
                                      description="{} was muted by {}".format(member.mention, ctx.author.mention),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by'
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                return

                overwrite = discord.PermissionsOverwrite(send_messages=False)
                newRole = await guild.create_role(name="Silenced")

                for channel in guild.text_channels:
                    await channel.set_permissions(newRole, overwrite=overwrite)

                await member.add_roles(newRole)
                embed = discord.Embed(title="**Mute**",
                                      description="{} was muted by {}".format(member.mention, ctx.author.mention),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by'
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

    # Unmute, removes the role mute
    @commands.command(aliases=['unsilence'])
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.remove_roles(role)
                embed = discord.Embed(title="**Unmute**",
                                      description="{} was unmuted by {}".format(member.mention, ctx.author.mention),
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot made by '
                                      'xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                return

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            embed = discord.Embed(title="**Lockdown**",
                                  description=f"`{channel.name}` has been put on lockdown! Type d!lockdown again to remove it!",
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[
            ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(title="**Lockdown**",
                                  description=f"`{channel.name}` has been put on lockdown! Type d!lockdown again to remove it!",
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(title="**Lockdown**",
                                  description=f"The lockdown on `{channel.name}` has been removed!",
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ModCog(bot))
    print('ModCog is loaded')
