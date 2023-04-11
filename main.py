import os
import discord
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()
token = os.getenv("TOKEN")

print("Connecting...")

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}!")

# import cogs
cogs = ["fun"]
for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

bot.run(token)