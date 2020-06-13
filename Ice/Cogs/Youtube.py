import discord
import datetime
from discord.ext import commands
import urllib.parse, urllib.request, re

class Youtube(commands.Cog, name='Youtube'):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def youtube(self, ctx, *, search):

        query_string = urllib.parse.urlencode({
            'search_query': search
        })
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string
        )
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        youtubemsg = ('http://www.youtube.com/watch?v=' + search_results[0])
        await ctx.send(youtubemsg)

def setup(bot):
    bot.add_cog(Youtube(bot))
    print('Youtube is loaded')
