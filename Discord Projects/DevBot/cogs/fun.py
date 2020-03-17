import datetime

from discord.ext import commands
import discord
import random


class FunCog(commands.Cog, name='Fun'):

    def __init__(self, bot):
        self.bot = bot

    # coin flip
    @commands.command(aliases=['coin'])
    async def flip(self, ctx):
        responses = ['Heads', 'Tails']
        flipmsg=f'Congrats! Your coin landed on **{random.choice(responses)}!**'
        embed = discord.Embed(title="**Flip**",
                              description=('{}'.format(flipmsg)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # joke
    @commands.command(aliases=['Joke', 'funny'])
    async def joke(self, ctx):
        embed = discord.Embed(title="**Joke**",
                              description=f'Jokes are for immature people...',
                              color=discord.Color.magenta())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # dice
    @commands.command(aliases=['dice'])
    async def roll(self, ctx):
        responses = ['1',
                     '2',
                     '3',
                     '4',
                     '5',
                     '6']
        dicemsg=f'Congrats! Your dice landed on **{random.choice(responses)}!**'
        embed = discord.Embed(title="**Roll**",
                              description=('{}'.format(dicemsg)),
                              color=discord.Color.dark_gold())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


    # fact
    @commands.command(aliases=['interesting', 'funfact'])
    async def fact(self, ctx):
        responses = ['Some cats are actually allergic to humans',
                     'There is a fruit that tastes like chocolate pudding.',
                     'Competitive art used to be in the Olympics.',
                     'A chefs hat has exactly 100 pleats.',
                     'The majority of your brain is fat.',
                     'Oranges arent naturally occurring fruits.',
                     'Most wasabi in the U.S. is not really wasabi.',
                     'Stop signs used to be yellow.',
                     'Green Eggs and Ham started as a bet.',
                     'Too much water can kill you.',
                     'The hottest temperature ever recorded on Earth was 2 billion degrees kelvin.',
                     'High heels were originally worn by men.',
                     'You might be drinking water that is older than the solar system.',
                     'Queen Elizabeth II is a trained mechanic.',
                     'New York was briefly named "New Orange."',
                     'Moonshiners used "cow shoes" to disguise their footprints during Prohibition.',
                     'It takes approx. 364 licks to get to the center of a Tootsie Pop.',
                     'Tree rings get wider during wet years.',
                     'The hottest inhabited place in the world is in Ethiopia.',
                     'Sea otters hold hands while they sleep.',
                     'Chainsaws, the horror-movie murder weapon of choice, were invented for aid in childbirth 😊',
                     'There is an island in Japan you can visit that is inhabited only by friendly bunnies.']
        factmsg=f'{random.choice(responses)}'
        embed = discord.Embed(title="**Fact**",
                              description=('{}'.format(factmsg)),
                              color=discord.Color.gold())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # 8ball
    @commands.command(aliases=['8ball', 'ask', 'curious', 'magic8ball'])
    async def eightball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again.',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.'
                     'Maybe.....idk']
        ballmsg=f'Question: {question}\nAnswer: {random.choice(responses)}'
        embed = discord.Embed(title="**Magic 8-Ball**",
                              description=('{}'.format(ballmsg)),
                              color=discord.Color.red())
        embed.set_footer(text='Bot made by'
                              'Aidan | XxBossxX#6216')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(FunCog(bot))
    print('Fun is loaded')
