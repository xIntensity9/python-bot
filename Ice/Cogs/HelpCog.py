import discord
from discord.ext import commands
import datetime


class HelpCog(commands.Cog, name='Help'):
    """Displays this help command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *cog):
        embed = discord.Embed(title='Ice', description='**Created by xIntensity#4217**',
                              color=discord.Color.blue())
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='d!about for more info')

        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="Fun 🎈\n", value="`eightball` ,`roll`, `flip`, `fact`, `joke`, `pepe`", inline=False)
        embed.add_field(name="Moderation 🚫", value="`ban/unban`, `kick`, `purge`, `mute/unmute`, `softban`, "
                                                    "`deafen/undeafen`, `warn`", inline=False)
        embed.add_field(name="Public Use 📢", value="`help`, `time`, `invite`, `userinfo`, `botinfo`, "
                                                    "`youtube`, `say`, `server`, `roles`, `id`, `avatar`, "
                                                    "`guildicon`, "
                                                    "`search` ,`youtube` ,`about` ", inline=False)
        embed.add_field(name="Developer Only 👑",
                        value="`quit`, `reload`, `load/unload`, `status`, `blacklist/unblacklist`", inline=False)
        embed.add_field(name="Leveling ⬆", value="`rank`, `level`, `exp`", inline=False)
        embed.add_field(name="Utility ⚙", value="`lockdown`, `snipe`, `addrole/removerole`, `setprefix`, `ping`,`eval `",
                        inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['aboutice', 'abouticebot'])
    async def about(self, ctx):
        About = "`Ice is a multi-purpose bot that can help run many servers. There are many different kinds of commands " \
                "to fit your needs. Ice is still in development stage and might be down for very long periods due to " \
                "this. If you are interested in inviting Ice to your server, you can type d!invite. If you would like " \
                "any custom developed discord bots, you can reach me by my email, aidanquach314@gmail.com` "
        embed = discord.Embed(title="**About**",
                              description=('{}'.format(About)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(aliases=['moreinfo'])
    async def cmdinfo(self, ctx, command=None):

        if command is None:
            info = '`Type d!cmdinfo <command> or d!moreinfo <command> to learn more about a particular command!`'
            embed = discord.Embed(title="**Command Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'joke':
            info = '`d!joke tells a random joke.`'
            embed = discord.Embed(title="**Joke Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'fact':
            info = '`d!fact tells a random fact.`'
            embed = discord.Embed(title="**Fact Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'flip':
            info = '`d!flip flips a coin. It will display heads or tails.`'
            embed = discord.Embed(title="**Flip Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'roll':
            info = '`d!roll rolls a dice. It will display a number between 1 and 6.`'
            embed = discord.Embed(title="**Roll Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['eightball', '8ball', 'magic8ball']:
            info = '`d!eightball <question> answers a particular question, note that the answers are completely ' \
                   'randomized, its nothing personal :)` '
            embed = discord.Embed(title="**Eightball Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['rank', 'level', 'exp']:
            info = '`d!rank displays the particular users level and exp. d!level and d!rank display what their ' \
                   'command is.` '
            embed = discord.Embed(title="**Leveling Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'status':
            info = '`d!status changes the status of the bot, note this is an owner-exclusive command, and the default ' \
                   'status is set to "Watching some servers", can be changed to "Playing" or "Streaming"` '
            embed = discord.Embed(title="**Status Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['reload', 'load', 'unload']:
            info = '`d!reload reloads a certain cog, d!load loads a certain cog, and d!unload unloads a certain cog, ' \
                   'note this is an owner-exclusive command.` '
            embed = discord.Embed(title="**Reload/Unload/Load Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['changeprefix', 'prefix']:
            info = '`d!prefix or d!changeprefix changes the prefix, note this is an owner-exclusive command, ' \
                   'and changed prefixes are kept even when the bot is restarted.` '
            embed = discord.Embed(title="**ChangePrefix Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'shutdown':
            info = '`d!shutdown shuts the bot down, note this is an owner-exclusive command.`'
            embed = discord.Embed(title="**Shutdown Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'guildicon':
            info = '`d!guildicon displays the icon of the particular guild or server.`'
            embed = discord.Embed(title="**GuildIcon Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['avatar', 'icon']:
            info = '`d!avatar or d!icon displays the icon of the requested user, if no user is put, the user that ' \
                   'sent the message will get their icon displayed.` '
            embed = discord.Embed(title="**Avatar Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'id':
            info = '`d!id displays the id of the requested user, if no user is put, the user that sent the message ' \
                   'will get their id displayed.` '
            embed = discord.Embed(title="**Id Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'roles':
            info = '`d!roles displays all the roles the particular user has.`'
            embed = discord.Embed(title="**Roles Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'server':
            info = "`d!server allows the user to join Ice's server by providing a link.`"
            embed = discord.Embed(title="**Server Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'say':
            info = '`d!say displays what the user wants the bot to say. Typing "d!say Hello!" will output in the bot ' \
                   'saying Hello!` '
            embed = discord.Embed(title="**Say Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'help':
            info = '`d!help displays all the usable commands for Ice Bot.`'
            embed = discord.Embed(title="**Ping Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'botinfo':
            info = '`d!botinfo displays basic info on the bot.`'
            embed = discord.Embed(title="**Botinfo Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'userinfo':
            info = '`d!userinfo displays basic info on a particular user. It displays when the user joined, ' \
                   'their icon, and more.` '
            embed = discord.Embed(title="**Userinfo Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == '`invite`':
            info = '`d!invite allows the user to invite this bot to their server!`'
            embed = discord.Embed(title="**Invite Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'time':
            info = '`d!time tells the time in UTC`'
            embed = discord.Embed(title="**Time Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'ping':
            info = '`d!ping tells the latency between the user and the API.`'
            embed = discord.Embed(title="**Ping Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'snipe':
            info = '`d!snipe shows the last deleted message since the bot was online.`'
            embed = discord.Embed(title="**Snipe Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'addrole':
            info = '`d!addrole adds a particular role to the requested user. d!removerole removes a particular role ' \
                   'from the requested user.`'
            embed = discord.Embed(title="**Add/Remove Role Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'deafen':
            info = '`d!deafen is pretty much like mute, but harsher, instead of disabling the ability to talk, ' \
                   'it disables the ability to read the chat.` '
            embed = discord.Embed(title="**Deafen Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'mute':
            info = '`d!mute mutes a particular member of the guild and by applying a `muted` role to them, they must ' \
                   'not have other roles that allows the member to talk`'
            embed = discord.Embed(title="**Mute Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'softban':
            info = '`d!softban bans a user, but instantly unbans them, it is basically a kick command that deletes ' \
                   'the users messages.`'
            embed = discord.Embed(title="**Softban Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'mute':
            info = '`d!mute mutes a particular member of the guild and by applying a `muted` role to them, they must ' \
                   'not have other roles that allows the member to talk`'
            embed = discord.Embed(title="**Mute Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'eval':
            info = '`d!eval or d!evaluate evaluates a selected piece of code. Typing the command d!eval ' \
                   '1 + 2 would output 3.`'
            embed = discord.Embed(title="**Eval Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['kick', 'boot', '409']:
            info = '`d!kick is pretty straight forward, it kicks a selected user from the guild. Typing the command ' \
                   'd!kick <user> will kick ' \
                   'the particular user out, you cannot kick the owner however.`'
            embed = discord.Embed(title="**Kick Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['ban', 'banish', 'permaboot', '410']:
            info = '`d!ban bans a particular user from the guild, once banned, the user cannot rejoin until unbanned. ' \
                   'Typing the command d!ban <user> will ban the particular user.`'
            embed = discord.Embed(title="**Ban Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == ['purge', 'removemsgs']:
            info = '`d!purge removes a selected amount of lines from the channel. Typing d!purge 10 will remove 10 ' \
                   'lines of text. Note that when you purge messages, they cannot be sniped!` '
            embed = discord.Embed(title="**Purge Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        if command == 'id':
            info = '`d!id reveals the id of the targeted user.`'
            embed = discord.Embed(title="**Purge Info**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

        else:
            info = '`Incorrect usage of d!cmdinfo, you are suppose to type d!cmdinfo <command>!`'
            embed = discord.Embed(title="**Cmdinfo Error**",
                                  description=('{}'.format(info)),
                                  color=discord.Color.blue())
            embed.set_footer(text='Bot made by '
                                  'xIntensity#4217')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))
    print('HelpCog is loaded')
