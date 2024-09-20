import datetime
from discord.ext import commands, tasks
import asyncio


class DemoTask(commands.Cog):

  tz = datetime.timezone(datetime.timedelta(hours=8))
  every_day_time = [
      datetime.time(hour=17,
                    minute=i,
                    tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
      for i in range(60)
  ]

  def __init__(self, bot):
    self.bot = bot
    self.index = 0
    self.printer.start()

  def cog_unload(self):
    self.printer.cancel()

  @tasks.loop(time=every_day_time, count=5)
  async def printer(self):
    print(self.index)
    print(datetime.datetime.now(tz=self.tz))
    self.index += 1

  @printer.before_loop
  async def wait_until_time(self):
    await self.bot.wait_until_ready()
    print("go...")

  @printer.after_loop
  async def after_printer(self):
    print('task end')


async def setup(bot: commands.Bot):
  await bot.add_cog(DemoTask(bot))
