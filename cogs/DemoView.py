import discord
from discord import app_commands
from discord.ext import commands

class DemoView(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="view_with_primary_button", description="View with primary button")
    async def view_with_primary_button(self, interaction: discord.Interaction):
        view = ViewClass(timeout=15)        
        print(view)
        print(await interaction.response.send_message('here are the btns', view=view))

    # 监听器方式处理
    # 注意：监听器方式和callback方式同时存在时，最终都会触发，但结果是callback方式的结果
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        print("on_interaction")
        if 'custom_id' in interaction.data:
            print(f"listener triggered, custome_id: {interaction.data['custom_id']}")
            await interaction.response.send_message(f"listener triggered, custom_id: {interaction.data['custom_id']}")


class ViewClass(discord.ui.View):
    def __init__(self, timeout:float | None = 180):
        super().__init__(timeout=timeout)
        print("ViewClass init")
        button = discord.ui.Button(label="Button1", style=discord.ButtonStyle.primary, custom_id="button1")
        button.callback = self.on_button
        button2 = discord.ui.Button(label="Button2", style=discord.ButtonStyle.primary, custom_id="button2")
        button2.callback = self.on_button
        self.add_item(button)
        self.add_item(button2)
        print(self.timeout)
        
        

    # view超时事件处理
    async def on_timeout(self):
        print("View timeout")
        self.remove_item(self.children[0])
        print(self.children)
        self.stop()

    # 按钮callback事件处理
    async def on_button(self, interaction: discord.Interaction):
        if interaction.data["custom_id"] == "button1":
            print(f"remove button1{self.children[0]}")
            self.remove_item(self.children[0])
            print(self.children)
        await interaction.response.send_message(f"call back triggered, custom_id = {interaction.data['custom_id']}", ephemeral=False, view=self)

    # 按监听器方式处理

async def setup(bot: commands.Bot):
    await bot.add_cog(DemoView(bot))
