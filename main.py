import os
import discord
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()
token = os.getenv("TOKEN")

print("Ing-Bot is starting...")

@bot.event
async def on_ready():
    print(f"Ing-Bot is logged in and online!")

# import cogs
cogs = ["meta", "fun"]
for cog in cogs:
    bot.load_extension(f"cogs.{cog}")

bot.run(token)