import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "christmas", description = "Just a week away!")
    async def christmas(self, ctx, text: discord.Option(str)):
        await ctx.respond(f"Can you believe it guys? {text}, just a week away! {text} is in a week! Woo-hoo! I am so happy about this information. {text}, just a week away. Oh, wow! Can you believe it? {text}, just in a week! It got here so fast.")

    @discord.slash_command(name = "hello", description = "Say hi")
    async def hello(self, ctx):
        await ctx.respond("https://cdn.discordapp.com/emojis/1093280397162455101.gif?size=48&quality=lossless")

def setup(bot):
    bot.add_cog(Commands(bot))
    