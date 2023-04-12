import discord
from discord.ext import commands

class MetaCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Display Ing-Bot's latency")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.respond(f"{latency}ms")

    @discord.slash_command(description = "Display helpful information about Ing-Bot's commands")
    async def help(self, ctx):
        embed = discord.Embed(
            title = "Ing-Bot Commands",
            description = "Information on all of Ing-Bot's commands",
            color = discord.Colour.blurple()
        )

        embed.set_author(name="Ingot Cultists United™️", icon_url="https://github.com/WaspVentMan/Ingot-Pack/blob/main/assets/ingot_cult/alt_logo_scaled.png?raw=true")
        embed.set_thumbnail(url="https://github.com/averagebrine/ing-bot/blob/main/assets/icon.png?raw=true")

        embed.set_image(url="https://github.com/WaspVentMan/Ingot-Pack/blob/main/assets/ingot_cult/emoji/bunger.png?raw=true")

        embed.add_field(name="Meta Commands", value="", inline=False)
        embed.add_field(name="/help", value="Displays this help embed")
        embed.add_field(name="/ping", value="Measures and displays Ing-Bot's latency")

        embed.add_field(name="Fun Commands", value="", inline=False)
        embed.add_field(name="/hello", value="Says hello to Ing-Bot")
        embed.add_field(name="/christmas", value="Recites the \"Christmas, just a week away!\" copypasta, replacing 'Christmas' with any word")

        embed.set_footer(text="Have a suggestion? Message Ing-Bot's maintainer averagebrine#2743")

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(MetaCommands(bot))