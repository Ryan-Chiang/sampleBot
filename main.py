import logging
import asyncio, os, discord
from discord.ext import commands
from dotenv import load_dotenv

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix="/", intents=intents)

# 載入.env檔案
load_dotenv()
token = os.getenv("TOKEN")
print(token)


@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    botCount = await bot.tree.sync()
    for cmdItem in botCount:
        print(f"sync cmd: {cmdItem.name}")


# @bot.command()
# # 輸入%Hello呼叫指令
# async def Hello(ctx):
#     # 回覆Hello, world!
#     await ctx.send("Hello, world!")


#load commands
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")


@bot.command()
async def unload(ctx, extention):
    await bot.unload_extension(f"cogs.{extention}")
    await ctx.send(f"Unloaded {extention} done.")


@bot.command()
async def reload(ctx, extention):
    await bot.reload_extension(f"cogs.{extention}")
    await ctx.send(f"Reloaded {extention} done.")


# 手动刷新命令提示
@bot.command()
async def refreshtree(ctx, extention):
    await bot.tree.sync()


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f'Loaded {filename[:-3]}')


async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
