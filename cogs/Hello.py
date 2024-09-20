import discord
from discord import app_commands
from discord.ext import commands


class Hello(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Hello Cog has been loaded.")

    @commands.command()
    async def helloworld(self, ctx: commands.Context):
        await ctx.send("Hello, world!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Hello(bot))
