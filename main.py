from discord.ext import commands
from dotenv import load_dotenv
from os import environ

load_dotenv(".env")
token = environ["TOKEN"]

#Sets the bot prefix
bot = commands.Bot("!")

@bot.command(name = "ping")
async def ping(ctx:commands.Context):
    await ctx.send("pong")

bot.run(token)