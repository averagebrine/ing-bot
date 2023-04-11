import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "test", description = "Template command")
    async def hello(self, ctx):
        await ctx.respond("Hello world!")

def setup(bot):
    bot.add_cog(Commands(bot))