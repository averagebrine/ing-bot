import os, discord, requests, random, urllib.request
from discord.ext import commands
from PIL import Image

backing_image_path = "assets/display/backing.png"
temp_image_path = "assets/temp/temp.png"
random_ingots_path = "assets/display/random_ingots/"

class IngotPackCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Search for an ingot or ingotmoji")
    async def search(
        self,
        ctx,
        mode: discord.Option(str, choices=["item", "emoji"]),
        query: discord.Option(str),
        raw: discord.Option(bool, required=False, default=False)
        ):

        ingot_name = str(query).lower().replace(" ", "_")

        if ingot_name == "turtle" or ingot_name == "vedal" or ingot_name == "hello":
            embed = discord.Embed(title=ingot_name.title(), color=discord.Colour.green())
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1093280397162455101.gif?quality=lossless")
            final_image = discord.File("assets/display/vedal.gif")
            embed.set_image(url="attachment://vedal.gif")
            embed.set_footer(text=ingot_name.title(), icon_url="https://cdn.discordapp.com/emojis/1093280397162455101.gif?quality=lossless")

            await ctx.respond(embed=embed, file=final_image)
            return

        if mode == "item":
            ingot_texture_path = "https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/minecraft/textures/item/" + ingot_name + ".png"
        else:
            ingot_texture_path = "https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/emoji/" + ingot_name + ".png"

        urllib.request.urlretrieve(ingot_texture_path, temp_image_path)

        embed = discord.Embed(title=ingot_name.title(), color=discord.Colour.blurple(), url=ingot_texture_path)

        # ingo descripto
        ingot_description = requests.get('https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/ing-bot/descriptions/' + ingot_name + '.txt').content.decode('utf-8')
        if ingot_description != '404: Not Found':
            embed.description = ingot_description

        # dumb rendering time!!!!
        if mode == "emoji":
            if not raw:
                ingot_image = Image.open(temp_image_path)
                ingot_image = ingot_image.resize((256, 256), 0)
                ingot_image.save(temp_image_path)
        elif not raw:

            backing_image = Image.open(backing_image_path)
            ingot_image = Image.open(temp_image_path).convert("RGBA")

            random_ingots = []
            for i in range(8):
                random_ingot_path = random_ingots_path + random.choice(os.listdir(random_ingots_path))
                random_ingots.append(Image.open(random_ingot_path).convert("RGBA"))

            backing_image.paste(ingot_image, (6, 6), ingot_image)
            random_ingot_positions = [(-12, -12), (6, -12), (24, -12), (-12, 6), (24, 6), (-12, 24), (6, 24), (24, 24)]
            for i in range(len(random_ingots)):
                backing_image.paste(random_ingots[i], random_ingot_positions[i], random_ingots[i])

            backing_image = backing_image.resize((504, 504), 0)
            backing_image.save(temp_image_path)

        final_image = discord.File("assets/temp/temp.png", filename="ingot.png")
        embed.set_image(url="attachment://ingot.png")

        await ctx.respond(embed=embed, file=final_image)

def setup(bot):
    bot.add_cog(IngotPackCommands(bot))