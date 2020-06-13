import discord
from discord.ext import commands
import datetime
import sqlite3
import math


class LvlCog(commands.Cog, name='Leveling'):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        db = sqlite3.connect('Users.sqlite')
        cursor = db.cursor()
        cursor.execute(
            f"SELECT user_id FROM levels WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = "INSERT INTO levels(guild_id, user_id, exp, lvl) VALUES(?,?,?,?)"
            val = (message.guild.id, message.author.id, 2, 0)
            cursor.execute(sql, val)
            db.commit()
        else:
            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
            result1 = cursor.fetchone()
            exp = int(result1[1])
            sql = "UPDATE levels SET exp = ? WHERE guild_id = ? and user_id = ?"
            val = (exp + 2, str(message.guild.id), str(message.author.id))
            cursor.execute(sql, val)
            db.commit()

            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
            result2 = cursor.fetchone()

            xp_start = int(result2[1])
            lvl_start = int(result2[2])
            xp_end = math.floor(5 * (lvl_start ^ 2) + 50 * lvl_start + 100)
            if xp_end < xp_start:
                print(f"{message.author.mention} has leveled up to level {lvl_start + 1}.")
                sql = "UPDATE levels SET lvl = ? WHERE guild_id = ? and user_id = ?"
                val = (int(lvl_start + 1), str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()
                sql = "UPDATE levels SET exp = ? WHERE guild_id = ? an user_id = ?"
                val = (0, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()

                cursor.close()
                db.close()

    @commands.command(aliases=['xp', 'experience'])
    async def exp(self, ctx, user: discord.User = None):
        if user is not None:
            db = sqlite3.connect('Users.sqlite')
            cursor = db.cursor()
            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{user.id}'")
            result = cursor.fetchone()
            if result is None:
                embed = discord.Embed(title="**Error**", description=f'`{user.name}` is not yet ranked.',
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="**Rank**",
                                      description=f"`{ctx.message.author.name}` has `{str(result[1])}` EXP.",
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            cursor.close()
            db.close()
        elif user is None:
            db = sqlite3.connect('Users.sqlite')
            cursor = db.cursor()
            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{ctx.message.author.id}'")
            result = cursor.fetchone()
            if result is None:
                embed = discord.Embed(title="**Rank**", description=f'`{user.name}` is not yet ranked.',
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by Aidan | XxBossxX')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="**Rank**",
                                      description=f"`{ctx.message.author.name}` has `{str(result[1])}` EXP.",
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            cursor.close()
            db.close()

    @commands.command()
    async def leaderboard(self, ctx):

        db = sqlite3.connect('Users.sqlite')
        cursor = db.cursor()
        cursor.execute(
            f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{ctx.message.author.id}'")
        result = cursor.fetchone()
        embed = discord.Embed(title="**Leaderboard**",
                              description=f"`{ctx.message.author.name}` is level `{str(result[2])}`",
                              color=discord.Color.blue())
        embed.set_footer(text='Bot created by xIntensity#4217')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
        cursor.close()
        db.close()

    @commands.command()
    async def level(self, ctx, user: discord.User = None):
        if user is not None:
            db = sqlite3.connect('Users.sqlite')
            cursor = db.cursor()
            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{user.id}'")
            result = cursor.fetchone()
            if result is None:
                embed = discord.Embed(title="**Error**", description=f'`{user.name}` is not yet ranked.',
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="**Rank**", description=f"`{user.name}` is level `{str(result[2])}`",
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            cursor.close()
            db.close()
        elif user is None:
            db = sqlite3.connect('Users.sqlite')
            cursor = db.cursor()
            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{ctx.message.author.id}'")
            result = cursor.fetchone()
            if result is None:
                embed = discord.Embed(title="**Rank**", description=f'`{user.name}` is not yet ranked.',
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by Aidan | XxBossxX')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="**Rank**",
                                      description=f"`{ctx.message.author.name}` is level `{str(result[2])}`",
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            cursor.close()
            db.close()

    @commands.command()
    async def rank(self, ctx, user: discord.User = None):
        if user is not None:
            db = sqlite3.connect('Users.sqlite')
            cursor = db.cursor()
            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{user.id}'")
            result = cursor.fetchone()
            if result is None:
                embed = discord.Embed(title="**Error**", description=f'`{user.name}` is not yet ranked.',
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="**Rank**", description=f"`{user.name}` is level `{str(result[2])}` and "
                                                                    f"has `{str(result[1])}` EXP.",
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            cursor.close()
            db.close()
        elif user is None:
            db = sqlite3.connect('Users.sqlite')
            cursor = db.cursor()
            cursor.execute(
                f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{ctx.message.author.id}'")
            result = cursor.fetchone()
            if result is None:
                embed = discord.Embed(title="**Rank**", description=f'`{user.name}` is not yet ranked.',
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by Aidan | XxBossxX')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="**Rank**",
                                      description=f"`{ctx.message.author.name}` is level `{str(result[2])}` and has `{str(result[1])}` EXP.",
                                      color=discord.Color.blue())
                embed.set_footer(text='Bot created by xIntensity#4217')
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)
            cursor.close()
            db.close()


def setup(bot):
    bot.add_cog(LvlCog(bot))
    print('Leveling is loaded')
