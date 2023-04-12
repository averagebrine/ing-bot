import discord, requests
from discord.ext import commands

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Say hi")
    async def hello(self, ctx):
        await ctx.respond("https://cdn.discordapp.com/emojis/1093280397162455101.gif?size=48&quality=lossless")

    @discord.slash_command(description = "Just a week away!")
    async def christmas(self, ctx, text: discord.Option(discord.SlashCommandOptionType.string)):
        text = text.replace("@", "")
        await ctx.respond(f"Can you believe it guys? {text}, just a week away! {text} is in a week! Woo-hoo! I am so happy about this information. {text}, just a week away. Oh, wow! Can you believe it? {text}, just in a week! It got here so fast.")

def setup(bot):
    bot.add_cog(FunCommands(bot))
    