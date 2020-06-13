import discord
from discord.ext import commands
import datetime

snipes = dict()
server_config = dict()


def snipe_embed(self, message, user):
    if message.author not in message.guild.members or message.author.color == discord.Color.blue():
        embed = discord.Embed(description=message.content, timestamp=message.created_at)
    else:
        embed = discord.Embed(description=message.content, color=discord.Color.blue(), timestamp=message.created_at)
        embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
    if message.attachments:
        embed.add_field(name='Attachment(s)', value='\n'.join([attachment.filename for attachment in
                                                               message.attachments]) + '\n\n__Attachment URLs are '
                                                                                       'invalidated once the message '
                                                                                       'is deleted.__')
    if message.channel != self:
        embed.set_footer(text='Sniped by ' + str(user) + ' | in channel: #' + message.channel.name)
    else:
        embed.set_footer(text='Sniped by ' + str(user))
    return embed


class Snipe(commands.Cog, name='Snipe'):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            del snipes[guild.id]
        except KeyError:
            pass

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        try:
            del snipes[channel.guild.id][channel.id]
        except KeyError:
            pass

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild and not message.author.bot:
            try:
                snipes[message.guild.id][message.channel.id] = message
            except KeyError:
                snipes[message.guild.id] = {message.channel.id: message}

    @commands.command(aliases=['snipes', 'deletedmsg','snipedmsg','msgsnipe','delmsg'])
    async def snipe(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.channel

        if not ctx.author.guild_permissions.manage_messages or not ctx.author.permissions_in(
                channel).read_messages or not ctx.author.permissions_in(channel).read_message_history:
            return
        try:
            sniped_message = snipes[ctx.guild.id][channel.id]
        except KeyError:
            errormsg = '❎  No messages can be sniped, please note the message deletion might have a slight delay when ' \
                       'reaching discord API! '
            embed = discord.Embed(title="**Snipe Error**",
                                  description=('{}'.format(errormsg)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=snipe_embed(ctx.channel, sniped_message, ctx.author))


def setup(bot):
    bot.add_cog(Snipe(bot))
    print('Snipe is loaded')
