from typing import Optional
import discord

from discord import app_commands

from discord.app_commands.commands import choices
from discord.app_commands.models import Choice
from discord.ext import commands


# 类定义
class SlashCmd(commands.Cog):
  # 构造
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  # 加载完成信息
  @commands.Cog.listener()
  async def on_ready(self):
    print("SlashCmd Cog has been loaded.")

  # hello命令
  @app_commands.command(name="hello", description="Say hello to the bot")
  async def hello(self, interaction: discord.Interaction):
    await interaction.response.send_message("Hello, world!")

  # hello 2 命令
  @app_commands.command(name="hello2", description="Say hello to the bot 2")
  async def hello2(self, interaction: discord.Interaction):
    await interaction.response.send_message(
        "this is a slash command in a cog with desc 2")

  # add 命令 with 参数提醒
  @app_commands.command(name="add", description="Add two numbers")
  @app_commands.describe(left="加号左边的数字", right="加号右边的数字")
  async def add(self, interaction: discord.Interaction, left: int, right: int):
    await interaction.response.send_message(f"The sum is {left + right}")

  # Anote someone
  @app_commands.command(name="anote", description="anote someone")
  @app_commands.describe(content="内容", user="用户")
  async def anote(self, interaction: discord.Interaction, content: str,
                  user: Optional[str]):
    if user == None or len(user) == 0:
      await interaction.response.send_message(f"Anote: {content}")
      return
    await interaction.response.send_message(
        f"you sent an anote to {user} with content {content}")

  # anote2
  @app_commands.command(name="anote2", description="anote with options")
  @app_commands.describe(type="类型", content="内容", user="用户")
  @app_commands.choices(type=[
      Choice(name="message", value="msg"),
      Choice(name="image", value="img"),
      Choice(name="voice", value="vol")
  ])
  async def anote2(self, interaction: discord.Interaction, type: Choice[str],
                   content: str, user: Optional[str]):
    targetUser = "" if user == None or user == "" else f"to {user}"
    content = type.value if type.value != "msg" else content
    await interaction.response.send_message(
        f"you send a message {content} {targetUser}")


async def setup(bot: commands.Bot):
  await bot.add_cog(SlashCmd(bot))
