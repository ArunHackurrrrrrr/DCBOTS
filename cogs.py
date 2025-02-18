import discord
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
import os
from dotenv import load_dotenv

load_dotenv("token.env")
TOKEN: str = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # ✅ Required for text commands

bot = commands.Bot(command_prefix="!", intents=intents)

bot_statuses = cycle(["STATUS One","Hello from arun","status code 123","reflex"])

@tasks.loop(seconds=5)          #status change hone ka time
async def change_bot_status():         #isse bot ka status change kar rahe hai
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")  # ✅ Fix extension path
                print(f"Loaded extension {filename}")
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    change_bot_status.start()

    try:
        synced_commands = await bot.tree.sync()
        print(f'synced {len(synced_commands)} command')
    except Exception as e:
        print(f'An error with syncing application commands has occured : {e}')

@bot.tree.command(name='hello',description='it say back hello')   #no capital letter in name and no spaces allowed only use lowercase letter wiht _ for spaced
async def hello(interaction : discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} Hello there!",ephemeral=True)

with open('token.txt','r') as file :
    token = file.read()


class RegData(discord.ui.Modal, title="Registration Data"):
    
    AuthID = discord.ui.TextInput(label="Auth ID", style=discord.TextStyle.short, placeholder="EX. - DSJI.EI3KJ#4$#.DS")
    userName = discord.ui.TextInput(label="Your Team Name", style=discord.TextStyle.short, placeholder="EX. - your team name")

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Thank you for reporting AuthID: {self.AuthID} and team name: {self.userName}", ephemeral=True)


@bot.tree.command(name="reg", description="Provide registration data")
async def report(interaction: discord.Interaction):
    modal = RegData()
    await interaction.response.send_modal(modal)




async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)  # ✅ Replace with your bot token

if __name__ == "__main__":
    asyncio.run(main())  # ✅ Ensure async loop runs properly
  