import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import MISSING

class DemoModal(commands.Cog):
    def __init__(self) -> None:
        super().__init__()
    
    @app_commands.command(name="modal", description="Modal")
    async def modal(self, interaction: discord.Interaction):
        view = ModalView()
        print(view)
        await interaction.response.send_modal(view)

class ModalView(discord.ui.Modal, title="测试Modal"):
    # 可以不要构造函数
    # 通过声明接受参数的变量的同时，填充modal的内容
    field_value = discord.ui.TextInput(label = 'input field',placeholder="请输入",required=True)

    async def on_submit(self, interaction: discord.Interaction):
        print(self.field_value)
        await interaction.response.send_message(f"submit, field value is : {self.field_value}")
    

async def setup(bot: commands.Bot):
    await bot.add_cog(DemoModal())