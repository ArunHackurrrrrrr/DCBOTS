import discord 
from discord.ext import commands
from random import choice
import asyncpraw as praw

class Redit(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Redit(bot))