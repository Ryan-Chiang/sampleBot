import os

import discord
from discord.ext import commands

token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')


bot.run(token)
