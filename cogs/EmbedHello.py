import discord
from discord import app_commands
from discord.ext import commands


class EmbedHello(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @app_commands.command(name="embed_hello", description="Embed Hello")
  async def embed_hello(self, interaction: discord.Interaction):    
    embed = discord.Embed(title="this is the title", 
                          description="This is an embed!", 
                          url="https://www.bing.com",
                         color=discord.Color.from_rgb(3, 116, 142)
                         )
    embed.set_author(name="sample_bot", url="https://github.io", icon_url="https://avatars.githubusercontent.com/u/88852722?s=48&v=4")
    embed.set_thumbnail(url="https://github.githubassets.com/assets/univers24-banner-graphic-9-a0118d396c7f.webp")
    embed.set_image(url="https://github.githubassets.com/assets/copilot-extensions-head-eeca4b3ed60b.webp")
    embed.add_field(name="this is a field", value="this is a value", inline=False)
    await interaction.response.send_message(embed=embed)



async def setup(bot: commands.Bot):
  await bot.add_cog(EmbedHello(bot))
  
    
  