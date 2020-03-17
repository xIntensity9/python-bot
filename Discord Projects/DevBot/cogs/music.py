from discord.ext import commands
import discord


layers = {}


class MusicCog(commands.Cog, name='Music'):

    def __init__(self, bot):
        self.bot = bot



    @commands.command(pass_context=True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice.channel
        await commands.join_voice_channel(channel)

    @commands.command(pass_context=True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = commands.voice_client_in(server)
        await voice_client.disconnect()

    @commands.command(pass_context=True)
    async def play (ctx, url):
        server = ctx.message.server
        voice_client = commands.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()


def setup(bot):
    bot.add_cog(MusicCog(bot))
    print('Music is loaded')

