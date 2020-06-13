import datetime
import json
import platform
import sys
import discord
import traceback
from discord.ext import commands
import logging
from pathlib import Path
import youtube_dl


def get_prefix(client, message):
    with open('Json_Files/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)

# Removing a Cog from here will leave it unloaded!
initial_extensions = 'Cogs.Snipe', 'Cogs.Evaluation', 'Cogs.OwnerCog', 'Cogs.HelpCog', 'Cogs.ErrorCog', 'Cogs.ModCog', \
                     'Cogs.FunCog', 'Cogs.Invites', 'Cogs.PublicCog', 'Cogs.Leveling', 'Cogs.Youtube'

client.blacklisted_users = []
players = {}


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="youtube"))
    data = read_json("blacklist")
    client.blacklisted_users = data["blacklistedUsers"]
    print(f'Bot has connected.\nLogged in as {client.user.name} : {client.user.id}. Prefix is d!')


client.help_command = None

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()

cwd = Path(__file__).parents[0]
cwd = str(cwd)


@client.command(aliases=['changestatus', 'renamestatus'])
async def status(ctx, *, message):
    if ctx.message.author.id == 356472972657295390:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))
        embed = discord.Embed(title="**Status**",
                              description=('{}'.format("Status was changed to `{}`".format(message))),
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


commands.version = '`v2.4`'


@client.command(aliases=['bi', 'botinfo', 'botstats', 'bot'])
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))

    embed = discord.Embed(title=f'{client.user.name} Stats', description='\uFEFF', color=discord.Colour.blue(),
                          timestamp=ctx.message.created_at)
    embed.add_field(name='Bot Version:', value=commands.version)
    embed.add_field(name='Python Version:', value=f'`{pythonVersion}`')
    embed.add_field(name='Library:', value='`Discord.py`')
    embed.add_field(name='Discord.py Version', value=f'`{dpyVersion}`')
    embed.add_field(name='Total Server:', value=f'`{serverCount}`')
    embed.add_field(name='Total Users:', value=f'`{memberCount}`')
    embed.add_field(name='Bot Developer:', value="<@356472972657295390>")

    embed.set_footer(text=f"Created by xIntensity#4217 | {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)


# Music

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_contect=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


# blacklist

@client.event
async def on_message(message):
    # ignore ourselves
    if message.author.id == client.user.id:
        return

    # blacklist system
    if message.author.id in client.blacklisted_users:
        return

    if message.content.lower().startswith("help"):
        embed = discord.Embed(title="**Help**",
                              description=("You can run the help command with d!help!"),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    await client.process_commands(message)


@client.command()
async def blacklist(ctx, user: discord.Member):
    if ctx.message.author.id == user.id:
        embed = discord.Embed(title="**Error**",
                              description=('{}'.format("You can't blacklist yourself.")),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        return

    if ctx.message.author.id == 356472972657295390:
        client.blacklisted_users.append(user.id)
        data = read_json("blacklist")
        data["blacklistedUsers"].append(user.id)
        write_json(data, "blacklist")
        message = f"{user.name} has been blacklisted from using Ice's commands!"
        embed = discord.Embed(title="**Blacklist**",
                              description=('{}'.format(message)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        errormsg = 'You are not the owner...'
        embed = discord.Embed(title="**Error**",
                              description=('{}'.format(errormsg)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


@client.command()
async def unblacklist(ctx, user: discord.Member):
    if ctx.message.author.id == 356472972657295390:
        client.blacklisted_users.remove(user.id)
        data = read_json("blacklist")
        data["blacklistedUsers"].remove(user.id)
        write_json(data, "blacklist")
        message = f"{user.name} is allowed to use Ice's commands again!"
        embed = discord.Embed(title="**Unblacklist**",
                              description=('{}'.format(message)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        errormsg = 'You are not the owner...'
        embed = discord.Embed(title="**Error**",
                              description=('{}'.format(errormsg)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


# prefix change
@client.event
async def on_guild_join(guild):
    with open('Json_Files/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'd!'

    with open('Json_Files/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('Json_Files/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('Json_Files/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command(aliases=['prefix', 'prefixchange', 'setprefix'])
@commands.has_permissions(manage_guild=True)
async def changeprefix(ctx, prefix):
    with open('Json_Files/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('Json_Files/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    embed = discord.Embed(title="**Change Prefix**",
                          description=f'Changed prefix to: {prefix}',
                          color=discord.Color.blue())
    embed.set_footer(text='Bot made by '
                          'xIntensity#4217')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


# Ping, checks the latency of the user to the API
@client.command(pass_context=True)
async def ping(ctx):
    ping = (
        f'Pong! Your ping is: `{round(client.latency * 1000)}ms`, *Please note this is not your actual '
        f'ping, this is '
        f'the latency of your connection to the API*')
    embed = discord.Embed(title="**Ping**",
                          description=('{}'.format(ping)),
                          color=discord.Color.blue())
    embed.set_footer(text='Bot made by '
                          'xIntensity#4217')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


def read_json(filename):
    with open(f"{cwd}/Json_Files/{filename}.json", "r") as file:
        data = json.load(file)
    return data


def write_json(data, filename):
    with open(f"{cwd}/Json_Files/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)


with open("Json_Files/Token.json", "r") as token_file:
    data = json.load(token_file)
    token = data['token']

client.run(token)
