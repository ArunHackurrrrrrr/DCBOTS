import discord
from discord.ext import commands
from discord import app_commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping',description="give ping of the server")
    async def ping(self, interaction : discord.Interaction, member : discord.Member = None):
            ping_embed = discord.Embed(title="Ping",description="value in ms",color=discord.Color.blue())
            ping_embed.add_field(name=f"{self.bot.user.name}'s Latency in (ms):",value=f"{round(self.bot.latency * 1000)}ms. ",inline=False)
            ping_embed.set_footer(text=f"Requested by {interaction.user.name}",icon_url=interaction.user.avatar)
            await interaction.response.send_message(embed = ping_embed)
    @app_commands.command(name="hello_slash",description='say back hello')
    async def hello(self,interaction : discord.Interaction, member : discord.Member = None):
        await interaction.response.send_message(f"HEllo there , {interaction.user.mention}")
async def setup(bot):
    await bot.add_cog(Test(bot))  # ✅ Correct async cog setup
