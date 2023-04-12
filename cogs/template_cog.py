import discord
from discord.ext import commands

class TemplateCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Template command")
    async def test(self, ctx):
        await ctx.respond("Hello world!")

def setup(bot):
    bot.add_cog(TemplateCommands(bot))