import discord
from discord.ext import commands
import youtube_dl


class Music(commands.Cog, name='Music'):

    def __init__(self, bot):
        self.bot = bot

    @commands.comand(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await commands.join_voice_channel(channel)


def setup(bot):
    bot.add_cog(Music(bot))
    print('Music is loaded')
