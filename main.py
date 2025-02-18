# import discord

# from discord.ext import commands

# bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
# @bot.event
# async def on_ready():
#     print("Bot Ready")

# @bot.command(name="hlo")     #name = "hlo" by this function ka name bina change kiye uska calling name change kar sakte hai , agar iske andar aliases = [list ] dede list of names then un all of the name se isko call kiya ja sakta hai 
# async def hello(ctx):            #ctx == context - variable which have all data about from where command is passed,who ran it , time , everything which you can think
#     await ctx.send(f"HEllo there , {ctx.author.mention}")

# @bot.command()
# async def embed(ctx):
#     embeded_msg = discord.Embed(title="Title of embed",description="description of embed", color=discord.Color.red())
#     embeded_msg.set_author(name="author text",icon_url=ctx.author.avatar)
#     embeded_msg.set_thumbnail(url=ctx.author.avatar)
#     embeded_msg.add_field(name= "Name of feild",value= "value of feild",inline=False)
#     embeded_msg.set_image(url=ctx.guild.icon)
#     embeded_msg.set_footer(text="Footer text",icon_url=ctx.author.avatar)
#     await ctx.send(embed = embeded_msg)

# @bot.command()
# async def Ping(ctx):
#     ping_embed = discord.Embed(title="Ping",description="value in ms",color=discord.Color.blue())
#     ping_embed.add_field(name=f"{bot.user.name}'s Latency in (ms):",value=f"{round(bot.latency * 1000)}ms. ",inline=False)
#     ping_embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
#     await ctx.send(embed = ping_embed)
# with open("token.txt",'r') as file:
#     token = file.read()
# bot.run(token)
