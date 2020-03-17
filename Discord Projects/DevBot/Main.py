import datetime
import sqlite3
import json
import ast
import asyncio
import sys
import discord
import traceback
from discord.ext import commands

"""aliases cannot be the same as async def or program will crash, manually change prefix from prefixes.json, 
without internet, the program will not function properly """


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)

initial_extensions = ['cogs.error1', 'cogs.moderation', 'cogs.fun', 'cogs.help']


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Type d!help for commands!'))
    print('Bot has successfully connected!')


client.help_command = None


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()



"""players = {}


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice.channel
    await commands.join_voice_channel(channel)


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = commands.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = commands.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()"""


# dm

@client.command(aliases=['message', 'directmessage', 'text', 'msg', 'm'])
async def dm(ctx, member: discord.Member, message, ):
    embed = discord.Embed(
        colour=discord.Colour.red()
    )
    embed.set_author(name="Direct Message")
    embed.add_field(name="Bot created by Aidan | XxBossxX#6216", value=message, inline=False)
    await ctx.send(embed=embed)


# ping
@client.command(pass_context=True)
async def ping(ctx):
    ping = (
        f'Pong! Your ping is: {round(client.latency * 1000)}ms, *Please note this is not your actual ping, this is '
        f'the ping from the connection to the bot :)*')
    embed = discord.Embed(title="**Say**",
                          description=('{}'.format(ping)),
                          color=discord.Color.dark_magenta())
    embed.set_footer(text='Bot made by'
                          'Aidan | XxBossxX#6216')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


# userinfo
@client.command(aliases=['info'])
async def userinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.member}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name", value=member.display_name)

    embed.add_field(name="created at:", value=member.created_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add(name="Bot?", value=member.bot)
    await ctx.send(embed=embed)


# prefix change
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
@commands.has_permissions(manage_guild=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    embed = discord.Embed(title="**Change Prefix**",
                          description=f'Changed prefix to: {prefix}',
                          color=discord.Color.teal())
    embed.set_footer(text='Bot made by'
                          'Aidan | XxBossxX#6216')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


# Say
@client.command(aliases=['speak', 'tell'])
async def say(ctx, *, arg1):
    embed = discord.Embed(title="**Say**",
                          description=('{}'.format(arg1)),
                          color=discord.Color.red())
    embed.set_footer(text='Bot made by'
                          'Aidan | XxBossxX#6216')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


# Time
@client.command(aliases=['datetime', 'date'])
async def time(ctx):
    time = (datetime.datetime.now())
    embed = discord.Embed(title="**Time**",
                          description=('{}'.format(time)),
                          color=discord.Color.purple())
    embed.set_footer(text='Bot made by'
                          'Aidan | XxBossxX#6216')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


# Shutdown closes program
@client.command(aliases=['Close', 'Terminate'])
async def shutdown(ctx):
    shutdownmsg = "Shutting Down!"
    embed = discord.Embed(title="**Shutdown**",
                          description=('{}'.format(shutdownmsg)),
                          color=discord.Color.orange())
    embed.set_footer(text='Bot made by'
                          'Aidan | XxBossxX#6216')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    exit()


# DO NOT EDIT THIS THE BOT WILL NOT RUN!!!!!!
client.run('NjgwNTg4NTI5NzU5NDIwNTU2.Xm1N6g.UIv0wc2VAPGp2CaCBzhcgtErICk')
