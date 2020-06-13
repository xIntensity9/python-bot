import datetime
from discord.ext import commands
import discord
import random


class FunCog(commands.Cog, name='Fun'):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['meme'])
    async def pepe(self, ctx):
        pepe = ['https://cdn.discordapp.com/emojis/656665539694952448.gif?v=1',
                'https://cdn.discordapp.com/emojis/680098905009946655.gif?v=1',
                'https://cdn.discordapp.com/emojis/620686647331258399.gif?v=1',
                'https://cdn.discordapp.com/emojis/589828801484161066.png?v=1',
                'https://cdn.discordapp.com/emojis/596132760532287488.png?v=1',
                'https://cdn.discordapp.com/emojis/402446616281350144.png?v=1',
                'https://cdn.discordapp.com/emojis/300046211300327425.png?v=1,']
        embed = discord.Embed(title="**Pepe**",
                              color=discord.Color.blue())
        embed.set_image(url=random.choice(pepe))
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


    # coin flip
    @commands.command(aliases=['coin'])
    async def flip(self, ctx):
        responses = ['Heads', 'Tails']
        flipmsg = f'Congrats! Your coin landed on **{random.choice(responses)}!**'
        embed = discord.Embed(title="**Flip**",
                              description=('{}'.format(flipmsg)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # joke
    @commands.command(aliases=['Joke', 'funny'])
    async def joke(self, ctx):
        jokemsg = ['A child asked his father, "How were people born?" So his father said, "Adam and Eve made babies, '
                   'then their babies became adults and made babies, and so on." The child then went to his mother, '
                   'asked her the same question and she told him, "We were monkeys then we evolved to become like we '
                   'are now." The child ran back to his father and said, "You lied to me!" His father replied, "No, '
                   'your mom was talking about her side of the family." ',
                   'My friend thinks he is smart. He told me an onion is the only food that makes you cry, so I threw '
                   'a '
                   'coconut at his face. ',
                   'A teacher asked her students to use the word "beans" in a sentence. "My father grows beans,'
                   '" said one girl. "My mother cooks beans," said a boy. A third student spoke up, "We are all human '
                   'beans." ',
                   'Why was 6 afraid of 7? Because 7 ate 9',
                   'Why did the witches team lose the baseball game? Their bats flew away',
                   'What starts with E and only has one letter in it? Envelope',
                   'Why did the can crusher quit his job? Because it was soda-pressing',
                   'Teacher: What do chickens give you? Kids: Meat! Teacher: What do pigs give you? Kids: Bacon! '
                   'Teacher: What does the fat cow give you? Kids: Homework! ',
                   'What happens to a frogs car when it breaks down? It gets toad away',
                   'Teacher: If I gave you 2 cats and another 2 cats and another 2, how many would you have?'
                   'Johnny: Seven.'
                   'Teacher: "No, listen carefully... If I gave you two cats, and another two cats and another two, '
                   'how many would you have?" '
                   'Johnny: Seven.'
                   'Teacher: Let me put it to you differently. If I gave you two apples, and another two apples and '
                   'another two, how many would you have? '
                   'Johnny: Six.'
                   'Teacher: Good. Now if I gave you two cats, and another two cats and another two, how many would '
                   'you '
                   'have? '
                   'Johnny: Seven!'
                   'Teacher: Johnny, where in the heck do you get seven from?!'
                   'Johnny: Because I already got a freaking cat!']
        embed = discord.Embed(title="**Joke**",
                              description=f'{random.choice(jokemsg)}',
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
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
        dicemsg = f'Your dice landed on `{random.choice(responses)}!`'
        embed = discord.Embed(title="**Roll**",
                              description=('{}'.format(dicemsg)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
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
        factmsg = f'{random.choice(responses)}'
        embed = discord.Embed(title="**Fact**",
                              description=('{}'.format(factmsg)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
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
                     'Maybe.']
        ballmsg = f'Question: `{question}`\nAnswer: `{random.choice(responses)}`'
        embed = discord.Embed(title="**Magic 8-Ball**",
                              description=('{}'.format(ballmsg)),
                              color=discord.Color.blue())
        embed.set_footer(text='Bot made by '
                              'xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(FunCog(bot))
    print('FunCog is loaded')
