import platform
import discord
from discord.ext import commands
import datetime


class PublicCog(commands.Cog, name='Public'):

    def __init__(self, bot):
        self.bot = bot

    # Search
    @commands.command(aliases=['google', 'searchup'])
    async def search(self, ctx, *, google):
        embed = discord.Embed(title="Google",
                              description=f"Click [here](http://www.google.com/search?q={google}) to find results for `{google}`",
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Roles, displays all the roles of the requested user
    @commands.command()
    async def roles(self, ctx, member: discord.Member = None):
        roles = [role for role in member.roles]
        embed = discord.Embed(title="**Roles**",
                              color=discord.Color.blue())
        embed.add_field(name=f"All roles: ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Time, displays the time in UTC
    @commands.command(aliases=['datetime', 'date', 'utc', 'UTC'])
    async def time(self, ctx):
        time = datetime.datetime.utcnow()
        embed = discord.Embed(title="**Time**",
                              description=('{}'.format(time)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Avatar, displays the users pfp
    @commands.command(aliases=['pfp', 'icon'])
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(color=discord.Color.blue(), timestamp=ctx.message.created_at)
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    # Guildicon, displays the servers pfp
    @commands.command(aliases=['guildpfp', 'guildavatar', 'servericon', 'serveravatar'])
    async def guildicon(self, ctx):
        embed = discord.Embed(color=discord.Color.blue(), timestamp=ctx.message.created_at)
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    # Direct Message, messages a user privately
    @commands.command()
    async def dm(self, ctx, member: discord.Member, *, message):
        embed = discord.Embed(title="**Direct Message**",
                              description="`{}` was sent from `{}`\n\n*You cannot respond to this message!*".format(message, ctx.author),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await member.send(embed=embed)
        embed1 = discord.Embed(title="**Direct Message**",
                               description=f"The message was successfully sent!",
                               color=discord.Color.blue())
        embed1.set_footer(text='Bot made by '
                               'xIntensity#4217')
        embed1.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed1)

    # Userinfo, displays basic info about the user
    @commands.command(aliases=['info', 'ui'])
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="User ID:", value=member.id)
        embed.add_field(name="Guild name:", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"All roles: ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Highest role:", value=member.top_role.mention)

        embed.add_field(name="Bot?", value=member.bot)

        await ctx.send(embed=embed)

    # Whohas, tells what users have a certain role
    @commands.command()
    async def whohas(self, ctx, role):
        embed = discord.Embed(title=f"**Members with `{role}`**",
                              description=('`{}`'.format(ctx.member.role)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()

    # Say, bot repeats the requested message
    @commands.command(aliases=['speak', 'tell'])
    async def say(self, ctx, *, arg1):
        embed = discord.Embed(title="**Say**",
                              description=('`{}`'.format(arg1)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # user-id, displays the users id
    @commands.command()
    async def id(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        user_id = f"{member.mention}'s id is: `{member.id}`"
        embed = discord.Embed(title="**User ID**",
                              description=('{}'.format(user_id)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(PublicCog(bot))
    print('PublicCog is loaded')
